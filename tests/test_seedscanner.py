# This file contains unit tests for SeedScanner library functionality
#
# Author: Josh McIntyre
#
import os
import unittest

import seedscanner

class TestSeedScanner(unittest.TestCase):

    # Constants for test data
    SEED1 = "orphan wolf valley genius music situate run pond dinner talk echo gather"
    SEED2 = "apple luggage example script aim canyon fancy fiction physical rubber globe extend certain split blame noise engage brush kind invite ring match banana trouble"
    SEED3 = "open enjoy banana health nut alarm clay mountain enter direct math immune"
    
    DIR = "./test"
    SEED_FILE1 = os.path.join(DIR, "supersecretseed.txt")
    SEED_FILE2 = os.path.join(DIR, "supersecretseed2.txt")
    SEED_FILE3 = os.path.join(DIR, "supersecretseed3.txt")
    SEED_FILE4 = os.path.join(DIR, "supersecretseed4.txt")
    NOSEED_FILE = os.path.join(DIR, "noseed.txt")
    
    # Test basic construction of classes
    def test_SeedScanner(self):
        s = seedscanner.SeedScanner(self.DIR)
        s2 = seedscanner.SeedScanner("c:/Users/foo/Desktop")
        s3 = seedscanner.SeedScanner("/home/foo")
        
        assert isinstance(s, seedscanner.SeedScanner)
        assert isinstance(s2, seedscanner.SeedScanner)
        assert isinstance(s3, seedscanner.SeedScanner)

        assert s.directory == self.DIR
        assert s2.directory == "c:/Users/foo/Desktop"
        assert s3.directory == "/home/foo"
        
    # Test seed scanning
    def test_scan(self):
    
        s = seedscanner.SeedScanner(self.DIR)
        seeds = s.scan()
        
        assert len(seeds) == 4

        assert seeds[0] == self.SEED1
        assert seeds[1] == self.SEED2
        assert seeds[2] == self.SEED2
        assert seeds[3] == self.SEED3

    # Test individual file scanning
    def test_search_file(self):

        s = seedscanner.SeedScanner(self.DIR)
        
        assert s._search_file(self.SEED_FILE1) == self.SEED1
        assert s._search_file(self.SEED_FILE2) == self.SEED2
        assert s._search_file(self.SEED_FILE3) == self.SEED2
        assert s._search_file(self.SEED_FILE4) == self.SEED3
        
        assert s._search_file(self.NOSEED_FILE) is None

