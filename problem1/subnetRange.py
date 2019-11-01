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
    def __init__(self,subnetString):
        try:
            subnetStringSplit = subnetString.split("/")
            self.ipAddress = subnetStringSplit[0]
            logging.debug("CLASS subnetRange:__init__,ipAddress="+str(self.ipAddress))
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
        maxVal = min(bv, key=bv.get)
        logging.debug("CLASS subnetRange:__getBroadcastValue,maxVal="+str(maxVal))
        broadcastValue = self.networkValueSum + bv[maxVal] - 1
        logging.debug("CLASS subnetRange:__getBroadcastValue,broadcastValue="+str(self.networkValueSum))
        return broadcastValue