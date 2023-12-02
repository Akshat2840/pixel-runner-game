import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = score_font.render(f'Score : {current_time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (300,30))
    screen.blit(score_surface,score_rect)
    return current_time


def game_intro_screen():
    screen.fill("#003566")

    heading_font = pygame.font.Font(None,60)

    heading1_surface = heading_font.render("Pixel Runner",False,"#ffb703")
    heading1_rect = heading1_surface.get_rect(center = (300,30))
    screen.blit(heading1_surface,heading1_rect)

    player_img = pygame.image.load("D:\Programming\PyGame\character.png").convert_alpha()
    player_img_size = (200,180)
    player_img = pygame.transform.scale(player_img,player_img_size)
    player_rect = player_img.get_rect(center = (300,155))
    screen.blit(player_img,player_rect)

    heading2_surface = heading_font.render("Press Space To Play",False,"#ffb703")
    heading2_rect = heading2_surface.get_rect(center = (300,290))
    screen.blit(heading2_surface,heading2_rect)

def game_over_screen():
    screen.fill("#003566")

    heading_font = pygame.font.Font(None,60)

    heading1_surface = heading_font.render(f"Score:{score}",False,"#ffb703")
    heading1_rect = heading1_surface.get_rect(center = (300,30))
    screen.blit(heading1_surface,heading1_rect)

    player_img = pygame.image.load("D:\Programming\PyGame\character.png").convert_alpha()
    player_img_size = (200,180)
    player_img = pygame.transform.scale(player_img,player_img_size)
    player_rect = player_img.get_rect(center = (300,155))
    screen.blit(player_img,player_rect)

    heading2_surface = heading_font.render("Press Space To Play Again",False,"#ffb703")
    heading2_rect = heading2_surface.get_rect(center = (300,290))
    screen.blit(heading2_surface,heading2_rect)

pygame.init()

screen = pygame.display.set_mode((600,350))
pygame.display.set_caption("Akshat")
clock = pygame.time.Clock()
score_font = pygame.font.Font(None,30)

background_surface = pygame.image.load('D:\Programming\PyGame\sky.jpg').convert()
background_rect = background_surface.get_rect(topleft = (0,0))


snail_surface = pygame.image.load("D:\Programming\PyGame\snail_img.png").convert_alpha()
snail_surface_size=(45,45)
snail_surface=pygame.transform.scale(snail_surface,snail_surface_size)
snail_rect = snail_surface.get_rect(topleft  = (400,238))

player_surface = pygame.image.load("D:\Programming\PyGame\character.png").convert_alpha()
player_surface_size=(58,58)
player_surface=pygame.transform.scale(player_surface,player_surface_size)
player_rect = player_surface.get_rect(topleft = (100,228))

player_gravity = 0
start_time=0
game_active = False 

score = 0

while(True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()

        if(game_active == True):
            if(event.type == pygame.KEYDOWN):
                if((event.key == pygame.K_SPACE or event.key == pygame.K_UP) and player_rect.top == 228):
                    player_gravity = -20 

                if(event.key == pygame.K_RIGHT):
                    player_rect.left += 10

                if(event.key == pygame.K_LEFT):
                    player_rect.left -= 10

                

        else:
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                game_active = True
                snail_rect.left = 600
                player_rect.topright = (100,228)
                start_time = int(pygame.time.get_ticks() / 1000)

    if(game_active == True):
        screen.blit(background_surface,background_rect)

        score = display_score()
        
        screen.blit(snail_surface,snail_rect)
        snail_rect.left-=4

        screen.blit(player_surface,player_rect)
        # pygame.draw.rect(screen ,(255,0,0),[100 , 228 , 10 , 10])


        player_gravity += 1
        player_rect.top += player_gravity


        if(snail_rect.right<0):
            snail_rect.left=600

        if(player_rect.top >= 228):
            player_rect.top = 228

        if(snail_rect.colliderect(player_rect)):
            game_active = False

        if(snail_rect.left == player_rect.left):
            score+=1

    else:
        if(score == 0):
            game_intro_screen()
        else:
            game_over_screen()



    pygame.display.update()
    clock.tick(60)