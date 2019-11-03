#main
from hexConvert import hexConvert
from subnetRange import subnetRange
from isThisSubnet import isThisSubnet
import unittest
import logging
import sys
import os

def main():
    logging.info("In This Subnet?\n")
    #Read & Write from csv on the fly
    try:
        inputFilePath = sys.argv[1]
        logging.debug("CLASS main:inputFilePath="+str(inputFilePath))
        outputFilePath = sys.argv[2]
        logging.debug("CLASS main:outputFilePath="+str(outputFilePath))
        if not os.path.isfile(inputFilePath):
            logging.error("\nFile Un-available: {}".format(inputFilePath))
            sys.exit(1)
        with open(outputFilePath, 'a') as ofp:
            ofp.write('INPUT,INPUT-IP,CIDR,RESULT'+'\n')
            with open(inputFilePath) as ifp:
                for line in ifp:
                    inputIpHash, cidrSubnet = line.splitlines()[0].split(",")
                    checker = isThisSubnet(inputIpHash,cidrSubnet)
                    inputIpAddress = checker.inputIp
                    verification = checker.verify()
                    logging.info("INPUT:{},INPUT-IP:{},CIDR:{},RESULT:{}".format(inputIpHash,inputIpAddress,cidrSubnet,verification))
                    result = str(inputIpHash+","+inputIpAddress+","+cidrSubnet+","+str(verification))+'\n'
                    ofp.write(result)
    except IndexError:
        logging.error("\nTwo inputs needed!\n 1. input File-path\n 2. output File-path")
if __name__=="__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    main()