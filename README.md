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
* Raspberry Pi

## Usage
____________

### Library Usage
* `import seedscanner`
* `scanner = seedscanner.SeedScanner("<directory to search>")`
* `seeds = scanner.scan()`

### Tkinter GUI Usage
* Run `python3 seedscannerui.py`
* Select folder to search by clicking "Choose directory" button and using the file dialog
* Run scan by clicking "Scan for seed phrases"
* A list of found seeds and the total will populate the text box, or "No seeds found" will be indicated

### Pygame GUI Usage
* Configure your own directory for finding seeds
* Run `python3 seedscannerrpi.py`

### Run unit tests
* Run `python -m pytest <test file>`
* WARNING: Do not use the example seed phrases shown in the unit tests. Anyone could steal your coins!