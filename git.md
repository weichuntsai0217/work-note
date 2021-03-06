* 本文須知
  - 本文中的指令都是運行在Terminal
  - "===>"表示補充說明, 而非指令


* 建立Repository
  - 新建自己的repository,
    例如我有個叫做mywebsite的專案資料夾,
    現在我想開始用Git管理mywebsite內的檔案, 因此我先將目錄切換到mywebsite底下後輸入:
    ```
    git init
    ```

  - 複製別人的repository, 假設在github(網址: https://github.com)上, 帳號為"jack1990", 專案名稱為"jackwebsite":
    ```
    git clone https://github.com/jack1990/jackwebsite.git
    ```

  - 複製別人的repository, 假設在已設好的git server上,
    假設server ip為"10.7.72.1", 帳號為"git", repository目錄為"ZETA-1.0":
    ```
    git clone git@10.7.72.1:ZETA-1.0
    ```

* 設定Git資訊
  - 設定使用者姓名, "--global"表全域:
    ```
    git config --global user.name "Jimmy"
    ```

  - 設定使用者email, "--global"表全域:
    ```
    git config --global user.email "jimmy@company.com"
    ```

  - 將"vim"設為編輯commit和tag messages時的編輯器, "--global"表全域:
    ```
    git config --global core.editor vim
    ```

  - 設定push時只將目前所在的local branch push到對應的remote branch:
    ```
    git config --global push.default simple
      ===> (假設remote repository為"origin")若無做此設定, 當你下指令"git push origin"後
           在Git 2.0以前的版本會將"所有"local的branch一起push到各自對應的remote branch,
           在Git 2.0以後的版本則默認simple為default
    ```

  - 觀看Git設定內容:
    ```
    git config --list
    ```

  - 其實Git的設定檔是儲存在你的家目錄的".gitconfig"這個隱藏檔中,
    你可以使用編輯器將它打開, 下例中"~/"為家目錄, "cat"則是文件瀏覽器:
    ```
    cat ~/.gitconfig
    ```

  - 打開Git顏色顯示(若default就有顏色, 其實不用設定):
    ```
    git config --global color.ui true
    ```

  - 關閉Git顏色顯示:
    ```
    git config --global color.ui false
    ```

  - 設定Git顏色, 例如要將"git diff"中屬於"meta"資訊的字設為"red", 背景設為"yellow", 字體粗細為"bold"
    (Git顏色選項有normal, black, red, green, yellow, blue, magenta, cyan, white):
    ```
    git config --global color.diff.meta "red yellow bold"
    ```

* local端取得最新的remote資訊
  - 將最新remote資訊更新至local端, 這樣才知道remote目前有哪些branch
    ```
    git fetch
    git remote prune origin
      ===> 別人在remote刪掉的branch, 自己在local是無法察覺的(用git fetch也無法), 這時就要在"git fetch"後多下一道 "git remote prune origin" 的指令(假設remote是origin)
    ```

* 查看重要資訊
  - 看目前local在哪個branch, 以及branch做了什麼修改:
    ```
    git status
    ```

  - 看所在branch的commit歷史:
    ```
    git log
    ```

  - 看特定branch的commit歷史, 假設要看的branch name為"br1":
    ```
    git log br1
    ```

  - list file change history for a specific file called "syslogsetting.js"
    ```
    git log --follow syslogsetting.js
    ```

* branch操作, 假設remote repository為"origin"
  - 列出目前local所有的branch:
    ```
    git branch
    ```

  - 列出目前remote的所有branch:
    ```
    git fetch
    git branch -r
    ```

  - 在local開新branch, 假設branch name為"br1":
    ```
    git checkout -b br1
    ```

  - 刪除local的branch "br1":
    ```
    git branch -d br1
    ```

  - 切換至branch "br1"
    ```
    git checkout br1
    ```

  - 已知remote有一新的branch "new_br", local端想開一個對應到"new_br"的同名branch:
    ```
    git fetch
    git checkout new_br
      ===> 此時local的"new_br"會被設定對應到remote的"new_br", 你應該會看到以下訊息:
             Branch new_br set up to track remote branch new_br from origin.
             Switched to a new branch 'new_br'
    ```

  - 自己開的local branch "br1"第一次push到remote(也就是說remote還沒有"br1"這個branch):
    ```
    git push origin br1
      ===> 因為remote沒有br1, 所以就算你先前有做"git config --global push.default simple",
           第一次push你也不能省略branch name "br1"
    git branch --set-upstream-to=origin/br1
      ===> local的br1對應到remote的br1    
    ```


* 將檔案從 unstaged 的狀態 還原至未被修改過的狀態
  - 還原單一的unstaged檔案, 假設檔名為"file1.txt":
    ```
    git checkout file1.txt
    ```

  - 還原所有的unstaged 檔案(staged的檔案不受影響), 必須在project的root目錄執行指令:
    ```
    git checkout .
    ```



* 將所有的unstaged 和 staged的檔案還原
  - (除了 untracked且unstaged 檔案不受影響, 其他的檔案均會還原):
    ```
    git checkout -f
    ```
    或
    ```
    git reset HEAD --hard
    ```


* 將檔案從 unstaged 的狀態 變成 staged 的狀態
  - 將"file1.txt"從 unstaged 的狀態 變成 staged 的狀態:
    ```
    git add file1.txt
    ```

  - 將所有 unstaged 狀態的檔案 變成 staged 的狀態:
    ```
    git add --all
    ```


* 將檔案從 staged 的狀態 變回 unstaged 的狀態
  - 將"file1.txt"從 staged 的狀態 變回 unstaged 的狀態:
    ```
    git reset HEAD file1.txt
    ```

  - 將所有 staged 狀態的檔案 變回 unstaged 的狀態:
    ```
    git reset
    ```


* untacked file其他操作:
  - 列出所有untracked file (不包含untracked資料夾):
    ```
    git clean -n
    ```

  - 刪除所有untracked file (不包含untracked資料夾):
    ```
    git clean -f
    ```

  - 列出所有untracked file 和 資料夾:
    ```
    git clean -n -d
    ```

  - 刪除所有untracked file 和 資料夾:
    ```
    git clean -f -d
    ```

* 版本提交(commit)
  - commit後才編輯commit message:
    ```
    git commit
      ===> 輸入後會進入一個編輯畫面, 可以編輯commit message
    ```

  - commit同時輸入commit message "Modified file1.txt":
    ```
    git commit -m "Modified file1.txt"
    ```


* 拿掉舊的commit:
    假設有5個commit由舊到新依序是 c1 -> c2 -> c3 -> c4 -> c5
    目前最新的commit為c5,
    "git log"如下方框所示:
    ```
    ___________________________________________________
    | commit b9aaf1075a50d171b6ae00018c91f2ad54c31bb3 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Sat Jan 14 19:28:33 2017 +0800          |
    |                                                 |
    |     c5                                          |
    |                                                 |
    | commit c1d7874849ca4149aef0f7875197ba74d0d1858a |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Sat Jan 14 19:28:12 2017 +0800          |
    |                                                 |
    |     c4                                          |
    |                                                 |
    | commit 7b1641aef19431ebc05d30a869a57def8b68cc76 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Sat Jan 14 19:28:00 2017 +0800          |
    |                                                 |
    |     c3                                          |
    |                                                 |
    | commit 24e18f45ab1ffee04716c8719711c6be479ab59e |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Sat Jan 14 19:13:46 2017 +0800          |
    |                                                 |
    |     c2                                          |
    |                                                 |
    | commit f01b688af8ae299749365c13e378a425ee893020 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Sat Jan 14 19:11:59 2017 +0800          |
    |                                                 |
    |     c1                                          |
    |_________________________________________________|
    ```
  - 不想修改commit history的情況下, 我想把c3的內容拿掉, 但保留c4和c5的內容:
    ```
    git revert 7b1641aef19431ebc05d30a869a57def8b68cc76
      ===> revert只會讓commit往前走(所以舊的commit history不會被動到),
           等於新增一個commit, 只是這個commit的內容是保留c4和c5的內容, 但把c3的內容拿掉,
           所以"git revert"指令輸入後會進到編輯commit message的畫面,
           編輯完message你輸入"git log"就會看到新增的commit
    ```

  - 修改commit history的情況下, 直接將c3這個commit抽掉, 但保留c4和c5的commit
    (注意: 必須在c3, c4, 和c5都還沒被push前才能執行以下指令!):
    ```
    git rebase -i 24e18f45ab1ffee04716c8719711c6be479ab59e
    ```
    接著會看到下列方框
    ```
    __________________________________________________________________________
    | pick 7b1641a c3                                                        |
    | pick c1d7874 c4                                                        |
    | pick 65f8f3f c5                                                        |
    |                                                                        |
    | # Rebase 24e18f4..65f8f3f onto 24e18f4 (3 command(s))                  |
    | #                                                                      |
    | # Commands:                                                            |
    | # p, pick = use commit                                                 |
    | # r, reword = use commit, but edit the commit message                  |
    | # e, edit = use commit, but stop for amending                          |
    | # s, squash = use commit, but meld into previous commit                |
    | # f, fixup = like "squash", but discard this commit's log message      |
    | # x, exec = run command (the rest of the line) using shell             |
    | #                                                                      |
    | # These lines can be re-ordered; they are executed from top to bottom. |
    | #                                                                      |
    | # If you remove a line here THAT COMMIT WILL BE LOST.                  |
    | #                                                                      |
    | # However, if you remove everything, the rebase will be aborted.       |
    | #                                                                      |
    | # Note that empty commits are commented out                            |
    |________________________________________________________________________|
    ```

    將"pick 7b1641a c3"這行刪掉如下方框
    ```
    __________________________________________________________________________
    | pick c1d7874 c4                                                        |
    | pick 65f8f3f c5                                                        |
    |                                                                        |
    | # Rebase 24e18f4..65f8f3f onto 24e18f4 (3 command(s))                  |
    | #                                                                      |
    | # Commands:                                                            |
    | # p, pick = use commit                                                 |
    | # r, reword = use commit, but edit the commit message                  |
    | # e, edit = use commit, but stop for amending                          |
    | # s, squash = use commit, but meld into previous commit                |
    | # f, fixup = like "squash", but discard this commit's log message      |
    | # x, exec = run command (the rest of the line) using shell             |
    | #                                                                      |
    | # These lines can be re-ordered; they are executed from top to bottom. |
    | #                                                                      |
    | # If you remove a line here THAT COMMIT WILL BE LOST.                  |
    | #                                                                      |
    | # However, if you remove everything, the rebase will be aborted.       |
    | #                                                                      |
    | # Note that empty commits are commented out                            |
    |________________________________________________________________________|
    ```

    存擋離開後會看到"Successfully rebased and updated refs/heads/master.", 且c3對應的內容消失了,
    "git log"後也會發現c3的commit不見了
    

* 回到舊的commit:
  注意! 必須在local端欲被回朔的commit(以下面的範例來說就是c3, c4, c5)尚未被push前!
    假設有5個commit由舊到新依序是 c1 -> c2 -> c3 -> c4 -> c5
    目前最新的commit為c5, "git log"如下方框所示:
    ```
    ___________________________________________________
    | commit b9aaf1075a50d171b6ae00018c91f2ad54c31bb3 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Sat Jan 14 19:28:33 2017 +0800          |
    |                                                 |
    |     c5                                          |
    |                                                 |
    | commit c1d7874849ca4149aef0f7875197ba74d0d1858a |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Sat Jan 14 19:28:12 2017 +0800          |
    |                                                 |
    |     c4                                          |
    |                                                 |
    | commit 7b1641aef19431ebc05d30a869a57def8b68cc76 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Sat Jan 14 19:28:00 2017 +0800          |
    |                                                 |
    |     c3                                          |
    |                                                 |
    | commit 24e18f45ab1ffee04716c8719711c6be479ab59e |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Sat Jan 14 19:13:46 2017 +0800          |
    |                                                 |
    |     c2                                          |
    |                                                 |
    | commit f01b688af8ae299749365c13e378a425ee893020 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Sat Jan 14 19:11:59 2017 +0800          |
    |                                                 |
    |     c1                                          |
    |_________________________________________________|
    ```

  - 我想將最新的commit回到c4:
    (注意: 使用reset回到c4後, c4之後的commit c5會被移除)
    ```
    git reset c1d7874849ca4149aef0f7875197ba74d0d1858a --hard
      ===> 若沒有"--hard", c5的提交時的內容會變成unstaged file保留下來
    ```
    或
    ```
    git reset HEAD^ --hard
      ===> 1個"^"符號表示回到前1個commit
    ```
    或
    ```
    git reset HEAD~1 --hard
      ===> "~1"表示回到前1個commit
    ```

  - 我想將最新的commit回到c3:
    (注意: 使用reset回到c3後, c3之後的commit c4, c5會被移除)
    ```
    git reset 7b1641aef19431ebc05d30a869a57def8b68cc76 --hard
      ===> 若沒有"--hard", c4和c5的提交時的內容會變回unstaged(或untracked) file保留下來
    ```
    或
    ```
    git reset HEAD^^ --hard
      ===> 2個"^"符號表示回到前2個commit
    ```
    或
    ```
    git reset HEAD~2 --hard
      ===> "~2"表示回到前2個commit
    ``` 

* 挑選(複製)特定commit (假設remote repository為"origin"): 
  我們可以使用"git cherry-pick"來挑選所需要的commit到特定的branch,
  cherry-pick的使用情境常見於產品版本(v0.1, v0.2, etc.)需要不同的功能(feature)來release,
  通常我們的master會有最完整的commit history, 也就是說master有產品所有的功能,
  然後我們再用cherry-pick將master上的不同的commit挑選到不同版本的branch.
  例如, 我有個客戶A只需要f1, 但客戶B只需要f2, 這時候我們在開發這2個功能前會先從master
  分出兩個branch, 分別為"0.1"和"0.2" , "0.1"這個branch是給客戶A, "0.2"這個branch是給客戶B,
  (假設0.1和0.2這兩個branch也都已經被push到remote讓其他工程師可以pull到他們自己的local)
  接著我們在master上commit f1(新增了檔案"f1")和f2(新增了檔案"f2"), 假設master的commit history看起來入下方框所示
  ```
  ___________________________________________________
  | commit 2e9cec1b01e321db34998da6f8e14ca5ff545335 |
  | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
  | Date:   Sun Jan 15 16:18:57 2017 +0800          |
  |                                                 |
  |     f2                                          |
  |                                                 |
  | commit c43f4e2e287cc4fb0b466f6a466155cbcf819e09 |
  | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
  | Date:   Sun Jan 15 16:18:49 2017 +0800          |
  |                                                 |
  |     f1                                          |
  |                                                 |
  | commit 4644078feb6a6fe0a7c86293b9c35293a843b76f | ===> branch "0.1" 和 "0.2" 是在common_feature這個commit切出去的
  | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
  | Date:   Sun Jan 15 16:16:59 2017 +0800          |
  |                                                 |
  |     common_feature                              |
  |_________________________________________________|
  ```
  - 假設目前在master, 我要把"f1"的commit選進branch "0.1", 而"f2"的commit則是選進branch "0.2":
    ```
    git checkout 0.1
    git cherry-pick c43f4e2e287cc4fb0b466f6a466155cbcf819e09
      ===> 把master上我要的那個commit挑選進branch "0.1"
    git checkout 0.2
    git cherry-pick 2e9cec1b01e321db34998da6f8e14ca5ff545335
      ===> 把master上我要的那個commit挑選進branch "0.2"
    ```
    完成後, 你在branch "0.1"會發現新增了檔案"f1",
    在branch "0.2"會發現新增了檔案"f2"(但0.2中不會有"f1", 若不知道原因請回想一下rebase)

* 從不同的遠端repo(非origin)挑選(複製)特定commit到local的branch "v0.9"
  ```
  git checkout v0.9
    ===> 先確認自己已經到v0.9
  git remote add general git@10.7.72.1:ZETA-web
    ===> 設定新的遠端repo叫"general"
  git fetch general
    ===> 將general的最新資訊抓到local
  git log general/v0.7 --grep='download' --regexp-ignore-case
    ===> 列出general的branch "v0.7"中含有關鍵字"download"的commit (--regexp-ignore-case為忽略大小寫)
  git cherry-pick e12fdcxxxxx
    ===> 執行cherry-pick, 其中e12fdcxxxxx為commit的SHA1
  ```

* 比較檔案差異
  - 比較單1個unstaged檔案和當前commit的差異, 例如檔名為"file1.txt":
    ```
    git diff file1.txt
    ```

  - 比較所有unstaged檔案和當前commit的差異:
    ```
    git diff
    ```

  - 比較當前commit與其他commit的差異:
    ```
    git diff ef190ecaf2dc124a3a0765a7adae5fc93eba6dbf
    ```
    或
    ```
    git diff ef190ecaf2dc124a3a0765a7adae5fc93eba6dbf HEAD
      ===> ef190ecaf2dc124a3a0765a7adae5fc93eba6dbf是欲比較的commit SHA-1
    ```

  - 比較兩個不同commit的差異:
    ```
    git diff ef190ecaf2dc124a3a0765a7adae5fc93eba6dbf 9607a0c96e08cd2a0abeaed1a808074d941a6e4f
      ===> ef190e... 和 9607a0... 都是commit的SHA-1, 實際上打前6碼就可以了
    ```

  - 比較單1個檔案在當前commit與其他commit之差異, 例如檔名為"file1.txt":
    ```
    git diff ef190ecaf2dc124a3a0765a7adae5fc93eba6dbf:file1.txt HEAD:file1.txt
      ===> HEAD表當前的commit
    ```

  - 比較單1個檔案在兩個不同commit的差異, 例如檔名為"file1.txt":
    ```
    git diff ef190ecaf2dc124a3a0765a7adae5fc93eba6dbf:file1.txt 9607a0c96e08cd2a0abeaed1a808074d941a6e4f:file1.txt
      ===> ef190e... 和 9607a0... 都是commit的SHA-1, 實際上打前6碼就可以了
    ```

  - 列出不同commit間有差異的檔名 (假設和上一個commit來比)
    ```
    git diff --name-only HEAD^
    ```
  強烈建議用SHA比, 而不要用HEAD^或HEAD~1這種相對符號來比, 因為HEAD^代表的是parent,
  而git log上看到的順序不一定代表parent順序, 詳情請見git rev-list)

  - 看某個commit的檔案 (假設該commit的SHA為602caff5e757c7b8d8ddf40e87ebe21620b0a099且該commit被tag 'v1.0', 要看的檔案是pom.xml):
    ```
    git show 602caff5e757c7b8d8ddf40e87ebe21620b0a099:pom.xml
    ```
    或
    ```
    git show v1.0:pom.xml
    ```
    以上兩個指令若沒加冒號和檔名, 就會顯示該commit和其parent的diff


* 看不同commit的code (假設你所在的local branch為"master"):
  - 將HEAD跳到某個舊commit觀看以前的舊code(並非revert或reset!!):
    ```
    git checkout 9607a0c96e08cd2a0abeaed1a808074d941a6e4f
      ===> 9607a0... 是commit的SHA-1, 實際上打前6碼就可以了
    ```

  - 將HEAD移回最新的commit:
    ```
    git checkout master
    ```


* push code 去更新對應的remote branch
  (假設你所在的local branch為"master" 且 remote repository為"origin" 且對應的remote branch為"master"):
  - 若你先前沒有做"git config --global push.default simple"這個設定:
    ```
    git push origin master
      ===> 請務必要打branch name "master"
    ```

  - 若你先前有做"git config --global push.default simple"這個設定:
    ```
    git push origin
      ===> 因為你先前有做"git config --global push.default simple"這個設定,
           所以若不打branch name, git會自動抓對應的remote branch name
    ```

  - 若別人比你早push code, 造成你push失敗, 這時請先pull code:
    ```
    git pull --rebase origin master
    ```
    或
    ```
    git pull --rebase origin
      ===> "--rebase"是為了不要有多餘的merge commit, 若有出現conflict請解決後再push
    ```


* pull code 來更新對應的local branch
  (假設你所在的local branch為"master" 且 remote repository為"origin" 且對應的remote branch為"master"):
  - 以下指令"--rebase"可以不打, 只是可能會出現多餘的merge commit:
    ```
    git pull --rebase origin
      ===> 若不打branch name, git會自動抓對應的remote branch name
    ```
    或
    ```
    git pull --rebase origin master
    ```


* unstaged的file其他操作
  - 把unstaged的檔案暫存起來(變成working directory clean),
    這樣checkout到別的branch時, unstaged的檔案就不會帶到別的branch:
    ```
    git stash
    ```

  - 把暫存的unstaged檔案再度拿出來
    ```
    git stash pop
    ```


* merge branch操作
  - "br1"是從"master"切出來的branch, 現在"master"要把"br1" merge回"master" (假設你已經在"master"):
    ```
    git merge br1
      ===> 一定要先"git status"確認自己是否在"master" branch
    ```

  - 若你有2個branch "br1" 和 "br2" 都是從"master"切出來的, 你在master上先merge了"br1", 接下來若要merge "br2",
    你可以直接用前面講的方法, 但這樣會產生無謂的merge commit, 這時比較好的做法是(假設你目前在"master"):
    ```
    git checkout br2
      ===> 切換branch至"br2"
    git rebase master
      ===> 透過rebase將"br1"的commit放到"br2"的commit的前面, 若發生conflict請自行解決
    git checkout master
      ===> 切換branch至"master"
    git merge br2
    ```
    

* 只push前n個的commit
  (假設你所在的local branch為"master" 且 remote repository為"origin" 且對應的remote branch為"master"):
  - 例如我local新增5個commit(commit message為"cm_1"~"cm_5"),
    remote最新的commit只到"cm_0",
    假設"git log"顯示的資訊如下方框所示
    ```
    ___________________________________________________
    | commit b3f8145b4777f7c765a3b1cd3d651d4162b0d6b0 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:02:27 2017 +0800          |
    |                                                 |
    |     cm_5                                        |
    |                                                 |
    | commit 67dc3c23d4327cfbb5bd0f21707a57b7e80e8430 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:02:21 2017 +0800          |
    |                                                 |
    |     cm_4                                        |
    |                                                 |
    | commit ade34cf8c89808cd273f73887ac60709fb2945c3 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:01:55 2017 +0800          |
    |                                                 |
    |     cm_3                                        |
    |                                                 |
    | commit 9607a0c96e08cd2a0abeaed1a808074d941a6e4f |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:01:21 2017 +0800          |
    |                                                 |
    |     cm_2                                        |
    |                                                 |
    | commit bd48b0665d771ea972447ce719f5eb4f0a532795 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:00:55 2017 +0800          |
    |                                                 |
    |     cm_1                                        |
    |                                                 |
    | commit cee1f617b6a8509e9c46585acc9137eb5e46be27 | ===> remote最新的commit只到"cm_0"
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 19:52:56 2017 +0800          |
    |                                                 |
    |     cm_0                                        |
    |_________________________________________________|
    ```
    但我只想push前2個commit(commit message為"cm_1" ~ "cm_2"), 則:
    ```
    git push origin 9607a0c96e08cd2a0abeaed1a808074d941a6e4f:master
      ===> 9607a0c(包含它自己)往前的那些新增的local commit都會進到remote, 也就是說
           只有"cm_1"和"cm_2"會進到remote, 但"cm_3"~"cm_5"不會
    ```


* 修改local端最新一次的commit (並非新增commit):
  注意! 必須在local端的commit尚未被push前!
  - 只是想改最新一次commit的message, 沒有檔案想提交(請先確保沒有檔案進入staged狀態), 然後:
    ```
    git commit --amend
      ===> 會進到編輯畫面讓你編輯最新一次commit的message, 但不會新增commit
    ```

  - 有檔案更動, 想將此檔案更動加進最新一次的commit(不想新增無謂的commit), 例如更動的檔案叫"file1.txt":
    ```
    git add file1.txt
    git commit --amend
    ```


* 交換commit順序:
  注意! 必須在local端欲被交換的commit尚未被push前!
  (假設你所在的local branch為"master" 且 remote repository為"origin" 且對應的remote branch為"master")
  - 假設"git log"顯示的資訊如下方框所示, 且remote最新的commit只到"cm_2"
    ```
    ___________________________________________________
    | commit b3f8145b4777f7c765a3b1cd3d651d4162b0d6b0 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:02:27 2017 +0800          |
    |                                                 |
    |     cm_5                                        |
    |                                                 |
    | commit 67dc3c23d4327cfbb5bd0f21707a57b7e80e8430 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:02:21 2017 +0800          |
    |                                                 |
    |     cm_4                                        |
    |                                                 |
    | commit ade34cf8c89808cd273f73887ac60709fb2945c3 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:01:55 2017 +0800          |
    |                                                 |
    |     cm_3                                        |
    |                                                 |
    | commit 9607a0c96e08cd2a0abeaed1a808074d941a6e4f | ===> remote最新的commit只到"cm_2"
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:01:21 2017 +0800          |
    |                                                 |
    |     cm_2                                        |
    |                                                 |
    | commit bd48b0665d771ea972447ce719f5eb4f0a532795 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:00:55 2017 +0800          |
    |                                                 |
    |     cm_1                                        |
    |                                                 |
    | commit cee1f617b6a8509e9c46585acc9137eb5e46be27 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 19:52:56 2017 +0800          |
    |                                                 |
    |     cm_0                                        |
    |_________________________________________________|
    ```
    我想將最新的3個commit(由新到舊依序是cm_5 -> cm_4 -> cm_3)的順序改成 cm_3 -> cm_5 -> cm_4 (由新到舊), 則:
    ```
    git rebase -i 9607a0c96e08cd2a0abeaed1a808074d941a6e4f
      ===> -i後面接的是不變動的commit的SHA-1, 也就是cm_2, 意即以cm_2作為base來調整cm_2之後(不含cm_2)的commits的意思
    ```
    接著會進入編輯畫面如下方框所示(和"git log"不同的是, 編輯畫面中是越新的commit越下面)
    ```
    __________________________________________________________________________
    | pick ade34cf cm_3                                                      |
    | pick 67dc3c2 cm_4                                                      |
    | pick b3f8145 cm_5                                                      |
    |                                                                        |
    | # Rebase 9607a0c..b3f8145 onto 9607a0c (3 command(s))                  |
    | #                                                                      |
    | # Commands:                                                            |
    | # p, pick = use commit                                                 |
    | # r, reword = use commit, but edit the commit message                  |
    | # e, edit = use commit, but stop for amending                          |
    | # s, squash = use commit, but meld into previous commit                |
    | # f, fixup = like "squash", but discard this commit's log message      |
    | # x, exec = run command (the rest of the line) using shell             |
    | #                                                                      |
    | # These lines can be re-ordered; they are executed from top to bottom. |
    | #                                                                      |
    | # If you remove a line here THAT COMMIT WILL BE LOST.                  |
    | #                                                                      |
    | # However, if you remove everything, the rebase will be aborted.       |
    | #                                                                      |
    | # Note that empty commits are commented out                            |
    |________________________________________________________________________|
    ```

    接著我們將有"pick"(如同註解所述, "pick"表 use commit)的那三行的順序改成如下方框所示
    ```
    __________________________________________________________________________
    | pick 67dc3c2 cm_4                                                      |
    | pick b3f8145 cm_5                                                      |
    | pick ade34cf cm_3                                                      |
    |                                                                        |
    | # Rebase 9607a0c..b3f8145 onto 9607a0c (3 command(s))                  |
    | #                                                                      |
    | # Commands:                                                            |
    | # p, pick = use commit                                                 |
    | # r, reword = use commit, but edit the commit message                  |
    | # e, edit = use commit, but stop for amending                          |
    | # s, squash = use commit, but meld into previous commit                |
    | # f, fixup = like "squash", but discard this commit's log message      |
    | # x, exec = run command (the rest of the line) using shell             |
    | #                                                                      |
    | # These lines can be re-ordered; they are executed from top to bottom. |
    | #                                                                      |
    | # If you remove a line here THAT COMMIT WILL BE LOST.                  |
    | #                                                                      |
    | # However, if you remove everything, the rebase will be aborted.       |
    | #                                                                      |
    | # Note that empty commits are commented out                            |
    |________________________________________________________________________|
    ```

    存擋退出後若出現成功訊息"Successfully rebased and updated refs/heads/master."
    你"git log"後就會發現這3個commit的順序(由新到舊)已經變成cm_3 -> cm_5 -> cm_4
    (但rebase後的SHA-1會改變)


* 合併commit:
  注意! 必須在local端欲被合併的commit尚未被push前!
  (假設你所在的local branch為"master" 且 remote repository為"origin" 且對應的remote branch為"master")
  - 假設"git log"顯示的資訊如下方框所示, 且remote最新的commit只到"cm_2"
    ```
    ___________________________________________________
    | commit de6d9b18ef9199a1f4e6f0c7228b523b6ea26f92 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Fri Jan 13 10:28:49 2017 +0800          |
    |                                                 |
    |     cm_6                                        |
    |                                                 |
    | commit 808209544ae38124cfd7a6b706176e026c02008b |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:02:27 2017 +0800          |
    |                                                 |
    |     cm_5                                        |
    |                                                 |
    | commit ced14cf58ddcac9cd660720c37e49afd67b2e804 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:02:21 2017 +0800          |
    |                                                 |
    |     cm_4                                        |
    |                                                 |
    | commit a487642a6b100527350aa7f5143ab35eb84ed0de |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:01:55 2017 +0800          |
    |                                                 |
    |     cm_3                                        |
    |                                                 |
    | commit 9607a0c96e08cd2a0abeaed1a808074d941a6e4f | ===> remote最新的commit只到"cm_2"
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:01:21 2017 +0800          |
    |                                                 |
    |     cm_2                                        |
    |                                                 |
    | commit bd48b0665d771ea972447ce719f5eb4f0a532795 |
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>    |
    | Date:   Thu Jan 12 20:00:55 2017 +0800          |
    |                                                 |
    |     cm_1                                        |
    |_________________________________________________|
    ```
    我想將cm_4, cm_5 合併進cm_3 (注意, Git只能將commit併進比較舊的commit, 不能併進比較新的commit), 則:
    ```
    git rebase -i 9607a0c96e08cd2a0abeaed1a808074d941a6e4f
      ===> -i後面接的是不變動的commit的SHA-1, 也就是cm_2, 意即以cm_2作為base來調整cm_2之後(不含cm_2)的commits的意思
    ```
    接著會進入編輯畫面如下方框所示(和"git log"不同的是, 編輯畫面中是越新的commit越下面)
    ```
    __________________________________________________________________________
    | pick a487642 cm_3                                                      |
    | pick ced14cf cm_4                                                      |
    | pick 8082095 cm_5                                                      |
    | pick de6d9b1 cm_6                                                      |
    |                                                                        |
    | # Rebase 9607a0c..de6d9b1 onto 9607a0c (4 command(s))                  |
    | #                                                                      |
    | # Commands:                                                            |
    | # p, pick = use commit                                                 |
    | # r, reword = use commit, but edit the commit message                  |
    | # e, edit = use commit, but stop for amending                          |
    | # s, squash = use commit, but meld into previous commit                |
    | # f, fixup = like "squash", but discard this commit's log message      |
    | # x, exec = run command (the rest of the line) using shell             |
    | #                                                                      |
    | # These lines can be re-ordered; they are executed from top to bottom. |
    | #                                                                      |
    | # If you remove a line here THAT COMMIT WILL BE LOST.                  |
    | #                                                                      |
    | # However, if you remove everything, the rebase will be aborted.       |
    | #                                                                      |
    | # Note that empty commits are commented out                            |
    |________________________________________________________________________|
    ```

    接下來將cm_4和cm_5前面的"pick"改成squash, 如下方框所示
    ```
    __________________________________________________________________________
    | pick a487642 cm_3                                                      |
    | squash ced14cf cm_4                                                    |
    | squash 8082095 cm_5                                                    |
    | pick de6d9b1 cm_6                                                      |
    |                                                                        |
    | # Rebase 9607a0c..de6d9b1 onto 9607a0c (4 command(s))                  |
    | #                                                                      |
    | # Commands:                                                            |
    | # p, pick = use commit                                                 |
    | # r, reword = use commit, but edit the commit message                  |
    | # e, edit = use commit, but stop for amending                          |
    | # s, squash = use commit, but meld into previous commit                |
    | # f, fixup = like "squash", but discard this commit's log message      |
    | # x, exec = run command (the rest of the line) using shell             |
    | #                                                                      |
    | # These lines can be re-ordered; they are executed from top to bottom. |
    | #                                                                      |
    | # If you remove a line here THAT COMMIT WILL BE LOST.                  |
    | #                                                                      |
    | # However, if you remove everything, the rebase will be aborted.       |
    | #                                                                      |
    | # Note that empty commits are commented out                            |
    |________________________________________________________________________|
    ```

    存檔離開後會出現編輯commit message畫面, 如下方框所示
    ```
    _____________________________________________________________________________________
    | # This is a combination of 3 commits.                                             |
    | # The first commit's message is:                                                  |
    | cm_3                                                                              |
    |                                                                                   |
    | # This is the 2nd commit message:                                                 |
    |                                                                                   |
    | cm_4                                                                              |
    |                                                                                   |
    | # This is the 3rd commit message:                                                 |
    |                                                                                   |
    | cm_5                                                                              |
    |                                                                                   |
    | # Please enter the commit message for your changes. Lines starting                |
    | # with '#' will be ignored, and an empty message aborts the commit.               |
    | #                                                                                 |
    | # Date:      Thu Jan 12 20:01:55 2017 +0800                                       |
    | #                                                                                 |
    | # rebase in progress; onto 9607a0c                                                |
    | # You are currently editing a commit while rebasing branch 'master' on '9607a0c'. |
    | #                                                                                 |
    | # Changes to be committed:                                                        |
    | # new file:   cm_3                                                                |
    | # new file:   cm_4                                                                |
    | # new file:   cm_5                                                                |
    | #                                                                                 |
    |___________________________________________________________________________________|
    ```

    這時就可以任意加入/修改自己想要的訊息, 例如我改成"Add cm_3, cm_4, and cm_5", 如下方框所示
    ```
    _____________________________________________________________________________________
    | Add cm_3, cm_4, and cm_5                                                          |
    |                                                                                   |
    | # Please enter the commit message for your changes. Lines starting                |
    | # with '#' will be ignored, and an empty message aborts the commit.               |
    | #                                                                                 |
    | # Date:      Thu Jan 12 20:01:55 2017 +0800                                       |
    | #                                                                                 |
    | # rebase in progress; onto 9607a0c                                                |
    | # You are currently editing a commit while rebasing branch 'master' on '9607a0c'. |
    | #                                                                                 |
    | # Changes to be committed:                                                        |
    | # new file:   cm_3                                                                |
    | # new file:   cm_4                                                                |
    | # new file:   cm_5                                                                |
    | #                                                                                 |
    |___________________________________________________________________________________|
    ```

    存擋離開後會出現"Successfully rebased and updated refs/heads/master."訊息, 表示合併成功,
    接下來你下"git log", 就會看到cm_3, cm_4, 和 cm_5已經合併成1個commit了


* tag操作
  - 列出所有tag:
    ```
    git tag
    ```

  - 看特定tag的commit資訊, 假設要看的tag是v0.4.15-release:
    ```
    git show v0.4.15-release
    ```

  - 對當前的commit標tag, 例如我想要的tag是"v0.4.15-release", 補充說明是"This is v0.4.15":
    ```
    git tag -a v0.4.15-release -m "This is v0.4.15"
    ```

  - push tag到遠端, 假設tag為'12345' (push commit並不會把tag push到遠端, tag一定要另外push):
    ```
    git push origin 12345
    ```

  - push local端所有tag到遠端 (push commit並不會把tag push到遠端, tag一定要另外push):
    ```
    git push origin --tags
    ```

  - delete local tag '12345':
    ```
    git tag -d 12345
    ```

  - delete remote tag '12345' (eg, GitHub version too):
    ```
    法1. git push --delete origin 12345
    法2. git push origin :refs/tags/12345
    ```




* 看commit的parent
  - 有個重要觀念先提, 除非你rebase, 否則單純做merge後commit的parent是不會變的!!!
    所以git log上看到的順序不一定代表parent順序! 僅會代表commit時間順序!
    所以 git diff若沒有用SHA比, 可能不會出現你(從git log上看)預期的結果
    例如: 我在master有個commit cm0, 然後我在cm0這個commit切了兩個branch, 一個叫br1, 另一個叫br2,
         我checkout到br1並新增一個commit叫cm1, 接下來我checkout到br2新增一個commit叫cm2,
         然後我checkout回master, 我在master先merge br1然後在merge br2, 最後master的log如下圖所示:
    ```
    ____________________________________________________________________________________
    | commit 4d339714827725a6896ae62a7cda12ab5c4c3103
    | Merge: 6f01bae bb19c44
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>
    | Date:   Fri Aug 4 17:29:25 2017 +0800
    | 
    |     Merge branch 'br1'
    | 
    | commit 6f01bae7d009a084b922479275aa812e22b04a74
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>
    | Date:   Fri Aug 4 17:28:46 2017 +0800
    | 
    |     cm2
    | 
    | commit bb19c444e66c77ce3f56b6ea73df1443589a0359
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>
    | Date:   Fri Aug 4 17:27:42 2017 +0800
    | 
    |     cm1
    | 
    | commit 0ee216fa3e7639abbd00b85d2b96bef2ad95e766
    | Author: Jimmy Tsai <jimmy_tsai@trend.com.tw>
    | Date:   Fri Aug 4 17:24:11 2017 +0800
    | 
    |     cm0
    |___________________________________________________________________________________
    ```
    這時你會發現
    ```
    git diff 6f01bae7d009a084b922479275aa812e22b04a74^ 6f01bae7d009a084b922479275aa812e22b04a74
    ```
    和
    ```
    git diff bb19c444e66c77ce3f56b6ea73df1443589a0359 6f01bae7d009a084b922479275aa812e22b04a74
    ```
    的結果是不一樣的(但從git log上看, 你會以為這兩個指令會得到一樣的結果, 因為merge後git log給你一種"cm1變成cm2的parent"的感覺)!
    原因是, "^" 和 "~" 指的都是parent, 而git merge是不會改變parent的!
    所以merge後, cm2的parent仍然是cm0, 而非cm1 !!! (除非你在br2 merge回master前先checkout到br2然後對master做rebase)


  - 看commit "8864bbf27c142136ddb36b0f917de75b6cdb03c4" 的所有parent:
    ```
    git rev-list --parents 8864bbf27c142136ddb36b0f917de75b6cdb03c4
    ```

  - 看commit "8864bbf27c142136ddb36b0f917de75b6cdb03c4" 的前1個parent
    ```
    git rev-list --parents -n 1 8864bbf27c142136ddb36b0f917de75b6cdb03c4
    ```

  - 看commit "8864bbf27c142136ddb36b0f917de75b6cdb03c4" 的前2個parent
    ```
    git rev-list --parents -n 2 8864bbf27c142136ddb36b0f917de75b6cdb03c4
    ```


* Open source社群常用的標準debug/patch流程:
  ```
  git checkout -b mybranch
  git commit -m "Insert a meaningful summary of changes here."
  git format-patch master --stdout > ~/patch-name.patch
  ```


* 看兩個branch是從哪個commit分出來的(也就是共同的ancestor)
  ```
  git merge-base dev General-v1.2
    ---> dev和General-v1.2都是branch name
  ```

* 看兩個commit共同的ancestor
  ```
  git merge-base b854bf 54b0b6
    ---> b854bf和54b0b6都是commit SHA1
  ```
