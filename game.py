import pygame
from player import Player
from monster import Monster
import os
from colors import *

pygame.init()
pygame.font.init() #initialisation pour le traitement de texte de python

#########################################################
#-------------Début IMPORTATION VARIABLES---------------#
#########################################################


""" Setup """

#Générer le fenêtre du jeux: 
width = 1080 #taille
height = 620 #hauteur
pygame.display.set_caption("SURPRISE NEGGA")
screen = pygame.display.set_mode ((width, height)) #ceci renvoie la surface pour permettre les dessins

#Importer le background:
background = pygame.image.load("assets/game_background_3.1.png") #importer le background
background = pygame.transform.scale(background,(width,height))
disableEffect = pygame.image.load(os.path.join("assets", "disabling.png"))
disableEffect = pygame.transform.scale(disableEffect,(width, height))
baniere = pygame.image.load(os.path.join("assets","baniere.png"))
play_button = pygame.image.load(os.path.join("assets","play_bouton.png"))
play_button = pygame.transform.scale(play_button,(300, 125))
play_button_normale = play_button
play_button_active = pygame.transform.scale(play_button,(325, 150))
play_button_rect = play_button.get_rect()
bgWidth = 1920
bgHeight = 1080
bgLoop = 0
power = True
intro = True
running = False
pausing = False
ani = 6 #animation cycle
fps = 120
level = 1

#LOADING TEXT:
text  = pygame.font.SysFont('comicsans', 50)
pause_label = text.render("PAUSING GAME", 1, WHITE)

###################################################################
#-----------------------FIN IMPORTATION VARIABLES-----------------#
###################################################################

###################################################################
#---------------------------Début CLASS---------------------------#
###################################################################
class Game:

    #Charger les caractéristiques de bases aux chargement du jeux!
    def __init__(self):
        #Définir si le jeux à commencer ou non!
        self.is_playing = False

        #Définir si le jeux est en pause ou non!
        self.is_pausing = False

        #Génerer le joueurs!
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)

        #Génerer les monstres!
        self.all_monster = pygame.sprite.Group()

        #initialise les listes des touches appuyer!
        self.pressed = {}   

        #gaming intro:
        self.intro = True

        #gaming inputn name:
        self.inputName = False

        self.score = 0
        
        
    def start_level(self,level):
        self.all_monster = pygame.sprite.Group()
        for i in range(level*5):
            self.spawn_monster()

    def game_over (self):
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.intro = True
        self.is_playing = False

    def update(self,screen):
        #Dessiner notre joueurs sur son surface:
        screen.blit(self.player.image, self.player.rect)
        self.player.spriting(ani)

        #Dessiner la barre de vie du joueurs:
        self.player.update_health_bar(screen)

        #Récuperer et Dessiner l'ensembles des projectiles du joeurs:
        for projectile in self.player.all_projectiles:
            projectile.move()
        self.player.all_projectiles.draw(screen)

        #Récuperer et Déssiner l'ensembles des monstres:
        for monster in self.all_monster:
            monster.update_health_bar(screen)
            monster.forward()
            if (monster.rect.x+monster.image.get_width() <= 0):
                self.all_monster.remove(monster)
                self.score += 5
            if (monster.health <=0):
                self.all_monster.remove(monster)
                self.score += 10

        self.all_monster.draw(screen)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self,level)
        self.all_monster.add(monster)

###################################################################
#-----------------------------FIN CLASS---------------------------#
###################################################################