#!/bin/bash

data_dir=`echo $1 | sed 's/\/*$//g'` # pass the data directory (absolute path) in the 1st argument
cleaned_data_folder='cleaned_data'
cleaned_data_dir="$data_dir/$cleaned_data_folder"
ignore_user_folder='no_handle'
ignore_user_dir="$data_dir/$ignore_user_folder"
ignore_sdk_folder='formula-trend-*'
ignore_sdk_dir="$data_dir/$ignore_sdk_folder"
csv_name='driving_log.csv'
find_mindepth=2
find_maxdepth=2

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
echo "Remove the old '$cleaned_data_dir' ..."
rm -rf $cleaned_data_dir
echo -e "Create a new '$cleaned_data_dir' ...\n"
mkdir $cleaned_data_dir

echo '===== Clean data start'
csv_files=`find $data_dir -maxdepth $find_maxdepth -mindepth $find_mindepth -type f -name $csv_name ! -path */$ignore_user_folder/* ! -path */$ignore_sdk_folder/*`
for csv_file in $csv_files 
do
  src_dir=`dirname $csv_file`
  src_folder=`basename $src_dir`
  target_dir="$cleaned_data_dir/$src_folder"
  target_csv_file="$target_dir/$csv_name"
  cp -r $src_dir $target_dir
  sed -i '' 's/^.*IMG/IMG/g' $target_csv_file
  sed -i '' 's/\\/\//g' $target_csv_file # remove back slashes from windows system.
  echo "$target_dir done."
done
echo -e '===== Clean data end\n'
