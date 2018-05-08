
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

#lista de cores
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
yellow = (200,200,0)#
blue = (0,200,200)#
purple = (139,0,139)#
black = (0,0,0)#
gray = (128,128,128)#
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue= (0,255,255)#
bright_yellow = (255,255,0)#
bright_purple = (255,0,255)#
bright_gray = (192,192,192)#

bal_height = 80
bal_width = 64
clock = py.time.Clock()
#Desktop - Trabalho - Abrindo em pen drive
agulha = py.image.load('C:\Ballooooon/PROJETO/imagens/agulha.png')
balpreto = py.image.load('C:\Ballooooon/PROJETO/imagens/balao-black.png')
balvermelho = py.image.load('C:\Ballooooon/PROJETO/imagens/balao-red.png')
balazul = py.image.load('C:\Ballooooon/PROJETO/imagens/balao-blue.png')
balverde = py.image.load('C:\Ballooooon/PROJETO/imagens/balao-green.png')
espinho = py.image.load('C:\Ballooooon/PROJETO/imagens/espinho.png')
balImg = balpreto
#Windows
#carImg = py.image.load('E:\Pygame_course/carrace.png')
#Linux
#carImg = py.image.load('/media/guilherme/USB DISK/Pygame_course/carrace.png')
def things_dodge(count):
    font = py.font.SysFont(None, 25)
    text = font.render("Dodge: " + str(count), True, black)
    screen.blit(text,(0,0))

def espinhos(x,y):
    screen.blit(espinho,(x,y))
    

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
        Stext = py.font.SysFont('freesansbold.ttf',40)
        TextSurf, TextRec = text_objects("Instruções",Text)##################################
        TextSurf1, TextRec1 = text_objects("Use as setas 'cima, baixo, esquerda, direita'" ,Stext)
        TextSurf2, TextRec2 = text_objects("para desviar das agulhas que vão cair randômicamente",Stext)
        TextSurf3, TextRec3 = text_objects("ao longo do tempo de jogo.",Stext)
        TextSurf4, TextRec4 = text_objects("A velocidade das agulhas aumenta gradativamente,",Stext)
        TextSurf5, TextRec5 = text_objects("cuidado!",Stext)


        TextRec.center = ((display_width/2),(display_height/6))
        TextRec1.center = ((display_width/2),(display_height/3))
        TextRec2.center = ((display_width/2),((display_height/3)+30))
        TextRec3.center = ((display_width/2),((display_height/3)+60))
        TextRec4.center = ((display_width/2),((display_height/3)+120))
        TextRec5.center = ((display_width/2),((display_height/3)+150))


        screen.blit(TextSurf, TextRec)
        screen.blit(TextSurf1, TextRec1)
        screen.blit(TextSurf2, TextRec2)
        screen.blit(TextSurf3, TextRec3)
        screen.blit(TextSurf4, TextRec4)
        screen.blit(TextSurf5, TextRec5)



        button("Play",650,500,100,50, green, bright_green, game_loop)
        button("Back",50,500,100,50,purple,bright_purple,game_intro)

        #py.draw.rect(screen, red,(550,450,100,50))

        py.display.flip()
        clock.tick(15)

def balblack():
    balImg = balpreto
    return game_intro()
def balred():
    balImg = balvermelho
    return game_loop()
def balgreen():
    balImg = balverde        
    return game_intro()
def balblue():
    balImg = balverde        
    return game_intro()

def game_customize():
    customize = True
    while customize:
        for event in py.event.get():
            #print(event)
            if event.type == py.QUIT:
                py.quit()
                quit()

        screen.fill(white)
        largeText = py.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRec = text_objects("Customização", largeText)
        TextRec.center = ((display_width/2),(display_height/6))
        screen.blit(TextSurf, TextRec)

        button("Cor preta",100,400,100,50, gray, bright_gray,balblack)#
        button("Cor vermelha",250,400,150,50, red, bright_red,balred)#
        button("Cor azul",450,400,100,50, blue, bright_blue,balblue)#
        button("Cor verde",600,400,100,50, green, bright_green,balgreen)#


        button("Play",650,500,100,50, green, bright_green, game_loop)
        button("Back",50,500,100,50,purple,bright_purple,game_intro)

        #py.draw.rect(screen, red,(550,450,100,50))

        py.display.flip()
        clock.tick(15)

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
    thing_speed = 10
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
                    if x <= 0:
                        x_change = 0
                    else:
                        x_change = -8
                elif event.key == py.K_RIGHT:
                    if x >= display_width - bal_width:
                        x_change = 0
                    else:
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
        if x >= display_width - bal_width or x <= 0:
            x_change = 0
            #if x >= display_width - bal_width:
                
                            
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodge += 1
            #thing_speed += 1
            #thing_width += (dodge * 1.2)


        #Nível 2
        if dodge > 10 and dodge<12:
            largeText = py.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRec = text_objects('Nível 2!', largeText)
            TextRec.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRec)
            py.display.flip()
            
            #time.sleep(1)
            thing_speed = 13
        #Nível 3
        elif dodge > 20 and dodge < 22:
            largeText = py.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRec = text_objects('Nível 3!', largeText)
            TextRec.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRec)
            py.display.flip()
            thing_speed = 16
        #Nível 4
        elif dodge > 30 and dodge < 32:
            largeText = py.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRec = text_objects('Nível 4!', largeText)
            TextRec.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRec)
            py.display.flip()
            thing_speed = 20
            if x >= display_width - bal_width or x <= 0:
                crash()
        #Nível 5
        elif dodge > 40 and dodge < 42:
            largeText = py.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRec = text_objects('Nível 5!', largeText)
            TextRec.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRec)
            py.display.flip()
            thing_speed = 25
            if x >= display_width - bal_width or x <= 0:
                crash()
        #Nível 6
        elif dodge > 40 and dodge < 42:
            largeText = py.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRec = text_objects('Nível 6!', largeText)
            TextRec.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRec)
            py.display.flip()
            thing_speed = 35
            if x >= display_width - bal_width or x <= 0:
                crash()
        if y <= thing_starty + thing_height and thing_starty <= y + bal_height:
            #print("y cross")

            if   thing_startx >= x and x + bal_width >= thing_startx or x+bal_width >= thing_startx and x + bal_width <= thing_startx+thing_width or x+(bal_width / 2) >= thing_startx and x+(bal_width / 2) <= thing_startx+thing_width :
                crash()



        py.display.flip()
        clock.tick(60)


    





game_intro()
game_loop()
py.quit()
quit()
