class EndSquare:
    def __init__(self, canvas, x, y):
        '''
        Initialize an instance of an end square area
        This is the end point of the maze
        
        The end square will be anchored "nw" of "x" and "y"
        
        The dimensions are already predetermined 
        
        PARAMETERS
        ----------
        canvas (Canvas object)
            The canvas where the end square will interact with all other objects on the same canvas
            
        x (int)
            The x coordinate of the end square
            
        y (int)
            The y coordinate of the end square 
        '''
        
        self.__leftSide = x 
        self.__topSide = y 
        self.__rightSide = self.__leftSide + 5 
        self.__bottomSide = self.__topSide + 50
        self.__canvas = canvas
        
        '''
        Create end square object
        '''
        self.__endSquare = self.__canvas.create_rectangle(self.__leftSide, self.__topSide, self.__rightSide, self.__bottomSide, fill = "lime")
        
    def hide(self):
        '''
        Moves portal off screen
        '''
        self.__leftSide = 2000
        self.__topSide = 2000
        self.__rightSide = 2020
        self.__bottomSide = 2020
        
        self.__canvas.coords(self.__endSquare, self.__leftSide, self.__topSide, self.__rightSide, self.__bottomSide)
    
    def setLocation(self, x , y):
        '''
        Sets location of the portal
        
        PARAMETERS
        ----------
        x (int)
            The x coordinate of the portal
        
        y (int)
            The y coordinate of the portal
        '''
        self.__leftSide = x
        self.__topSide = y
        self.__rightSide = x + 5
        self.__bottomSide = y + 50
        self.__canvas.coords(self.__endSquare, self.__leftSide, self.__topSide, 
                            self.__rightSide, self.__bottomSide)
        
    def getLeftSide(self):
        '''
        Returns the coordinate of the left side of the finish square
        
        RETURNS
        -------
        self.__leftSide (int)
            The coordinate of the left side of the finish square
        '''
        return self.__leftSide
    
    def getRightSide(self):
        '''
        Returns the coordinate of the right side of the finish square
        
        RETURNS
        -------
        self.__rightSide (int)
            The coordinate of the right side of the finish square
        '''
        return self.__rightSide 
    
    def getTopSide(self):
        '''
        Returns the coordinate of the top side of the finish square
        
        RETURNS
        -------
        self.__topSide (int)
            The coordinate of the top side of the finish square
        '''
        return self.__topSide
    
    def getBottomSide(self):
        '''
        Returns the coordinate of the bottom side of the finish square
        
        RETURNS
        -------
        self.__bottomSide (int)
            The coordinate of the bottom side of the finish square
        '''
        return self.__bottomSide