# File created by: Diego Avila

# import libraries
# to delay code as needed
from time import sleep
# to generate a random result
from random import randint
# a comprehensive game library for use with Python
import pygame as pg
# to manage files and folders in terms of directories
import os
# giving a file path to where we currently are
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors, rgb values
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# choices of the game of rps
choices = ["rock", "paper", "scissors"]
# draws text on screen with the font of arial
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

# cpu randomly decides
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice
# initializes pygame
pg.init()
pg.mixer.init()
# displays the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
# displays name in top left corner
pg.display.set_caption("rock, paper, scissors...")
clock = pg.time.Clock()
# stores the pixels for the rock image
rock_image = pg.image.load(os.path.join(game_folder, "rock.jpg")).convert()
# computer is storing x and y values to move image
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()
# stores pixels for paper image
paper_image = pg.image.load(os.path.join(game_folder, "paper.jpg")).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()
# stores pixels for scissors image
scissors_image = pg.image.load(os.path.join(game_folder, "scissors.jpg")).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()
# start screen shows
start_screen = True

# player can choose between rock, paper, or scissors
player_choice = ""
# cpu can choose between rock, paper, or scissors
cpu_choice = ""
running = True
replay = False
# loop runs until it breaks
while running:
    # forces the framerate to 30 framerates per second
    clock.tick(FPS)

    for event in pg.event.get():
        # listening for anytime the mouse closes the python file
        if event.type == pg.QUIT:
            running = False
        ######## get user input ########
        # HCI - human keyboard interaction
        # keyboard, mouse, controller, vr headset
        # to detect if key is pressed down
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("Let's play")
                start_screen = False
        # to detect if key is pressed down
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                print("replay")
                replay = True
        # sets up the events when clicking on the mousebutton and releasing it
        if event.type == pg.MOUSEBUTTONUP:
            # displays coordinates where you click
            print(pg.mouse.get_pos()[0])
            print(pg.mouse.get_pos()[1])
            # stores mouse position
            mouse_coords = pg.mouse.get_pos()
            # if pg.mouse.get_pos()[0] <= my_image_rect.width and pg.mouse.get_pos()[1] < my_image_rect.height:
            #     print("i clicked the rock")
            # else:
            #     print("no rock")
            # datatype returning a true or false
            print (rock_image_rect.collidepoint(mouse_coords))
            # the player chooses rock
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock...")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
            # the player chooses paper
            elif paper_image_rect.collidepoint(mouse_coords):
                print("you clicked on paper")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            # the player chooses scissors
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()
            else:
                print("you did not click on anything...")
    
    ######## update ########
    # rock_image_rect.x += 1
    # rock_image_rect.y += 1

    ######## draw ########
    screen.fill(BLACK)
    # drawing the rock on the screen
    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
    # waits for player to hit spacebar
    if start_screen:
        print("it works")
        # waits 3 seconds for it works to print in the terminal
        sleep(3)
        # text appears that tells player to press spacebar
        draw_text("Press space to play rock paper scissors", 22, WHITE, WIDTH/2, HEIGHT/10)
        rock_image_rect.y = 2000
        paper_image_rect.y = 2000
        scissors_image_rect.y = 2000

    # allows player to choose rock paper or scissors
    if not start_screen and player_choice == "":
        rock_image_rect.y = 50
        paper_image_rect.y = 200
        scissors_image_rect.y = 400
    
    
    # checks to see outcome of game
    if player_choice == "rock":
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You tie", 22, WHITE, WIDTH/2, HEIGHT/10)
        # text saying you lose appears and image of paper is drawn
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You lose", 22, WHITE, WIDTH/2, HEIGHT/10)
        # text saying you win appears and image of scissors is drawn
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You win", 22, WHITE, WIDTH/2, HEIGHT/10)
    # checks to see outcome of game
    if player_choice == "paper":
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            # screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You tie", 22, WHITE, WIDTH/2, HEIGHT/10)
        # text saying you win and image of rock is drawn
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You win", 22, WHITE, WIDTH/2, HEIGHT/10)
        # text saying you lose and image of scissors is drawn
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You lose", 22, WHITE, WIDTH/2, HEIGHT/10)
    # checks to see outcome of game
    if player_choice == "scissors":
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            # screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You tie", 22, WHITE, WIDTH/2, HEIGHT/10)
        # text saying you lose and image of rock is drawn
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You lose", 22, WHITE, WIDTH/2, HEIGHT/10)
        # text saying you win and image of paper is drawn
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You win", 22, WHITE, WIDTH/2, HEIGHT/10)

    # updates contents of entire display in pygame
    pg.display.flip()
# ends function for pygame
pg.quit()