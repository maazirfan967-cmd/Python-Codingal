# Step 1: Import the pygame library.
import pygame
# Step 2: Initialize all required Pygame modules using pygame.init().# Step 3: Create a 400x500 window using screen = pygame.display.set_mode((400,500)).
pygame.init()
screen = pygame.display.set_mode((400,500))
# Step 4: Create a variable done = False to control the main loop.
done = False
# Step 5: Start the loop using while not done:, so the window keeps running.
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
# Step 6: Inside the loop, check every event in the queue using for event in pygame.event.get():.

# Step 7: If the event type is pygame.QUIT, call pygame.quit() to end Pygame.

# Step 8: Update the display every pass through the loop using pygame.display.flip().