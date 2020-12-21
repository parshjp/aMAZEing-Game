class Background:
    def __init__(self, canvas, colour = "white"):
        '''
        Initiate an instance of a background of the maze
        
        PARAMETERS
        ----------
        
        canvas (Canvas object)
            The canvas on which the background is placed on
            
        colour (str)
            The colour of the background 
        '''
        self.__canvas = canvas 
        self.__colour = colour 
        self.__leftSide = 50
        self.__topSide = 50
        self.__rightSide = 850
        self.__bottomSide = 650
        self.__background = self.__canvas.create_rectangle(self.__leftSide, self.__topSide,
            self.__rightSide, self.__bottomSide, fill = self.__colour)
        
    def getLeftSide(self):
        '''
        Returns the coordinate of the left side of the background
        
        RETURNS
        -------
        self.__leftSide (int)
            The coordinate of the left side of the background 
        '''
        return self.__leftSide
    
    def getTopSide(self):
        '''
        Returns the coordinate of the top side of the background 
        
        RETURNS
        -------
        self.__topSide (int)
            The coordinate of the top side of the background
        '''
        return self.__topSide
    
    def getRightSide(self):
        '''
        Returns the coordinate of the right side of the background 
        
        RETURNS
        -------
        self.__rightSide (int)
            The coordinate of the right side of the background 
        '''
        return self.__rightSide
    
    def getBottomSide(self):
        '''
        Returns the coordinate of the bottom side of the background 
        
        RETURNS
        -------
        self.__bottomSide (int)
            The coordinate of the bottom side of the background 
        '''
        return self.__bottomSide
    
    def setColor(self, color):
        '''
        Sets the color of the background
        
        PARAMETERS
        ----------
        color (str)
            The color of the background
         
        '''
        self.__colour = color
        self.__canvas.itemconfig(self.__background, fill = self.__colour)