#!/bin/bash

if [[ $# -lt 2 ]]; then
    echo "Requires at least two command line arguments (and a 3rd optional one)!"
    echo "ex. "
    echo "    bash copy_files.sh <copy_path> <file_list> (<script_path>)"
    exit 1
fi

copy_path=$1
file_list=$2
if [[ $# -lt 3 ]]; then
    script_path=~/work/hpcutils
else
    script_path=$3
fi

while read -r file; do
    path=`basename $(dirname $file)`
    python3 $script_path/pllxrdcp.py -r $file $copy_path/$path
done < $file_list
