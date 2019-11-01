#testHExConvert
from hexConvert import hexConvert
import unittest
import logging
import sys
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
    def testGetIpLong(self):
        longSample = '14264566700'
        test_getIp = hexConvert(longSample).getIp()
        print(test_getIp)
        self.assertEqual(test_getIp,self.sampleIp)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    unittest.main()