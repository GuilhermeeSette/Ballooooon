import pygame as py
import random


def cresce(x,y):
  balImg = 'Balão Grande'
  py.display.blit(balImg,(x,y))


def mini(x,y):
  balImg = 'Balão mini'
  py.display.blit(balImg,(x,y))

def escudo(x,y):
  '''
  Não tem colisão com as agulhas por 7 dodges
  '''

def gad():
  power = random.randint(1,3)
  x = random.randint(0,800)
  y = random.randint(0,600)
  if power == 1:
    escudo(x,y)
  elif power == 2:
    mini(x,y)
  elif power == 3:
    cresce(x,y)
    
    
