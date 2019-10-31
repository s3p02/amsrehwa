#hexConvert
import logging
class hexConvert:
    """\n
    This class is initialized with a hexadecimal input, hexNumber. Has the following methods:
    1. get()
    2. getList()
    3.getIp()
    \n"""
    def __init__(self, hexNumber):
        self.hexNumber = hexNumber
        logging.debug("CLASS hexConvert:__init__,hexNumber="+str(hexNumber))
    
    def get(self):
        """\n
        This method returns the binary value of the hexa-decimal input.
        \n"""
        getResult = format(int(self.hexNumber,16),'b')
        logging.debug("CLASS hexConvert:get,getResult="+str(getResult))
        return getResult
    
    def getList(self):
        """\n
        This method returns the binary value of the hexa-decimal input as a list of binary values, 4 values of 8 bits each.
        \n"""
        getResult = format(int(self.hexNumber,16),'b')
        logging.debug("CLASS hexConvert:get,getResult="+str(getResult))
        getResultList = [(getResult[i:i+8]) for i in range(0, len(getResult), 8)]
        logging.debug("CLASS hexConvert:get,getResultList="+str(getResultList))
        return getResultList
    
    def getIp(self):
        """\n
        This method returns the ip address of the hexa-decimal input.
        \n"""
        ipAddress = ""
        c = 3
        binNumberList = self.getList()
        for i in binNumberList:
            ipAddress = ipAddress+str(int(i,2))
            if(c != 0):
                ipAddress += "."
                c -= 1
        logging.debug("CLASS hexConvert:getIp,ipAddress="+str(ipAddress))
        return ipAddress