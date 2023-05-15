import unittest

from scapy.all import *

class TestExtractFeatures(unittest.TestCase):

    def test_extract_features_tcp(self):
        packet = IP(dst="192.168.1.1", src="192.168.1.2") / TCP(sport=80, dport=22)
        features = extract_features(packet)
        self.assertEqual(features[0], 4)
        self.assertEqual(features[1], 5)
        self.assertEqual(features[2], 0)
        self.assertEqual(features[3], 20)
        self.assertEqual(features[4], 0x2)
        self.assertEqual(features[5], 0)
        self.assertEqual(features[6], 64)
        self.assertEqual(features[7], 6)
        self.assertEqual(features[8], 80)
        self.assertEqual(features[9], 22)
        self.assertEqual(features[10], 12345)
        self.assertEqual(features[11], 65535)
        self.assertEqual(features[12], 0x2)
        self.assertEqual(features[13], 8192)

    def test_extract_features_udp(self):
        packet = IP(dst="192.168.1.1", src="192.168.1.2") / UDP(sport=53, dport=53)
        features = extract_features(packet)
        self.assertEqual(features[0], 4)
        self.assertEqual(features[1], 5)
        self.assertEqual(features[2], 0)
        self.assertEqual(features[3], 20)
        self.assertEqual(features[4], 0x2)
        self.assertEqual(features[5], 0)
        self.assertEqual(features[6], 64)
        self.assertEqual(features[7], 17)
        self.assertEqual(features[8], 53)
        self.assertEqual(features[9], 53)
        self.assertEqual(features[10], 0)
        self.assertEqual(features[11], 0)
        self.assertEqual(features[12], 0)
        self.assertEqual(features[13], 0)

if __name__ == "__main__":
    unittest.main()
