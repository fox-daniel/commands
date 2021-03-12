#!/bin/bash

for f in hello* 
do
	echo "Executing $f"
	./$f
done