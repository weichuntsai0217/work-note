alias ll='ls -alFh'
alias backupzeta='node /Users/jimmy_tsai/projects/work-note/utils/backupzeta.js $(PWD)'
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

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/jimmy_tsai/google-cloud-sdk/path.bash.inc' ]; then source '/Users/jimmy_tsai/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/jimmy_tsai/google-cloud-sdk/completion.bash.inc' ]; then source '/Users/jimmy_tsai/google-cloud-sdk/completion.bash.inc'; fi

dcbash() {
  local container_name="$1"
  if [ -z "$container_name" ]; then
    echo "Please provide the container name in the 1st argument."
    echo "For example, dkbash my_container"
    return 1
  else
    docker exec -it $container_name bash
  fi
}

sptt() {
  local arg="$1"
  if [ "$arg" == '2' ]; then
    ssh bbsu@ptt2.cc
  else
    ssh bbsu@ptt.cc
  fi
}
