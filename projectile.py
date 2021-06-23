import pygame

###################################################################
#---------------------------Début CLASS---------------------------#
###################################################################
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity= 7
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (45,45))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x+80
        self.rect.y = player.rect.y+50
        self.origin_image = self.image #On va dévoir garder l'image d'origine parce qu'on va le modifier
        self.angle = 0 #Angle rotation


    def rotate(self):
        self.angle += 20
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for monster in (self.player.game.check_collision(self,self.player.game.all_monster)):
            monster.damage(self.player.attack)
            self.remove()

        if self.rect.x > 1080:
            self.remove()

    def remove(self):
        self.player.all_projectiles.remove(self)

###################################################################
#-----------------------------FIN CLASS---------------------------#
###################################################################