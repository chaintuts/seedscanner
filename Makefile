# This file contains a make script for the SeedScanner application
#
# Author: Josh McIntyre
#

# This block defines makefile variables
SRC_FILES=src/*.py
RES_FILES=res/*.txt
TEST_FILES=tests/*.py 
TEST_RES_FILES=tests/res/*.txt

BUILD_DIR=bin/seedscanner
TEST_RES_DIR=bin/seedscanner/test

# This rule builds the application
build: $(SRC_FILES) $(RES_FILES) $(TEST_FILES)
	mkdir -p $(BUILD_DIR)
	mkdir -p $(TEST_RES_DIR)
	cp $(SRC_FILES) $(BUILD_DIR)
	cp $(RES_FILES) $(BUILD_DIR)
	cp $(TEST_FILES) $(BUILD_DIR)
	cp $(TEST_RES_FILES) $(TEST_RES_DIR)

# This rule cleans the build directory
clean: $(BUILD_DIR)
	rm $(BUILD_DIR)/*
	rmdir $(BUILD_DIR)
