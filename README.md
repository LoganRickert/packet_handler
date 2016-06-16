
# Packet Handler

This is a simple application that works with the supplied pcap files.
This will probably not work with all pcap files.

## Installation

Make sure you have the following things installed:

* pip install pypcapfile
* python2.7

## Requirements

Before running, make sure you run `split_pcap.bash`.

### Running split_pcap.bash

Create a directory called gzpcaps and place all of your `.gz.pcap` files in 
this directory. From there, all you need to do is run the following command:

```./split_pcap.bash gzpcaps```

This will create a pcap[number] folder for each `.gz.pcap` file. In each folder
you will find the original `.gz.pcap` file split into multiple files, each file
no larger than 1 Megabyte. This is to make the files easier to work with
and take up way less memory.

## Modifying the Program

In `main.py` you will find the following function:

```
def primary_function(packet):
    print packet.get_obj()
```

this is where you should write your code. When you run main.py, you will be
prompted to enter a directory. You should enter a pcap[number] directory.
For every sequential packet this function will be called and will pass
that packet as a `Packet` object.

You can call the following functions on the packet object and it will
return the data.

```
# Returns the source IP of the packet.
temp = packet.get_src_ip()

# Returns the destination ip of the packet.
temp = packet.get_dst_ip()

# Returns the protocol for the packet. ('UDP', 'TCP', etc)
temp = packet.get_protocol()

# Returns the EPOCH time the packet arrived.
temp = packet.get_time()

# Returns the payload contents in hex.
temp = packet.get_payload()
```

## Running The Program

To run the program, just do:

```
python main.py
```
