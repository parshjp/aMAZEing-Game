class Player:
    def __init__(self, canvas, background, xpos, ypos, walls, coins):
        '''
        Initialize an instance of a player
        
        PARAMETERS
        ----------
        canvas (Canvas object)
            The canvas which the player will interact with. Also will serve as a border
            
        maze (.create_rectangle object)
            The background/ main moving area for the player
            
        xpos (int)
            Initializes the starting x position of the player
            
        ypos (int)
            Initializes the starting y position of the player
            
        walls (list)
            A list of walls that the player cannot move into
            
        coins (list of Coin objects)
            The coins that the user can get
        '''
        self.__canvas = canvas
        self.__background = background 
        self.__startx = xpos 
        self.__starty = ypos
        self.__xpos = xpos
        self.__ypos = ypos
        self.__width = 20
        self.__height = 20
        self.__walls = walls
        
        '''
        Create player object
        '''
        self.__player = self.__canvas.create_rectangle(self.__xpos, self.__ypos, 
            self.__xpos + self.__width, self.__ypos + self.__height, fill = "blue")

        self.__contact = False 
        
        self.__coins = coins
        self.__coinsCollected = 0
        '''
        The purpose of the variables below is to give a more practical 
        variable name to do collision detection
        '''
        self.__topSide = self.__ypos
        self.__leftSide = self.__xpos
        self.__bottomSide = self.__ypos + self.__height
        self.__rightSide = self.__xpos + self.__width
        '''
        The player will be in the shape of a rectangle with a height and width of self.__height and 
        self.__width. The starting x position and y position will be relative to self.__canvas, ie, 
        the player will be placed "xpos" pixels into the canvas, NOT the maze
        '''    
        
    def checkCoins(self):
        '''
        Checks for collision between the player and the coins
        '''
        for coin in self.__coins: #iterate through each coin and see if collision occured
            if self.__topSide <= coin.getBottomSide() - 3 and self.__bottomSide >= coin.getTopSide() + 3:
                if self.__rightSide >= coin.getLeftSide() + 3 and self.getLeftSide() <= coin.getRightSide() - 3:
                    if not coin.checkCollected(): #if the coin has not been collect it already, collect it
                        coin.collect()
                        self.__coinsCollected += 1 #increase number of coins the player has collected
        
    def checkObstacles(self, direction):
        '''
        method returns True if the player can move, checks the walls
        '''
        if direction == "east": #if the player tries to move east
            for wall in self.__walls: #iterate through all the existing walls 
                if self.__topSide < wall.getBottomSide() and self.__bottomSide > wall.getTopSide(): #check if the player is in the bounds vertically
                    if wall.getRightSide() >= self.__rightSide >= wall.getLeftSide(): #check if the player is in the bounds horizontally 
                        move = False #player cannot move
                        break 
                    else: 
                        move = True #player can move
                else:
                    move = True #player can move
        elif direction == "west": #if the player tries to move west
            for wall in self.__walls: #iterate through all the existing walls
                if self.__topSide < wall.getBottomSide() and self.__bottomSide > wall.getTopSide(): #check if the player is in the bounds vertically
                    if wall.getLeftSide() <= self.__leftSide <= wall.getRightSide(): #check if the player is in the bounds horizontally 
                        move = False #player cannot move
                        break
                    else:
                        move = True #player can move
                else:
                    move = True #player can move
        elif direction == "north": #if player tries to move north
            for wall in self.__walls: #iterate through all the existing walls
                if self.__rightSide > wall.getLeftSide() and self.__leftSide < wall.getRightSide(): #check if the player is in the bounds horizontally
                    if wall.getTopSide() <= self.__topSide <= wall.getBottomSide(): #check if the player is in the bounds vertically
                        move = False #player cannot move
                        break 
                    else:
                        move = True #player can move
                else:
                    move = True #player can move
        elif direction == "south": #if player tries to move south 
            for wall in self.__walls: #iterate through all the existing walls
                if self.__rightSide > wall.getLeftSide() and self.__leftSide < wall.getRightSide(): #check if the player is in the bounds horizontally 
                    if wall.getBottomSide() >= self.__bottomSide >= wall.getTopSide(): #check if the player is in the bounds vertically 
                        move = False #player cannot move
                        break 
                    else:
                        move = True #player can move
                else:
                    move = True #player can move
                    
        return move

    def move(self, direction):
        '''
        Move the player
        
        PARAMETERS
        ----------
        direction (string)
            Helps decide which direction the player will travel
        '''
        
        #get the direction the player is moving
        #check if the player is in the maze boundaries 
        #if the player can move in that direction, increase or decrease the coordinate value
        if direction == "east":
            if self.getRightSide() <= self.__background.getRightSide() - 5:
                if self.checkObstacles("east"):
                    self.__xpos += 5
        elif direction == "west":
            if self.getLeftSide() >= self.__background.getLeftSide() + 5:
                if self.checkObstacles("west"):
                    self.__xpos -= 5
        elif direction == "north":
            if self.getTopSide() >= self.__background.getTopSide() + 5:
                if self.checkObstacles("north"):
                    self.__ypos -= 5
        elif direction == "south":
            if self.getBottomSide() <= self.__background.getBottomSide() - 5:
                if self.checkObstacles("south"):
                    self.__ypos += 5
        #draw the player at the new position 
        self.__canvas.coords(self.__player, self.__xpos, self.__ypos, 
            self.__xpos + self.__width, self.__ypos + self.__height)
        
        #update the variable values
        self.__topSide = self.__ypos
        self.__leftSide = self.__xpos
        self.__bottomSide = self.__ypos + self.__height
        self.__rightSide = self.__xpos + self.__width
        

        self.checkCoins() #check if the player made contact with a coin
    
    def setCoins(self, coins):
        '''
        Set coins of the level
        
        PARAMETERS
        ----------
        coins (list of Coin objects)
            The coins that the user can get
        '''
        self.__coins = coins
    
    def setWalls(self, walls):
        '''
        Set walls of the level
        
        PARAMETERS
        ----------
        walls (list)
            A list of walls that the player cannot move into
        '''
        self.__walls = walls 
        
    def setLocation(self, x, y):
        '''
        Sets the location of the player
        
        PARAMETERS 
        ----------
        x (int)
            The x coordinate of the player 
        
        y (int)
            The y coordinate of the player
        '''
        self.__xpos = x 
        self.__ypos = y
        self.__canvas.coords(self.__player, self.__xpos, self.__ypos,
            self.__xpos + self.__width, self.__ypos + self.__height)
    
    def setNumCoins(self, numCoins):
        '''
        Sets number of coins collected
        
        PARAMETERS
        ----------
        numCoins (int)
            The number of coins collected
        '''
        self.__coinsCollected = numCoins
        
    def getLeftSide(self):
        '''
        Return the x coordinate of the left side of the player
        
        RETURNS
        -------
        self.__xpos (int)
            The x coordinate of the left side of the player
        '''
        return self.__xpos
    
    def getRightSide(self):
        '''
        Return the x coordinate of the right side of the player
        
        RETURNS
        -------
        self.__xpos + self.__width (int)
            The x coordinate of the right side of the player
        '''
        return self.__xpos + self.__width
    
    def getTopSide(self):
        '''
        Return the y coordinate of the top side of the player
        
        RETURNS
        -------
        self.__ypos (int)
            The y coordinate of the top side of the player
        '''
        return self.__ypos
        
    def getBottomSide(self):
        '''
        Return the y coordinate of the bottom side of the player
        
        RETURNS
        -------
        self.__ypos + self.__height (int)
            The y coordinate of the bottom side of the player
        '''
        return self.__ypos + self.__height
    
    def getContact(self):
        '''
        Return the contact status of the player
        
        RETURNS
        -------
        self.__contact (boolean)
            The finish status of the player 
        '''
        return self.__contact
    
    def getNumCoins(self):
        '''
        Returns the number of coins the player collected 
        
        RETURNS 
        -------
        self.__coinsCollected (int)
            The number of coins collected 
        '''
        return self.__coinsCollected