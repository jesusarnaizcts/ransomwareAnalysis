# -*- coding: utf-8 -*-
import unittest
from keyDatProcessor import KeyDatProcessor

class keyDatProcessorTest(unittest.TestCase):     
    def setUp(self):
        self.kdProcessor = KeyDatProcessor("key.dat")
    
    def testValidateFields(self):
        """
        1. Si le pido que me de la bitcoin address, deberia devolver: 13bGiahjQW8B4qifrY5LzoCZavsFFSmcad
        """
        self.assertEqual(self.kdProcessor.getBitcoinAddress(), '13bGiahjQW8B4qifrY5LzoCZavsFFSmcad')

        """
        2. Si le pido que me de el unknown1, debe ser:
        ('Z', '=', '\xeb', '\x99', 'd', ',', 'z', '?', '2', 'P', '\xbe', 'n', 'x', '\xb4', '\x98', '\xe7', '"', 'S', '\xd1', '\xea', '\x96', '1', '\xa1', '\xed', '\xce', '\xe7', '5', '\x1f', '\x15', 'G', '\x07', '\x1e', '\\', '\x84', '\x9b', 'b', 'T', '\xe1', '\xee', 'H', '\x94', 'M', '\x11', '\x97', '\xca', '\x08', '\x13', ':', '\x95', '\xc9', '2', '\x8d', '\xc8', 'J', '\x0f', '\x8e', 'X', 'g', '\xfe', 'e', '>', '0', '\xd8', ']', '\xbc', '\xfe', 'V', '\xa3', '\x19', 'q', 'C', 'P', '\x9d', '_', 'G', '\xc2', '3', '\xb5', '\x08', 'B', '\xcb', 'b', '\xc7', 'U', 'x', '\xfe', ':', '\x8c', 'l', '\xa5', ' ', '(', '\xba', '\xf4', '$', '\x91') != '1JYNvhjYpuakPWxrWkqntSqYVwHTDsSSmT'
        """
        self.assertEqual(self.kdProcessor.getUnknown1(), ('Z', '=', '\xeb', '\x99', 'd', ',', 'z', '?', '2', 'P', '\xbe', 'n', 'x', '\xb4', '\x98', '\xe7', '"', 'S', '\xd1', '\xea', '\x96', '1', '\xa1', '\xed', '\xce', '\xe7', '5', '\x1f', '\x15', 'G', '\x07', '\x1e', '\\', '\x84', '\x9b', 'b', 'T', '\xe1', '\xee', 'H', '\x94', 'M', '\x11', '\x97', '\xca', '\x08', '\x13', ':', '\x95', '\xc9', '2', '\x8d', '\xc8', 'J', '\x0f', '\x8e', 'X', 'g', '\xfe', 'e', '>', '0', '\xd8', ']', '\xbc', '\xfe', 'V', '\xa3', '\x19', 'q', 'C', 'P', '\x9d', '_', 'G', '\xc2', '3', '\xb5', '\x08', 'B', '\xcb', 'b', '\xc7', 'U', 'x', '\xfe', ':', '\x8c', 'l', '\xa5', ' ', '(', '\xba', '\xf4', '$', '\x91'))
        """
        3. Si le pido que me de el unknown1, debe ser:
        ('\x00', '}', '}', '\x01', '!', '\xbd', 'Y', '\xe5', '}', '\xe6', '\x8e', 'U', '9', 'U', '\x98', '\xb9', '\x18', 'm', '\xdd', 'g', '\x8e', '\x95', '\xdd', 'u', '\x95', '\x11', 'n', '\xb4', '^', '\x9b', '\xdd', '>', 'L', '\xd4', 'J', '\xc1', '\xf3', 'a', '\xf7', '\r', '2', '(', '\x97', ' ', 'Z', '\xa6', '^', '\xeb', '\xbe', '\xef')
        """
        self.assertEqual(self.kdProcessor.getUnknown2(), ('}', '}', '\x01', '!', '\xbd', 'Y', '\xe5', '}', '\xe6', '\x8e', 'U', '9', 'U', '\x98', '\xb9', '\x18', 'm', '\xdd', 'g', '\x8e', '\x95', '\xdd', 'u', '\x95', '\x11', 'n', '\xb4', '^', '\x9b', '\xdd', '>', 'L', '\xd4', 'J', '\xc1', '\xf3', 'a', '\xf7', '\r', '2', '(', '\x97', ' ', 'Z', '\xa6', '^', '\xeb', '\xbe', '\xef', '?', '\x07', '\x99', '3', '\xc6', '*', '>', 'v', '\x08', 'V', 'R', '\xda', 'v', '\xbb', 'c', '\x00', '\xdf', '\x07', '\x05', '\x00', '\x03', '\x00', '\r', '\x00', '\x0b', '\x00', '*', '\x00', '0', '\x00', '\xd7') )
        