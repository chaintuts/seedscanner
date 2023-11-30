# This file contains code for a cryptocurrency seed-phrase scanning library
#
# Author: Josh McIntyre
#
import glob
import os
import re

# Define a seed scanning class
class SeedScanner:

    # Constants
    WORDLIST_FILENAME = "bip39_words.txt"
    EXTENSIONS_FILENAME = "extensions.txt"

    # Initialize the scanner
    def __init__(self, directory):
    
        self.directory = directory
        self.regex = self._build_regex()
        self.extensions = self._build_glob_extensions()

    # Scan for seeds in the filesystem
    def scan(self):

        seeds = []
        files = self._find_files()
        for file in files:
            match = self._search_file(file)
            if match:
                seeds.append(match)
        
        return seeds

    # Build and compile a regex for matching a seed
    def _build_regex(self):

        with open(self.WORDLIST_FILENAME) as f:
            words = [word.strip() for word in f]

        combined_words = "|".join(words)
        regex_str = r"((" + combined_words + r")\s*){12,24}"
        regex = re.compile(regex_str, flags=re.IGNORECASE|re.MULTILINE)

        return regex
        
    # Read a file from the listing and search for the seed
    def _search_file(self, file):

        with open(file) as f:

            # A seed doc likely isn't huge, so just read the whole contents into memory
            contents = f.read()
            
            # Search for the seed in the file contents
            match = self.regex.search(contents)

            # Clean up any newlines/garbage from the string
            seed = None
            if match:
                seed = match.group(0).strip().replace("\n", "")
            
            return seed

    # Build a list of file extensions to scan
    def _build_glob_extensions(self):
    
        with open(self.EXTENSIONS_FILENAME) as f:
            extensions = [ext.strip() for ext in f]
        
        return extensions

    # Build a list of files to search
    def _find_files(self):
    
        dir_listing = []
        for extension in self.extensions:
            dir_listing += glob.glob(f"{self.directory}/*{extension}")
        files = [file for file in dir_listing if os.path.isfile(file)]

        return files
        