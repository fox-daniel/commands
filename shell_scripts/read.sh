#!/bin/bash
CONTINUE="yes"
if [ "$CONTINUE" = "yes" ]; then
	echo $CONTINUE
else
	echo "oops"
fi


# while [ "$CONTINUE" = "y" ]; do
# 	echo "What is your favorite number?"
# 	read number
# 	echo "I prefer -3 to $number"
# 	echo "Do you want to continue? [y or n]"
# 	read $CONTINUE
# done