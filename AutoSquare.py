class AutoSquare:
    def __init__(self, canvas, direction, movement, bounds, x, y, colour = "red"):
        '''
        Create moving object given its initial x and y position
        
        The auto square will be anchored "nw" of "x" and "y"
        
        Its size is predetermined to 20 pixels width and 20 pixels height
        
        Initial direction is either north, south, east, or west
        
        Initial movement is either vertical or horizontal
        
        Bounds:
            Back and Forth: 
                vertical: (Top Side, Bottom Side)
                horizontal:(Left Side, Right Side)
            
            Orbit:
                initial movement: (Top Side, Bottom Side, Left Side, Right Side)
                
        PARAMETERS
        ----------
        canvas (Canvas object)
            The canvas where the auto square will interact with all other objects on the same canvas
        
        direction (str)
            Initial direction of the auto square ("north", "south", "east", or "west")
        
        movement (str)
            Initial movement of auto square ("vertical, "horizontal")
        
        bounds (tuple)
            Tuple must only contain integers
    
            Back and Forth: 
                vertical: (Top Side, Bottom Side)
                horizontal:(Left Side, Right Side)
            
            Orbit:
                initial movement: (Top Side, Bottom Side, Left Side, Right Side)
            
        x (int)
            The x coordinate of the auto square
            
        y (int)
            The y coordinate of the auto square 
        
        colour (str)
            The colour of the auto square
        '''
        
        self.__canvas = canvas  
        self.__direction = direction
        self.__movement = movement 
        self.__colour = colour 
        self.__speed = 0.25
        self.__width = 20 
        self.__height = 20
        self.__bounds = bounds
        self.__leftSide = x
        self.__topSide = y
        self.__rightSide = self.__leftSide + self.__width
        self.__bottomSide = self.__topSide + self.__height
        
        '''
        Create auto square object
        '''
        self.__autoSquare = self.__canvas.create_rectangle(self.__leftSide, self.__topSide, 
            self.__leftSide + self.__width, self.__topSide + self.__height, fill = self.__colour) 
        
    def move(self):
        '''
        Moves object back and forth depending on the movement (vertical or horizontal)
        self.__bounds (tuple)
            Vertical: (Top Side, Bottom Side)
            Horizontal: (Left Side, Right Side)
            These are the boundaries of the back and forth movement
        '''
        
        if self.__movement == "vertical":
            
            if self.__direction == "south":
                self.__topSide += self.__speed
                self.__bottomSide += self.__speed
                
                if self.__bottomSide >= self.__bounds[1]:
                    self.__direction = "north"
            
            elif self.__direction == "north":
                self.__topSide -= self.__speed
                self.__bottomSide -= self.__speed
                
                if self.__topSide <= self.__bounds[0]:
                    self.__direction = "south"
            
        elif self.__movement == "horizontal":
            
            if self.__direction == "east":
                self.__leftSide += self.__speed
                self.__rightSide += self.__speed
                
                if self.__rightSide >= self.__bounds[1]:
                    self.__direction = "west"
            
            elif self.__direction == "west":
                self.__leftSide -= self.__speed
                self.__rightSide -= self.__speed
                
                if self.__leftSide <= self.__bounds[0]:
                    self.__direction = "east"
        
        self.__canvas.coords(self.__autoSquare, self.__leftSide, self.__topSide, 
                             self.__rightSide, self.__bottomSide)
        
    def orbit(self):
        '''
        Moves object counter clockwise
        self.__bounds (tuple)
            (Top Side, Bottom Side, Left Side, Right Side)
            These are the boundaries of the object's orbit
        '''
        
        if self.__movement == "vertical":
            
            if self.__direction == "south":
                self.__topSide += self.__speed
                self.__bottomSide += self.__speed
                
                if self.__bottomSide >= self.__bounds[1] and self.__leftSide == self.__bounds[2]:
                    self.__direction = "east"
                    self.__movement = "horizontal"
                    
            
            elif self.__direction == "north":
                self.__topSide -= self.__speed
                self.__bottomSide -= self.__speed
                
                if self.__topSide <= self.__bounds[0] and self.__rightSide == self.__bounds[3]:
                    self.__direction = "west"
                    self.__movement = "horizontal"
            
        elif self.__movement == "horizontal":
            
            if self.__direction == "east":
                self.__leftSide += self.__speed
                self.__rightSide += self.__speed
                
                if self.__rightSide >= self.__bounds[3] and self.__bottomSide == self.__bounds[1]:
                    self.__direction = "north"
                    self.__movement = 'vertical'
            
            elif self.__direction == "west":
                self.__leftSide -= self.__speed
                self.__rightSide -= self.__speed
                
                if self.__leftSide <= self.__bounds[2] and self.__topSide == self.__bounds[0]:
                    self.__direction = "south"
                    self.__movement = "vertical"
        
        self.__canvas.coords(self.__autoSquare, self.__leftSide, self.__topSide, 
                             self.__rightSide, self.__bottomSide)
    
    def getLeftSide(self):
        '''
        Returns the coordinate of the left side of the autoSquare
        
        RETURNS
        -------
        self.__leftSide (int)
            The coordinate of the left side of the autoSquare
        '''
        return self.__leftSide
    
    def getRightSide(self):
        '''
        Returns the coordinate of the right side of the autoSquare
        
        RETURNS
        -------
        self.__rightSide (int)
            The coordinate of the right side of the autoSquare
        '''
        return self.__rightSide
    
    def getTopSide(self):
        '''
        Returns the coordinate of the top side of the autoSquare
        
        RETURNS
        -------
        self.__topSide (int)
            The coordinate of the top side of the autoSquare
        '''
        return self.__topSide
    
    def getBottomSide(self):
        '''
        Returns the coordinate of the bottom side of the autoSquare
        
        RETURNS
        -------
        self.__bottomSide (int)
            The coordinate of the bottom side of the autoSquare
        '''
        return self.__bottomSide
    
    def delete(self):
        '''
        Deletes the class object from the canvas
        '''
        self.__canvas.delete(self.__autoSquare)