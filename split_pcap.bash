#!/bin/bash

## Written by Logan Rickert
## June 15th, 2016

# The function that splits up the files
split_pcap() {
    # -C 1 is how large the largest file is. In this case, 1 Megabyte.
    tcpdump -r $1 -w $2/pcap -C 1
}

# If there is no first argument, throw an error.
if [ -z "$1" ];
then
    echo "Error: ./$0 <directoryname>"
    exit 0;
fi

# Keep count of directory names.
i=0

# Go through each file in given directory and split the file.
for f in $1/*.gz.pcap
do
    echo Spliting file $f
    mkdir -p pcap$i
    split_pcap $f pcap$i
    i=$((i+1))
done
