# Step 1: Import the pygame library.
import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Maaz's Game")
background = pygame.transform.scale(pygame.image.load("C:/Users/ersab/Downloads/Cat image.webp").convert(),(400,500))
cat = pygame.transform.scale(pygame.image.load("C:/Users/ersab/Downloads/cat image.2.jpg").convert_alpha(),(200,200))
cat_rect = cat.get_rect(center=(220,250))
text = pygame.font.Font(None,36).render("Cat",True,pygame.Color("orange"))
text_rect = text.get_rect(center=(250,220))
def game_loop():
    Clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background,(0,0))
        screen.blit(cat,cat_rect)
        screen.blit(text,text_rect)
        pygame.display.flip()
        Clock.tick(7)
    pygame.quit
if __name__=='__main__':
    game_loop()
# Step 2: Initialize Pygame using pygame.init(), then set SCREEN_WIDTH and SCREEN_HEIGHT to 500.

# Step 3: Create the window using display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)), then set its title using pygame.display.set_caption().

# Step 4: Load "background.png" with .convert() for faster drawing, then scale it to fill the window using pygame.transform.scale().

# Step 5: Load "penguin.png" with .convert_alpha() to keep its transparency, then scale it down to (200, 200).

# Step 6: Create penguin_rect using penguin_image.get_rect(center=...) to position the penguin near the middle of the screen.

# Step 7: Create a font with pygame.font.Font(None, 36), then render the text "Hello World" in black to create a text Surface.

# Step 8: Create text_rect using text.get_rect(center=...) to position the text just below the penguin.

# Step 9: Define a function game_loop() to hold the main loop.

# Step 10: Inside game_loop(), create a clock using pygame.time.Clock(), then set running = True.

# Step 11: Start the loop using while running:, checking every event with pygame.event.get() and setting running = False when pygame.QUIT is seen.

# Step 12: Draw the background, penguin, and text onto the screen in order using display_surface.blit(), then update the display with pygame.display.flip().

# Step 13: Limit the loop to 30 frames per second using clock.tick(30), then call pygame.quit() once the loop ends.