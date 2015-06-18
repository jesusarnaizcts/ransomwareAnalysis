# -*- coding: utf-8 -*-
import string
import struct

class ECCProcessor:
    def __init__(self, eccFileName):
        self.eccFileName = eccFileName
        self.__processECC()
        
        
    def __processNullData(self, inputFile, bytesToIgnore):
            inputFile.read(bytesToIgnore)

    def __processECC(self):
        with open(self.eccFileName, "rb") as inputFile:
            self.AESInitVector = inputFile.read(16)
            self.fileSize = struct.unpack('<L', inputFile.read(4))[0]
            self.cryptData = inputFile.read()     
            #self.cryptData = struct.unpack(len(self.cryptData) + "c", self.cryptData) 
                    
    def getFileSize(self):
        return self.fileSize
    
    def getCryptData(self):
        return self.cryptData
    
     
    
    