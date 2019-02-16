alias ll='ls -alFh'
# alias backupzeta='node /Users/jimmy_tsai/projects/work-note/utils/backupzeta.js $(PWD)'
alias grep='grep --color=always'
export CLICOLOR="true"
export LSCOLORS="gxfxcxdxbxegedabagacad"

if [ -f ~/.git-completion.bash ]; then
  . ~/.git-completion.bash
fi
export M2_HOME=/opt/apache-maven
export PATH=$M2_HOME/bin:$PATH
export JAVA_HOME="$(/usr/libexec/java_home)"

export PATH="/Applications/HPE_Security/Fortify_SCA_and_Apps_17.10/bin:$PATH"
export PATH="$HOME/Library/Python/3.7/bin:$PATH"

dcbash() {
  local container_name="$1"
  if [ -z "$container_name" ]; then
    echo "Please provide the container name in the 1st argument."
    echo "For example, dcbash my_container"
    return 1
  else
    docker start $container_name
    docker exec -it $container_name bash
  fi
}

dcrm() {
  local args="$@"
  for ctn in $args; do
    docker stop $ctn
    docker rm $ctn
  done
}

sptt() {
  local arg="$1"
  if [ "$arg" == '2' ]; then
    ssh bbsu@ptt2.cc
  else
    ssh bbsu@ptt.cc
  fi
}
