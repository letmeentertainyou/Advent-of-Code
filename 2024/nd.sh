#!/bin/bash

# This script copies the template for the given day and opens those files.
# NOTE: This could use a -o mode that opens the files in an existing dir.
dir_path="days/$1"

# Don't overwrite existing days.
if [ -d $dir_path ]; then
    echo "Directory $1 exists - exiting."
    exit -1
fi

echo "Creating day $1 from the template."
cp -r template $dir_path
rm $dir_path/utils.py

echo "Opening the new day in VSCode."
for file in $dir_path/*; do
    if [ -f "$file" ]; then 
        echo "Opening $file in code."
        code $file
    fi
done

# Can't do this in a sub shell but you can copy/paste it.
echo "cd $dir_path"