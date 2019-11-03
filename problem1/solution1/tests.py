#testHExConvert
from hexConvert import hexConvert
from subnetRange import subnetRange
from isThisSubnet import isThisSubnet
import unittest
import logging
import sys
class testHexConvert(unittest.TestCase):
    sample = '0x62D2ED4B'
    sampleIp = '98.210.237.75'
    def testInit(self):
        test_init = hexConvert(self.sample)
        self.assertEqual(test_init.hexNumber,self.sample)
        self.assertEqual(test_init.ipAddr,self.sampleIp)
class testSubnetRange(unittest.TestCase):
    sample = '98.210.237.192/26'
    sample2sameSubnet = '98.210.237.193/26'
    sample3sameSubnet = '98.210.237.254/26'
    sampleForCompare = '197.165.218.75/26'
    ip = '98.210.237.192'
    block = 26
    binaryString = "11111111111111111111111111000000"
    bitRotatedBinaryOctetDict = {0: '11111111', 8: '11111111', 16: '11111111', 24: '11000000'}
    ipAddressOctetDict={0: '98', 8: '210', 16: '237', 24: '192'}
    #subnetMaskList = ["255","255","255","192"]
    networkIp = "98.210.237.192"
    broadcastIp = "98.210.237.255"
    def testInit(self):
        test_init = subnetRange(self.sample)
        self.assertEqual(test_init.ipAddress,self.ip)
        self.assertNotEqual(test_init.ipAddress,'98.210.237.197')
        self.assertEqual(test_init.block,self.block)
        self.assertNotEqual(test_init.block,29)
        self.assertEqual(test_init.bitRotatedBinaryString,self.binaryString)
        self.assertEqual(test_init.bitRotatedBinaryOctetDict,self.bitRotatedBinaryOctetDict)
        test_init2 = subnetRange(self.sample2sameSubnet)
        self.assertEqual(test_init.networkIp,test_init2.networkIp)
        self.assertEqual(test_init.broadcastIp,test_init2.broadcastIp)
        test_init3 = subnetRange(self.sample3sameSubnet)
        self.assertEqual(test_init.networkIp,test_init3.networkIp)
        self.assertEqual(test_init.broadcastIp,test_init3.broadcastIp)
        test_init4 = subnetRange(self.sampleForCompare)
        self.assertNotEqual(test_init.networkIp,test_init4.networkIp)
        self.assertNotEqual(test_init.broadcastIp,test_init4.broadcastIp)
class test_isThisSubnet(unittest.TestCase):
    sampleInput = '0x62D2ED4B'
    sampleCidrSubnet = '98.210.237.192/26'
    result = True
    def testVerify(self):
        compute = isThisSubnet(self.sampleInput,self.sampleCidrSubnet)
        self.assertEqual(compute.verifyNetworkAndBroadcast(),self.result)
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    unittest.main()