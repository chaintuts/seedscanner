# This file contains code for displaying large-format seeds on a Raspberry Pi HDMI display
#
# Author: Josh McIntyre
# 
import time

import pygame

import seedscanner
import rpiconfig

# Define a class for displaying seed information on a display
class SeedScannerRpi:

    # Class constants
    SEED_NUMBER_FORMAT = "Found seed #{}:"
    WORDS_PER_LINE = 4

    FONT_SIZE = 60
    ROW_SPACE = 40
    HEADER_POS = [10, 10]
    START_POS = [10, 50]

    SEED_ROTATION_SEC = 7.0

    # Initialize the UI
    def __init__(self, seeds):

        # Store the found seeds
        self.seeds = seeds

        # UI component data
        self._seed_index = 0
        self._seed_time_sec = time.time()

        # Initialize UI components
        pygame.init()
        self.display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    # Input management
    def _handle_input(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()


    # Draw UI components
    def _draw(self, seed, seed_number):

        # Draw the background
        self.display.fill((255, 255, 255))

        # Draw the seed words
        self._draw_seed(seed, seed_number)

        # Flip
        pygame.display.flip()

    # Draw a seed phrase
    # Handle splitting the words across the screen
    def _draw_seed(self, seed, seed_number):

        font = pygame.font.SysFont(None, self.FONT_SIZE)

        # Display a context message
        img = font.render(self.SEED_NUMBER_FORMAT.format(seed_number), True, (0,0,0))
        self.display.blit(img, self.HEADER_POS)

        # Split the seed into segments for display
        words_all = seed.split()
        words_split = []
        for i in range(0, len(words_all), self.WORDS_PER_LINE):
            words_split.append(words_all[i:i+self.WORDS_PER_LINE])
        word_segments = [ " ".join(word_split) for word_split in words_split ]

        pos = self.START_POS.copy()
        for word_segment in word_segments:
            img = font.render(word_segment, True, (0,0,0))
            self.display.blit(img, pos)
            pos[1] += self.ROW_SPACE

    # Seed display handling
    def _display_seeds(self, seeds):

        # Draw the seed data
        self._draw(self.seeds[self._seed_index], self._seed_index + 1)

        # Handle rotating through the found seeds
        cur_seed_time = time.time()
        if (cur_seed_time - self._seed_time_sec) >= self.SEED_ROTATION_SEC:
            if self._seed_index == len(self.seeds) - 1:
                self._seed_index = 0
            else:
                self._seed_index += 1
            self._seed_time_sec = cur_seed_time

    # The main UI loop
    def main_loop(self):

        clock = pygame.time.Clock()

        while True:

            # Handle input
            self._handle_input()

            # Draw UI components
            self._display_seeds(self.seeds)

            # Set tick rate
            clock.tick(60)

# The main entry point for the program
def main():

    ss = seedscanner.SeedScanner(rpiconfig.SEEDSCANNER_DIR)
    seeds = ss.scan()
    
    ui = SeedScannerRpi(seeds)
    ui.main_loop()


if __name__ == "__main__":
    main()
