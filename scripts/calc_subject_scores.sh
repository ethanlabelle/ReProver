#!/bin/bash

if [ -z "$1" ]
    then
        echo "specify ../experiments subdir"
	exit -1
fi
for res in ../experiments/"$1"/*; do
    python3 stats.py "$res"
done
