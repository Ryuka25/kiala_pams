#Importation des modules nécessaires:

import sys

import pygame

pygame.init()
from game import *
from projectile import *
from scoreStorage import *

# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_name = ''

# create rectangle pour l'input du nom
input_rect = pygame.Rect(200, 200, 140, 32)

# change la couleur quand l'joueur appuye sur le label
color_active = pygame.Color('lightskyblue3')

#couleur normale du label de l'input:
color_passive = pygame.Color('chartreuse4')
color = color_passive

#initialization du couleur du label
active = False
scorefinale = 0

#score dico
scoreDico = fileToDico("score.txt")

###################################################################
#-----------------------DéBUT LOOOOOOOPPPPPPPP--------------------#
###################################################################

#Charger le game:
game = Game()

"""
    Main Loop
            """

#demmarage Intro:
clock = 0 #initialization compteur pour le jeux!
run = True
while run:
    while game.intro:
        clock += 1
        (pygame.time.Clock()).tick(fps)

        #Dessiner le background sur la surface 'screen'
        screen.blit(background, (bgLoop,0)) #Position (x,y)
        screen.blit(background, (width+bgLoop,0))

        if (bgLoop == -width):
            screen.blit(background, (width+bgLoop,-40))
            bgLoop = 0
        bgLoop -= 2

        if clock >= fps:
            #Importation de la banière:
            screen.blit(baniere, (0,0))

            #Importation de la banière:
            screen.blit(baniere, (0,0))
            screen.blit(play_button, play_button_rect)
            play_button_rect.x = ((screen.get_width()/2) - play_button.get_width()/2)
            play_button_rect.y = ((screen.get_height()/2) - (play_button.get_height()/2)+50 )

        #mettre à jour la fenêtre   
        pygame.display.update()

        #action répondant aux touches du clavier!
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    pygame.quit()
                    sys.exit()
                finally:
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                #Vérifier si la souris est en collision avec le rectangle du button!
                if play_button_rect.collidepoint(event.pos):
                    play_button, play_button_active = play_button_active, play_button
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button_rect.collidepoint(event.pos):
                    play_button, play_button_active = play_button_active, play_button
                    game.start_level(level)
                    game.inputName = True
                    game.intro = False

    while game.inputName:

        orderList = dicoToOrderList(scoreDico)

        #ajout du fond:
        screen.blit(disableEffect, (0,0))

        #!Réceuil des intéractions:
        for event in pygame.event.get():
        
        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
    
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]

                elif event.key == pygame.K_RETURN and len(user_name) >= 3:
                    game.is_playing = True
                    game.inputName = False  
                else:
                    user_name += event.unicode
                
        if active:
            color = color_active
        else:
            color = color_passive
            
        pygame.draw.rect(screen, color, input_rect)
    
        text_surface = base_font.render(user_name, True, WHITE)
        
        # Ajuste la position des charactères:
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        # Ajoute un max pour réstreindre les inputs:
        input_rect.w = max(100, text_surface.get_width()+10)

        #ajout des 5 premiers:
       
        stat_label = text.render(f"TOP 5 BEST PLAYERS:", 1, WHITE)
        screen.blit(stat_label, (width/2,100))
        first_label = text.render(f"{orderList[0]}", 1, WHITE)
        screen.blit(first_label, (width/2,150))
        second_label = text.render(f"{orderList[1]}", 1, WHITE)
        screen.blit(second_label, (width/2,200))
        third_label = text.render(f"{orderList[2]}", 1, WHITE)
        screen.blit(third_label, (width/2,250))
        fourth_label = text.render(f"{orderList[3]}", 1, WHITE)
        screen.blit(fourth_label, (width/2,300))
        fifth_label = text.render(f"{orderList[4]}", 1, WHITE)
        screen.blit(fifth_label, (width/2,350))

        screen.blit(baniere, (0,250))
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    while game.is_playing: #Tant que le jeux est lancée:
        
        (pygame.time.Clock()).tick(fps)

        scorefinale = game.score

        #Dessiner le background sur la surface 'screen'
        screen.blit(background, (bgLoop,0)) #Position (x,y)
        screen.blit(background, (width+bgLoop,0))
        if (bgLoop == -width):
            screen.blit(background, (width+bgLoop,-40))
            bgLoop = 0
        bgLoop -= 2

        #Gérer les levels!
        if len(game.all_monster) == 0:
                level += 1
                game.start_level(level)
                game.score += 50

        #Dessiner les labels du jeux:
        level_label = text.render(f"Level : {level}", 1, WHITE)
        screen.blit(level_label, (10,10))
        

        score_label = text.render(f"Score: {scorefinale}", 1, WHITE)
        screen.blit(score_label, (width-score_label.get_width()-10, 10))

        game.update(screen)

        while game.is_pausing:
            #Récupère le background sur la surface 'screen'
            screen.blit(background, (bgLoop,-40)) #Position (x,y)
            screen.blit(background, (width+bgLoop,-40))
            if (bgLoop == -width):
                screen.blit(background, (width+bgLoop,-40))
                bgLoop = 0
            bgLoop -= 2

            #ajouter des affichages pendant le pause!
            screen.blit(disableEffect, (0,0))
            screen.blit(pause_label, (width/2 - pause_label.get_width()/2, 350))            
            
            #On ajoute rien d'autres pour avoir un jeux non trichée !

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game.pressed = {}
                        game.is_pausing = False

        #mettre à jour la fenêtre
        pygame.display.update()

        #action répondant aux touches du clavier!
        if (game.pressed.get(pygame.K_RIGHT) or (game.pressed.get(ord("d")))) and ((game.player.rect.x)+game.player.rect.width < width):
            game.player.moveRight()
        elif (game.pressed.get(pygame.K_LEFT) or (game.pressed.get(ord('q')))) and ((game.player.rect.x)> 0):
            game.player.moveLeft()
        if ((game.pressed.get(pygame.K_UP)) or (game.pressed.get(ord("z")))) and ((game.player.rect.y)-10 > 0):
            game.player.moveUp()
        elif ((game.pressed.get(pygame.K_DOWN)) or (game.pressed.get(ord("s")))) and ((game.player.rect.y)+game.player.rect.height < height):
            game.player.moveDown()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    pygame.quit()
                    sys.exit()
                except:
                    running = False
                finally:
                    quit()

            if event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                    
                if event.key == pygame.K_SPACE:
                    game.player.launchProjectile()
                if event.key == pygame.K_p:
                    game.is_pausing = True

            if event.type == pygame.KEYUP:
                game.pressed[event.key] = False
    
    scoreDico.__setitem__(user_name,scorefinale)
    dicoToFile(scoreDico,"score.txt")
###################################################################
#-----------------------FIN LOOOOOOOPPPPPPPP----------------------#
###################################################################
