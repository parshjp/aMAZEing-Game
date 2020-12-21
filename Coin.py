from tkinter import PhotoImage
import pygame

class Coin:
    def __init__(self, canvas, x, y):
        '''
        Initialize an instance of a coin 
        
        PARAMETERS 
        ----------
        canvas (Canvas object)
            The canvas that the coin will interact with
            
        x (int)
            The x coordinate of the coin
            
        y (int)
            The y coordinate of the coin
        '''
        self.__canvas = canvas 
        self.__image = PhotoImage(file = "images/coin.png") #create the image of the coin
        self.__image.subsample(2) #resize the coin
        '''
        The set of variables below will make collision detection easier
        '''
        self.__leftSide = x 
        self.__topSide = y 
        self.__rightSide = self.__leftSide + self.__image.width()
        self.__bottomSide = self.__topSide + self.__image.height()
        
        #create the coin image
        self.__coin = self.__canvas.create_image(self.__leftSide, self.__topSide, 
            image = self.__image, anchor = "nw")
        
        self.__isCollected = False #boolean var to check if the coin is collected
        
        self.__coinSound = pygame.mixer.Sound("audio/coin_collect.wav") #the audio file for when the coin is collected 
        
    def getLeftSide(self):
        '''
        Returns the coordinate of the left side of the coin
        
        RETURNS
        -------
        self.__leftSide (int)
            The coordinate of the left side of the coin
        '''
        return self.__leftSide
    
    def getRightSide(self):
        '''
        Returns the coordinate of the right side of the coin
        
        RETURNS
        -------
        self.__rightSide (int)
            The coordinate of the right side of the coin
        '''
        return self.__rightSide 
    
    def getTopSide(self):
        '''
        Returns the coordinate of the top side of the coin
        
        RETURNS
        -------
        self.__topSide (int)
            The coordinate of the top side of the coin
        '''
        return self.__topSide
    
    def getBottomSide(self):
        '''
        Returns the coordinate of the bottom side of the coin
        
        RETURNS
        -------
        self.__bottomSide (int)
            The coordinate of the bottom side of the coin
        '''
        return self.__bottomSide
    
    def checkCollected(self):
        '''
        Returns True if the coin has been collected by the player, False if it has not
        
        RETURNS
        -------
        self.__isCollected (boolean)
        '''
        return self.__isCollected
    
    def collect(self):
        '''
        Indicates that the coin is collected
        
        PARAMETERS 
        ----------
        bool (boolean)
        '''
        
        pygame.mixer.Sound.play(self.__coinSound)
        self.__canvas.itemconfig(self.__coin, image = "") #visually remove the coin from the maze
        self.__isCollected = True #set to True to indicate that the coin was collected 
        
    def delete(self):
        '''
        Delete object from canvas
        '''
        self.__canvas.delete(self.__coin)
        