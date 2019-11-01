#testHExConvert
from hexConvert import hexConvert
from subnetRange import subnetRange
from isThisSubnet import isThisSubnet
import unittest
import logging
import sys
"""
class testHexConvert(unittest.TestCase):
    sample = '0x62D2ED4B'
    sampleBin = '1100010110100101110110101001011'
    sampleResultList = ['11000101','10100101','11011010','1001011']
    sampleNullList = []
    sampleIp = "197.165.218.75"
    def testInit(self):
        test_init = hexConvert(self.sample)
        self.assertEqual(test_init.hexNumber,self.sample)
    def testGet(self):
        test_get = hexConvert(self.sample).get()
        self.assertEqual(test_get,self.sampleBin)
    def testGetList(self):
        
        test_getList = hexConvert(self.sample).getList()
        self.assertEqual(test_getList,self.sampleResultList)
        self.assertNotEqual(test_getList,self.sampleNullList)
    def testGetIp(self):
        test_getIp = hexConvert(self.sample).getIp()
        self.assertEqual(test_getIp,self.sampleIp)
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
        self.assertNotEqual(test_init.broadcastIp,test_init4.broadcastIp)"""
class test_isThisSubnet(unittest.TestCase):
    sampleInput = '0x62D2ED4B'
    sampleCidrSubnet = '98.210.237.192/26'
    sampleInSubnet = '0x62D2EDC1'
    result = False
    resultInSubnet = True
    def testInit(self):
        #compute = isThisSubnet(self.sampleInput,self.sampleCidrSubnet)
        #self.assertEqual(compute.verify(),self.result)
        compute2 = isThisSubnet(self.sampleInSubnet,self.sampleCidrSubnet)
        self.assertEqual(compute2.verify(),self.resultInSubnet)
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    unittest.main()