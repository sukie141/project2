from Tkinter import *

window = Tk()
canvas = Canvas(width = 454, height = 312,)
canvas.pack(expand = YES, fill = BOTH)

gif1 = PhotoImage(file = 'Background_Image.gif')
canvas.create_image(0,0, image = gif1, anchor = NW)


class Fuel:
   'Common base class for all Fuel'
   x=0
   y=0
   gif=PhotoImage(file = 'jerrycan.gif')

   def _init_(self):
       self.x=0
       self.y=0
   
   def Draw(self):
        canvas.create_image(self.x,self.y,image = self.gif)

   def set_coords(self, x, y):
   
       self.x = x
       self.y=y
       
fuelcans = [Fuel() for i in range(5)]

fuelcans[0].set_coords(155,60)
fuelcans[1].set_coords(60,170)
fuelcans[2].set_coords(60,170)
fuelcans[3].set_coords(200,180)
fuelcans[4].set_coords(300,55)


id1=canvas.create_rectangle(5,110,10,115, width=2)


def Left():
    print "Left button pressed"
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1-20,y1,x2-20,y2)
def Right():
    print "Right button pressed"
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1+20,y1,x2+20,y2)
def Up():
    print "Up button pressed"
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1,y1-20,x2,y2-20)
def Down():
    print "Down button pressed"
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1,y1+20,x2,y2+20)

buttonL=Button(window,text='Left', command=Left)
buttonL.pack(side=LEFT)
buttonR=Button(window,text='Right', command=Right)
buttonR.pack(side=RIGHT)
buttonU=Button(window,text='Up', command=Up)
buttonU.pack(side=LEFT)
buttonD=Button(window,text='Down', command=Down)
buttonD.pack(side=RIGHT)
canvas.pack(padx=10,pady=10)



for i in range (0,5):
    fuelcans[i].Draw()

mainloop()
