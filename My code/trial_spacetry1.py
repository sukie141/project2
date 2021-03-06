import time
import random
from Tkinter import *

window = Tk()
canvas = Canvas(width = 330, height = 200, bg='lightblue')
canvas.pack()

class Robot:
#Create  Robot

    def __init__(self):
        self.x=0
        self.y=0
        self.shape = canvas.create_rectangle(3,7,13,17)
        
    #need to make class so that when it moves it checks if its collided into an object along the way



        
   # def hitObject(self):
       # for ob in Plot1:
           # x1,y1,x2,y2 = canvas.coords(ob)
           #print "\t~~~~\t:",x1,y1,x2,y2

class Treasure:
    count = 0
    def count():
        if (hitObject()==True):
            count = 1
            print ("you have found some treasure")
        else:
            count = 0
            print ("There is no treasure here!")
    

class Plot:
   'Common base class for all Fuel'
   def __init__(self):
       self.x=0
       self.y=0
   
   def Draw(self, width=10, height=10):
        canvas.create_rectangle(22,37,32,90, fill='blue'),
        canvas.create_rectangle(22,37,90,32, fill='red')
        canvas.create_rectangle(90,180,110,120, fill='yellow')
        canvas.create_rectangle(90,180,10,170, fill='purple')
        canvas.create_rectangle(230,180,300,170, fill='black')
        canvas.create_rectangle(270,100,290,170, fill='green')
        canvas.create_rectangle(300,37,270,90, fill='red')
        canvas.create_rectangle(270,50,220,30, fill='blue')
     

    

   def set_coords(self, x, y):
   
       self.x = x
       self.y = y

class Fuel(Plot):
   'Common base class for all Fuel'
   x=0
   y=0
   gif=PhotoImage(file = 'jerrycan.gif')

   def __init__(self):
       Plot.__init__(self)

   def Draw(self):
       Plot.Draw(self,20,16)
       canvas.create_image(self.x+10,self.y+8,image = self.gif)

r = Robot()
Plot1 = [Plot() for i in range(5)]

Plot1 = {
    canvas.create_rectangle(50,37,32,90, fill='blue'),
    }

fuelcans = [Fuel() for i in range(5)]

fuelcans[0].set_coords(60,60)
fuelcans[1].set_coords(250,60)
fuelcans[2].set_coords(60,150)
fuelcans[3].set_coords(250,150)


for i in range (0,5):
    fuelcans[i].Draw()

gif=PhotoImage(file = 'jerrycan.gif')



# The velocity, or distance moved per time step
vx = 10.0 # x velocity
vy = 8.0 # y velocity
# Boundaries
x_min = 0.0
y_min = 0.0
x_max = 330.0
y_max = 200.0


id2=canvas.create_rectangle(3,7,3+10,7+10)

#create random position for the robot
Obx1=random.randint(0,175)
Oby1=random.randint(0,175)
Obx2=Obx1+75
Oby2=Oby1+75

#count for steps to move away from the objects
count=0
count_forward=0

#create object to avoid

# Generate x and y coordinates for 500 timesteps
for t in range(1, 300):
    x1,y1,x2,y2=canvas.coords(id2)
    #Detect left side of object
    if x2>(Obx1 - 10) and x2<(Obx1+10) and y1< Oby1 and y1>Oby2:
        print "Object detected left side"
        count=5
    #Detect right side of object
    if x1<(Obx2 + 10) and x1>(Obx2 - 10) and y1< Oby1 and y1>Oby2:
        print "Object detected right side"
        count_forward=5
    # If a boundary has been crossed, reverse the direction
    if x1 >= x_max:
        vx = -10.0
    if y1 <= y_min:
        vy = 5.0
    if y2 >= y_max:
        vy = -5.0
    if x1 <= x_min:
        vx = 10.0
    # Reposition the robot
    canvas.coords(id2,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
    # Pause for 0.1 seconds, then delete the image
    time.sleep(0.1)
# Generate x and y coordinates for 500 timesteps
for t in range(1, 500):
    x1,y1,x2,y2=canvas.coords(id2)
    #Detect left side of object
    if x2>(Obx1 - 10) and x2<(Obx1+10) and y1< Oby1 and y1>Oby2:
        print "Object detected left side"
        count=5
    #Detect right side of object
    if x1<(Obx2 + 10) and x1>(Obx2 - 10) and y1< Oby1 and y1>Oby2:
        print "Object detected right side"
        count_forward=5
    #Detect Bottom of object
    if y1>(Oby1 - 10) and y1<(Oby1+10) and x1>Obx1 and x1<Obx2:
        print "Object detected bottom of object"
        count=5
    #Detect top of object
    if y1>(Oby2 - 10) and y1<(Oby2+10) and x1>Obx1 and x1<Obx2:
        print "Object detected top of object"
        count_forward=5
#if counter set move away from left side or bottom of object
    if count>0:
        vx=-10
        vy=+5
        count=count-1
    if count_forward>0:
        vx=10
        vy=-5
        print ("moving away forward")
        count_forward=count_forward-1

    # Pause for 0.1 seconds, then delete the image
    time.sleep(0.1)
window.mainloop()
