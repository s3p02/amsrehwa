#hexConvert
import logging
class hexConvert:
    """\n
    hexConvert class is initialized with a hexadecimal input, hexNumber eg: 0x62D2ED4B\n\t
    hexNumber - input\n\t
    ipAddr - Calls the __hex2decimal2Ip method to obtain the ip in dotted decimal format\n\t
    longIpAddr - is the long/decimal value of the hexNumber\n\t
    hexConvert class has the following methods:\n\t
    1. get() --> returns ip-address of hexNumber\n\t
    """
    __octetDecimalDict = {}
    def __init__(self, hexNumber):
        self.hexNumber = hexNumber
        logging.debug("CLASS hexConvert:__init__,hexNumber="+str(hexNumber))
        self.ipAddr = self.__hex2decimal2Ip()
        logging.debug("CLASS hexConvert:__init__,ipAddr="+str(self.ipAddr))
        self.longIpAddr = int(self.hexNumber,16)
        logging.debug("CLASS hexConvert:__init__,longIpAddr="+str(self.longIpAddr))
    
    def __hex2decimal2Ip(self):
        """ private method that converts hexadecimal value to decimal ip\n
        example: 0x62D2ED4B --> 98.120.237.75
        """
        ipAddrCount = 0
        ipAddr = ""
        try:
            _hexSplit0x = self.hexNumber.split('0x')[1]
            for i in range(0, len(_hexSplit0x), 2):
                self.__octetDecimalDict[i] = int(_hexSplit0x[i:i+2],16)
                ipAddr += str(self.__octetDecimalDict[i])
                ipAddrCount += 1
                if ipAddrCount < 4:
                    ipAddr += "."
        except IndexError:
            logging.error("CLASS hexConvert:__hex2decimalIp,Input not in format 0x________,hexNumber="+str(self.hexNumber))
            pass
        logging.debug("CLASS hexConvert:hex2decimalDict,_octetDecimalDict="+str(self.__octetDecimalDict))
        logging.debug("CLASS hexConvert:hex2decimalDict,ipAddr="+str(ipAddr))
        return ipAddr
    def get(self):
        """\n
        This method returns the ip-address of the hexa-decimal input.
        \n"""
        logging.debug("CLASS hexConvert:get,ipAddr="+str(self.ipAddr))
        return self.ipAddr