# -*- coding: utf-8 -*-
import string
import struct

class KeyDatProcessor:
    def __init__(self, keyDatFileName):
        self.keyDatFileName = keyDatFileName
        self.__processKeyDat()
        
        
    def __processNullData(self, inputFile, bytesToIgnore):
            inputFile.read(bytesToIgnore)

    def __processKeyDat(self):
        with open(self.keyDatFileName, "rb") as inputFile:
            self.bitcoinAddress = inputFile.read(34)
            self.__processNullData(inputFile, 66)
            self.unknown1 = struct.unpack("96c", inputFile.read(96))
            self.__processNullData(inputFile, 33)
            self.unknown2 = struct.unpack("80c", inputFile.read(80))     
                    
    def getBitcoinAddress(self):
        return self.bitcoinAddress
    
    def getUnknown1(self):
        return self.unknown1
   
    def getUnknown2(self):
        return self.unknown2
    
    def getUnknown3(self):
        return self.unknown3
    
    def getUnknown4(self):
        return self.unknown4
    
     
    
    