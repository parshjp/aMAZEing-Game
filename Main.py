# hashtag   Jonah Dabu, Eduardo Salvacion, Parshva Parikh
# hashtag   2020-11-12
# hashtag   ICS4U
# hashtag   Maze Game (obstacles, coins, timer, scoreboard, levels)

'''
MAC > WINDOWS
'''

# hashtag   level 0 - Jonah, level 1 - Eddie, level 2 - Parshva

from tkinter import Tk, Canvas, messagebox, Button, font, simpledialog, END, Toplevel, scrolledtext, Label, PhotoImage
from Player import Player
from Wall import Wall
from Background import Background           # hashtag  import necessary classes and modules
from EndSquare import EndSquare
from Coin import Coin
from AutoSquare import AutoSquare   
import pygame                               # hashtag  import pygame for collision, portal and coin sound effects
from operator import itemgetter                          
pygame.mixer.init()

# hashtag  create mixer.Sound objects
deadSound = pygame.mixer.Sound("audio/dead.wav")
victorySound = pygame.mixer.Sound("audio/victory_noise.wav")
portalSound = pygame.mixer.Sound("audio/portal.wav")

def gametime():         # hashtag  game timer
    global score_time, seconds, minutes
    seconds += 1
    if seconds == 60:
        minutes += 1        # hashtag  minute and second vars
        seconds = 0
    if seconds <= 9:
        canvas.itemconfig(showTime, text = "TIME:   " + str(minutes) + ':' + '0' + str(seconds))      # hashtag  formatting to display current time
    else:
        canvas.itemconfig(showTime, text = "TIME:   " + str(minutes) + ':' + str(seconds))
    score_time = window.after(1000, gametime)
    
def onkeypress(event):      # hashtag  WASD to move player object
    global wall, player, level, complete
    
    # hashtag  Move the player
    if event.char == "d" or event.char == "D":
        player.move("east")
    elif event.char == "a" or event.char == "A":
        player.move("west")
    elif event.char == "s" or event.char == "S":
        player.move("south")
    elif event.char == "w" or event.char == "W":
        player.move("north")
    
    # hashtag  Iterate through the list of end portals
    for index in range(len(listPortals)):
        
        # hashtag  Check if the user enters the end portal of the level
        if player.getRightSide() >= listPortals[index].getLeftSide() and player.getLeftSide() <= listPortals[index].getRightSide():
            if player.getBottomSide() >= listPortals[index].getTopSide() and player.getTopSide() <= listPortals[index].getBottomSide():
                
                # hashtag  Update the level 
                level += 1
                
                if level == 3:
                    complete = True
                    window.after_cancel(score_time)
                    updateScoreboard()
                    messagebox.showinfo('aMAZEing Game', 'All levels completed!')
                    showScoreboard()
                    showVictory()
                    
                else:
                    updateLevel()
                    pygame.mixer.Sound.play(portalSound)
                    break
    # hashtag  Update the amount of coins the user collected 
    canvas.itemconfig(showCoins, text = "COINS: " + str(player.getNumCoins()))
        
def setWalls():
    global listWalls, level
    
    # hashtag  Set list of walls depending on the current level
    listWalls = [0] * len(WallDimensions[level])
    
    # hashtag  Iterate through the parameters of each wall for the current level and initialize Wall class object
    for index in range(len(listWalls)):
        dimensions = WallDimensions[level][index]
        listWalls[index] = Wall(canvas, dimensions[0], dimensions[1], dimensions[2], dimensions[3])

def setCoins():
    global listCoins, level
    
    # hashtag  Set list of coins depending on the current level
    listCoins = [0] * len(CoinDimensions[level])
    
    # hashtag  Iterate through the parameters of each coin for the current level and initialize Coin class object
    for index in range(len(listCoins)):
        dimensions = CoinDimensions[level][index]
        listCoins[index] = Coin(canvas, dimensions[0], dimensions[1])

def setAutoSquares():
    global listAutoSquares, listAutoOrbits, level
    
    # hashtag  Set list of moving objects  depending on the current level (back and forth movement)
    listAutoSquares = [0] * len(AutoSquareDimensions[level])
    
    # hashtag  Iterate through the parameters of each moving object for the current level and initialize AutoSquare class object
    for index in range(len(listAutoSquares)):
        dimensions = AutoSquareDimensions[level][index]
        listAutoSquares[index] = AutoSquare(canvas, dimensions[0], dimensions[1], dimensions[2], dimensions[3], dimensions[4])
    
    # hashtag  Set list of moving objects  depending on the current level (orbit movement)
    listAutoOrbits = [0] * len(AutoOrbitDimensions[level])
    
    # hashtag  Iterate through the parameters of each moving object for the current level and initialize AutoSquare class object
    for index in range(len(listAutoOrbits)):
        dimensions = AutoOrbitDimensions[level][index]
        listAutoOrbits[index] = AutoSquare(canvas, dimensions[0], dimensions[1], dimensions[2], dimensions[3], dimensions[4])
        
def moveAuto():
    global moveID, listAutoSquares
    
    # hashtag  Initialize contact to False
    contact = False
    
    if player != None:
        # hashtag  Iterate through each moving object (back and forth movement) and move the object
        for index in listAutoSquares:
            index.move()
            
            # hashtag  Check for player to object collision
            if player.getRightSide() > index.getLeftSide() and player.getLeftSide() < index.getRightSide():
                if player.getBottomSide() > index.getTopSide() and player.getTopSide() < index.getBottomSide():
                    contact = True
                    break
                    
        # hashtag  Iterate through each moving object (orbit movement) and move the object   
        for index in listAutoOrbits:
            index.orbit()
            
            # hashtag  Check for player to object collision
            if player.getRightSide() > index.getLeftSide() and player.getLeftSide() < index.getRightSide():
                if player.getBottomSide() > index.getTopSide() and player.getTopSide() < index.getBottomSide():
                    contact = True
                    break
        
        # hashtag  If the user makes contact with the moving object, reset location depending on level
        if contact == True:
            pygame.mixer.Sound.play(deadSound)            
            player.setLocation(listSpawn[level][0], listSpawn[level][1])
    
    # hashtag  Recall function
    moveID = canvas.after(5, moveAuto)

          
def setPortals():
    global level
    
    # hashtag  Depending on the level, display and hide the corresponding portals
    if level == 0:
        listPortals[0].setLocation(PortalDimensions[0][0], PortalDimensions[0][1])
        listPortals[1].hide()
        listPortals[2].hide()
        
    elif level == 1:       
        listPortals[0].hide()
        listPortals[1].setLocation(PortalDimensions[1][0], PortalDimensions[1][1]) 
        listPortals[2].hide() 
        
    elif level == 2:
        listPortals[0].hide()
        listPortals[1].hide() 
        listPortals[2].setLocation(PortalDimensions[2][0], PortalDimensions[2][1])
    
def updateLevel():
    global listWalls, listCoins, listAutoSquares, moveID
    
    # hashtag  Set the color of the buttons, texts, and background depending on the current level 
    if level == 0:
        background.setColor('navajo white')
        btnRestart.config(fg = 'navajo white'), btnScoreboard.config(fg = 'navajo white'), btnHelp.config(fg = 'navajo white')
        btnExit.config(fg = 'navajo white'), canvas.itemconfig(showCoins, fill = 'navajo white'), canvas.itemconfig(showTime, fill = 'navajo white')
        if showName!= None:
            canvas.itemconfig(showName, fill = 'navajo white')

    elif level == 1:
        background.setColor('grey74')
        btnRestart.config(fg = 'grey74'), btnScoreboard.config(fg = 'grey74'), btnHelp.config(fg = 'grey74')
        btnExit.config(fg = 'grey74'), canvas.itemconfig(showCoins, fill = 'grey74'), canvas.itemconfig(showTime, fill = 'grey74')
        if showName!= None:
            canvas.itemconfig(showName, fill = 'grey74')
        
    elif level == 2:
        background.setColor('MediumPurple1')
        btnRestart.config(fg = 'MediumPurple1'), btnScoreboard.config(fg = 'MediumPurple1'), btnHelp.config(fg = 'MediumPurple1')
        btnExit.config(fg = 'MediumPurple1'), canvas.itemconfig(showCoins, fill = 'MediumPurple1'), canvas.itemconfig(showTime, fill = 'MediumPurple1')
        if showName!= None:
            canvas.itemconfig(showName, fill = 'MediumPurple1')
        
    # hashtag  Delete all class objects of the level and cancel moveID
    for x in listWalls:       
        x.delete()
    for x in listCoins:
        x.delete()
    for x in listAutoSquares:
        x.delete()
    for x in listAutoOrbits:
        x.delete()
    if moveID != None:
        moveID = window.after_cancel(moveID)
    
    # hashtag  Display all of the class objects for the current level and start moveID
    setWalls()
    setCoins()
    setAutoSquares()
    moveAuto()
    setPortals()
    
    # hashtag  Pass wall and coin objects to the player
    if player != None:
        player.setWalls(listWalls)
        player.setCoins(listCoins)
        
        # hashtag  Set spawn location of the player
        player.setLocation(listSpawn[level][0], listSpawn[level][1])
       
def close_program():
    # hashtag  Confirm if the user wants to exit
    answer = messagebox.askyesno('aMAZEing Game', 'Are you sure you want to exit?')
    if answer == True:
        exit()
    
def restart_program():
    global level, score_time, moveID, seconds, minutes, complete, score
    window.after_cancel(score_time)
    # hashtag  Confirm if the user wants to reset the game
    answer = messagebox.askyesno("aMAZEing Game", "Would you like to restart?\n\n(If 'Restart' was clicked, this attempt will still be saved on the score board)")
   
    if answer == True and complete == False:
        updateScoreboard()
        # hashtag  Reset window to first level and reset all variables
        level = 0
        updateLevel()
        player.setNumCoins(0)
        seconds, minutes = 0, 0
        gametime()
        complete = False
        score = 0
        # hashtag  Update the amount of coins the user collected 
        canvas.itemconfig(showCoins, text = "COINS: " + str(player.getNumCoins()))
        
    elif answer == True and complete == True:
        window.update()
        window.deiconify()
        # hashtag  Reset window to first level and reset all variables
        level = 0
        updateLevel()
        player.setNumCoins(0)
        seconds, minutes = 0, 0
        gametime()
        complete = False
        score = 0
        # hashtag  Update the amount of coins the user collected 
        canvas.itemconfig(showCoins, text = "COINS: " + str(player.getNumCoins()))
        
    elif answer == False and complete == True:
        exit()
    else: 
        gametime()      #start the game timer again
        

def showScoreboard():
    global name
    window.withdraw()       #show scoreboard window
    top_scoreboard.update()
    top_scoreboard.deiconify()
    window.after_cancel(score_time)
    txtScoreboard.config(state = 'normal')
    txtScoreboard.delete(0.0, END)      #columns for scoreboard
    txtScoreboard.insert(END, "{:^20s}{:^20s}{:^20s}\n\n".format('NAME:', 'SCORE:', 'TIME:'))
    file = open("scoreboard.txt", "r")
    
    listScores = []
    for line in file:
        #Iterate through the text file and add its values to a list
        if line != '' and line != '\n':
            listUser = line.split(',')
            listUser[2] = listUser[2].strip('\n')
            listUser[1] = int(listUser[1])
            listScores.append(listUser)
    
    # hashtag  Sort by name, score
    listScores.sort(key = itemgetter(0))
    listScores.sort(key = itemgetter(1), reverse = True)
    
    # hashtag  Iterate through the list of scores and display it on the text widget
    for index in range(len(listScores)):
        txtScoreboard.insert(END, "{:^20s}{:^20d}{:^20s}\n".format(listScores[index][0], listScores[index][1], listScores[index][2]))
    
    txtScoreboard.config(state = 'disabled')
    
    file.close()

def updateScoreboard():    
    global name, score, minutes, seconds, score, complete 
    # hashtag  Update Score board
    total_seconds = (minutes * 60) + seconds
    if complete == True:
        # hashtag Allow bonus points only if the user completes the whole game
        if total_seconds <= 180:
            bonus_points = 180 - total_seconds
        else:
            bonus_points = 0
    else:
        bonus_points = 0
    
    # hashtag Score is calculated by 20 points per collected coin and if time is less than 3 minutes, bonus point per second remainder
    score = (20 * player.getNumCoins()) + bonus_points
    
    #Add the score of the user to the text file
    with open("scoreboard.txt", "a") as file:
        if seconds <= 9:
            file.write(str(name) + ',' + str(score) + ',' + str(minutes) + ':' +'0'+ str(seconds) + '\n')
        else:
            file.write(str(name) + ',' + str(score) + ',' + str(minutes) + ':' + str(seconds) + '\n')

def close_scoreboard():
    global complete
    # hashtag Display game window when the score board is closed
    if complete == True:
        #Restart program when the score board is shown at the end of the game
        top_scoreboard.withdraw()
        gametime()
        restart_program()
    else:
        top_scoreboard.withdraw()
        window.update()
        window.deiconify()
        gametime()
     
def showHelp():     #readme message
    window.after_cancel(score_time)
    messagebox.showinfo('aMAZEing Game', 'Welcome to an amazing maze game!\n\nNavigate (WASD) your avatar around 3 levels to reach the end portals, while trying to avoid obstacles and getting coins, to achieve the best score you can.\n\n'
                        'The score is based off the amount of coins you collect and the amount of seconds you take to complete all the levels. Each coin is worth 20 points and if the final time is less than 3 minutes, a point is'
                        'awarded for every second you have remaining until 3 minutes.\n\nThere is no penalty for hitting an obstacle, it simply resets you to the level spawn.\n\nThe scoreboard will record scores when you choose to "Restart"'
                        'or when you complete all the levels. It will permanently store them and it will display them in order of highest scores.\n\nWhen you are looking at a pop-up or different window, the time will pause until you come back to the game.')
    gametime()
            
def close_victory():
    # hashtag Withdraw victory window
    top_victory.withdraw()
     
def showVictory():
    # hashtag Display victory top level window
    window.withdraw()
    top_victory.update()
    top_victory.deiconify()
    # hashtag Display victory image
    lblImg.place(x = 2000, y = 2000)
    lblVictory.place(y = window.winfo_screenheight() //2 - 50, x = window.winfo_screenwidth()//2 - 400)
    top_victory.after(3000, showImg)

def showImg():
    # hashtag Display victory and play sound track
    pygame.mixer.Sound.play(victorySound)
    lblVictory.place(x = 2000, y = 2000)
    lblImg.place(x = window.winfo_screenwidth() //2 - 640, y = window.winfo_screenheight() //2 - 360)
    
# hashtag  Initialize window
window = Tk()
window.title('aMAZEing Game')
window.protocol('WM_DELETE_WINDOW', close_program)
WINDOW_WIDTH, WINDOW_HEIGHT = 900,800
window.geometry("%dx%d+%d+%d" % (WINDOW_WIDTH, WINDOW_HEIGHT, window.winfo_screenwidth() // 2 -
    WINDOW_WIDTH // 2, window.winfo_screenheight() // 2 -WINDOW_HEIGHT // 2))

# hashtag  Initialize the main canvas 
canvas = Canvas(window, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, background = "black")
canvas.pack()

# hashtag  Initialize and display button widgets to restart game, display scoreboard, show help, and exit
myFont = font.Font(family = "Comic Sans MS", size = 10, weight = "bold")
btnRestart = Button(canvas, text = 'Restart', font = myFont, fg = 'navajo white', bg = 'black', borderwidth = 10, command = restart_program)
btnRestart.place(x = 270, y = 670, height = 50, width = 100)
btnScoreboard = Button(canvas, text = 'Scoreboard', font = myFont, fg = 'navajo white', bg = 'black', borderwidth = 10, command = showScoreboard)
btnScoreboard.place(x = 50, y = 670, height = 50, width = 100)
btnHelp = Button(canvas, text = 'Help', font = myFont, fg = 'navajo white', bg = 'black', borderwidth = 10, command = showHelp)
btnHelp.place(x = 160, y = 670, height = 50, width = 100)
btnExit = Button(canvas, text = 'Exit', font = myFont, fg = 'navajo white', bg = 'black', borderwidth = 10, command = close_program)
btnExit.place(x = 380, y = 670, height = 50, width = 100)

# hashtag  Bind the controls for the game
window.bind("<KeyPress>", onkeypress)

# hashtag  Initial level and player setting
level = 0
player = None
complete = False

# hashtag  Initialize variables to store name, time components, time ID, and movement ID, user name
seconds = 0
minutes = 0
score = 0
score_time = None
moveID = None
showName = None

# hashtag  Create background
background = Background(canvas, "navajo white")

# hashtag  Initialize list of walls 
listWalls = [] 

# hashtag  Store list of Wall parameters for class object
WallDimensions = [
    
    # hashtag  Level 0
    [   
    (150,50,190,150),
    (50,250,190,290),
    (150,390,330,430),
    (150,430,190,550),
    (290,430,330,650),
    (290,150,330,250),
    (290,250,610,290),
    (610,150,750,190),
    (430,50,470,150),
    (570,150,610,250),
    (430,290,470,390),
    (430,390,710,430),
    (710,290,750,510),
    (710,510,850,550),
    (430,510,610,550),
    (570,510,610,650)
    ],

    # hashtag  Level 1
    [
    (150,50,190,190),
    (150,250,190,390),
    (50,350,150,390),
    (110,490,250,530),
    (250,150,290,650),
    (290,350,530,390),
    (390,50,430,250),
    (530,150,570,390),
    (630,50,670,490),
    (730,150,770,390),
    (770,150,850,190),
    (730,450,850,490),
    (390,450,630,490),
    (290,550,750,590)
    ],
    
    # hashtag  Level 2
    [
    [50, 600, 125, 650],
    [125, 625, 250, 650],
    [275, 625, 400, 650],
    [400, 575, 475, 650],
    [475, 625, 600, 650],
    [750, 625, 825, 650],
    [825, 525, 850, 650],
    [825, 350, 850, 475],
    [825, 175, 850, 300],
    [825, 50, 850, 125],
    [50, 525, 100, 550],
    [100, 100, 125, 550],
    [125, 425, 150, 500],
    [150, 550, 350, 575],
    [150, 425, 225, 475],
    [225, 425, 275, 450],
    [275, 125, 325, 175],
    [275, 240, 300, 300],
    [300, 275, 350, 300],
    [350, 300, 400, 325],
    [175, 50, 200, 375],
    [200, 90, 375, 100],
    [375, 75, 475, 175],
    [475, 100, 700, 150],
    [700, 125, 750, 150],
    [725, 150, 750, 250],
    [750, 200, 775, 250],
    [300, 500, 350, 550],
    [325, 475, 350, 500],
    [350, 350, 375, 525],
    [375, 475, 475, 500],
    [450, 425, 475, 475],
    [375, 350, 475, 375],
    [400, 375, 425, 425],
    [425, 225, 475, 350],
    [375, 225, 425, 275],
    [325, 225, 375, 250],
    [325, 200, 350, 225],
    [450, 550, 575, 575],
    [525, 525, 725, 550],
    [725, 275, 750, 550],
    [750, 275, 775, 325],
    [525, 475, 675, 500],
    [550, 450, 625, 475],
    [600, 350, 625, 450],
    [550, 275, 575, 400],
    [575, 275, 665, 300],
    [665, 250, 675, 475],
    [550, 175, 675, 250],
    [250, 150, 275, 425]
    
    ]
    
    # hashtag  Wall End Bracket
    ]

# hashtag  Initialize list of coins
listCoins = []

# hashtag  Store list of Coin parameters for class object
CoinDimensions = [
    
    # hashtag  Level 0
    [
    (220, 460),
    (780, 445),
    (505, 320)
    ],
    
    # hashtag  Level 1
    [
    (180,570),
    (560, 80),
    (790, 210),
    (300,600)
    ],
    
    # hashtag  Level 2
    [
    [60, 50],
    [60, 490],
    [200,50],
    [275, 200],
    [275, 300],
    [315, 300],
    [575, 50],
    [475, 575],
    [625, 435],
    [675, 250]
    ]
    
    # hashtag  Coin End Bracket
    ]

# hashtag  Initialize list of moving objects
listAutoSquares = []

# hashtag  Store list of AutoSquare parameters for the class object (back and forth movement)
AutoSquareDimensions = [
    
    # hashtag  Level 0
    [
    ("north", "vertical", (290, 390), 160, 370),
    ("south", "vertical", (150, 250), 440, 150),
    ("south", "vertical", (430, 510), 430, 430),
    ("north", "vertical", (430, 510), 590, 490),
    ("east", "horizontal", (750, 850), 750, 290),
    ("north", "vertical", (190, 290), 730, 270)
    ],
    
    # hashtag  Level 1
    [
    ('east', 'horizontal', (50, 150), 50, 290),
    ('east', 'horizontal', (290, 390), 290, 150),
    ('east', 'horizontal', (290, 390), 370, 230),
    ('east', 'horizontal', (430, 530), 430, 150),
    ('east', 'horizontal', (430, 530), 510, 230),
    ('east', 'horizontal', (750, 850), 750, 550),
    ('east', 'horizontal', (750, 850), 830, 570),
    ('east', 'horizontal', (290, 390), 290, 450),
    ('east', 'horizontal', (290, 390), 370, 470),
    ('south', 'vertical', (50, 150), 730, 50),
    ('south', 'vertical', (390, 490), 110, 390),
    ],
    
    # hashtag  Level 2
    [
    ('east', 'horizontal', (75, 175), 100, 75),
    ('north', 'vertical', (350, 425), 50, 375),
    ('south', 'vertical', (275, 350), 75, 300),
    ('north', 'vertical', (475, 550), 175, 500),
    ('south', 'vertical', (450, 550), 225, 500),
    ('north', 'vertical', (225, 350), 200, 250),
    ('south', 'vertical', (100, 225), 225, 200),
    ('south', 'vertical', (275, 350), 500, 300),
    ('east', 'horizontal', (250, 325), 275, 475),
    ('east', 'horizontal', (275, 350), 275, 350),
    ('east', 'horizontal', (275, 350), 325, 375),
    ('east', 'horizontal', (275, 450), 325, 175),
    ('west', 'horizontal', (425, 550), 425, 50),
    ('west', 'horizontal', (400, 550), 450, 500),
    ('east', 'horizontal', (625, 725), 650, 550),
    ('west', 'horizontal', (625, 725), 650, 600),
    ('north', 'vertical', (125, 175), 800, 150),
    ('north', 'vertical', (300, 350), 800, 325),
    ('north', 'vertical', (475, 525), 800, 500)
    ]
    
    # hashtag  AutoSquare End Bracket
    ]

# hashtag  Initialize list of moving objects
listAutoOrbits = []

# hashtag  Store list of AutoSquare parameters for the class object (orbit movement)
AutoOrbitDimensions = [
    
    # hashtag  Level 0, no orbit objects
    [],
    
    # hashtag  Level 1
    [
    ('south', 'vertical', (550, 630, 160, 240), 160, 550),
    ('north', 'vertical', (550, 630, 160, 240), 220, 610),
    ('south', 'vertical', (60, 140, 540, 620), 540, 60),
    ('north', 'vertical', (60, 140, 540, 620), 600, 120),
    ('south', 'vertical', (190, 270, 770, 850), 770, 190),
    ('north', 'vertical', (190, 270, 770, 850), 830, 250)   
    ],
    
    # hashtag  Level 2
    [
    ('south', 'vertical', (50, 125, 725, 800), 725, 50),
    ('south', 'vertical', (400, 475, 275, 350), 275, 400),
    ('south', 'vertical', (400, 475, 475, 550), 475, 400),
    ('south', 'vertical', (175, 250, 475, 550), 475, 175)
    ]
    
    # hashtag  Auto Orbits End Bracket
    ]

# hashtag  Initialize and create list of EndSquare (Portal) class objects
listPortals = [
    
    # hashtag  Level 0
    EndSquare(canvas, 845, 570),
    
    # hashtag  Level 1
    EndSquare(canvas, 845, 75), 
    
    # hashtag  Level 2
    EndSquare(canvas, 420, 288)
    
    ]

# hashtag  Store list of EndSquare parameters for the class object
PortalDimensions = [
    
    (845, 570),
    (845, 75),
    (420, 288)
    
    ]

# hashtag  Store x-position and y-position for spawns, varying by level
listSpawn = [
    
    (90, 90),
    (90, 90), 
    (60, 565)
    
    ]

# hashtag  Create player
player = Player(canvas, background, listSpawn[level][0], listSpawn[level][1], listWalls, listCoins)

# hashtag  Show the number of coins the user has collected and play time 
myFont1 = font.Font(family = "Comic Sans MS", size = 30, weight = "bold")
showCoins = canvas.create_text(610, 660, text = "COINS: " + str(player.getNumCoins()), fill = "navajo white", anchor = "nw", font = myFont1)
showTime = canvas.create_text(610, 710, text = "TIME  : 0:00", fill = "navajo white", anchor = "nw", font = myFont1)
showName = None
# hashtag  Start timer and display all of the level objects depending on the current level
updateLevel()

nameflag = True
while nameflag:
    #Loop until the user enters a name
    name = simpledialog.askstring("aMAZEing Game", 'Player name (no spaces): ')
    if name == None or name == '':
        messagebox.showerror("aMAZEing Game", 'Please enter a valid player name to track score.')
    else:
        # hashtag Store user's name and break from loop
        name = name.strip()
        if name == '':
            messagebox.showerror("aMAZEing Game", 'Please enter a valid player name to track score.')
        else:
            nameflag = False

# hashtag Create canvas text to display player's name        
showName = canvas.create_text(50, 730, text = 'Player: ' + name, fill = "navajo white", anchor = "nw", font = myFont1)
# hashtag Call game timer
gametime()

# hashtag  Bind the controls for the game
window.bind("<KeyPress>", onkeypress)

# hashtag  create window that is shown when the player finishes the maze
top_victory = Toplevel(padx = 10, pady = 10, bg = 'black') # hashtag  initialize a TopLevel widget
top_victory.title('Victory') # hashtag  set the title
top_victory.resizable(False, False)
top_victory.protocol('WM_DELETE_WINDOW', close_victory) # hashtag  set the command for when the user wants to exit the window
top_victory.geometry('%dx%d+%d+%d' % (window.winfo_screenwidth(), window.winfo_screenheight(), 0, 0)) # hashtag  place the window
top_victory.withdraw() # hashtag  withdraw the other windows so that this win
myFont2 = font.Font(family = "Comic Sans MS", size = 6, weight = "bold")
img = PhotoImage(file = 'images/victory.png') # hashtag  create the celebration picture 
lblImg = Label(top_victory, image = img) # hashtag  put the image in a label
lblImg.place(x = 2000, y = 2000, height = 720 , width = 1280) # hashtag  place the label
lblVictory = Label(top_victory, text = 'You completed! Please zoom in and look carefully here for your prize!', fg = 'white', font = myFont2, bg = 'black')
lblVictory.place(y = window.winfo_screenheight() //2 - 50, x = window.winfo_screenwidth()//2 - 400, height = 100 , width = 800)

# hashtag  Initialize top level widget for the score board
top_scoreboard = Toplevel(padx = 10, pady = 10, bg = 'black')
top_scoreboard.title('Scoreboard')
top_scoreboard.resizable(False, False)
top_scoreboard.protocol('WM_DELETE_WINDOW', close_scoreboard)
top_scoreboard.withdraw()

# hashtag  Initialize scrolled text widget for scoreboard 
txtScoreboard = scrolledtext.ScrolledText(top_scoreboard, width = 60, height = 30, padx = 10, pady = 10, state = 'disabled')
txtScoreboard.pack()

window.mainloop()