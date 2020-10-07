#!/bin/bash
letters=ABC
echo "The first three letters are ${letters}."

file_name='file_'$(/bin/date +%Y-%m-%d)
echo "A file named '$file_name' was created."
touch $file_name

touch file_$1.txt
touch file_$2.csv