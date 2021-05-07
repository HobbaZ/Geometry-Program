print("Geometry Program")

import random
import math

class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = float((self.width*self.height)/2.0)
        return area
    
    def getHeight(self):
        height = float((self.width*self.height)/self.width)
        return height

    def getWidth(self):
        width = float((self.width*self.height)/self.height) 
        return width

class Square:
    def __init__(self, length):
        self.length = length

    def getArea(self):
        area = float((self.length*self.length))
        return area
    
    def getLength(self):
        height = float((self.length*self.length)/self.length)
        return height

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = float((self.width*self.height))
        return area
    
    def getHeight(self):
        height = float((self.width*self.height)/self.width)
        return height

    def getWidth(self):
        width = float((self.width*self.height)/self.height) 
        return width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = float(3.1416*(self.radius*self.radius))
        return area
    
    def getDiameter(self):
        diameter = float((math.sqrt((3.1416*(self.radius*self.radius))/3.1416))*2)
        return diameter

    def getCircumference(self):
        circumference = float((2*3.1416)*self.radius) 
        return circumference
    
    def getRadius(self):
        radi = float (math.sqrt((3.1416*(self.radius*self.radius))/3.1416)) 
        return radi 


generateProblems = (int(input("How many math questions would you like to generate? ")))

#Get random problem
def randomProblem():
    randQuestionType = random.randint(9,11)
#triangle
    if(randQuestionType ==1): 
       calculateTriArea()

    elif(randQuestionType ==2): 
       calculateTriHeight()

    elif(randQuestionType == 3): 
       calculateTriWidth()
#square
    elif(randQuestionType == 4):
       calculateSqrArea()

    elif(randQuestionType == 5):
       calculateSqrLength()
#rectangle
    elif(randQuestionType == 6):
       calculateRectArea()

    elif(randQuestionType == 7):
       calculateRectHeight()

    elif(randQuestionType == 8):
       calculateRectWidth()
#circle
    elif(randQuestionType == 9):
       calculateCircArea()

    elif(randQuestionType == 10):
       calculateCircRadius()

# Diameter from area
    elif(randQuestionType == 11):
       calculateCircDiameter()    

#____________Triangle functions_______________

def calculateTriArea():
    width = random.randint(1,20)
    height = random.randint(1,20) 
    myTriangle = Triangle(width, height)
    print("A triangle has a width of", myTriangle.width,\
          "and a height of", myTriangle.height)
    triangleArea = myTriangle.getArea()
    answer = (float(input("What is it's area?  ")))
    if (answer == triangleArea):
        print("Yes, ", answer, "m\u00B2 is correct")
    else:
        print("Incorrect, the triangle's area is:",triangleArea, "m\u00B2")
        print("Remember, you can calculate a triangle's area by multipying width by height and dividing by 2")
       
def calculateTriHeight():
   width = random.randint(1,20)
   height = random.randint(1,20)
   myTriangle = Triangle(width, height)
   triangleArea = myTriangle.getArea() 
   print("A triangle has a width of", myTriangle.width,\
          "and an area of", triangleArea, "m\u00B2")
   triangleHeight = myTriangle.getHeight()
   answer = (float(input("What is it's height?  "))) 
   if (answer == triangleHeight):
        print("Yes, ", answer, "m is correct")
   else:
        print("Incorrect, the triangle's height is:",triangleHeight, "m")
        print("Remember, you can calculate a triangle's height by multiplying area by 2 and dividing by width")

def calculateTriWidth():
   width = random.randint(1,20)
   height = random.randint(1,20) 
   myTriangle = Triangle(width, height)
   triangleArea = myTriangle.getArea() 
   print("A triangle has a height of", myTriangle.height,\
          "and an area of", triangleArea, "m\u00B2")
   triangleWidth = myTriangle.getWidth()
   answer = (float(input("What is it's width?  "))) 
   if (answer == triangleWidth):
        print("Yes, ", answer, "m is correct")
   else:
        print("Incorrect, the triangle's width is:",triangleWidth, "m")
        print("Remember, you can calculate a triangle's width by multiplying area by 2 and dividing by height")

#____________Square functions_______________

def calculateSqrArea():
    length = random.randint(1,20) 
    mySquare = Square(length)
    print("A square has a width and a height of", mySquare.length)
    squareArea = mySquare.getArea()
    answer = (float(input("What is it's area?  ")))
    if (answer == squareArea):
        print("Yes, ", answer, "m\u00B2 is correct")
    else:
        print("Incorrect, the square's area is:",squareArea, "m\u00B2")
        print("Remember, you can calculate a square's area by multipying width by height")

def calculateSqrLength():
    length = random.randint(1,20) 
    mySquare = Square(length)
    squareArea = mySquare.getArea() 
    print("A square has an area of", squareArea,"m\u00B2 and a length of", mySquare.length)
    squareLength = mySquare.getLength()
    answer = (float(input("What is the length of the opposite side?  ")))
    if (answer == squareLength):
        print("Yes, ", answer, "m is correct")
    else:
        print("Incorrect, the square's opposite length is:",squareLength, "m")
        print("Remember, a square's opposite length is the same as all sides are equal length")

#____________Rectangle functions_______________

def calculateRectArea():
    width = random.randint(1,20)
    height = random.randint(1,20) 
    myRectangle = Rectangle(width, height)
    print("A rectangle has a width of", myRectangle.width,\
          "and a height of", myRectangle.height)
    rectangleArea = myRectangle.getArea()
    answer = (float(input("What is it's area?  ")))
    if (answer == rectangleArea):
        print("Yes, ", answer, "m\u00B2 is correct")
    else:
        print("Incorrect, the rectangle's area is:",rectangleArea, "m\u00B2")
        print("Remember, you can calculate a rectangle's area by multipying width by height")
       
def calculateRectHeight():
   width = random.randint(1,20)
   height = random.randint(1,20)
   myRectangle = Rectangle(width, height)
   rectangleArea = myRectangle.getArea() 
   print("A rectangle has a width of", myRectangle.width,\
          "and an area of", rectangleArea, "m\u00B2")
   rectangleHeight = myRectangle.getHeight()
   answer = (float(input("What is it's height?  "))) 
   if (answer == rectangleHeight):
        print("Yes, ", answer, "m is correct")
   else:
        print("Incorrect, the rectangle's height is:",rectangleHeight, "m")
        print("Remember, you can calculate a rectangle's height by dividing the area by the width")

def calculateRectWidth():
   width = random.randint(1,20)
   height = random.randint(1,20)
   myRectangle = Rectangle(width, height)
   rectangleArea = myRectangle.getArea() 
   print("A rectangle has a width of", myRectangle.height,\
          "and an area of", rectangleArea, "m\u00B2")
   rectangleWidth = myRectangle.getWidth()
   answer = (float(input("What is it's height?  "))) 
   if (answer == rectangleWidth):
        print("Yes, ", answer, "m is correct")
   else:
        print("Incorrect, the rectangle's width is:",rectangleWidth, "m")
        print("Remember, you can calculate a rectangle's height by dividing the area by the height")

#____________Circle functions_______________
        
def calculateCircArea():
    radius = random.randint(1,20) 
    myCircle = Circle(radius)
    print("A circle has a radius of", myCircle.radius)
    circleArea = myCircle.getArea()
    answer = (float(input("What is it's area?  ")))
    if (answer == circleArea):
        print("Yes, ", answer, "m\u00B2 is correct")
    else:
        print("Incorrect, the circle's area is:",circleArea, "m\u00B2")
        print("Remember, you can calculate a circle's area by multipying \u03C0 by radius\u00B2")

def calculateCircDiameter():
    radius = random.randint(1,20) 
    myCircle = Circle(radius)
    circleArea = myCircle.getArea() 
    print("A circle has an area of", circleArea,"m\u00B2")
    circleDiameter = myCircle.getDiameter()
    answer = (float(input("What is it's diameter?  ")))
    if (answer == circleDiameter):
        print("Yes, ", answer, "m is correct")
    else:
        print("Incorrect, the circle's diameter is:",circleDiameter, "m")
        print("Remember, you can calculate a circle's diameter by dividing the area by \u03C0 and multiplying by 2")

def calculateCircRadius():
    radius = random.randint(1,20) 
    myCircle = Circle(radius)
    circleArea = myCircle.getArea() 
    print("A circle has an area of", circleArea,"m\u00B2")
    circleRadius = myCircle.getRadius() 
    answer = (float(input("What is it's radius?  ")))
    if (answer == circleRadius):
        print("Yes, ", answer, "m is correct")
    else:
        print("Incorrect, the circle's radius is:",circleRadius, "m")
        print("Remember, you can calculate a circle's radius by finding the square root of dividing the area by \u03C0")

def calculateCircCircumference():
    radius = random.randint(1,20) 
    myCircle = Circle(radius)
    circleArea = myCircle.getArea() 
    print("A circle has an radius of", myCircle.radius)
    circleCircumference = myCircle.getCircumference() 
    answer = (float(input("What is it's circumference?  ")))
    if (answer == circleCircumference):
        print("Yes, ", answer, "m is correct")
    else:
        print("Incorrect, the circle's radius is:",circleCircumference, "m")
        print("Remember, you can calculate a circle's circumference by multiplying the radius by \u03C0 by 2")

# inputs (now changed to local inputs for questions, global inputs give variations of same ints)
#width = random.randint(1,20)
#height = random.randint(1,20) 

for i in range (1, (generateProblems+1)):
     print ("") 
     print("Question.",i)
     print ("") 
     randomProblem()
     print ("")

      
