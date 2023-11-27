# This file contains a simple GUI for auditing seed phrases stored on a system
#
# Author: Josh McIntyre
#
import tkinter
import tkinter.filedialog

import seedscanner

# Define a SeedScanner UI class
class SeedScannerUI:

    # Constants
    TITLE = "SeedScanner"
    WIDTH = 800
    HEIGHT = 500
    GEOMETRY = f"{WIDTH}x{HEIGHT}"
    LISTBOX_WIDTH = 80
    LISTBOX_HEIGHT = 20
    NO_SEEDS_TEXT = "No seeds found"
    SEEDS_FOUND_TEXT = "seeds found:"

    # Constructor, sets basic variables up
    def __init__(self):
    
        # Set up basic class storage
        self.dir_name = None
        self.seeds = None
        self.seeds_updated = False
        
        # Configure UI elements
        self.configure_ui()
        
        # Start the main loop
        self.main_loop()
        
    # Configure UI elements
    def configure_ui(self):
    
        self.window = tkinter.Tk()
        self.window.title(self.TITLE)
        self.window.geometry(self.GEOMETRY)
        
        self.dir_button = tkinter.Button(text="Choose directory", command=self.choose_dir)
        self.dir_label = tkinter.Label(text=self.dir_name)
        
        self.scan_button = tkinter.Button(text="Scan for seed phrases", command=self.scan)
        self.scan_text = tkinter.Text(width=self.LISTBOX_WIDTH, height=self.LISTBOX_HEIGHT, wrap=tkinter.WORD)

    # Main loop for the UI
    def main_loop(self):
    
        while True:
        
            # Update any elements that need updating
            self.dir_label.config(text=self.dir_name)

            if self.seeds_updated:
            
                if self.seeds:
                    # If we have a new set of seeds from a scan,
                    # clear and update the textbox
                    self.scan_text.delete(1.0, tkinter.END)
                    content = f"{len(self.seeds)} {self.SEEDS_FOUND_TEXT}\n"
                    content += "\n".join([ f"* {seed}" for seed in self.seeds ])
                    self.scan_text.insert(1.0, content)
                else:
                    # Otherwise, indicate no seeds were found
                    self.scan_text.delete(1.0, tkinter.END)
                    self.scan_text.insert(1.0, self.NO_SEEDS_TEXT)
                
                self.seeds_updated = False

            # Pack the UI elements
            self.dir_button.pack()
            self.dir_label.pack()
            self.scan_button.pack()
            self.scan_text.pack()
        
            # Update the tkinter window
            self.window.update() 
            
    # Directory browser handler
    def choose_dir(self):

        self.dir_name = tkinter.filedialog.askdirectory()

    # Scan for seeds
    def scan(self):
    
        scanner = seedscanner.SeedScanner(self.dir_name)
        self.seeds = scanner.scan()
        self.seeds_updated = True
        
# The main entry point for the program
def main():

    ssui = SeedScannerUI()

if __name__ == "__main__":
    main()