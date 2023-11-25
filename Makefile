# This file contains a make script for the SeedScanner application
#
# Author: Josh McIntyre
#

# This block defines makefile variables
SRC_FILES=src/*.py
RES_FILES=res/*.txt

BUILD_DIR=bin/seedscanner

# This rule builds the application
build: $(SRC_FILES) $(RES_FILES)
	mkdir -p $(BUILD_DIR)
	cp $(SRC_FILES) $(BUILD_DIR)
	cp $(RES_FILES) $(BUILD_DIR)

# This rule cleans the build directory
clean: $(BUILD_DIR)
	rm $(BUILD_DIR)/*
	rmdir $(BUILD_DIR)
