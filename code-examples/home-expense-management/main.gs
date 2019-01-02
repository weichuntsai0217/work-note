/**
 * User input - START
 */
// 更改設定時, 請順便確認 月範例 和 支出項目分類 這兩個sheet
var HEADER_ROW = 1
var DATA_START_ROW = HEADER_ROW + 1
var TOP_CATEGORY = 3
var TOP_SUB_ITEM_IN_CAT = 10
var TOP_ITEM = 20
var DEFAULT_EMPTY_SHEET_ROW = 35 + TOP_CATEGORY * (TOP_SUB_ITEM_IN_CAT + 4) + TOP_ITEM
var SUFFIX_SUMMARY = '-summary'
var SUFFIX_PASS = '-pass'
var SUFFIX_ZHTW_COPY = '的副本'
var SUFFIX_EXP = '-Expense'
var PROJ_NAME = 'homeExpMgt'
var TIME_ZONE = 'GMT+8'

// Field column definition - START
var TIME = 'time'
var ITEM = 'item'
var EXPENSE= 'expense'
var PAYER = 'payer'
var CATEGORY = 'category'
var DETAIL = 'detail'
var ZHTWRATE = 'zhtwRate'
var KEY_MAP = {
  '時間': TIME,
  '項目': ITEM,
  '支出': EXPENSE,
  '付費者': PAYER,
  '分類': CATEGORY,
  '細節': DETAIL,
  '台幣匯率': ZHTWRATE
}
var REV_KEY_MAP = getReverseKeyMap(KEY_MAP)
// Field column definition - END

function getTplName() { return '月範例' }
function getCategoryName() { return '支出項目分類' }
function getCodeDescName() { return '說明' }
function getCurMonth() {
  return Utilities.formatDate(new Date(), TIME_ZONE, 'M') // current month
}
function getCurYear() {
  return Utilities.formatDate(new Date(), TIME_ZONE, 'YYYY') // current year
}
function getReverseKeyMap(keyMap) {
  var res = {}
  for (var key in keyMap) {
    res[keyMap[key]] = key
  }
  return res
}
/**
 * User input - END
 */

/**
 * GUI Interface - START
 */
function Add_New_Month() {
  var spreadSheet = SpreadsheetApp.getActiveSpreadsheet()
  var sheetName = getCurMonth()
  var newSheet = spreadSheet.getSheetByName(sheetName)
  if (newSheet) {
    var ui = SpreadsheetApp.getUi()
    if (ui && ui.alert) {
      var sheetNameStr = 'Sheet "' + sheetName + '"'
      var title = [sheetNameStr, '未新增成功。'].join(' ')
      var content = [
        '原因：您想新增的',
        sheetNameStr,
        '已存在，所以無法新增。請手動刪除再執行本指令。'
      ].join(' ')
      var result = ui.alert(title, content, ui.ButtonSet.OK)
    }
    return
  }
  createExpenseSheet(spreadSheet, sheetName)
}

function Add_One_Summary() {
  var spreadSheet = SpreadsheetApp.getActiveSpreadsheet()
  var srcSheet = spreadSheet.getActiveSheet()
  createOneSummarySheet(spreadSheet, srcSheet)
}

function Add_All_Summaries() {
  var spreadSheet = SpreadsheetApp.getActiveSpreadsheet()
  createAllSummarySheets(spreadSheet)
}
/**
 * GUI Interface - END
 */

/**
 * Schedule Interface - START
 */
function Schd_Add_All_Summaries() {
  // Triggered at 3:00 in the 1st day of every month
  var spreadSheet = SpreadsheetApp.getActiveSpreadsheet()
  if (stopSchd(spreadSheet, true)) return
  createAllSummarySheets(spreadSheet)
}

function Schd_Add_New_Month() {
  // Triggered at 4:00 in the 1st day of every month
  var spreadSheet = SpreadsheetApp.getActiveSpreadsheet()
  if (stopSchd(spreadSheet)) return
  var sheetName = getCurMonth()
  createExpenseSheet(spreadSheet, sheetName)
}
/**
 * Schedule Interface - END
 */

function stopSchd(spreadSheet, extendToJanOfNextYear) { // need to stop schedule
  var spreadSheetName = spreadSheet.getName()
  if (spreadSheetName === PROJ_NAME) return false
  var curYear = getCurYear()
  var curYearExpName = curYear + SUFFIX_EXP
  if (spreadSheetName === curYearExpName) return false
  var curMonth = getCurMonth()
  if (extendToJanOfNextYear && curMonth === '1') {
    var prevYearExpName = String(Number(curYear) - 1) + SUFFIX_EXP
    if (spreadSheetName === prevYearExpName) return false
  }
  return true
}

function createAllSummarySheets(spreadSheet) {
  var sheets = []
  spreadSheet.getSheets().forEach(function(item){
    var sheetName = item.getName()
    if (sheetName.indexOf(SUFFIX_SUMMARY) !== -1) {
      deleteExistedSheet(spreadSheet, sheetName)
      return
    }
    if (
      sheetName !== getTplName() &&
      sheetName !== getCategoryName() &&
      sheetName !== getCodeDescName() &&
      sheetName.indexOf(SUFFIX_PASS) === -1 &&
      sheetName.indexOf(SUFFIX_ZHTW_COPY) === -1
    ) {
      sheets.push(item)
    }
  })
  sheets.forEach(function(srcSheet) {
    createOneSummarySheet(spreadSheet, srcSheet)
  })
}

function createOneSummarySheet(spreadSheet, srcSheet) {
  var srcSheetName = srcSheet.getName()
  var schema = getTplSchema(spreadSheet, getTplName())
  var plainObjData = getPlainObjData(srcSheet, schema)
  plainObjData.sort(sortRule(EXPENSE)) // in-place sorting, the original plainObjData now is sorted.
  var catData = getCollapseData(plainObjData, CATEGORY, EXPENSE, true)
  catData.sort(sortRule(1)) //  in-place sorting, the original catData now is sorted.
  var finalTopItem = plainObjData.length < TOP_ITEM ? plainObjData.length : TOP_ITEM
  var finalTopCategory = catData.length < TOP_CATEGORY ? catData.length : TOP_CATEGORY
  var topSubItemData = getTopSubItemDataInCat(plainObjData, catData.slice(0, finalTopCategory))
  var dstSheetName = getSummaryName(srcSheetName)
  deleteExistedSheet(spreadSheet, dstSheetName)
  var dstSheet = createEmptySheet(spreadSheet, dstSheetName, srcSheet.getIndex())
  
  // Start to render dstSheet
  var startRow = 1
  startRow = renderSummaryTitle(dstSheet, startRow, spreadSheet)
  startRow = renderSummaryStatistics(dstSheet, startRow, plainObjData)
  startRow = renderSummaryTopCategories(dstSheet, startRow, catData.slice(0, finalTopCategory), topSubItemData, schema)
  startRow = renderSummaryTopItems(dstSheet, startRow, plainObjData.slice(0, finalTopItem), schema)
  startRow = renderPieChart(dstSheet, startRow, catData, CATEGORY, EXPENSE)
}

function getTopSubItemDataInCat(plainObjData, slicedCatData) {
  var res = []
  slicedCatData.forEach(function() {
    res.push([])
  })
  
  function isOnTarget() {
    var flag = true
    slicedCatData.forEach(function(item, index) {
      flag = flag && (res[index].length >= TOP_SUB_ITEM_IN_CAT )
    })
    return flag
  }
  
  for (var i = 0; i < plainObjData.length ; i++) {
    if (isOnTarget()) {
      break
    }
    var data = plainObjData[i]
    for (var j = 0; j < slicedCatData.length ; j++) {
      var cat = slicedCatData[j]
      if (data[CATEGORY] === cat[0] && res[j].length < TOP_SUB_ITEM_IN_CAT) {
        res[j].push(data)
        break
      }
    }
  }
  return res
}

function getTplSchema(spreadSheet, tplSheetName) {
  var schema = {}
  var tplSheet = spreadSheet.getSheetByName(tplSheetName)
  var firstRow = tplSheet.getRange(String(HEADER_ROW) + ':' + String(HEADER_ROW))
  var lastColumn = firstRow.getLastColumn()
  for (var col = 1; col <= lastColumn; col++) {
    var value = firstRow.getCell(1, col).getValue()
    if (KEY_MAP[value]) {
      schema[KEY_MAP[value]] = col
    }
  }
  return schema
}

function sortRule(key, isAscending) {
  // default is descending
  return function(a, b) {
    if (typeof a === 'number' && typeof b === 'number') {
      if (isAscending) return a - b
      return b - a
    } else {
      if (isAscending) return a[key] - b[key]
      return b[key] - a[key]
    }
  }
}

function renderSummaryTitle(sheet, startRow, spreadSheet) {
  var marginBottomRows = 3
  var label = [
    '[',
    spreadSheet.getName(),
    ']'
  ].join(' ')
  sheet
    .getRange(startRow, 1)
    .setHorizontalAlignment('left')
    .setValue([label, sheet.getName(), '(本頁幣值皆為台幣)'].join(' '))
  return startRow + marginBottomRows
}

function renderSummaryStatistics(sheet, startRow, plainObjData) {
  var marginBottomRows = 3
  var titleCol = 1
  var valueCol = 2
  var items = [
    { title: '總支出', value: getSum(plainObjData)},
    { title: '支出項目數', value: getTotalItems(plainObjData)},
    { title: '平均支出', value: getMean(plainObjData)},
    { title: '支出標準差', value: getSampleStdev(plainObjData)},
  ]
  
  items.forEach(function(item, index) {
    sheet.getRange(startRow + index, titleCol).setValue(item.title)
    sheet
      .getRange(startRow + index, valueCol)
      .setHorizontalAlignment('right')
      .setNumberFormat('0.0')
      .setValue(item.value)
  })
    
  return startRow + (items.length - 1) + marginBottomRows
}

function renderSummaryTopCategories(sheet, startRow, slicedCatData, topSubItemData, schema) {
  // plainObjData must be sorted descendingly by EXPENSE before passed into this function
  var marginBottomRows = 1
  sheet
    .getRange(startRow, 1)
    .setHorizontalAlignment('left')
    .setValue('前' + String(slicedCatData.length) + '名' + REV_KEY_MAP[CATEGORY] + '支出如下 =====')
  var startCatRow = startRow + 1
  slicedCatData.forEach(function(cat, index) {
    var catRowValue = [
      '第',
      String(index+1),
      '名的',
      REV_KEY_MAP[CATEGORY],
      '為 ',
      cat[0],
      ' ',
      getOneDecimalStr(cat[1])
    ].join('')
    sheet
      .getRange(startCatRow, 1)
      .setHorizontalAlignment('left')
      .setValue(catRowValue)
    subItem = topSubItemData[index]
    startCatRow = renderSummaryTopItems(sheet, startCatRow + 1, subItem, schema, cat[0] + '中的')
  })
  return startCatRow + marginBottomRows
}
    
function renderSummaryTopItems(sheet, startRow, slicedData, schema, prefix) {
  // plainObjData must be sorted descendingly by EXPENSE before passed into this function
  var finalPrefix = prefix || '所有資料中的'
  var marginBottomRows = 2
  sheet
    .getRange(startRow, 1)
    .setHorizontalAlignment('left')
    .setValue(finalPrefix + '前' + String(slicedData.length) + '名' + REV_KEY_MAP[ITEM] + '支出:')

  // Render header row
  var startHeaderRow = startRow + 1
  sheet.getRange(startHeaderRow, schema[TIME]).setValue(REV_KEY_MAP[TIME])
  sheet.getRange(startHeaderRow, schema[ITEM]).setValue(REV_KEY_MAP[ITEM])
  sheet.getRange(startHeaderRow, schema[EXPENSE]).setValue(REV_KEY_MAP[EXPENSE])
  sheet.getRange(startHeaderRow, schema[PAYER]).setValue(REV_KEY_MAP[PAYER])
  sheet.getRange(startHeaderRow, schema[CATEGORY]).setValue(REV_KEY_MAP[CATEGORY])
  
  // Render data rows
  var startDataRow = startHeaderRow + 1
  slicedData.forEach(function(data, index) {
    sheet.getRange(startDataRow + index, schema[TIME]).setValue(data[TIME])
    sheet.getRange(startDataRow + index, schema[ITEM]).setValue(data[ITEM])
    sheet
      .getRange(startDataRow + index, schema[EXPENSE])
      .setHorizontalAlignment('right')
      .setNumberFormat('0.0')
      .setValue(data[EXPENSE])
    sheet.getRange(startDataRow + index, schema[PAYER]).setValue(data[PAYER])
    sheet.getRange(startDataRow + index, schema[CATEGORY]).setValue(data[CATEGORY])
  })
  
  return startDataRow + (slicedData.length - 1) + marginBottomRows
}

function renderPieChart(sheet, startRow, src, titleCol, valueCol) {
  // 要可以調整寬度和高度
  var marginBottomRows = 11
  var data = Charts.newDataTable()
    .addColumn(Charts.ColumnType.STRING, REV_KEY_MAP[titleCol])
    .addColumn(Charts.ColumnType.NUMBER, REV_KEY_MAP[valueCol])
  src.forEach(function(item) {
    data.addRow(item)
  })
  data.build()

  var chart = Charts.newPieChart()
    .setDataTable(data)
    .setTitle([REV_KEY_MAP[titleCol], '比例'].join(''))
    .build()
    .getAs(MimeType.PNG)

  var col = 1
  sheet.insertImage(chart, col, startRow)
  return startRow + marginBottomRows
}

function getSummaryName(srcName) { return [String(srcName), SUFFIX_SUMMARY].join('') }

function getOneDecimalStr(num) {
  var strSrc = String(num)
  var strArray = strSrc.split('.')
  if (strArray.length === 1) {
    return strArray[0] + '.0'
  } else if (strArray.length === 2) {
    return [strArray[0], strArray[1].slice(0,1)].join('.')
  } else {
    return strSrc
  }
}

function getPlainObjData(sheet, schema) {
  var data = []
  var maxRows = sheet.getMaxRows()
  var maxCols = sheet.getMaxColumns()
  var isFirstDataRateFound = false
  var firstDataRate = null
  for (var row = DATA_START_ROW; row <= maxRows; row++) {
    if (sheet.getRange(row, schema[EXPENSE]).getValue()) { // skip expense = 0 or undefined or null
      var tmp = {}
      if (!isFirstDataRateFound) {
        isFirstDataRateFound = true
        firstDataRate = sheet.getRange(row, schema[ZHTWRATE]).getValue()
      }
      var currentDataRate = sheet.getRange(row, schema[ZHTWRATE]).getValue()
      var rate = getRate(currentDataRate, firstDataRate)
      tmp[TIME] = sheet.getRange(row, schema[TIME]).getValue()
      tmp[ITEM] = sheet.getRange(row, schema[ITEM]).getValue()
      tmp[EXPENSE] = (sheet.getRange(row, schema[EXPENSE]).getValue()) * rate // has been changed into the currency 'New Taiwan Dollar'
      tmp[PAYER] = sheet.getRange(row, schema[PAYER]).getValue()
      tmp[CATEGORY] = sheet.getRange(row, schema[CATEGORY]).getValue()
      tmp[DETAIL] = sheet.getRange(row, schema[DETAIL]).getValue()
      tmp[ZHTWRATE] = rate
      data.push(tmp)
    }
  }
  return data
}

function getRate(currentDataRate, firstDataRate) { // get exchange rate
  if (currentDataRate) return currentDataRate
  if (firstDataRate) return firstDataRate
  return 1
}

function getSum(plainObjData) {
  var res = 0
  plainObjData.forEach(function(item, index) {
    res += item[EXPENSE]
  })
  return res
}

function getTotalItems(plainObjData) { return plainObjData.length }

function getMean(plainObjData) { return getSum(plainObjData) / getTotalItems(plainObjData) }

function getSampleStdev(plainObjData) {
  var mean = getMean(plainObjData)
  var N = getTotalItems(plainObjData)
  var squareSum = 0
  plainObjData.forEach(function(item, index) {
    var x = item[EXPENSE]
    squareSum += Math.pow((x - mean), 2)
  })
  return Math.pow((squareSum / (N - 1)), 0.5)
}

function createExpenseSheet(spreadSheet, sheetName) {
  if (spreadSheet.getSheetByName(sheetName)) {
    return
  }
  var options = { template: spreadSheet.getSheetByName(getTplName()) }
  var newSheet = spreadSheet.insertSheet(sheetName, 0, options)
}

function createEmptySheet(spreadSheet, sheetName, index) {
  var targetRows = DEFAULT_EMPTY_SHEET_ROW
  var targetCols = (spreadSheet.getSheetByName(getTplName())).getMaxColumns() - 2
  var sheet = null
  if (typeof index === 'number') {
    sheet = spreadSheet.insertSheet(sheetName, index)
  } else {
    sheet = spreadSheet.insertSheet(sheetName)
  }
  var maxRows = sheet.getMaxRows()
  var maxCols = sheet.getMaxColumns()
  
  if (maxRows > targetRows) {
    sheet.deleteRows(targetRows+1, maxRows-targetRows);
  } else {
    sheet.insertRowsAfter(maxRows, targetRows-maxRows);
  }
  
  if (maxCols > targetCols) {
    sheet.deleteColumns(targetCols+1, maxCols-targetCols);
  } else {
    sheet.insertColumnsAfter(maxCols, targetCols-maxCols);
  }

  var allRange = sheet.getRange('1:' + String(sheet.getMaxRows()))
  allRange
    .setHorizontalAlignment('center')
    .setVerticalAlignment('middle')
    .setFontSize(11)
  sheet.setRowHeights(1, targetRows, 32)

  return sheet
}

function deleteExistedSheet(spreadSheet, sheetName) {
  var sheet = spreadSheet.getSheetByName(sheetName)
  if (sheet) {
    spreadSheet.deleteSheet(sheet)
  }
}

function getCollapseData(plainObjData, titleCol, valueCol, toArray) {
  var src = {}
  plainObjData.forEach(function(item, index) {
    var title = item[titleCol]
    var value = item[valueCol]
    if (title in src) {
      src[title] += value
    } else {
      src[title] = value
    }
  })
  if (toArray) {
    var ary = []
    for (var key in src) {
      ary.push([key, src[key]])
    }
    return ary
  }
  return src
}
