import pygame
import random

RADIUS=15
SCREEN=600


class View:
    def __init__(self,screen,model,app):
        self.model=model
        self.screen = screen
        self.start=True
        self.gameOver=False
        self.app=app
        
        
    def update(self):
        #identify if runs into self
        if self.model.curPos in self.model.coordinates[:-1]:
            self.gameOver = True
                    
        #identify if runs out of boundary
        if self.model.curPos[0] not in range(600) or self.model.curPos[1] not in range(600):
            self.gameOver = True
        green=[(0,153,0),(0,102,0),(0,102,51),(0,204,102),(0,153,76)]
        red=(255,0,0)
        pygame.draw.circle(self.screen, red, (self.app.xCoor,self.app.yCoor), RADIUS, 0)
        
        for i in self.model.coordinates:
            pygame.draw.circle(self.screen, green[random.randint(0,4)], (i[0],i[1]), RADIUS, 0)

        pygame.display.update()
      
        

class Model:
    def __init__(self,curPos,app):
        self.coordinates=[]
        self.curPos=curPos
        self.coordinates.append(self.curPos)
        self.app=app

   
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #identify pressed key
                if event.key == pygame.K_LEFT:
                    self.move(-1,0)
                elif event.key == pygame.K_RIGHT:
                    self.move(1,0)
                elif event.key == pygame.K_UP:
                    self.move(0,-1)
                elif event.key == pygame.K_DOWN:
                    self.move(0,1) 

    def move(self,x,y):
        self.curPos=(self.curPos[0]+x*RADIUS*2,self.curPos[1]+y*RADIUS*2)
        self.coordinates.append(self.curPos)
        #identify eat apple or not
        if self.curPos!=(self.app.xCoor,self.app.yCoor):
            self.coordinates=self.coordinates[1:]
        else:   
            self.app.xCoor=random.randint(0,19)*2*RADIUS+RADIUS
            self.app.yCoor=random.randint(0,19)*2*RADIUS+RADIUS

class Start:
    
    def __init__(self,screen,view):
        self.view=view
        self.screen=screen
        pygame.draw.rect(self.screen, (60,60,60),(250,450,100,50),2)
        font = pygame.font.Font(None, 36)
        screen.blit(font.render("Start",True,(255,0,0)),(270,465))
        self.image()
        self.click()
    def image(self):
        pic = pygame.image.load("fruit.jpg").convert()
        self.screen.blit(pic, (50, 100))
    def click(self):
        for event in pygame.event.get():
            if event.type ==pygame.MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                if position[0] in range(250,350) and position[1] in range(450,500):
                    self.view.start=False
                          
class App():
    def __init__(self):
        self.xCoor=random.randint(0,19)*2*RADIUS+RADIUS
        self.yCoor=random.randint(0,19)*2*RADIUS+RADIUS  
    def main(self):
    # initialize the pygame environment
        pygame.init()
        # config the screen
        screen_size = (SCREEN,SCREEN)
        screen = pygame.display.set_mode(screen_size)
        white = (255, 255, 255)
        screen.fill(white)
        model = Model((315,315),self)
        view = View(screen,model,self)
        
        while view.start==True:
            screen.fill(white)
            Start(screen,view)
            pygame.display.update()
    
        while view.start==False and view.gameOver == False:
            screen.fill(white)
            model.update()
            view.update()
        
        while view.gameOver == True:
            font = pygame.font.Font(None, 50)
            screen.blit(font.render("Game Over!",True,(255,0,0)),(200,100))
            pygame.display.update()
            event=pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
        

if __name__ == "__main__":
    app=App()
    app.main()
    