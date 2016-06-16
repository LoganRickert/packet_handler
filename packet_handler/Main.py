#!/usr/bin/env python

from pcapfile import savefile
from Packet import Packet
import glob

class Main:
    
    def __init__(self, directory):
        self.files = self._get_files(directory)
    
    def run(self, primary_function):
        """
            Go through each file in the given directory
            that starts with pcap and for each packet
            pass it to the function primary function.
        """
        try:
            from pcapfile import savefile
        except ImportError:
            print "[-] Error: Make sure you have pcapfile installed!"
            print "[-] pip install pypcapfile"
            exit(0)
        
        for filename in self.files:
            print "Opening with", filename
            capfile = open(filename, 'rb')
            cap = savefile.load_savefile(capfile, verbose=True)
            
            for packet in cap.packets:
                primary_function(Packet(packet))
            
            capfile.close()
    
    def _get_files(self, directory):
        """
            Get a list of files that start with pcap.
        """
        return glob.glob(directory + '/pcap*')

