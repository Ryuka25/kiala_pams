import pygame
import os
from colors import *
from projectile import *
from game import *

###################################################################
#---------------------------Début CLASS---------------------------#
###################################################################
class Player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.airCapacity = 5
        self.images = []
        self.frame = 7 #compter le nombre d'images
        for i in range(7):
            self.image = pygame.image.load(os.path.join("assets/player{}{}.png".format("Walk",i)))
            self.image = pygame.transform.scale(self.image, (100, 120))
            self.images.append(self.image)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 360

    def damage(self,amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar(self,surface):
        #Ajouter des pixels au position pour bien placer!
        bar_position = [self.rect.x+20, self.rect.y-10, self.health, 5] #position x, position y, width, height
        max_bar_position = [self.rect.x+20, self.rect.y-10, self.max_health, 5] #position x, position y, width, height
        pygame.draw.rect(surface, RED, max_bar_position)
        pygame.draw.rect(surface, LIGHT_GREEN, bar_position)

    #animation pour le personnages!
    def launchProjectile(self):
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def spriting(self,ani):
        self.frame += 1
        if self.frame > 6*ani:
            self.frame = 0
        self.image = self.images[self.frame//ani]

    def moveRight(self):
        if not (self.game.check_collision(self,self.game.all_monster)):
            self.rect.x += self.velocity

    def moveLeft(self):
        self.rect.x -= self.velocity

    def moveUp(self):
        self.rect.y -= self.airCapacity

    def moveDown(self):
        self.rect.y += self.airCapacity

###################################################################
#-----------------------------FIN CLASS---------------------------#
###################################################################