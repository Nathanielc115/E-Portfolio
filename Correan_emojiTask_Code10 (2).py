from cmu_graphics import *

#These lines are the face of the emoji
Circle(170,170,160,border='black',borderWidth=3,fill=gradient('yellow','yellow','yellow','yellow','yellow','yellow','yellow','orange',start='center'))

#These lines are the nose 
Line(170,170,150,200)
Line(170,170,190,200)

#These lines are the eyes
Oval(100,120,35,60,border='black',borderWidth=2,fill='white')
Oval(240,120,35,60,border='black',borderWidth=2,fill='white')
Oval(240,130,30,36)
Oval(100,130,30,36)

#This line is for the mouth
Polygon(153,244,123,242,90,233,110,270,140,279,175,285,185,242,border='black',borderWidth=2,fill='white')

#These lines are the volleyball
Circle(280,280,107,border='black',borderWidth=3,fill=gradient('white','white','white','white','white','white','white','white','white','white','white','grey',start='center'))
Oval(233,280,114,170,border='black',borderWidth=2,fill='royalBlue')
Oval(329,280,114,170,border='black',borderWidth=2,fill='red')
Rect(269,209,26,150,fill='white')


cmu_graphics.run()
