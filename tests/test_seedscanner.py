# This file contains unit tests for SeedScanner library functionality
#
# Author: Josh McIntyre
#
import unittest

import seedscanner

class TestSeedScanner(unittest.TestCase):

    # Test basic construction of classes
    def test_SeedScanner(self):
        s = seedscanner.SeedScanner("./test")
        s2 = seedscanner.SeedScanner("c:/Users/foo/Desktop")
        s3 = seedscanner.SeedScanner("/home/foo")
        
        assert isinstance(s, seedscanner.SeedScanner)
        assert isinstance(s2, seedscanner.SeedScanner)
        assert isinstance(s3, seedscanner.SeedScanner)

        assert s.directory == "./test"
        assert s2.directory == "c:/Users/foo/Desktop"
        assert s3.directory == "/home/foo"
        
    # Test seed scanning
    def test_scan(self):
    
        s = seedscanner.SeedScanner("./test")
        seeds = s.scan()
        
        assert len(seeds) == 4

        assert seeds[0] == "orphan wolf valley genius music situate run pond dinner talk echo gather"
        assert seeds[1] == "apple luggage example script aim canyon fancy fiction physical rubber globe extend certain split blame noise engage brush kind invite ring match banana trouble"
        assert seeds[2] == "apple luggage example script aim canyon fancy fiction physical rubber globe extend certain split blame noise engage brush kind invite ring match banana trouble"
        assert seeds[3] == "open enjoy banana health nut alarm clay mountain enter direct math immune"

    # Test individual file scanning
    def test_search_file(self):
    
        seed_files = [ "./test/supersecretseed.txt" ] + [ f"./test/supersecretseed{i}.txt" for i in range(2,5) ]
        no_seed_file = "./test/noseed.txt"

        s = seedscanner.SeedScanner("./test")
        
        assert s._search_file(seed_files[0]) == "orphan wolf valley genius music situate run pond dinner talk echo gather"
        assert s._search_file(seed_files[1]) == "apple luggage example script aim canyon fancy fiction physical rubber globe extend certain split blame noise engage brush kind invite ring match banana trouble"
        assert s._search_file(seed_files[2]) == "apple luggage example script aim canyon fancy fiction physical rubber globe extend certain split blame noise engage brush kind invite ring match banana trouble"
        assert s._search_file(seed_files[3]) == "open enjoy banana health nut alarm clay mountain enter direct math immune"
        
        assert s._search_file(no_seed_file) is None

