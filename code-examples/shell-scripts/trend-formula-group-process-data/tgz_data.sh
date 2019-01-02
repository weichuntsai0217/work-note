#!/bin/bash

data_dir=`echo $1 | sed 's/\/*$//g'` # pass the data directory (absolute path) in the 1st argument
ignore_user_folder='no_handle'
ignore_user_dir="./$ignore_user_folder"
ignore_sdk_folder='formula-trend-*'
ignore_sdk_dir="./$ignore_sdk_folder"
ignore_clean_folder='cleaned_data'
ignore_clean_dir="./$ignore_clean_folder"
find_mindepth=1
find_maxdepth=1
script_dir=$PWD

if [ "$data_dir" == '' ]; then
  # Error message for empty arguments
  echo -e '[ERROR] Please provide the source data directory (absolute path) in the 1st argument.\n'
  exit 1
fi

if [ ! -d "$data_dir" ]; then
  # Error message for wrong arguments
  echo -e "[ERROR] the source data directory '$data_dir' does not exist.\n"
  exit 1
fi

echo "The data directory you choose is '$data_dir'"

echo '===== Compress data start'
cd $data_dir
src_dirs=`find . -maxdepth $find_maxdepth -mindepth $find_mindepth -type d ! -path $ignore_user_dir ! -path $ignore_sdk_dir ! -path $ignore_clean_dir`
for src_dir in $src_dirs
do
  tar -zc -f $src_dir.tar.gz $src_dir
  echo "$src_dir => $src_dir.tar.gz"
done
echo -e '===== Compress data end\n'
cd $script_dir
# echo $script_dir
