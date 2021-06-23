import pygame
import random
import os
from colors import *

###################################################################
#---------------------------Début CLASS---------------------------#
###################################################################
class Monster(pygame.sprite.Sprite):

    def __init__(self, game, level): #Charger les caractéristique de bases de notre monstres!
        super().__init__()
        self.game = game
        self.health= 100
        self.max_health= 100
        self.attack = 0.2
        self.image = pygame.image.load(os.path.join("assets", "monster0.png"))
        self.image = pygame.transform.scale(self.image,(130,150))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = 1000+ random.randint (0,1000)
        self.rect.y = random.randint(0,500)
        self.velocity = random.randint(2, (level*5))


    def damage(self, amount):
        self.health -= amount
        
    def update_health_bar(self,surface):
        #Ajouter des pixels au position pour bien placer!
        bar_position = [self.rect.x+20, self.rect.y-10, self.health, 5] #position x, position y, width, height
        max_bar_position = [self.rect.x+20, self.rect.y-10, self.max_health, 5] #position x, position y, width, height
        pygame.draw.rect(surface, RED, max_bar_position)
        pygame.draw.rect(surface, LIGHT_GREEN, bar_position)

    def forward(self):
        if not (self.game.check_collision(self,self.game.all_player)):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)