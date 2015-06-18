# -*- coding: utf-8 -*-
import unittest
from eccProcessor import ECCProcessor

class ECCProcessorTest(unittest.TestCase):     
    def setUp(self):
        self.eccProcessor = ECCProcessor("Honey1.txt.ecc")
    
    def testValidateFields(self):
        """
        1. Si le pido que me devuelva el tam del fichero, devolverá 18
        """
        self.assertEqual(self.eccProcessor.getFileSize(), 18)

        """
        2. Si le pido cryptData, debe devolver 32 bytes
        """
        self.assertEqual(len(self.eccProcessor.getCryptData()), 32)