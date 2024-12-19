# TODO: don't forget to pip install pygame in the terminal.  Else pygame functions won't be recognized.
import pygame, random

pygame.init()

# Set display window
Window_Width = 600
Window_Height = 600
display_surface = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption("~~Snake~~")

Fps = 20
clock = pygame.time.Clock

Snake_Size = 20
head_x = Window_Width // 2
head_y = Window_Height // 2
snake_dx = 0
snake_dy = 0
score = 0

RED = 255, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
DARKGREEN = 10, 50 , 10
DARKRED = 150, 0, 0


# Set fonts
font = pygame.font.SysFont('gabriola', 48)


# Set text

def create_text_and_rect(text, color, background_color, **locations):
    text = font.render(text, True, color, background_color)
    rect = text.get_rect()
    for location in locations.keys():
        if location == "center":
            rect.center = locations[location]
        if location == "topleft":
            rect.topleft = locations[location]
    # TODO: add an if condition for "topleft" similar to the if condition for "center"
    return text, rect


title_text, title_rect = create_text_and_rect("~~Snake~~", GREEN, DARKRED,
                                             center=(Window_Width // 2, Window_Height // 2))

score_text, score_rect = create_text_and_rect("Score:  " + str(score), GREEN, DARKRED, topleft =(10, 10))

game_over_text, game_over_rect =create_text_and_rect("GAMEOVER", GREEN, DARKRED,
                                             center=(Window_Width // 2, Window_Height // 2))

continue_text, continue_rect = create_text_and_rect("Press any key to play again", RED, DARKGREEN,
                                             center=(Window_Width // 2, Window_Height // 2 + 64))

pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

apple_coord = 500, 500 , Snake_Size, Snake_Size
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = head_x, head_y, Snake_Size, Snake_Size
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

body_coords = [ ]


# The main game loop
running = True
is_paused = False


def move_snake(event):
    global snake_dx, snake_dy
    if event.type == pygame.KEYDOWN:
        key = event.key
    elif event.type == pygame.K_LEFT:
        snake_dx = -1 * Snake_Size
        snake_dy = 0
    elif event.type == pygame.K_RIGHT:
        snake_dx = Snake_Size
        snake_dy = 0
    elif event.type == pygame.K_UP:
        snake_dx = 0
        snake_dy = -1 * Snake_Size
    elif event.type == pygame.K_DOWN:
        snake_dx = 0
        snake_dy = Snake_Size

def check_quit(event):
    global running
    if event == pygame.QUIT:
        running = False

def check_events():
    global running
    # TODO: create a for loop events is the variable pygame.event.get() is the list
        # TODO: call check_quit(event)
        # TODO: call move_snake(event)
    pass  # TODO: remove this pass when done.

def handle_snake():
    global body_coords
    global head_x
    global head_y
    global head_coord
    # TODO: call body_coords.insert() method and pass in 0, head_coord
    # TODO: call body_coords.pop()
    # TODO: add snake_dx to head_x
    # TODO: add snake_dy to head_y
    # TODO: set head_coord to (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

def reset_game_after_game_over(event):
    global is_paused, score, head_x, head_y, head_coord, body_coords, snake_dx, snake_dy
    if event.type == pygame.KEYDOWN:
        score = 0
        head_x = Window_Width // 2
        head_y = Window_Height //2 + 100
        head_coord = (head_x, head_y, Snake_Size, Snake_Size)
        snake_dx = 0
        snake_dy = 0
        is_paused = False


def check_end_game_after_game_over(event):
    global is_paused
    global running
    if event.type == pygame.QUIT:
        is_paused = False
        running = False



def check_game_over():
    global head_rect
    global head_coord
    global body_coords
    global running
    global is_paused
    if head_rect.left < 0 or head_rect.right > Window_Width or head_rect.top < 0 or head_rect.bottom > Window_Height or head_coord in body_coords:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        is_paused = True
        while is_paused:
            for event in pygame,event.get():
                reset_game_after_game_over(event)
                check_end_game_after_game_over(event)


def check_collisions():
    global score, apple_x, apple_y, apple_coord, body_coords
    # TODO: if head_rect.colliderect(apple_rect)
        # TODO: add 1 to the score
        # TODO: call pick_up_sound.play()
        # TODO: set apple_x to random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        # TODO: set apple_y to random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        # TODO: set apple_coord to (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
        # TODO: call body_coords.append(head_coord)
          pass # TODO: remove this pass when done.

def blit_hud():
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    # TODO: call display_surface.blit(title_text, title_rect)
    # TODO: call display_surface.blit(score_text, score_rect)
    pass  # TODO: remove this pass when done.

def blit_assets():
    for body in body_coords:
        pygame.draw.rect(display_surface, DARKGREEN, body)\
        head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
        apple_rect = pygame.draw.rect(display_surface, RED,apple_coord)

def update_display_and_tick_clock():
    pygame.display.update()
    clock.tick(Fps)


while running:
    # Check pygame events
    check_events()

    # handle growing and manipulating the snake
    handle_snake()

    # Check for game over
    check_game_over()

    # Check for collisions
    check_collisions()

    # Update HUD
    score_text = font.render("score: " + str(score), True, GREEN, DARKGREEN)

    # Fill the surface
    display_surface.fill(WHITE)

    # Blit HUD
    blit_hud()

    # Blit assets
    blit_assets()

    # Update display and tick clock
    update_display_and_tick_clock()

# End the game
pygame.quit()
