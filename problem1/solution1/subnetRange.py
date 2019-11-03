#subnetRange
import logging
class subnetRange:
    bitLookUp = {
        0:128,
        1:64,
        2:32,
        3:16,
        4:8,
        5:4,
        6:2,
        7:1
    }
    subnetMask = {}
    primaryOctet = None
    networkValueSum = 0
    ipRange = {}
    def __init__(self,subnetString):
        try:
            subnetStringSplit = subnetString.split("/")
            self.ipAddress = subnetStringSplit[0]
            logging.debug("CLASS subnetRange:__init__,ipAddress="+str(self.ipAddress))
            self.ipAddressOctetDict = self.__getIpAddressOctetDict()
            logging.debug("CLASS subnetRange:__init__,ipAddressOctetDict="+str(self.ipAddressOctetDict))
            self.block = int(subnetStringSplit[1])
            logging.debug("CLASS subnetRange:__init__,block="+str(self.block))
            self.bitRotatedBinaryString = self.__getBitRotatedBinaryString()
            logging.debug("CLASS subnetRange:__init__,turnedOnBitRotated="+str(self.bitRotatedBinaryString))
            self.bitRotatedBinaryOctetDict = self.__getBitRotatedBinaryOctetDict()
            logging.debug("CLASS subnetRange:__init__,bitRotatedBinaryOctetDict="+str(self.bitRotatedBinaryOctetDict))
            self.focusValue = self.__getFocusValue()
            logging.debug("CLASS subnetRange:__init__,focusValue="+str(self.focusValue))
            self.binaryNetworkValue = self.__getBinaryNetworkValue()
            logging.debug("CLASS subnetRange:__init__,binaryNetworkValue="+str(self.binaryNetworkValue))
            self.broadcastValue = self.__getBroadcastValue()
            logging.debug("CLASS subnetRange:__init__,broadcastValue="+str(self.broadcastValue))
            self.networkIp = self.__getIp("network")
            logging.debug("CLASS subnetRange:__init__,networkIp="+str(self.networkIp))
            self.broadcastIp = self.__getIp("broadcast")
            logging.debug("CLASS subnetRange:__init__,broadcastIp="+str(self.broadcastIp))
            self.maxHosts = self.__GetMaxHosts()
            logging.debug("CLASS subnetRange:__init__,maxHosts="+str(self.maxHosts))
            self.networkDict = self.__getIpAddressOctetDict(self.networkIp)
            logging.debug("CLASS subnetRange:__init__,networkDict="+str(self.networkDict))
            self.broadcastDict = self.__getIpAddressOctetDict(self.broadcastIp)
            logging.debug("CLASS subnetRange:__init__,broadcastDict="+str(self.broadcastDict))
            self.binaryNetworkIp = self.__getBinaryValueOfIp(self.networkDict)
            logging.debug("CLASS subnetRange:__init__,binaryNetworkIp="+str(self.binaryNetworkIp))
            self.binaryBroadcastIp = self.__getBinaryValueOfIp(self.broadcastDict)
            logging.debug("CLASS subnetRange:__init__,binaryBroadcastIp="+str(self.binaryBroadcastIp))
            self.longNetworkIp = self.__getLongValueOfBinaryValue(self.binaryNetworkIp)
            logging.debug("CLASS subnetRange:__init__,longNetworkIp="+str(self.longNetworkIp))
            self.longBroadcastIp = self.__getLongValueOfBinaryValue(self.binaryBroadcastIp)
            logging.debug("CLASS subnetRange:__init__,longBroadcastIp="+str(self.longBroadcastIp))
            self.__getRange()
            logging.debug("CLASS subnetRange:__init__,ipRange="+str(self.ipRange))
        except IndexError:
            logging.error("CLASS subnetRange:subnetString="+str(subnetString)+",\'/\'SPLIT FAILED")
    def __getBitRotatedBinaryString(self):
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
        bitRotatedBinaryOctetDict ={}
        for i in range(0, len(self.bitRotatedBinaryString), 8):
            bitRotatedBinaryOctetDict[i] = self.bitRotatedBinaryString[i:i+8]
            self.subnetMask[i] = int(bitRotatedBinaryOctetDict[i],2)
        logging.debug("CLASS subnetRange:__getBitRotatedBinaryOctetDict,bitRotatedBinaryOctetDict="+str(bitRotatedBinaryOctetDict))
        logging.debug("CLASS subnetRange:__getBitRotatedBinaryOctetDict,subnetMask="+str(self.subnetMask))
        return bitRotatedBinaryOctetDict
    def __getIpAddressOctetDict(self,ipAddr=None):
        if ipAddr == None:
            ipAddr = self.ipAddress
        ipAddressOctetDict ={}
        ipAddressSplit = ipAddr.split(".")
        for i in range(len(ipAddressSplit)):
            ipAddressOctetDict[i*8] = ipAddressSplit[i]
        logging.debug("CLASS subnetRange:__getIpAddressOctetDict,ipAddressOctetDict="+str(ipAddressOctetDict))
        return ipAddressOctetDict
    def __getFocusValue(self):
        po = {}
        for o,v in self.subnetMask.items():
            if(v < 255 and v >= 0):
                po[o] = v
        pok = max(po, key=po.get)
        self.primaryOctet = pok
        logging.debug("CLASS subnetRange:__getBitRotatedBinaryOctetDict,pok="+str(pok))
        logging.debug("CLASS subnetRange:__getBitRotatedBinaryOctetDict,primaryOctet="+str(self.primaryOctet))
        return self.subnetMask[pok]
    def __getBinaryNetworkValue(self):
        def mulBinSum(i1,i,j):
            if int(i)*int(j):
                self.networkValueSum += self.bitLookUp[i1]
                return "1"
            else:
                return "0"
        binaryNetworkValue = ""
        startVal = int(self.focusValue)
        binaryFocusValue = format(int(self.focusValue),'b')
        binaryMul = ""
        for i in range(8):
            diffVal = (startVal - self.bitLookUp[i])
            if(diffVal < 0):
                bnv = "0"
            else:
                startVal = diffVal
                bnv = "1"
            binaryNetworkValue += bnv
            binaryMul += mulBinSum(i,binaryFocusValue[i],bnv)
        logging.debug("CLASS subnetRange:__getBinaryNetworkValue,binaryNetworkValue="+str(binaryNetworkValue))
        logging.debug("CLASS subnetRange:__getBinaryNetworkValue,binaryMul="+str(binaryMul))
        logging.debug("CLASS subnetRange:__getBinaryNetworkValue,networkValueSum="+str(self.networkValueSum))
        return binaryNetworkValue
    def __getBroadcastValue(self):
        bv = {}
        for i in range(len(self.binaryNetworkValue)):
            if self.binaryNetworkValue[i] == "1":
                bv[i] = self.bitLookUp[i]
        logging.debug("CLASS subnetRange:__getBroadcastValue,bv="+str(bv))
        minVal = min(bv, key=bv.get)
        logging.debug("CLASS subnetRange:__getBroadcastValue,minVal="+str(minVal))
        broadcastValue = self.networkValueSum + bv[minVal] - 1
        logging.debug("CLASS subnetRange:__getBroadcastValue,broadcastValue="+str(self.networkValueSum))
        return broadcastValue
    def __getIp(self,choice):
        choiceDict = {
            "network":self.networkValueSum,
            "broadcast":self.broadcastValue
        }
        value = choiceDict[choice]
        valueIp = ""
        c = 0
        def addDot(c):
            if c < 4:
                return "."
            else:
                return ""
        for k in self.subnetMask:
            if(self.subnetMask[k] == 0):
                valueIp += "0"
                c +=1
                valueIp += addDot(c)
            elif(self.subnetMask[k] == 255):
                valueIp += self.ipAddressOctetDict[k]
                c += 1
                valueIp += addDot(c)
            else:
                valueIp += str(value)
                c += 1
                valueIp += addDot(c)
        return valueIp
    def __GetMaxHosts(self):
        maxHosts = 2**(32-int(self.block))-2
        logging.debug("CLASS subnetRange:__maxHosts,maxHosts="+str(maxHosts))
        return maxHosts
    def __getBinaryValueOfIp(self,ipAddrOctetDict):
        binVal = ""
        try:
            for k in ipAddrOctetDict:
                binVal += bin(int(ipAddrOctetDict[k])).split(("0b"))[1]
            return binVal
        except IndexError:
            logging.error("CLASS subnetRange:__getBinaryValueOfIp,Input Error,ipAddrOctetDict="+str(ipAddrOctetDict))
    def __getLongValueOfBinaryValue(self,binaryValue):
        logging.debug("CLASS subnetRange:__getLongValueOfBinaryValue,binaryValue="+str(binaryValue))
        return int(binaryValue,2)
    def __getRange(self):
        rangeStart = self.longNetworkIp+1
        logging.debug("CLASS subnetRange:__getRange,rangeStart="+str(rangeStart))
        rangeStop = self.longBroadcastIp
        logging.debug("CLASS subnetRange:__getRange,rangeStop="+str(rangeStop))
        diff = rangeStop - rangeStart
        logging.debug("CLASS subnetRange:__getRange,diff="+str(diff))
        j = 0
        for i in range(diff):
            self.ipRange[i] = j+rangeStart
            j += 1
        logging.debug("CLASS subnetRange:__getRange,ipRange="+str(self.ipRange))
    def searchValueInRange(self,searchValue):
        logging.debug("CLASS subnetRange:searchValueInRange,searchValue="+str(searchValue))
        for key, value in self.ipRange.items():
            if searchValue == value:
                logging.debug("CLASS subnetRange:searchValueInRange,searchValue="+str(searchValue)+" found @key="+str(key))
                return True
            else:
                logging.debug("CLASS subnetRange:searchValueInRange,searchValue="+str(searchValue)+" not-found")
                return False