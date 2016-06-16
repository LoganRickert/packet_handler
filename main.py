#!/usr/bin/env python

import packet_handler

def primary_function(packet):
    print packet.get_obj()
    """
        Other information you can extract:
        
            print packet.get_src_ip()
            print packet.get_dst_ip()
            print packet.get_protocol()
            print packet.get_time()
            print packet.get_payload()
    """

if __name__ == '__main__':
    directory = raw_input("Directory> ")
    main = packet_handler.Main(directory)
    main.run(primary_function)
