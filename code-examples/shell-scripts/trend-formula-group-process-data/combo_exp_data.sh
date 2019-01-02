#!/bin/bash

data_dir=`echo $1 | sed 's/\/*$//g'` # pass the data directory (absolute path) in the 1st argument
cleaned_data_folder='cleaned_data'
cleaned_data_dir="$data_dir/$cleaned_data_folder"

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

./cln_data.sh $data_dir
./tgz_data.sh $cleaned_data_dir
./mrg_data.sh $cleaned_data_dir
