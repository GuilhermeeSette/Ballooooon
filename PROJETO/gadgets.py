        def pow_e(posx,posy):
            circ = py.draw.circle(screen, (0,0,255), (posx, posy), 5)
            if y <= posy + 10 and posy <= y + bal_height:
                    #print("y cross")

                    if   posx >= x and x + bal_width >= posx or x+bal_width >= posx and x + bal_width <= posx+10 or x+(bal_width / 2) >= posx and x+(bal_width / 2) <= posx+10 :
                        escudo()
                        
        def pow_c(posx, posy):
            circ = py.draw.circle(screen, (0,0,0), (posx, posy), 5)
            if y <= posy + 10 and posy <= y + bal_height:
                    #print("y cross")

                if   posx >= x and x + bal_width >= posx or x+bal_width >= posx and x + bal_width <= posx+10 or x+(bal_width / 2) >= posx and x+(bal_width / 2) <= posx+10 :
                    cresce()

        def pow_m(posx, posy):
            circ = py.draw.circle(screen, (0,255,0), (posx, posy), 5)
            if y <= posy + 10 and posy <= y + bal_height:
                    #print("y cross")

                if   posx >= x and x + bal_width >= posx or x+bal_width >= posx and x + bal_width <= posx+10 or x+(bal_width / 2) >= posx and x+(bal_width / 2) <= posx+10 :
                    mini()
                        
        def cresce():
          global balImg
          balImg = balazul
          


        def mini():
          global balImg
          balImg = balverde
          

        def escudo():
          for i in range(dodge,dodge + 10,1):
            if y <= thing_starty + thing_height and thing_starty <= y + bal_height:
                    #print("y cross")

                    if   thing_startx >= x and x + bal_width >= thing_startx or x+bal_width >= thing_startx and x + bal_width <= thing_startx+thing_width or x+(bal_width / 2) >= thing_startx and x+(bal_width / 2) <= thing_startx+thing_width :
                        print('Funcionou!')

        def gad():
          power = random.randint(1,3)
          posx = random.randint(0,800)
          posy = random.randint(0,600)
          if power == 1:
            pow_m(posx,posy)
          elif power == 2:
            pow_e(posx,posy)
          elif power == 3:
            pow_c(posx,posy)

        if dodge > 2 != 0 and dodge < 10 != 0:
            gad()
