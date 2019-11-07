#subnetRange
import logging
class subnetRange:
    """
    isThisSubnet CLASS:\n\t
    This class initiated with one value:\tsubnetString - 98.210.237.192/26\n\t
    accessible CLASS Attributes:\n\t
    block - the block value from CIDR : ipv4/block
    networkIp - the Network ip of subnet
    broadcastIp - teh Broadcast ip of subnet
    longNetworkIp - the long/decimal value of the networkIp
    longBroadcastIp - the long/decimal value of the broadcastIp
    """
    __bitLookUp = {
        0:128,
        1:64,
        2:32,
        3:16,
        4:8,
        5:4,
        6:2,
        7:1
    }
    __subnetMask = {}
    __primaryOctet = None
    __networkValueSum = 0
    #__ipRange = {}
    def __init__(self,subnetString):
        try:
            __subnetStringSplit = subnetString.split("/")
            self.__ipAddress = __subnetStringSplit[0]
            logging.debug("CLASS subnetRange:__init__,ipAddress="+str(self.__ipAddress))
            self.__ipAddressOctetDict = self.__getIpAddressOctetDict()
            logging.debug("CLASS subnetRange:__init__,ipAddressOctetDict="+str(self.__ipAddressOctetDict))
            self.block = int(__subnetStringSplit[1])
            logging.debug("CLASS subnetRange:__init__,block="+str(self.block))
            self.__bitRotatedBinaryString = self.__getBitRotatedBinaryString()
            logging.debug("CLASS subnetRange:__init__,turnedOnBitRotated="+str(self.__bitRotatedBinaryString))
            self.__bitRotatedBinaryOctetDict = self.__getBitRotatedBinaryOctetDict()
            logging.debug("CLASS subnetRange:__init__,bitRotatedBinaryOctetDict="+str(self.__bitRotatedBinaryOctetDict))
            self.__focusValue = self.__getFocusValue()
            logging.debug("CLASS subnetRange:__init__,focusValue="+str(self.__focusValue))
            self.__binaryNetworkValue = self.__getBinaryNetworkValue()
            logging.debug("CLASS subnetRange:__init__,binaryNetworkValue="+str(self.__binaryNetworkValue))
            self.__broadcastValue = self.__getBroadcastValue()
            logging.debug("CLASS subnetRange:__init__,broadcastValue="+str(self.__broadcastValue))
            self.networkIp = self.__getIp("network")
            logging.debug("CLASS subnetRange:__init__,networkIp="+str(self.networkIp))
            self.broadcastIp = self.__getIp("broadcast")
            logging.debug("CLASS subnetRange:__init__,broadcastIp="+str(self.broadcastIp))
            self.maxHosts = self.__GetMaxHosts()
            logging.debug("CLASS subnetRange:__init__,maxHosts="+str(self.maxHosts))
            self.__networkDict = self.__getIpAddressOctetDict(self.networkIp)
            logging.debug("CLASS subnetRange:__init__,networkDict="+str(self.__networkDict))
            self.__broadcastDict = self.__getIpAddressOctetDict(self.broadcastIp)
            logging.debug("CLASS subnetRange:__init__,broadcastDict="+str(self.__broadcastDict))
            self.__binaryNetworkIp = self.__getBinaryValueOfIp(self.__networkDict)
            logging.debug("CLASS subnetRange:__init__,binaryNetworkIp="+str(self.__binaryNetworkIp))
            self.__binaryBroadcastIp = self.__getBinaryValueOfIp(self.__broadcastDict)
            logging.debug("CLASS subnetRange:__init__,binaryBroadcastIp="+str(self.__binaryBroadcastIp))
            self.longNetworkIp = self.__getLongValueOfBinaryValue(self.__binaryNetworkIp)
            logging.debug("CLASS subnetRange:__init__,longNetworkIp="+str(self.longNetworkIp))
            self.longBroadcastIp = self.__getLongValueOfBinaryValue(self.__binaryBroadcastIp)
            logging.debug("CLASS subnetRange:__init__,longBroadcastIp="+str(self.longBroadcastIp))
        except IndexError:
            logging.error("CLASS subnetRange:subnetString="+str(subnetString)+",\'/\'SPLIT FAILED")
    def __getBitRotatedBinaryString(self):
        """This provate method return a binary string based on the block value\n\t
        If block value is 26, the value 11111111111111111111111111000000 as string
        """
        maxBit = 32
        rotatedBlock = ""
        for i in range(maxBit):
            if i < self.block:
                rotatedBlock += "1"
            else:
                rotatedBlock += "0"
        logging.debug("CLASS subnetRange:__getBitRotated,rotatedBlock="+str(rotatedBlock))
        return rotatedBlock
    def __getBitRotatedBinaryOctetDict(self):
        """This is a private method that updates the subnetMask(dict) based on the __bitRotatedBinaryString and also maintains a dict with octet values of it(__bitRotatedBinaryOctetDict).
        if BitRotatedBinaryString is 11111111111111111111111111000000, subnetMask={0: 255, 8: 255, 16: 255, 24: 192} and bitRotatedBinaryOctetDict={0: '11111111', 8: '11111111', 16: '11111111', 24: '11000000'}
        """
        bitRotatedBinaryOctetDict ={}
        for i in range(0, len(self.__bitRotatedBinaryString), 8):
            bitRotatedBinaryOctetDict[i] = self.__bitRotatedBinaryString[i:i+8]
            self.__subnetMask[i] = int(bitRotatedBinaryOctetDict[i],2)
        logging.debug("CLASS subnetRange:__getBitRotatedBinaryOctetDict,bitRotatedBinaryOctetDict="+str(bitRotatedBinaryOctetDict))
        logging.debug("CLASS subnetRange:__getBitRotatedBinaryOctetDict,subnetMask="+str(self.__subnetMask))
        return bitRotatedBinaryOctetDict
    def __getIpAddressOctetDict(self,ipAddr=None):
        """This is a private method that returns decimal values as a dicts based on ip address provided or takes the constructor __ipAddress value.
        if ipAddr = 98.210.237.192, ipAddressOctetDict={0: '98', 8: '210', 16: '237', 24: '192'}
        """
        if ipAddr == None:
            ipAddr = self.__ipAddress
        ipAddressOctetDict ={}
        ipAddressSplit = ipAddr.split(".")
        for i in range(len(ipAddressSplit)):
            ipAddressOctetDict[i*8] = ipAddressSplit[i]
        logging.debug("CLASS subnetRange:__getIpAddressOctetDict,ipAddressOctetDict="+str(ipAddressOctetDict))
        return ipAddressOctetDict
    def __getFocusValue(self):
        """This is a private method that returns the key of the subnetmask from where the networkIp and BroadcastIp can be determined.
        If subnetMask={0: 255, 8: 255, 16: 255, 24: 192}, returns subnetMask[24] = 192
        """
        po = {}
        for o,v in self.__subnetMask.items():
            if(v < 255 and v >= 0):
                po[o] = v
        pok = max(po, key=po.get)
        self.__primaryOctet = pok
        logging.debug("CLASS subnetRange:__getFocusValue,pok="+str(pok))
        logging.debug("CLASS subnetRange:__getFocusValue,primaryOctet="+str(self.__primaryOctet))
        return self.__subnetMask[pok]
    def __getBinaryNetworkValue(self):
        """This is a private method that returns the networkValue (for the newtork ip ) using the focus value.
        The __bitLookUp dict is used, beginning with key 0, the difference is determined and 1 is returned if difference > 0 and the next key is deducted in similar manner, 0 is returned if not.
        The network value is determined by AND'ing the binary value and focus value using the mulBinSum inner-method.
        """
        def mulBinSum(i1,i,j):
            if int(i)*int(j):
                self.__networkValueSum += self.__bitLookUp[i1]
                return "1"
            else:
                return "0"
        binaryNetworkValue = ""
        startVal = int(self.__focusValue)
        binaryFocusValue = format(int(self.__focusValue),'b')
        binaryMul = ""
        for i in range(8):
            diffVal = (startVal - self.__bitLookUp[i])
            if(diffVal < 0):
                bnv = "0"
            else:
                startVal = diffVal
                bnv = "1"
            binaryNetworkValue += bnv
            binaryMul += mulBinSum(i,binaryFocusValue[i],bnv)
        logging.debug("CLASS subnetRange:__getBinaryNetworkValue,binaryNetworkValue="+str(binaryNetworkValue))
        logging.debug("CLASS subnetRange:__getBinaryNetworkValue,binaryMul="+str(binaryMul))
        logging.debug("CLASS subnetRange:__getBinaryNetworkValue,networkValueSum="+str(self.__networkValueSum))
        return binaryNetworkValue
    def __getBroadcastValue(self):
        """This private method determines the broadcast value(used for broadcast ip) using the __binaryNetworkValue & __networkValueSum
        The minimum __bitLookUp value is determined and added to the __networkValueSum, finally deducting 1 from it
        """
        bv = {}
        for i in range(len(self.__binaryNetworkValue)):
            if self.__binaryNetworkValue[i] == "1":
                bv[i] = self.__bitLookUp[i]
        logging.debug("CLASS subnetRange:__getBroadcastValue,bv="+str(bv))
        minVal = min(bv, key=bv.get)
        logging.debug("CLASS subnetRange:__getBroadcastValue,minVal="+str(minVal))
        broadcastValue = self.__networkValueSum + bv[minVal] - 1
        logging.debug("CLASS subnetRange:__getBroadcastValue,broadcastValue="+str(self.__networkValueSum))
        return broadcastValue
    def __getIp(self,choice):
        """This private method returnd the network ip ot broadcast ip in the dotted decimal fashion based on choice
        """
        choiceDict = {
            "network":self.__networkValueSum,
            "broadcast":self.__broadcastValue
        }
        value = choiceDict[choice]
        valueIp = ""
        c = 0
        def addDot(c):
            if c < 4:
                return "."
            else:
                return ""
        for k in self.__subnetMask:
            if(self.__subnetMask[k] == 0):
                valueIp += "0"
                c +=1
                valueIp += addDot(c)
            elif(self.__subnetMask[k] == 255):
                valueIp += self.__ipAddressOctetDict[k]
                c += 1
                valueIp += addDot(c)
            else:
                valueIp += str(value)
                c += 1
                valueIp += addDot(c)
        return valueIp
    def __GetMaxHosts(self):
        """This private method returns the maximum number of hosts that are possibly usable in a subnet based on block value
        """
        maxHosts = 2**(32-int(self.block))-2
        logging.debug("CLASS subnetRange:__maxHosts,maxHosts="+str(maxHosts))
        return maxHosts
    def __getBinaryValueOfIp(self,ipAddrOctetDict):
        """This is a private method that returns an ip address for the provided octet dict
        """
        binVal = ""
        try:
            for k in ipAddrOctetDict:
                binVal += bin(int(ipAddrOctetDict[k])).split(("0b"))[1]
            return binVal
        except IndexError:
            logging.error("CLASS subnetRange:__getBinaryValueOfIp,Input Error,ipAddrOctetDict="+str(ipAddrOctetDict))
    def __getLongValueOfBinaryValue(self,binaryValue):
        """This is a private method that returns the decimal/long value of a binary input
        input - binaryValue
        """
        logging.debug("CLASS subnetRange:__getLongValueOfBinaryValue,binaryValue="+str(binaryValue))
        return int(binaryValue,2)