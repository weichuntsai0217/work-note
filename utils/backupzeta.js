const fs = require('fs');
const { exec } = require('child_process');
const srcDir = process.argv[2]
const srcArray = srcDir.split('/')
const srcFolder = srcArray[srcArray.length - 1]
const parentDir = srcArray.slice(0, srcArray.length - 1).join('/')

/**
 * User defined data - START
 */
const targetDirMap = {
  'ZETA-frontend': '/Users/jimmy_tsai/GoogleDrive/TrendMicro_Jimmy/projects/ZETA-frontend/code-backup',
  'Titanic_Machine_Learning_from_Disaster': '/Users/jimmy_tsai/GoogleDrive/TrendMicro_Jimmy/projects/kaggle',
  'demo-pytest': '/Users/jimmy_tsai/GoogleDrive/TrendMicro_Jimmy/projects',
  'demo-python-class-inheritance': '/Users/jimmy_tsai/GoogleDrive/TrendMicro_Jimmy/projects',
  'demo-python-import': '/Users/jimmy_tsai/GoogleDrive/TrendMicro_Jimmy/projects',
  'exp-mgr': '/Users/jimmy_tsai/GoogleDrive/TrendMicro_Jimmy/projects'
}
const srcRelativePath = './' + srcFolder
const excludePattern = '*/node_modules/\\*'
/**
 * User defined data - END
 */
 
const targetDir = targetDirMap[srcFolder] || '.'
if (!fs.existsSync(targetDir)) {
  throw 'The targetDir does not exist. Please set targetDir in targetDirMap.'
}

exec(
  "git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \\(.*\\)/\\1/'",
  function(error, stdout, stderr) {
    if (error) {
      console.log('--- Error In git & sed ---')
      console.log(error)
      return
    }
    const gitBranchName = stdout.trim() || 'null'
    const targetZipName = srcFolder + '__branchIs-' + gitBranchName + '.zip'
    const targetZipPath = [targetDir, targetZipName].join('/')
    const zipCmd = ['zip -r -q', targetZipPath, srcRelativePath, '-x', excludePattern].join(' ')
    console.log('Source Directory: ', srcDir)
    console.log('Current Git Branch: ', gitBranchName)
    console.log('Target Zip: ', targetZipPath)
    console.log('excludePattern: ', excludePattern)
    console.log('Zip Cmd Execution Directory: ', parentDir)
    console.log('Zip Cmd: ', zipCmd)
    if (fs.existsSync(targetZipPath)) {
      console.log('Remove old', targetZipName, '...')
      fs.unlinkSync(targetZipPath)
    }
    exec(zipCmd, {cwd: parentDir}, function(error, stdout, stderr) {
      if (error) {
        console.log('--- Error In Zip Cmd ---')
        console.log(error)
        return
      }
      console.log('Backup successed!')
    })
  }
)
