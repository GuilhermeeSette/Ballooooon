import pygame as py
from aula_13 import teste
def game_intro():
    intro = True
    while intro:
        for event in py.event.get():
            #print(event)
            if event.type == py.QUIT:
                py.quit()
                quit()

        teste.screen.fill(teste.white)
        largeText = py.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRec = text_objects("A Bit racey!", largeText)
        TextRec.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRec)


        button("Play",150,450,100,50, green, bright_green, game_loop)
        button("Instructions",350,450,100,50, yellow,bright_yellow,instrucao)
        button("Quit",550,450,100,50, red, bright_red, quitgame)

        #py.draw.rect(screen, red,(550,450,100,50))

        py.display.flip()
        clock.tick(15)
#def instrucao():
