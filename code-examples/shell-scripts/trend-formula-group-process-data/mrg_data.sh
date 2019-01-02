#!/bin/bash

data_dir=`echo $1 | sed 's/\/*$//g'` # pass the data directory (absolute path) in the 1st argument
script_dir=$PWD
target_dir="$script_dir/../app/data"
tmp_dir="$script_dir/../app/data/tmp"
ignore_user_folder='no_handle'
ignore_user_dir="$data_dir/$ignore_user_folder"
ignore_sdk_folder='formula-trend-*'
ignore_sdk_dir="$data_dir/$ignore_sdk_folder"
find_mindepth=1
find_maxdepth=1
csv_header='center,steering,throttle,brake,speed,time,lap'
csv_name='driving_log.csv'
target_csv_file="$target_dir/$csv_name"
line_head='IMG' # the data you want to merge should be cleaned first.
data_list="$target_dir/datalist.txt"

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

echo "The source data directory is '$data_dir'"
echo "The target data directory is '$target_dir'"

echo "Remove the old '$target_dir' ..."
rm -rf $target_dir || true

echo -e "Create a new '$target_dir'\n"
mkdir $target_dir

echo '===== Merge data start'
src_tgzs=`find $data_dir -maxdepth $find_maxdepth -mindepth $find_mindepth -type f -name *.tar.gz ! -path $ignore_user_dir ! -path $ignore_sdk_dir`
echo $csv_header > $target_csv_file
touch $data_list
for src_tgz in $src_tgzs
do
  rm -rf $tmp_dir || true
  mkdir $tmp_dir
  tar -zx -f $src_tgz -C $tmp_dir
  tail_name="__from_`basename $src_tgz | sed 's/\./_/g'`"
  untgz_dir=`find $tmp_dir -maxdepth $find_maxdepth -mindepth $find_mindepth -type d ! -path $ignore_user_dir ! -path $ignore_sdk_dir`
  head_name=`basename $untgz_dir`
  final_folder="$head_name$tail_name" # this line is to prevent duplicated folder name after uncompress data.
  final_dir="$target_dir/$final_folder"
  mv $untgz_dir $final_dir
  tmp_csv_file="$final_dir/$csv_name"
  new_line_head="$final_folder\\/$line_head"
  cat $tmp_csv_file | sed "s/^$line_head/$new_line_head/g" >> $target_csv_file 
  rm -rf $tmp_dir || true
  echo `basename $src_tgz` >> $data_list
  echo "$final_dir is done."
done
echo -e "===== Merge data end, all *.tar.gz you used is recorded in '$data_list'.\n"
