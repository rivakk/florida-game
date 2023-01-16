'''
Name: Riva Kansakar
CSC 201
Programming Project 3

In this game, there will be a bucket, crabs and seashells in a
beach setting. The player will have to collect the seashells using
the bucket. If they miss, they loose one point, if they collect a
seashell, they gain one point. If you touch the crab with the bucket,
you loose. You need 20 points to win the game.

Assistance: I took help of the group tutoring to use Class function.

'''

from graphics import *
import time
import random
import math
import sys

#values used repeatedly
game_speed = .1
win_width = 620
win_height = 620
bucket_move = 25
shell_speed = 30
crab_speed = 20
win_score = 20


class Florida:
    
    def __init__(self,win):
        self.win = win 
            
    def directions(self):
        """
        A window with game instructions are given and to start the game,
        you can click anywhere on the window.
        
        """
        self.win.setBackground("light blue")
        
        string = ("Instructions to play Florida:\n\n"
                  "1. To move the bucket:\n"
            "Use your left and right keys \n\n"
                  "2. How you score a point:\n"
                    "When the bucket collects a seashell\n"
                  "(when the bucket touches a seashell)\n\n"
                  "3. How you loose a point\n"
                    "When you miss collecting a seashell\n"
                  "(when the bucket doesn't touch a seashell)\n\n"
                    f"{win_score} points wins the game!\n\n"
                    "If a crab reaches the bucket\n"
                     "GAME OVER, YOU LOSE!\n\n"
                      "Click to start Florida!!")
        
        Text(Point(self.win.getWidth() / 2, self.win.getHeight() / 2), string).draw(self.win)
        
        self.win.getMouse()

    #code similar to dragon spider game
    def distanceBetweenPoints(self,object1, object2):
        """
        Takes 2 characters(objects) that is called in the isCloseEnough() function
        and finds out its X and Y coordinates to calculate its distance between
        each other
        
        Params:
        object1: 1st character that is being checked
        object2: 2nd character that is being checked
        
        Returns:
        applies distance formula and returns distance between object1 and object 2
        
        """
        p1x = object1.getX()
        p1y = object1.getY()
        p2x = object2.getX()
        p2y = object2.getY()
        
        return math.sqrt((p1x - p2x) * (p1x - p2x) + (p1y - p2y) * (p1y - p2y))

    #code similar to dragon spider game
    def isCloseEnough(self,object1, object2):
        """
        Takes 2 characters(objects) that is called in the isCloseEnough() function
        and calculates if the distance between eachother (calculated in distanceBetweenPoints()
        is less than the threshold
        
        Params:
        object1: 1st character that is being checked
        object2: 2nd character that is being checked
        
        Returns:
        false if the two objects are near to eachother (if their distance is less than the threshold)
        
        """
        threshold = min((object1.getWidth() + object2.getWidth() / 3.2), (object1.getHeight() + object2.getHeight()) / 3.2)
        
        return self.distanceBetweenPoints(object1.getAnchor(), object2.getAnchor()) < threshold

    #code similar to dragon spider game
    def moveShell(self,shellList, points):
        """
        Shells fall vertically and updates points
        
        Params:
        shellList: used to keep track of shells on the screen
        points: keeps track
        
        Returns:
        updated points(minus if the user missed shells and plus if they collected)
        
        """
        for shell in shellList:
            
            shell.move(0, shell_speed)
            
            if shell.getAnchor().getY() > win_height + shell.getHeight():
                shell.undraw()
                shellList.remove(shell)
                points = points -1
                
        return points
    
    #code similar to dragon spider game
    def moveCrab(self,crabList):
        """
        Crabs fall vertically
        
        Params:
        crabList: used to keep track of crabs on the screen
        
        """
        for crab in crabList:
            
            crab.move(0, crab_speed)
            
            if crab.getAnchor().getY() > win_height+crab.getHeight():
                crab.undraw()
                crabList.remove(crab)

    def moveBucket(self,click, bucket):
        """
        Bucket moves using keys
        
        Params:
        click: used to recieve which key is being pressed by the user
        bucket: identify which character needs to move (the bucket)
        
        """
        if click != None:
            
            if click == 'Left':
                bucket.move(-bucket_move,0)
                
            elif click == 'Right':
                bucket.move(bucket_move,0)  

    #code similar to dragon spider game
    def addShell(self,win):
        """
        Used to add more shells in the window
        
        Params:
        win: to specify which window
        
        Returns:
        shells that were added
        
        """
        #add seashells in the window
        shell = Image(Point(0,0), 'floridaShell.gif')
        
        shellX = random.randrange(shell.getWidth(), win_width - shell.getWidth())
        shellY = -shell.getHeight()
        
        #move shell
        shell.move(shellX, shellY)
        #draw shells
        shell.draw(win)
        
        return shell
    
    #code similar to dragon spider game
    def addCrab(self,win):
        """
        Used to add more crabs in the window
        
        Params:
        win: to specify which window
        
        Returns:
        crabs that were added
        
        """
        #add crabs in the window
        crab = Image(Point(0,0), 'floridaCrab.gif')
        crabX = random.randrange(crab.getWidth(), win_width - crab.getWidth())
        crabY = -crab.getHeight()
        
        #move crabs
        crab.move(crabX, crabY)
        
        #draw crabs
        crab.draw(win)
        
        return crab
        
    def exitGame(self,win):
        """
        When a crab touches the bucke, exitGame() function takes user
        to a window showing they loose and exits system.
        
        Params:
        win: to specify which window
        
        """
        #cover background using rectangle
        cover = Rectangle(Point(0, 0), Point(win_width, win_height))
        cover.setFill('red')
        cover.draw(win)
        
        #display text
        gameOver = Text(Point(win_width / 2, win_height / 2), "Better luck next time! You Lose")
        gameOver.setSize(22)
        gameOver.draw(win)
        
        time.sleep(5)
        sys.exit(1)
        
    def winMessage(self,win):
        """
        When user gets to win_score, winMessage() takes user
        to a window showing they win
        
        Params:
        win: to specify which window
        
        """
        #cover background using rectangle
        cover = Rectangle(Point(0, 0), Point(win_width, win_height))
        cover.setFill('turquoise')
        cover.draw(win)
        
        #images used for crab dance
        crabWin = Image(Point(150,200), 'floridaCrabWin.gif')
        crabWin1 = Image(Point(150,200), 'floridaCrabWin1.gif')
        
        #display text
        gameWin = Text(Point(win_width / 2, win_height / 2), "You won!")
        gameWin.setSize(28)
        gameWin.setFill('black')
        gameWin.draw(win)
        
        crabDance = Text(Point(win_width / 2, 350), "Here's a crab dance for you!")
        crabDance.setSize(22)
        crabDance.setFill('black')
        crabDance.draw(win)
        
        #code to make the crab dance
        for i in range(15):
            crabWin.draw(win)
            time.sleep(.2)
            crabWin.undraw()
            crabWin1.draw(win)
            time.sleep(.2)
            crabWin1.undraw()
            
        time.sleep(5)

    #code similar to dragon spider game
    def setPoints(self,win):
        """
        To display updated score during the game
        
        Params:
        win: to specify which window
        
        """
        label = Text(Point(500, 50), "Points: ")
        label.setFill('white')
        label.draw(win)
        
        pointsLabel = Text(Point(540, 50), '0')
        pointsLabel.setFill('white')
        pointsLabel.draw(win) 
        
        return pointsLabel

    def gameLoop(self,win, bucket):
        """
        Execute everything during the game such as add shell,
        remove shells, add crabs, remove crabs, updaate points,
        move the bucket, etc
        
        Params:
        win: to specify which window
        
        """
        shellList = []
        crabList = []
        points = 0
        crab = -50
        pointsLabel = self.setPoints(self.win)
        
        while points< win_score:
            
            if random.randrange(100) < 15:
                newShell = self.addShell(self.win)
                shellList.append(newShell)
                
            if random.randrange(600) < 15:
                newCrab = self.addCrab(self.win)
                crabList.append(newCrab)
                
            self.moveCrab(crabList) 
            click = self.win.checkKey()
            points = self.moveShell(shellList, points)
            pointsLabel.setText(points)
            
            if points<win_score:
                self.moveBucket(click, bucket)
                
                for shell in shellList:
                    
                    if self.isCloseEnough(bucket, shell):
                        shell.undraw()
                        shellList.remove(shell)
                        points = points + 1
                        pointsLabel.setText(points)

                for crab in crabList:
                    if self.isCloseEnough(crab, bucket):
                        self.exitGame(self.win)     

            time.sleep(game_speed)
        self.winMessage(self.win)
        

def main():
    
    #draw window and set  background
    background = Image(Point(win_width / 2, win_height / 2), 'floridaBg.gif')
    win = GraphWin("Florida", win_width, win_height)
    
    #execute Class
    florida = Florida(win)
    
    #display direction
    florida.directions()
    
    #after clickMouse() in directions()
    background.draw(win)
    
    # draw bucket
    bucket = Image(Point(0,0), 'floridaBucket.gif')
    bucket.move(win_width / 2, win_height - bucket.getHeight() / 2)
    bucket.draw(win)
    
    #to run the game
    florida.gameLoop(win, bucket)
    
    win.close()
    
if __name__ == "__main__":
    main()

