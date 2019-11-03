#IsThisSubnet
import logging
from hexConvert import hexConvert as hc
from subnetRange import subnetRange as sr
class isThisSubnet:
    def __init__(self,inputIp,cidrSubnet):
        self.__ipc = hc(inputIp)
        self.inputIp = self.__ipc.ipAddr
        logging.debug("CLASS isThisSubnet:__init__,inputIp="+str(self.inputIp))
        self.inputIpLong = self.__ipc.longIpAddr
        logging.debug("CLASS isThisSubnet:__init__,inputIpLong="+str(self.inputIpLong))
        self.cidrSubnetInfo = sr(cidrSubnet)
        logging.debug("CLASS isThisSubnet:__init__,cidrSubnetInfo="+str(cidrSubnet))
        self.blockNumber = self.cidrSubnetInfo.block
        logging.debug("CLASS isThisSubnet:__init__,blockNumber="+str(self.blockNumber))
        self.inputIpCidrSubnet = self.inputIp+"/"+str(self.blockNumber)
        logging.debug("CLASS isThisSubnet:__init__,inputIpCidrSubnet="+str(self.inputIpCidrSubnet))
        self.inputIpCidrSubnetInfo = sr(self.inputIpCidrSubnet)
    def verifyNetworkAndBroadcast(self):
        condition1 = (self.inputIpCidrSubnetInfo.networkIp == self.cidrSubnetInfo.networkIp)
        logging.debug("CLASS isThisSubnet:verify,condition1(NetworkIp)="+str(condition1))
        condition2 = (self.inputIpCidrSubnetInfo.broadcastIp == self.cidrSubnetInfo.broadcastIp)
        logging.debug("CLASS isThisSubnet:verify,condition2(BroadcastIp)="+str(condition2))
        condition3 = (self.inputIpLong >= self.cidrSubnetInfo.longNetworkIp and self.inputIpLong <= self.cidrSubnetInfo.longBroadcastIp)
        logging.debug("CLASS isThisSubnet:verify,condition3(ip in subnet search)="+str(condition3))
        if (condition1 and condition2 and condition3):
            logging.debug("CLASS isThisSubnet:verify,condition1 and condition2 and condition3="+str(True))
            return True
        else:
            logging.debug("CLASS isThisSubnet:verify,condition1 and condition2="+str(False))
            return False