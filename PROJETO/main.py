
import pygame as py
import time
import random
#py.display.init()
#py.font.init()



py.init()
display_width = 800
display_height = 600
screen = py.display.set_mode((display_width,display_height))
py.display.set_caption("Balloon Survey!")

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
yellow = (200,200,0)#
blue = (0,200,200)#
purple = (139,0,139)#
black = (0,0,0)#
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue= (0,255,255)#
bright_yellow = (255,255,0)#
bright_purple = (255,0,255)#

bal_width = 60
clock = py.time.Clock()
#Desktop - Trabalho
agulha = py.image.load('G:\PROJETO/imagens/agulha.png')
balImg = py.image.load('G:\PROJETO/imagens/balao-black.png')
#Windows
#carImg = py.image.load('E:\Pygame_course/carrace.png')
#Linux
#carImg = py.image.load('/media/guilherme/USB DISK/Pygame_course/carrace.png')
def things_dodge(count):
    font = py.font.SysFont(None, 25)
    text = font.render("Dodge: " + str(count), True, black)
    screen.blit(text,(0,0))

def things(thingx, thingy):
    screen.blit(agulha,(thingx,thingy))

def bal(x,y):
    screen.blit(balImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = py.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRec = text_objects(text, largeText)
    TextRec.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRec)
    py.display.flip()

    time.sleep(2)

    game_intro()

def crash():
    message_display("You Crashed!")


def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = py.mouse.get_pos()
    click = py.mouse.get_pressed()
    #print(click)
    #print(mouse)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        py.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
#            if action == "Play":
#                game_loop()
#            elif action == "quit":
#                py.quit()
#                quit()
#            print("Ok")
    else:
        py.draw.rect(screen, ic,(x,y,w,h))


    smallText = py.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def quitgame():
    py.quit()
    quit()

def game_intro():
    intro = True
    while intro:
        for event in py.event.get():
            #print(event)
            if event.type == py.QUIT:
                py.quit()
                quit()

        screen.fill(white)
        largeText = py.font.Font('freesansbold.ttf', 95)
        TextSurf, TextRec = text_objects("Balloon Survey!", largeText)
        TextRec.center = ((display_width/2),(display_height/4))
        screen.blit(TextSurf, TextRec)


        button("Play",350,250,100,50, green, bright_green, game_loop)
        button("Customize",335,350,125,50,blue,bright_blue,game_customize)
        button("Instructions",325,450,150,50, yellow,bright_yellow,game_instruction)
        button("Quit",350,550,100,50, red, bright_red, quitgame)

        #py.draw.rect(screen, red,(550,450,100,50))

        py.display.flip()
        clock.tick(15)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0
    bal_speed = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 15
    thing_height = 70
    dodge = 0

    gameExit = False
    while not gameExit:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()

            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    x_change = -8
                elif event.key == py.K_RIGHT:
                    x_change = 8
                elif event.key == py.K_UP:
                    y_change = -2
                elif event.key == py.K_DOWN:
                    y_change = 2

            if event.type == py.KEYUP:
                if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                    x_change = 0
                elif event.key == py.K_UP or event.key == py.K_DOWN:
                    y_change = 0
        x += x_change
        y += y_change


        screen.fill((white))

        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty)
        thing_starty += thing_speed
        bal(x,y)
        things_dodge(dodge)
        if x > display_width - bal_width or x <= 0:
            crash()


        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodge += 1
            thing_speed += 1
            #thing_width += (dodge * 1.2)

        if y <= thing_starty + thing_height:


            if x >= thing_startx and x <= thing_startx + thing_width or x+bal_width  >= thing_startx and x + bal_width <= thing_startx+thing_width or x+(bal_width // 2) >= thing_startx and x + (bal_width // 2) <= thing_startx+thing_width:

                crash()


        py.display.flip()
        clock.tick(60)
def game_instruction():
    instruction = True
    while instruction:
        for event in py.event.get():
            #print(event)
            if event.type == py.QUIT:
                py.quit()
                quit()

        screen.fill(white)
        
        
        Text = py.font.SysFont('freesansbold.ttf',100)
        Stext = py.font.SysFont('freesansbold.ttf',20)
        TextSurf, TextRec = text_objects("Instruções",Text)##################################
        TextSurf1, TextRec1 = text_objects("Use as setas 'cima, baixo, esquerda, direita' para desviar dos objetos que caem randômicamente",Stext)
        
        TextRec.center = ((display_width/2),(display_height/6))
        TextRec1.center = ((display_width/3),(display_height/3))

        screen.blit(TextSurf, TextRec)
        screen.blit(TextSurf1, TextRec1)


        button("Back",50,500,100,50,purple,bright_purple,game_intro)

        #py.draw.rect(screen, red,(550,450,100,50))

        py.display.flip()
        clock.tick(15)
def game_customize():
    customize = True
    while instruction:
        for event in py.event.get():
            #print(event)
            if event.type == py.QUIT:
                py.quit()
                quit()

        screen.fill(white)
        largeText = py.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRec = text_objects("A Bit racey!", largeText)
        TextRec.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRec)


        button("Go",150,450,100,50, green, bright_green, game_loop)
        button("Instructions",350,450,100,50, yellow,bright_yellow,game_instruction)
        button("Quit",550,450,100,50, red, bright_red, quitgame)

        #py.draw.rect(screen, red,(550,450,100,50))

        py.display.flip()
        clock.tick(15)
    

    





game_intro()
game_loop()
py.quit()
quit()
