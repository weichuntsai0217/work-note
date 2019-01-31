# 1.1共同的部分 for texlive-small + puredoc + dosbox + xserver
* 要有gen-readme.sh 的 script 搭配 tpl-readme.md
* tpl-readme.md 要填入的變數有
  - `$PROJ_NAME$`, ex: 在gen-readme.sh中 `PROJ_NAME=puredoc`
  - `$DOCKER_REPO$`, ex: 在gen-readme.sh中 `DOCKER_REPO=weichuntsai/${PROJ_NAME}`
  - `$DOCKER_VER$`, ex: 在gen-readme.sh中 `DOCKER_VER=1.1`

# texlive-small 1.1
* txfont 來安裝user自行下載字體檔 (README要說用法)
* setmainfont => 要可以選用Roboto
* cjk font 加入Noto
* README.md 加入setmainfont的說明, 然後cjk的範例改成Noto (ARPL UMING不要安裝也不用show在README了)

# puredoc 1.1
* 要有flag -m, --main-font to setmainfont (`puredoc` and all templates 都要有對應修改)
* 要有flag -s, --sans to use default sans-serif font (`puredoc` and all templates 都要有對應修改)
* 要有flag --fcb 讓user為沒有bold的字體開啟 偽粗體, fcb 是 "fake CJK bold" (`puredoc` and all templates 都要有對應修改)
* 要有flag --fci 讓user為沒有italic的字體開啟 偽斜體, fc 是 "fake CJK italic" (`puredoc` and all templates 都要有對應修改)
* 要有flag -l, --line-skip 讓user 設定行距, 相對單位或絕對單位皆可 (`puredoc` and all templates 都要有對應修改)
* default cjk 要改成 Noto CJK Serif tc (`puredoc` and all templates 都要有對應修改)
* run-all-examples.sh

# dosbox 1.1
* dosbox放個遊戲的preview圖 (就如同xserver那樣)
* Dockerfile中 "ADD https://raw.githubusercontent.com/weichuntsai0217/xserver/master/setup-xclient.sh /" 來源URL要綁定在某個xserver的commit, 不可以只瞄準master的最新

# xserver 1.1
* 在 "Other examples to initialize xserver" 的 第一點 "I want to set screen_size and screen_dpi for Xvfb:" 要改成 "I want to set SCREEN_SIZE as 1200x675x24 and SCREEN_DPI as 75 for Xvfb:"
