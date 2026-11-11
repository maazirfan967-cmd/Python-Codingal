# Step 1: Define a main() function, initialize pygame, and create a 500x500 window with a caption.
import pygame
pygame.init()
def main():
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Moving Sprite")
    colors = {"Red":pygame.Color("red"),
              "Blue":pygame.Color("blue"),
              "Green":pygame.Color("green"),
              "Yellow":pygame.Color("yellow"),
              "White":pygame.Color("white")}
    current_color = colors["White"]
    x = 30
    y = 30
    width = 60
    height = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-=3
        if pressed[pygame.K_RIGHT]: x+=3
        if pressed[pygame.K_UP]: y-=3
        if pressed[pygame.K_DOWN]: y+=3
        x = min(max(0,x),(500-width))
        y = min(max(0,y),(500-height))
        if x==0:
            current_color = colors["Blue"]
        elif x==500-width:
            current_color = colors["Green"]
        elif y==0:
            current_color = colors["Red"]
        elif y==500-height:
            current_color = colors["Yellow"]
        else:
            current_color = colors["White"]
        screen.fill((0,0,0))
        pygame.draw.rect(screen,current_color,(x,y,width,height))
        pygame.display.flip()
    pygame.quit()
if __name__=='__main__':
    main()
# Step 2: Store five named colors in a colors dictionary, and set current_color to white.

# Step 3: Set the sprite's starting x, y position and its width and height, then create a clock to control frame rate.

# Step 4: Start the main loop, checking pygame.event.get() for the pygame.QUIT event.

# Step 5: Call pygame.key.get_pressed() and use four if checks on the arrow keys to adjust x and y.

# Step 6: Clamp x and y with min() and max() so the sprite stays fully inside the screen.

# Step 7: Use an if/elif chain on x and y to set current_color whenever the sprite touches an edge.

# Step 8: Fill the screen black, draw the sprite rectangle in current_color, flip the display, and tick the clock.