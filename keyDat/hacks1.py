# -*- coding: utf-8 -*-
"""
    For now this is only random tests used as example.
"""
from keyDatProcessor import KeyDatProcessor
import unittest

class keyDatProcessorTest(unittest.TestCase):     
    def __listAsString(self, finalStringChar):
        return ''.join(finalStringChar)
    
    def __leftShift(self, c, positions):
        return (ord(c) << positions) & 0xFF
    
    def __printResults(self):
        print "Decimal"
        print "Original: ", self.originalStringDecimal
        print "Final:    ", self.finalStringDecimal, "\n\n"
        
        print "Hexadecimal"
        print "Original: ", self.originalStringHexa
        print "Final:    ", self.finalStringHexa, "\n\n"
        """
        print "String"
        print "Original: ", self.__listAsString(self.kdProcessor.getUnknown1())
        print "Final:    ", self.__listAsString(self.finalStringChar)"""
        
    def setUp(self):
        self.kdProcessor = KeyDatProcessor("key.dat")
        self.originalStringDecimal = []
        self.originalStringHexa = []
        self.finalStringDecimal = []
        self.finalStringHexa = []
        self.finalStringChar = []
    
    def tearDown(self):
        self.__printResults()
   
    def testShiftOneLeft(self):
        print "Testing to bit shift one to the left"
        for c in self.kdProcessor.getUnknown1():
            self.originalStringDecimal.append(ord(c))
            self.originalStringHexa.append(hex(ord(c)))
            self.finalStringDecimal.append(self.__leftShift(c, 1))
            self.finalStringHexa.append(hex(self.__leftShift(c, 1)))
            self.finalStringChar.append(chr((self.__leftShift(c, 1))))
        pass

    def testShiftTwoLeft(self):
        print "Testing to bit shift two to the left"
        for c in self.kdProcessor.getUnknown1():
            self.originalStringDecimal.append(ord(c))
            self.originalStringHexa.append(hex(ord(c)))
            self.finalStringDecimal.append(self.__leftShift(c, 2))
            self.finalStringHexa.append(hex(self.__leftShift(c, 2)))
            self.finalStringChar.append(chr((self.__leftShift(c, 2))))
        pass

    