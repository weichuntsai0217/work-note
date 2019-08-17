# 1.1共同的部分 for texlive-small + puredoc + dosbox + xserver + dev-base + dev-code
* 要有gen-readme.sh 的 script 搭配 tpl-readme.md
* tpl-readme.md 要填入的變數有
  - `$PROJ_NAME$`, ex: 在gen-readme.sh中 `PROJ_NAME=puredoc`
  - `$PROJ_REPO$`, ex: 在gen-readme.sh中 `PROJ_REPO=weichuntsai/${PROJ_NAME}`
  - `$PROJ_VER$`, ex: 在gen-readme.sh中 `PROJ_VER=1.1`
* 讓contaier 啟動後時區default是使用者電腦的時區, 允許user在container啟動時設定他想要的時區
* 將.bashrc中的 `alias ll='ls -alF` 改成 `alias ll='ls -alFh'`

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
* Dockerfile中的base image 改成weichuntsai/texlive-small:1.1
* 要有flag -m, --main-font to setmainfont (`puredoc` and all templates 都要有對應修改)
* 要有flag -s, --sans to use default sans-serif font (`puredoc` and all templates 都要有對應修改)
* 要有flag --fcb 為沒有bold的字體開啟 偽粗體, fcb 是 "fake CJK bold" (`puredoc` and all templates 都要有對應修改)
* 要有flag --fci 為沒有italic的字體開啟 偽斜體, fc 是 "fake CJK italic" (`puredoc` and all templates 都要有對應修改)
* 要有flag -l, --line-skip 讓user 設定行距, 相對單位或絕對單位皆可 (`puredoc` and all templates 都要有對應修改)
* default cjk 要改成 Noto CJK Serif tc (`puredoc` and all templates 都要有對應修改)
* "puredoc-tpl-resume.tex" 要增加可單獨修改"姓名字體大小"和"position字體大小"的選項
* run-all-examples.sh
* README.md 加 License
* Merge develop into master and release

# dosbox 1.1 (正在develop開發)
* README.md 中提及版本都改成1.1 (含dosbox + xserver) ===> done
* Installation & run 的 Step 1 "so you can run xserver on" 要改成 "so you can run dosbox on" ===> done
* dosbox放個遊戲的preview圖 (就如同xserver那樣) ===> done
* 確認大富翁三的游標不對準是什麼問題導致(是dosbox的設定嗎? 還是xserver的SCREEN_DPI)
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
* Dockerfile中 "ADD https://raw.githubusercontent.com/weichuntsai0217/xserver/master/setup-xclient.sh /" 來源URL要改成綁定在某個xserver的commit (這次release請綁定xserver 1.1), 不可以只瞄準master的最新
* README.md 加 License
* Merge develop into master and release

# xserver 1.1 (正在develop開發)
* README.md 中提及版本都改成1.1 ===> done
* 在 "Other examples to initialize xserver" 的 第一點 "I want to set screen_size and screen_dpi for Xvfb:" 要改成 "I want to set SCREEN_SIZE as 1200x675x24 and SCREEN_DPI as 75 for Xvfb:" ===> done
* SCREEN_SIZE 和 SCREEN_DPI 的預設值必須確認一下在非retina的螢幕上的表現後再來調整(例如是否該改成: 若SCREEN_DPI沒餵就用Xvfb自己預設的值就好)
* README.md 加 License
* Merge develop into master and release

# vim 1.1
* 確認一下為何"yy"複製的結果在host的剪貼簿讀不到... (解決方案必須是Mac OSX, windows, Linux都要可以適用)
* modelines 改成 2
* 簡單的c++ 和 java 的IDE方案寫成script, 讓user自己決定是否安裝

# dev-base 1.1
* Dockerfile的最後一行"ADD https://raw.githubusercontent.com/weichuntsai0217/vim/master/.vimrc /root" 來源URL要改成綁定在某個vim的commit (這次release請綁定vim 1.1)
* 舊的git移除, 改成裝目前最新但固定版本的git (版本要寫死, 而非總是描latest)

# dev-code 1.1
* Dockerfile的base image改成 weichuntsai/dev-base:1.1
* `Dockerfile`的第19列`RUN npm install --global yarn@1.6.0 eslint` 要改成裝目前最新但固定版本的yarn和eslint (版本要寫死, 而非總是描latest)
