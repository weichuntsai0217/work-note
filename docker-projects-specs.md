# 1.1共同的部分 for texlive-small + puredoc + dosbox + xserver
* 要有gen-readme.sh 的 script 搭配 tpl-readme.md
* tpl-readme.md 要填入的變數有
  - `$PROJ_NAME$`, ex: 在gen-readme.sh中 `PROJ_NAME=puredoc`
  - `$PROJ_REPO$`, ex: 在gen-readme.sh中 `PROJ_REPO=weichuntsai/${PROJ_NAME}`
  - `$PROJ_VER$`, ex: 在gen-readme.sh中 `PROJ_VER=1.1`

# texlive-small 1.1
* README.md 中提及版本都改成1.1
* txfont 來安裝user自行下載字體檔 (README要說用法), 例如:
  - 1. `mv Noto /usr/local/share/fonts/`
  - 2. `chmod 755 /usr/local/share/fonts/Noto`
  - 3. `chmod 755 /usr/local/share/fonts/Noto/* -R`
  - 4. `fc-cache -fv`
* setmainfont 要可以選用Roboto
* cjk font 加入Noto
* README.md 加入setmainfont的說明, 然後cjk的範例改成Noto (ARPL UMING不要安裝也不用show在README了)
* README.md 加 License
* Merge develop into master and release

# puredoc 1.1
* README.md 中提及版本都改成1.1
* 要有flag -m, --main-font to setmainfont (`puredoc` and all templates 都要有對應修改)
* 要有flag -s, --sans to use default sans-serif font (`puredoc` and all templates 都要有對應修改)
* 要有flag --fcb 為沒有bold的字體開啟 偽粗體, fcb 是 "fake CJK bold" (`puredoc` and all templates 都要有對應修改)
* 要有flag --fci 為沒有italic的字體開啟 偽斜體, fc 是 "fake CJK italic" (`puredoc` and all templates 都要有對應修改)
* 要有flag -l, --line-skip 讓user 設定行距, 相對單位或絕對單位皆可 (`puredoc` and all templates 都要有對應修改)
* default cjk 要改成 Noto CJK Serif tc (`puredoc` and all templates 都要有對應修改)
* run-all-examples.sh
* README.md 加 License
* Merge develop into master and release

# dosbox 1.1
* README.md 中提及版本都改成1.1 (含dosbox + xserver) ===> done
* Installation & run 的 Step 1 "so you can run xserver on" 要改成 "so you can run dosbox on" ===> done
* dosbox放個遊戲的preview圖 (就如同xserver那樣) ===> done
* dosbox-0.74.conf 要改成(若不做以下設定, 遊戲畫面會很小):
```
fullscreen=true
fulldouble=false
fullresolution=1200x675
windowresolution=original
output=overlay
```
在README.md中寫, `fullresolution=Some_Size` 的 `Some_Size`若比xserver啟動時的size還大, dosbox會開不起來

* Installation & run 的 Step 4 的xserver README.md的連結要指到xserver 1.1 的commit的README.md
* Dockerfile中 "ADD https://raw.githubusercontent.com/weichuntsai0217/xserver/master/setup-xclient.sh /" 來源URL要綁定在某個xserver的commit (這次release請綁定xserver 1.1), 不可以只瞄準master的最新
* README.md 加 License
* Merge develop into master and release

# xserver 1.1
* README.md 中提及版本都改成1.1 ===> done
* 在 "Other examples to initialize xserver" 的 第一點 "I want to set screen_size and screen_dpi for Xvfb:" 要改成 "I want to set SCREEN_SIZE as 1200x675x24 and SCREEN_DPI as 75 for Xvfb:" ===> done
* SCREEN_SIZE 和 SCREEN_DPI 的預設值必須確認一下在非retina的螢幕上的表現後再來調整(例如是否該改成: 若SCREEN_DPI沒餵就用Xvfb自己預設的值就好)
* 確認不同解析度對大富翁三的游標影響(用dosbox container測)
* README.md 加 License
* Merge develop into master and release
