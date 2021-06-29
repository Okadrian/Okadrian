grid_size=15

import random

import pygame

import time

from pygame.locals import *

class Snake_game_main():

    windowWidth = 410

    windowHeight = 410

    def __init__(self, grid_row, grid_column):

        self._running=True

        self.snake_direction=1

        self.step=1

        self.length_of_snake=3

        self.__row = grid_row

        self.__col = grid_column

        self.__board=[]

        self.snake_x=[3,3,3]

        self.snake_y=[3,4,5]

        self.apple_x=2

        self.apple_y=4

        self.delta=30

    def on_init(self):  

        pygame.init()   

        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)    

        self._running = True    

        self._image_surf = pygame.image.load("block.jpg").convert() 

        self._apple_surf = pygame.image.load("greenblock.jpg").convert()    

        self._wall_surf = pygame.image.load("wallblock.jpg").convert()    

    def on_cleanup(self):   

        pygame.quit()   

    def on_event(self, event):  

        if event.type == QUIT:  

            self._running = False   

    


    def on_execute(self):#Start programmet via theAPP

        if self.on_init() == False:

            self._running = False

        while( self._running ):

            pygame.event.pump()

            keys = pygame.key.get_pressed()
 
            if (keys[K_RIGHT]):#HÖGER
                self.snake_direction=1
 
            if (keys[K_LEFT]):#Vänster
                self.snake_direction=3
 
            if (keys[K_UP]):#UP
                self.snake_direction=0
 
            if (keys[K_DOWN]):#NER
                self.snake_direction=2
 
            if (keys[K_ESCAPE]):#Stäng av spelet om jag klickar ner

                self._running = False

            self.snake_collide()

            self.update_game()

            self.snake_print_on_grid()#Byter ut en plats på brädet

            self.game_field_list_print()

            time.sleep (200.0 / 1000.0);#Vänta

        self.on_cleanup()#stäng av spelet 

    def game_field_list_print(self): #Prints the gamefield by making it into strings

        self._display_surf.fill(((0,0,0)))

        for k in range (0,len(self.__board)):

            a=k*self.delta

            for i in range (0,len(self.__board[0])-1):

                b=i*self.delta


                if self.__board[k][i]=="S":

                    self._display_surf.blit(self._apple_surf,(b,a))

                if self.__board[k][i]=="W":

                    self._display_surf.blit(self._wall_surf,(b,a))

                if self.__board[k][i]=="F":

                    self._display_surf.blit(self._image_surf,(b,a))

        pygame.display.update()#Updates the window

    def new_apple_postion(self):

        print("THIS IS A SUCCESS")

        TEST=True

        count=0


        while TEST==True:

            self.apple_y=random.randint(2,grid_size-2)

            self.apple_x=random.randint(2,grid_size-2)

            for i in range(0,self.length_of_snake):

                if self.apple_y==self.snake_y:

                    count+1#VI KAN GÖRA SÅ ATT DEN ANPASSAR SIG GENOM ATT TA + ELLER - I FÖRHÅLLANDE TILL DEN TAGNA RUTAN

                if self.apple_x==self.snake_x:

                    count+1

                if count==0:

                    TEST=False
    def update_game(self):
        self.snake_take_place_of_part_before_this_part()#Ormen tar följer efter sutt huvud

        spawn_new_apple=self.snake_move()#Om vi får en vis return så får ett äpplet en ny placering

        if spawn_new_apple==1:

            self.new_apple_postion()#ger en ny placering år äpplet
    def make_board(self):

        for row in range(self.__row):

            self.__board.append([])

            for col in range(self.__col):

                self.__board[row].append('0')

        return self.__board

    def snake_collide(self):

        for i in range (0,self.length_of_snake):

            if [self.snake_x[0]]==[self.snake_x[i]]:

                if [self.snake_y[0]]==[self.snake_y[i]]:

                    self.lost()

        if [self.snake_x[0]]==0:

            self.lost()

        if [self.snake_y[0]]==grid_size:

            self.lost()

        if [self.snake_y[0]]==0:

            self.lost()

        if [self.snake_y[0]]==grid_size:  

            self.lost()

    def lost(self):

        large_text = pygame.font.Font('freesansbold.ttf',115)

        red=(255,0,0)

        text_surf, text_rect = self.text_objects("You lost", large_text, red)

        self._display_surf.blit(text_surf, text_rect)

    def text_objects(self, text, font,color):#Defines text that i use in intro and outro

        textSurface = font.render(text, True, color)

        return textSurface, textSurface.get_rect()

    def snake_take_place_of_part_before_this_part(self):

        try:

            for i in range (self.length_of_snake-1, 0, -1):

                self.snake_x[i]=self.snake_x[i-1]

                self.snake_y[i]=self.snake_y[i-1]

        except:

            print("ERROR CODE")

    def snake_print_on_grid(self):

        for s in range (0,grid_size):

            for k in range (0,grid_size):

                 self.__board[s][k]="0"

        self.__board[self.apple_y][self.apple_x]="F"

        for i in range (0,self.length_of_snake):
            try:
                self.__board[self.snake_y[i]][self.snake_x[i]]="S"
            except:
                continue


    def snake_move(self):

        if self.snake_direction==0:

            self.snake_y[0]=self.snake_y[0]-1

            #rör dig upp
        if self.snake_direction==1:

            self.snake_x[0]=self.snake_x[0]+1

            #Rör dig höger ut
        if self.snake_direction==2:

            self.snake_y[0]=self.snake_y[0]+1

            #Rör dig ner
        if self.snake_direction==3:

            self.snake_x[0]=self.snake_x[0]-1

            #Rör dig åt vänster
        if (self.snake_x[0]==self.apple_x):

            if (self.snake_y[0]==self.apple_y):

                self.snake_x.append(len(self.snake_x))

                self.snake_y.append(len(self.snake_x))

                print("DID I APPEND?")

                print(self.snake_x)

                print(self.snake_y)

                self.length_of_snake=self.length_of_snake+1

                return(1)

        return(0)

    def __repr__(self):

        return '\n'.join([' '.join(row) for row in self.__board])




g = Snake_game_main(grid_size,grid_size)#Definerar g som grid och säger att grid har fem rader och 5 columner

g.make_board()#Skapar ett bräde med antalet rader och kolumner som definerades i klassen

g.new_apple_postion()#Vi skapar ett plats år äpplet

g.on_execute()

