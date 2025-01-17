import pygame
import random

WIDTH=800
HEIGHT=571
FPS=50

#IMAGES

    #menu background
menubackground=pygame.image.load('pictures/BackgroundMenu.jpg')
game_title=pygame.image.load('pictures/menutitle.png')

    #game background
bg = pygame.image.load('pictures/Background.jpg')
background=pygame.transform.scale(bg,(WIDTH,HEIGHT))

    #buttons
play_button=pygame.image.load('pictures/buttonplay.png')
highscores_button=pygame.image.load('pictures/buttonhighscores.png')
about_button=pygame.image.load('pictures/buttonabout.png')
back_button=pygame.image.load('pictures/buttonback.png')

    #about
about_info=pygame.image.load('pictures/about.png')

    #highscores
highscores_info=pygame.image.load('pictures/highscores.png')

    #game over
go=pygame.image.load('pictures/gameover.jpg')
gameover=pygame.transform.scale(go,(WIDTH,HEIGHT))

    #empty space
void=pygame.image.load('pictures/void.png')

    #lives
l3=pygame.image.load('pictures/3lives.png')
l2=pygame.image.load('pictures/2lives.png')
l1=pygame.image.load('pictures/1lives.png')
lives_3=pygame.transform.scale(l3,(235,95))
lives_2=pygame.transform.scale(l2,(235,95))
lives_1=pygame.transform.scale(l1,(235,95))

    #wolf
UL=pygame.image.load('pictures/wLG.png')
UR=pygame.image.load('pictures/wPG.png')
DL=pygame.image.load('pictures/wLD.png')
DR=pygame.image.load('pictures/wPD.png')
wolf_UL=pygame.transform.scale(UL,(290,290))
wolf_DL=pygame.transform.scale(DL,(290,290))
wolf_UR=pygame.transform.scale(UR,(275,275))
wolf_DR=pygame.transform.scale(DR,(275,275))

    #eggs
e1=pygame.image.load('pictures/Egg1.png')
e2=pygame.image.load('pictures/Egg2.png')
e3=pygame.image.load('pictures/Egg3.png')
e4=pygame.image.load('pictures/Egg4.png')
e5=pygame.image.load('pictures/Egg5.png')
eT=pygame.image.load('pictures/Egg_toxic.png')
egg_1=pygame.transform.scale(e1,(60,60))
egg_2=pygame.transform.scale(e2,(60,60))
egg_3=pygame.transform.scale(e3,(60,60))
egg_4=pygame.transform.scale(e4,(60,60))
egg_5=pygame.transform.scale(e5,(60,60))
egg_toxic=pygame.transform.scale(eT,(50,50))

#MUSIC
generate_soundtrack=random.choice(['music/music1.mp3','music/music2.mp3','music/music3.mp3','music/music4.mp3'])

#PARAMETERS
i=0
j=-1
n=125
speed=[]
for _ in range(23):
    speed.append(n)
    n-=5
n_copied=speed[i]
n_mod=int(n_copied/5)
first_pos=0
    
score=0
lives=3

end_game=False
toxic_egg=False

name='Username: (press any key to add)'

highscores_text=open('highscores.txt','r')
highscores_lines=highscores_text.readlines()
highscores_help=[]
lines_help=[]
highscores_text.close()

for line in highscores_lines:
    try:
        a=line.split('...',1)
        a[0]=int(a[0])
        highscores_help.append(a)
    except:
        pass

    
#CLASSES
class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=void
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/2,HEIGHT/2)
        
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.image=wolf_UL
            self.rect=self.image.get_rect()
            self.rect.center=(WIDTH/2,HEIGHT/2)
        if keys[pygame.K_a]:
            self.image=wolf_DL
            self.rect=self.image.get_rect()
            self.rect.center=(WIDTH/2,HEIGHT/2)
        if keys[pygame.K_p]:
            self.image=wolf_UR
            self.rect=self.image.get_rect()
            self.rect.center=(450,300)
        if keys[pygame.K_l]:
            self.image=wolf_DR
            self.rect=self.image.get_rect()
            self.rect.center=(450,300)
        if end_game:
            self.image=void
            self.rect=self.image.get_rect()
            self.rect.center=(WIDTH/2,HEIGHT/2)
            

class PhantomWolf(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=void
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/2,HEIGHT/2)
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.image=void
            self.rect.center=(0,0)
        if keys[pygame.K_a]:
            self.image=void
            self.rect.center=(0,HEIGHT)
        if keys[pygame.K_p]:
            self.image=void
            self.rect.center=(WIDTH,0)
        if keys[pygame.K_l]:
            self.image=void
            self.rect.center=(WIDTH,HEIGHT)
        if end_game:
            self.image=void
            self.rect=self.image.get_rect()
            self.rect.center=(WIDTH/2,HEIGHT/2)
        
            
class Eggs(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=void
        self.rect=self.image.get_rect()
        self.rect.center=(100,100)
        self.positions=[]
        self.toxic_egg_pos=0
        self.updated_egg=False
        self.updated_toxic=False
        
    def update(self):
        #normal eggs (all corners)
            #drawn positions
        if first_pos==1:
            self.positions=[(100,100),(150,125),(190,170),(230,200),(275,220),(0,0)]
            self.updated_egg=True
        if first_pos==2:
            self.positions=[(75,325),(140,325),(175,325),(215,315),(260,320),(0,HEIGHT)]
            self.updated_egg=True
        if first_pos==3:
            self.positions=[(700,100),(675,125),(625,160),(600,180),(575,195),(WIDTH,0)]
            self.updated_egg=True
        if first_pos==4:
            self.positions=[(720,350),(670,335),(625,325),(580,315),(550,305),(WIDTH,HEIGHT)]
            self.updated_egg=True

            #positions displaing
        if self.updated_egg==True and n==n_copied:
            self.image=egg_1
            self.rect.center=self.positions[0]
            egg_sound1.play()
            
        if self.updated_egg==True and n==n_copied-1*n_mod:
            self.image=egg_2
            self.rect.center=self.positions[1]
            egg_sound2.play()
            
        if self.updated_egg==True and n==n_copied-2*n_mod:
            self.image=egg_3
            self.rect.center=self.positions[2]
            egg_sound3.play()
            
        if self.updated_egg==True and n==n_copied-3*n_mod:
            self.image=egg_4
            self.rect.center=self.positions[3]
            egg_sound4.play()
            
        if self.updated_egg==True and n==n_copied-4*n_mod:
            self.image=egg_5
            self.rect.center=self.positions[4]
            egg_sound5.play()
            
        if self.updated_egg==True and n==1:
            self.image=void
            self.rect.center=self.positions[5]
            self.updated_egg=False

        
        #toxic egg
        if first_pos==5:
            self.image=egg_toxic
            self.toxic_egg_pos=random.choice([1,2,3,4])
            self.updated_toxic=True

            #drawn positions
        if self.toxic_egg_pos==1:
            self.positions=[(100,100),(150,125),(190,170),(230,200),(275,220),(0,0)]
        if self.toxic_egg_pos==2:
            self.positions=[(75,325),(140,325),(175,325),(215,315),(260,320),(0,HEIGHT)]
        if self.toxic_egg_pos==3:
            self.positions=[(700,100),(675,125),(625,160),(600,180),(575,195),(WIDTH,0)]
        if self.toxic_egg_pos==4:
            self.positions=[(720,350),(670,335),(625,325),(580,315),(550,305),(WIDTH,HEIGHT)]
        
            #positions displaing
        if self.updated_toxic==True and n==n_copied:
            self.rect.center=self.positions[0]
            egg_sound1.play()
            
        if self.updated_toxic==True and n==n_copied-1*n_mod:
            self.rect.center=self.positions[1]
            egg_sound2.play()            

        if self.updated_toxic==True and n==n_copied-2*n_mod:
            self.rect.center=self.positions[2]
            egg_sound3.play()
            
        if self.updated_toxic==True and n==n_copied-3*n_mod:
            self.rect.center=self.positions[3]
            egg_sound4.play()
            
        if self.updated_toxic==True and n==n_copied-4*n_mod:
            self.rect.center=self.positions[4]
            egg_sound5.play()
            
        if self.updated_toxic==True and n==1:
            self.image=void
            self.rect.center=self.positions[5]
            self.toxic_egg_pos=0
            self.updated_toxic=False
        
        #game over
        if end_game==True:
            self.image=void
            self.rect=self.image.get_rect()
            self.rect.center=(100,100)

            self.updated_egg=False
            self.updated_toxic=False

#FUNCTIONS
def points(score,colour,place):
    font = pygame.font.SysFont("comicsansms", 41)
    text=font.render(str(score), True, colour)
    screen.blit(text,place)
    

def game_intro():
    global name
    global highscores_help
    global highscores_lines
    
    beep_play=0
    k=0
    
    intro = True
    while intro:
        screen.blit(menubackground,(0,0))
        screen.blit(game_title,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if k==0:
                    name=name[:-22]
                    k+=1
                if event.key==pygame.K_BACKSPACE:
                    if len(name)>10:
                        name=name[:-1]
                else:
                    if len(name)<29:
                        name+=event.unicode

        #username
        font = pygame.font.SysFont("comicsansms", 20)
        text=font.render(name, True, (255,0,0))
        screen.blit(text,(270,500))
                
        #buttons
        screen.blit(play_button,(195,160))
        screen.blit(highscores_button,(217,250))
        screen.blit(about_button,(245,330))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 200<mouse[0]<600 and 170<mouse[1]<230:
            pygame.draw.circle(screen,(0,0,0),(180,200),10)
            pygame.draw.circle(screen,(0,0,0),(630,200),10)
            if beep_play==0:
                beep.play()
                beep_play=1
            
            if click[0]==1:
                
                game_loop()
                i=0
                j=-1
                n=125
                n_copied=speed[i]
                n_mod=int(n_copied/5)
                    
                score=0
                lives=3
                first_pos=0
                
        elif 220<mouse[0]<580 and 250<mouse[1]<310:
            pygame.draw.circle(screen,(0,0,0),(200,280),10)
            pygame.draw.circle(screen,(0,0,0),(610,280),10)
            if beep_play==0:
                beep.play()
                beep_play=1
            if click[0]==1:
                game_highscores()
            
        elif 240<mouse[0]<560 and 330<mouse[1]<390:
            pygame.draw.circle(screen,(0,0,0),(225,360),10)
            pygame.draw.circle(screen,(0,0,0),(575,360),10)
            if beep_play==0:
                beep.play()
                beep_play=1
            if click[0]==1:
                game_about()
        else:
            beep_play=0

        #sorting highscores
        highscores_help=sorted(highscores_help,key=lambda sc: sc[0],reverse=True)
        highscores_help=highscores_help[:10]
        highscores_text=open('highscores.txt','w+')
        
        for hh in highscores_help:
            new=str(hh[0])+'...'+hh[1]
            highscores_text.write(new)
        highscores_text.close()
        
        
        pygame.display.update()
                
    
def game_loop():    
    global name
    global first_pos
    global i
    global j
    global n
    global speed
    global n_copied
    global n_mod
    global score
    global highscores_help
    global lives
    global end_game
    global toxic_egg
    
    beep_play=0
   
    running=True
    while running:
        screen.blit(background,(0,0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                highscores_help.append([score,name[10:]+'\n'])
                i=0
                j=-1
                n=125
                score=0
                lives=3
                first_pos=0
                running=False
                
        #time & speed
        if n>1:
            n-=1
            first_pos=0
            
        else:
            n_copied=speed[i]
            n=n_copied
            first_pos=random.choice([1,2,3,4,5])
            if first_pos==5:
                toxic_egg=True
            else:
                toxic_egg=False
            n_mod=int(n_copied/5)
            j+=1
            if j%3==0 and i<22:
                j+=1
                i+=1
            
            
        wolves.update()
        eggs.update()
        
        #score & lives
        if pygame.sprite.spritecollide(phantomwolf,eggs,False):
            if toxic_egg==True:
                lives=-1
                egg_cracking.play()
            else:
                score+=1
                collect.play()
        if n==1 and not pygame.sprite.spritecollide(phantomwolf,eggs,False):
            if toxic_egg==False:
                lives-=1
                if lives!=2:
                    egg_cracking.play()
        if lives==2 or lives==3:
            screen.blit(lives_3,(390,475))
        if lives==1:
            screen.blit(lives_2,(390,475))
        if lives==0:
            screen.blit(lives_1,(390,475))
        if lives==-1:
            end_game=True
            wolves.update()
            wolves.draw(screen)
            eggs.update()
            end_game=False
            highscores_help.append([score,name[10:]+'\n'])
            game_over()
            i=0
            j=-1
            n=125
            score=0
            lives=3
            first_pos=0
            running=False
            
        wolves.draw(screen)
        eggs.draw(screen)
        points(score,(0,0,0),(440,7))

        pygame.display.update()
        clock.tick(FPS)


def game_over():
    global score
    
    running=True
    while running:
        screen.blit(gameover,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    running=False

        points(score,(255,0,0),(540,280))

        pygame.display.update()


def game_highscores():
    beep_play=0
    
    running= True
    while running:
        screen.blit(menubackground,(0,0))
        screen.blit(highscores_info,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        highscores_text=open('highscores.txt')
        highscores_display=highscores_text.readlines()
        
        k=0
        font = pygame.font.SysFont("comicsansms", 20)
        for line in highscores_display:
            text=font.render(line.rstrip("\n"), True, (0,0,0))
            screen.blit(text,(285,120+k))
            k+=25

        #back button
        screen.blit(back_button,(260,400))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 260<mouse[0]<550 and 400<mouse[1]<460:
            pygame.draw.circle(screen,(0,0,0),(245,430),8)
            pygame.draw.circle(screen,(0,0,0),(560,430),8)
            if beep_play==0:
                beep.play()
                beep_play=1
            if click[0]==1:
                highscores_text.close()
                running=False
        else:
            beep_play=0
                
        pygame.display.update()


def game_about():
    about = True
    while about:
        screen.blit(menubackground,(0,0))
        screen.blit(about_info,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #back button
        screen.blit(back_button,(260,400))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 260<mouse[0]<550 and 400<mouse[1]<460:
            pygame.draw.circle(screen,(0,0,0),(245,430),8)
            pygame.draw.circle(screen,(0,0,0),(560,430),8)
            if beep_play==0:
                beep.play()
                beep_play=1
            if click[0]==1:
                about=False
        else:
            beep_play=0
                
        pygame.display.update()


#GAME
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Wolf & Chicken cops')
pygame.display.set_icon(eT)
clock=pygame.time.Clock()

#music adjusting
music=pygame.mixer.music.load(generate_soundtrack)
pygame.mixer.music.set_volume(0.02)
pygame.mixer.music.play(-1)

#sound effects adjusting
beep=pygame.mixer.Sound('music/cursor.wav')
beep.set_volume(0.008)
egg_sound1=pygame.mixer.Sound('music/egg_sound1.wav')
egg_sound2=pygame.mixer.Sound('music/egg_sound2.wav')
egg_sound3=pygame.mixer.Sound('music/egg_sound3.wav')
egg_sound4=pygame.mixer.Sound('music/egg_sound4.wav')
egg_sound5=pygame.mixer.Sound('music/egg_sound5.wav')
egg_cracking=pygame.mixer.Sound('music/egg_cracking.wav')
collect=pygame.mixer.Sound('music/collect.wav')

#sprites
wolves= pygame.sprite.Group()
eggs=pygame.sprite.Group()

wolf=Wolf()
wolves.add(wolf)

phantomwolf=PhantomWolf()
wolves.add(phantomwolf)

eggs.add(Eggs())

#start game
game_intro()

pygame.quit()
