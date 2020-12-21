class Wall:
    def __init__(self, canvas, x1, y1, x2, y2):
        '''
        Initialize and instance of a wall. Each x and y coordinate is in relation to the canvas, ie.
        "x1" pixels into the canvas
        
        !!!!!!!!!!LIMITS!!!!!!!!!
        !                       !
        !  50 <= x1, x2 <= 850  !
        !  50 <= y1, y2 <= 650  !
        !                       !
        !!!!!!!!!!!!!!!!!!!!!!!!!
        
        PARAMETERS
        ----------
        canvas (Canvas object)
            The canvas which the walls will be placed on
            
        x1 (int)
            The 1st x coordinate, or left side of the wall
            
        y1 (int)
            The 1st y coordinate, or top side of the wall
            
        x2 (int)
            The 2nd x coordinate, or right side of the wall
            
        y2 (int)
            The 2nd y coordinate, or bottom side of the wall
        '''
        self.__canvas = canvas 
        self.__x1 = x1 
        self.__x2 = x2 
        self.__y1 = y1 
        self.__y2 = y2
        
        '''
        Create wall object
        '''
        self.__wall = self.__canvas.create_rectangle(self.__x1, self.__y1, self.__x2, self.__y2, fill = "black")
    
    def getLeftSide(self):
        '''
        Returns the coordinate of the left side of the wall
        
        RETURNS
        -------
        self.__x1 (int)
            The coordinate of the left side of the wall
        '''
        return self.__x1
    
    def getRightSide(self):
        '''
        Returns the coordinate of the right side of the wall
        
        RETURNS
        -------
        self.__x2 (int)
            The coordinate of the right side of the wall
        '''
        return self.__x2
    
    def getTopSide(self):
        '''
        Returns the coordinate of the top side of the wall
        
        RETURNS
        -------
        self.__y1 (int)
            The coordinate of the top side of the wall
        '''
        return self.__y1
    
    def getBottomSide(self):
        '''
        Returns the coordinate of the bottom side of the wall
        
        RETURNS
        -------
        self.__y2 (int)
            The coordinate of the bottom side of the wall
        '''
        return self.__y2
    
    def delete(self):
        '''
        Delete object from canvas
        '''
        self.__canvas.delete(self.__wall)