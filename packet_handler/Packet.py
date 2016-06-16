#!/usr/bin/env python

from decimal import Decimal

class Packet:
    
    def __init__(self, pkt):
        self.payload = pkt.packet
        self.pkt_time = pkt.timestamp + Decimal('.' + str(pkt.timestamp_ms))
        self.src_ip = self.payload[56:64]
        self.dst_ip = self.payload[64:72]
        self.protocol = self.payload[50:52]
        self.real_payload = self.payload[88:]
        
        self.protoenum = {
            '01': 'ICMP',
            '11': 'UDP',
            '06': 'TCP',
            '29': 'IPv6',
        }
    
    def get_src_ip(self):
        return '.'.join(
            map(lambda x: str(int(x, 16)),
            self._get_ip_array(self.src_ip))
        )
    
    def get_dst_ip(self):
        return '.'.join(
            map(lambda x: str(int(x, 16)),
            self._get_ip_array(self.dst_ip))
        )
        
    def get_protocol(self):
        if ''.join(self.protocol) in self.protoenum:
            return self.protoenum[''.join(self.protocol)]
        else:
            return 'Unknown protocol:', ''.join(self.protocol), '. Refer to: https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers'
    
    def get_time(self):
        return self.pkt_time
        
    def get_payload(self):
        return ''.join(temp)
        
    def get_obj(self):
        return {
            'src_ip': self.get_src_ip(),
            'dst_ip': self.get_dst_ip(),
            'proto': self.get_protocol(),
            'time': self.get_time(),
            'payload': self.get_payload()
        }
    
    def _get_ip_array(self, ip):
        return [
            ip[0] + ip[1],
            ip[2] + ip[3],
            ip[4] + ip[5],
            ip[6] + ip[7]
        ]
