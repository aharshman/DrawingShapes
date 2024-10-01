# -*- coding: utf-8 -*-
"""
Alexander Harshman

9/14/21

CS 135

Using three seperate for loops to make:
lines based on where the user clicks and calculating the slope
triangles based on where the user clicks and calculating the area
circles based on where the user clicks on the center and radius and calculating the area
inside a decorated graphics window.
"""

from graphics import *
import math


def main():
    
# Opening the Window
    win = GraphWin("Program 1 CS 135", 800, 500)
    win.setBackground('light blue')
    
# Set Border Varaibles
    LBN = 400
    RBN = 400
    TBN = 0
    BBN = 0
    
# Border Loops
    
    # Top Border Loop
    for top in range (1, 9):
        TB = Image(Point(TBN, 0), 'Border1.gif').draw(win)
        TBN = TBN + 100
        
    # Bottom Border Loop
    for bottom in range (1, 9):
        BB = Image(Point(BBN, 500), 'Border1.gif').draw(win)
        BBN = BBN + 100
    
    # Left Border Loop
    for left in range (1, 7):
        LB = Image(Point(0, LBN), 'Border1.gif').draw(win)
        LBN = LBN - 72
        
     # Right Border Loop
    for right in range (1, 7):
        RB = Image(Point(800, RBN), 'Border1.gif').draw(win)
        RBN = RBN - 72
        
    # Box around white area
    Rect = Rectangle(Point(700, 428), Point(100, 72))
    Rect.setWidth(4)
    Rect.setOutline('light pink')
    Rect.draw(win)
    
# Introduction
    intro = Text(Point(400, 250), 'Press any Key')
    intro.setSize(36)
    intro.setFace("courier")
    intro.setStyle('bold italic')
    intro.draw(win)
    win.getKey()
    intro.undraw()
    
# Intro to Lines
    IP = Image(Point(400, 250), 'introlightpink.gif').draw(win)
    IL = Text(Point(400, 250), "Go ahead and make some lines")
    IL.setSize(24)
    IL.setFace('courier')
    IL.setStyle('bold italic')
    IL.draw(win)
    time.sleep(2)
    IL.undraw()
    IP.undraw()

# Taking how many lines the user wants to make
    linetext = Text(Point(400, 480), 'How many lines would you like to draw?')
    linetext.setFace('courier')
    linetext.setStyle("bold italic")
    linetext.draw(win)
    linetext.setSize(13)
    lineEntry = Entry(Point(400, 450),2)
    lineEntry.setFill('light pink')
    lineEntry.setText('0')
    lineEntry.draw(win)
    
# Taking the input and making a for loop
    x = ''
    while x != 'Return':
        x = win.getKey()
    
    linetext.undraw()
    Nlines = int(lineEntry.getText())
    lineEntry.undraw()
    
    
    for i in range(Nlines):

# Text asking the user to click on two points
        linestext = Text(Point(400, 480), 'Please Click on two points using your mouse.')
        linestext.setFace('courier')
        linestext.setStyle("bold italic")
        linestext.draw(win)
        linestext.setSize(16)

# Making the points    
        p1 = win.getMouse()
        p1.setFill('light pink')
        p1.draw(win)
        p2 = win.getMouse()
        p2.setFill('light pink')
        p2.draw(win)
        
# Getting the coordinates of the points
        xv1 = p1.getX()
        yv1 = p1.getY()
        xv2 = p2.getX()
        yv2 = p2.getY()

# Drawing the line
        linestext.undraw()
        line = Line(Point(xv1,yv1), Point(xv2,yv2))
        line.setWidth(4)
        line.setFill('light pink')
        line.draw(win)
        
# Calculating and displaying the slope of the line
        slope = (yv2 - yv1) / (xv2 - xv1)
        sloper = slope * (-1)
        slopeR = round(sloper, 6)
        slopetext = Text((Point(400, 480)), 'The Slope of your line is: ' + str(slopeR))
        slopetext.setFace('courier')
        slopetext.setStyle("bold italic")
        slopetext.setSize(18)
        slopetext.draw(win)
        time.sleep(4)
        line.undraw()
        slopetext.undraw()
        p1.undraw()
        p2.undraw()
        
# Transistion to Triangles
    triangle_image = Image(Point(400, 250), 'Triangle2.gif').draw(win)
    trit = Text(Point(400, 250), "Let's move on to triangles now")
    trit.setSize(20)
    trit.setFace("courier")
    trit.setStyle('bold italic')
    trit.draw(win)
    time.sleep(2)
    trit.undraw()
    triangle_image.undraw()
        
# Taking how many triangles the user wants to make
    trittext = Text(Point(400, 480), 'How many triangles would you like to draw?')
    trittext.setFace('courier')
    trittext.setStyle("bold italic")
    trittext.draw(win)
    trittext.setSize(13)
    triEntry = Entry(Point(400, 450),2)
    triEntry.setFill('light pink')
    triEntry.setText('0')
    triEntry.draw(win)
    
# Taking the input and making a for loop
    x = ''
    while x != 'Return':
        x = win.getKey()
        
    trittext.undraw()
    Ntri = int(triEntry.getText())
    triEntry.undraw()
    
    for i in range(Ntri):

# Text asking the user to click on three points
        tritext = Text(Point(400, 480), 'Please Click on three points using your mouse.')
        tritext.draw(win)
        tritext.setSize(16)
        tritext.setFace('courier')
        tritext.setStyle("bold italic")

# Making the points    
        p1 = win.getMouse()
        p1.setFill('light pink')
        p1.draw(win)
        p2 = win.getMouse()
        p2.setFill('light pink')
        p2.draw(win)
        p3 = win.getMouse()
        p3.setFill('light pink')
        p3.draw(win)
        
# Getting the coordinates of the points
        xv1 = p1.getX()
        yv1 = p1.getY()
        xv2 = p2.getX()
        yv2 = p2.getY()
        xv3 = p3.getX()
        yv3 = p3.getY()

# Drawing the Triangle
        tritext.undraw()
        tri = Polygon(Point(xv1,yv1), Point(xv2,yv2), Point(xv3,yv3))
        tri.setWidth(0)
        tri.draw(win)
        tri.setFill('light pink')
        tri.setOutline('light pink')
        
# Calculating the length of each line using distance formula
        a = math.sqrt(((p2.getX() - p1.getX())**2)+ (p2.getY() - p1.getY())**2)
        b = math.sqrt(((p3.getX() - p2.getX())**2)+ (p3.getY() - p2.getY())**2)
        c = math.sqrt(((p1.getX() - p3.getX())**2)+ (p1.getY() - p3.getY())**2)
        
# Finding S
        s = (a + b + c)/2
        
# Finding the area
        A = math.sqrt(s * ((s - a) * (s - b) * (s - c)))
        
# Rounding the area
        Ar = round(A, 7)
        
# Displaying the area
        areatext = Text((Point(400, 480)), 'The area of your triangle is: ' + str(Ar))
        areatext.setFace('courier')
        areatext.setStyle("bold italic")
        areatext.setSize(18)
        areatext.draw(win)
        time.sleep(4)
        tri.undraw()
        tritext.undraw()
        p1.undraw()
        p2.undraw()
        p3.undraw()
        areatext.undraw()
        
# Transition to Circles
    CP = Image(Point(400, 250), 'lightpinkcircle.gif').draw(win)
    tcirc = Text(Point(400, 250), "Now let's make some circles")
    tcirc.setSize(24)
    tcirc.setFace("courier")
    tcirc.setStyle('bold italic')
    tcirc.draw(win)
    time.sleep(2)
    tcirc.undraw()
    CP.undraw()
    
# Asking how many circles the user wants to make
    circtext = Text(Point(400, 480), 'How many circles would you like to draw?')
    circtext.setFace('courier')
    circtext.setStyle("bold italic")
    circtext.setSize(12)
    circtext.draw(win)
    circEntry = Entry(Point(400, 450),2)
    circEntry.setFill('light pink')
    circEntry.setText('0')
    circEntry.draw(win)

# Taking the input and making a for loop
    x = ''
    while x != 'Return':
        x = win.getKey()
        
    circtext.undraw()
    Nc = int(circEntry.getText())
    circEntry.undraw()
    
    for i in range(Nc):

# Text asking the user to click on the center of their circle
        centertext = Text(Point(400, 480), 'Please Click where ever you would like the center of your circle to be.')
        centertext.setFace('courier')
        centertext.setStyle("bold italic")
        centertext.draw(win)
        centertext.setSize(13)

# Making the center point  
        p1 = win.getMouse()
        p1.setFill('light pink')
        p1.draw(win)
        centertext.undraw()
        
# Getting the coordinates of the center point
        xv1 = p1.getX()
        yv1 = p1.getY()
        
# Text asking the user to click on the outer edge of their circle
        outertext = Text(Point(400, 480), 'Please Click where ever you would like the outer edge of your circle to be.')
        outertext.setFace('courier')
        outertext.setStyle("bold italic")
        outertext.draw(win)
        outertext.setSize(13)

# Making the outer edge point  
        p2 = win.getMouse()
        p2.setFill('light pink')
        p2.draw(win)
        outertext.undraw()
        
# Getting the coordinates of the outer edge point
        xv2 = p2.getX()
        yv2 = p2.getY()
        
# Finding the radius using distance formula
        r = math.sqrt(((p2.getX() - p1.getX())**2)+ (p2.getY() - p1.getY())**2)
        
# Drawing the circle
        circle = Circle(Point(xv1,yv1), r)
        circle.setFill('light pink')
        circle.setOutline('light pink')
        circle.setWidth(0)
        circle.draw(win)
        
# Calculating and displaying the area of the circle
        A = math.pi * (r)**2
        AcircR = round(A, 6)
        Atext = Text(Point(400,480), 'The area of your circle is: ' + str(AcircR))
        Atext.setSize(16)
        Atext.setFace('courier')
        Atext.setStyle('bold italic')
        Atext.draw(win)
        time.sleep(4)
        
# Clearing the screen
        p1.undraw()
        p2.undraw()
        Atext.undraw()
        circle.undraw()
        
# Wrap up background

    # Getting rid of the box
    Rect.undraw()
    
    # Assigning Variables
    BRBN2 = 0
    BRBN3 = 0
    BRBN4 = 0
    BRBN5 = 0
    BRBN6 = 0
    BRBN7 = 0
    BRBN8 = 0
    
    # Making each image in a loop
    for BCRD in range(1, 7):
        BRBN = 0
        for line2 in range (1, 8):
            BRB = Image(Point(BRBN2, 0), 'Border1.gif').draw(win)
            BRBN2 = BRBN2 + 100
        for line3 in range (1, 8):
            BRB = Image(Point(BRBN3, 72), 'Border1.gif').draw(win)
            BRBN3 = BRBN3 + 100
        for line4 in range (1, 8):
            BRB = Image(Point(BRBN4, 144), 'Border1.gif').draw(win)
            BRBN4 = BRBN4 + 100
        for line5 in range (1, 8):
            BRB = Image(Point(BRBN5, 216), 'Border1.gif').draw(win)
            BRBN5 = BRBN5 + 100
        for line6 in range (1, 8):
            BRB = Image(Point(BRBN6, 288), 'Border1.gif').draw(win)
            BRBN6 = BRBN6 + 100
        for line7 in range (1, 8):
            BRB = Image(Point(BRBN7, 360), 'Border1.gif').draw(win)
            BRBN7 = BRBN7 + 100
        for line8 in range (1, 8):
            BRB = Image(Point(BRBN8, 432), 'Border1.gif').draw(win)
            BRBN8 = BRBN8 + 100
        
# Wrap up
    outro = Text(Point(400, 250), 'This program will now close')
    outro.setSize(36)
    outro.setFace("courier")
    outro.setStyle('bold italic')
    outro.draw(win)
    intro.undraw()
    
# Closing the window
    time.sleep(2)
    win.close()
    
    


main()

