## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* SeedScanner scans for plaintext cryptocurrency seed phrases in a filesystem

## Development
________________

### Git Workflow
* master for releases (merge development)
* development for bugfixes and new features

### Building
* make build
Build the application
* make clean
Clean the build directory

### Features
* Specify a directory to search
* Specify desired extensions to search via configuration file
* Search all files of that extension using a regular expression
* Report a list of all found seed phrases

### Requirements
* Requires Python

### Platforms
* Windows
* MacOSX
* Linux

## Usage
____________

### Library Usage
* `import seedscanner`
* `scanner = seedscanner.SeedScanner("<directory to search>")
* `seeds = scanner.scan()`
