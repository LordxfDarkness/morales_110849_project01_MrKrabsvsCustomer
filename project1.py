from graphics import *
def circle_position(win):
    punto=win.getMouse()
    x=int(punto.getX())
    y=int(punto.getY())
    #Column 1
    if(x>=0 and x<=95 and y>=0 and y<=80):
        x=50
        y=40
    elif(x>=0 and x<=95 and y>=81 and y<=160):
        x=50
        y=120
    elif(x>=0 and x<=95 and y>=161 and y<=240):
        x=50
        y=200
    elif(x>=0 and x<=95 and y>=241 and y<=320):
        x=50
        y=280
    elif(x>=0 and x<=95 and y>=321 and y<=400):
        x=50
        y=360
    elif(x>=0 and x<=95 and y>=401 and y<=480):
        x=50
        y=440
    #Column 2
    if(x>=96 and x<=185 and y>=0 and y<=80):
        x=140
        y=40
    elif(x>=96 and x<=185 and y>=81 and y<=160):
        x=140
        y=120
    elif(x>=96 and x<=185 and y>=161 and y<=240):
        x=140
        y=200
    elif(x>=96 and x<=185 and y>=241 and y<=320):
        x=140
        y=280
    elif(x>=96 and x<=185 and y>=321 and y<=400):
        x=140
        y=360
    elif(x>=96 and x<=185 and y>=401 and y<=480):
        x=140
        y=440
    #Column 3
    if(x>=186 and x<=275 and y>=0 and y<=80):
        x=230
        y=40
    elif(x>=186 and x<=275 and y>=81 and y<=160):
        x=230
        y=120
    elif(x>=186 and x<=275 and y>=161 and y<=240):
        x=230
        y=200
    elif(x>=186 and x<=275 and y>=241 and y<=320):
        x=230
        y=280
    elif(x>=186 and x<=275 and y>=321 and y<=400):
        x=230
        y=360
    elif(x>=186 and x<=275 and y>=401 and y<=480):
        x=230
        y=440
    #Column 4
    if(x>=276 and x<=365 and y>=0 and y<=80):
        x=320
        y=40
    elif(x>=276 and x<=365 and y>=81 and y<=160):
        x=320
        y=120
    elif(x>=276 and x<=365 and y>=161 and y<=240):
        x=320
        y=200
    elif(x>=276 and x<=365 and y>=241 and y<=320):
        x=320
        y=280
    elif(x>=276 and x<=365 and y>=321 and y<=400):
        x=320
        y=360
    elif(x>=276 and x<=365 and y>=401 and y<=480):
        x=320
        y=440
    #Column 5
    if(x>=366 and x<=455 and y>=0 and y<=80):
        x=410
        y=40
    elif(x>=366 and x<=455 and y>=81 and y<=160):
        x=410
        y=120
    elif(x>=366 and x<=455 and y>=161 and y<=240):
        x=410
        y=200
    elif(x>=366 and x<=455 and y>=241 and y<=320):
        x=410
        y=280
    elif(x>=366 and x<=455 and y>=321 and y<=400):
        x=410
        y=360
    elif(x>=366 and x<=455 and y>=401 and y<=480):
        x=410
        y=440
    #Column 6
    if(x>=456 and x<=545 and y>=0 and y<=80):
        x=500
        y=40
    elif(x>=456 and x<=545 and y>=81 and y<=160):
        x=500
        y=120
    elif(x>=456 and x<=545 and y>=161 and y<=240):
        x=500
        y=200
    elif(x>=456 and x<=545 and y>=241 and y<=320):
        x=500
        y=280
    elif(x>=456 and x<=545 and y>=321 and y<=400):
        x=500
        y=360
    elif(x>=456 and x<=545 and y>=401 and y<=480):
        x=500
        y=440
    #Column 7
    if(x>=546 and x<=640 and y>=0 and y<=80):
        x=590
        y=40
    elif(x>=546 and x<=640 and y>=81 and y<=160):
        x=590
        y=120
    elif(x>=546 and x<=640 and y>=161 and y<=240):
        x=590
        y=200
    elif(x>=546 and x<=640 and y>=241 and y<=320):
        x=590
        y=280
    elif(x>=546 and x<=640 and y>=321 and y<=400):
        x=590
        y=360
    elif(x>=546 and x<=640 and y>=401 and y<=480):
        x=590
        y=440
    return(x,y)
def point_assignment(x,y):
    #Column 
    points=0
    if(x>=0 and x<=95 and y>=0 and y<=80):
        points=2
    elif(x>=0 and x<=95 and y>=81 and y<=160):
        points=4
    elif(x>=0 and x<=95 and y>=161 and y<=240):
        points=18
    elif(x>=0 and x<=95 and y>=241 and y<=320):
        points=25
    elif(x>=0 and x<=95 and y>=321 and y<=400):
        points=2
    elif(x>=0 and x<=95 and y>=401 and y<=480):
        points=2
    #Column 2
    if(x>=96 and x<=185 and y>=0 and y<=80):
        points=8
    elif(x>=96 and x<=185 and y>=81 and y<=160):
        points=2
    elif(x>=96 and x<=185 and y>=161 and y<=240):
        points=9
    elif(x>=96 and x<=185 and y>=241 and y<=320):
        points=3
    elif(x>=96 and x<=185 and y>=321 and y<=400):
        points=1
    elif(x>=96 and x<=185 and y>=401 and y<=480):
        points=7
    #Column 3
    if(x>=186 and x<=275 and y>=0 and y<=80):
        points=25
    elif(x>=186 and x<=275 and y>=81 and y<=160):
        points=50
    elif(x>=186 and x<=275 and y>=161 and y<=240):
        points=75
    elif(x>=186 and x<=275 and y>=241 and y<=320):
        points=19
    elif(x>=186 and x<=275 and y>=321 and y<=400):
        points=5
    elif(x>=186 and x<=275 and y>=401 and y<=480):
        points=8
    #Column 4
    if(x>=276 and x<=365 and y>=0 and y<=80):
        points=6
    elif(x>=276 and x<=365 and y>=81 and y<=160):
        points=32
    elif(x>=276 and x<=365 and y>=161 and y<=240):
        points=75
    elif(x>=276 and x<=365 and y>=241 and y<=320):
        points=90
    elif(x>=276 and x<=365 and y>=321 and y<=400):
        points=15
    elif(x>=276 and x<=365 and y>=401 and y<=480):
        points=18
    #Column 5
    if(x>=366 and x<=455 and y>=0 and y<=80):
        points=2
    elif(x>=366 and x<=455 and y>=81 and y<=160):
        points=75
    elif(x>=366 and x<=455 and y>=161 and y<=240):
        points=5
    elif(x>=366 and x<=455 and y>=241 and y<=320):
        points=2
    elif(x>=366 and x<=455 and y>=321 and y<=400):
        points=90
    elif(x>=366 and x<=455 and y>=401 and y<=480):
        points=7
    #Column 6
    if(x>=456 and x<=545 and y>=0 and y<=80):
        points=25
    elif(x>=456 and x<=545 and y>=81 and y<=160):
        points=10
    elif(x>=456 and x<=545 and y>=161 and y<=240):
        points=40
    elif(x>=456 and x<=545 and y>=241 and y<=320):
        points=2
    elif(x>=456 and x<=545 and y>=321 and y<=400):
        points=22
    elif(x>=456 and x<=545 and y>=401 and y<=480):
        points=23
    #Column 7
    if(x>=546 and x<=640 and y>=0 and y<=80):
        points=2
    elif(x>=546 and x<=640 and y>=81 and y<=160):
        points=90
    elif(x>=546 and x<=640 and y>=161 and y<=240):
        points=2
    elif(x>=546 and x<=640 and y>=241 and y<=320):
        points=2
    elif(x>=546 and x<=640 and y>=321 and y<=400):
        points=78
    elif(x>=546 and x<=640 and y>=401 and y<=480):
        points=5
    return(points)
def position_verifier(xlist,ylist,x,y,win):
    for i in range(len(xlist)):
        while(xlist[i]==x and ylist[i]==y):
            print("pick again")
            x,y=circle_position(win)
    return(x,y)
def winner(kpoint,cpoint,win):
    if(kpoint>cpoint):
        rect=Rectangle(Point(50,120),Point(560,360))
        rect.setFill("black")
        rect.draw(win)
        Message1=Text(Point(280,135),"The winner is Mr.Krabs, he got more $ ")
        Message1.setSize(25)
        Message1.setTextColor((color_rgb(75,83,32)))
        Message1.draw(win)
        Message2=Text(Point(80,160),kpoint)
        Message2.setSize(25)
        Message2.setTextColor((color_rgb(75,83,32)))
        Message2.draw(win)
        Message3=Text(Point(265,190),"The Customer lost, the customer got")
        Message3.setSize(25)
        Message3.setTextColor("Red")
        Message3.draw(win)
        Message4=Text(Point(80,220),cpoint)
        Message4.setSize(25)
        Message4.setTextColor("Red")
        Message4.draw(win)
        Message5=Text(Point(260,280),"Customer lost by these many points: ")
        Message5.setSize(25)
        Message5.setTextColor("Red")
        Message5.draw(win)
        lost=kpoint-cpoint
        Message6=Text(Point(90,310),lost)
        Message6.setSize(25)
        Message6.setTextColor("Red")
        Message6.draw(win)
        win.getMouse()
        Message1.undraw()
        Message2.undraw()
        Message3.undraw()
        Message4.undraw()   
        Message5.undraw()
        Message6.undraw()
        rect.undraw()
    elif(kpoint<cpoint):
        rect=Rectangle(Point(50,120),Point(550,360))
        rect.setFill("black")
        rect.draw(win)
        Message1=Text(Point(300,135),"The winner is the Customer, he got more $ ")
        Message1.setSize(25)
        Message1.setTextColor((color_rgb(75,83,32)))
        Message1.draw(win)
        Message2=Text(Point(80,160),cpoint)
        Message2.setSize(25)
        Message2.setTextColor((color_rgb(75,83,32)))
        Message2.draw(win)
        Message3=Text(Point(220,190),"MrKrabs lost, MrKrabs got $ ")
        Message3.setSize(25)
        Message3.setTextColor("Red")
        Message3.draw(win)
        Message4=Text(Point(80,220),kpoint)
        Message4.setSize(25)
        Message4.setTextColor("Red")
        Message4.draw(win)
        Message5=Text(Point(260,280),"MrKrabs lost by these many points: ")
        Message5.setSize(25)
        Message5.setTextColor("Red")
        Message5.draw(win)
        lost=cpoint-kpoint
        Message6=Text(Point(90,310),lost)
        Message6.setSize(25)
        Message6.setTextColor("Red")
        Message6.draw(win)
        win.getMouse()
        Message1.undraw()
        Message2.undraw()
        Message3.undraw()
        Message4.undraw()   
        Message5.undraw()
        Message6.undraw()
        rect.undraw()
def main():
    x=Image(Point(320,240),"/Users/lordofdarkness/Downloads/krabs_rag3do.gif")
    win=GraphWin("Mr.Krabs vs Customer",x.getWidth(),x.getHeight())
    x.draw(win)
    img=Image(Point(320,240),"/Users/lordofdarkness/Downloads/maxresdefault.gif")
    img.draw(win)
    Message0=Text(Point(300,110),"CLICK TO BEGIN GAME")
    Message0.setSize(25)
    Message0.setTextColor("yellow")
    Message0.draw(win)
    win.getMouse()
    Message0.undraw()
    rect=Rectangle(Point(50,120),Point(560,360))
    rect.setFill("pink")
    rect.setOutline("yellow")
    rect.draw(win)
    Message1=Text(Point(300,135),"Welcome to the Mr.KrabsvsCustomer game")
    Message1.setSize(25)
    Message1.setTextColor("red")
    Message1.draw(win)
    Message=Text(Point(205,190),"Press anywhere to START")
    Message.setSize(25)
    Message.setTextColor((color_rgb(75,83,32)))
    Message.draw(win)
    win.getMouse()
    Message1.undraw()
    Message.undraw()
    rect.undraw()
    img.undraw()
    xlist=[]#saves x positions in window
    ylist=[]#saves y position in window
    kpoint=0#stores the points from the positions of the red circles
    cpoint=0#stores the points from the positions of the green circles
    for num in range(42):
        x,y=circle_position(win)
        x,y=position_verifier(xlist,ylist,x,y,win)       
        xlist.append(x)
        ylist.append(y)
        circulo=Circle(Point(x,y),35)        
        if(num%2==0):
            kpoint+=point_assignment(x,y)
            circulo.setFill("Red")
            circulo.draw(win)   
        elif(num%2!=0):
            cpoint+=point_assignment(x,y)
            circulo.setFill((color_rgb(75,83,32)))
            circulo.draw(win)
    winner(kpoint,cpoint,win)
    img1=Image(Point(320,240),"/Users/lordofdarkness/Downloads/131-1312259_report-abuse-spongebob-patrick-meme.png.gif")
    img1.draw(win)    
    win.getMouse()
main()
#primary coordinates 50,40
#x+90 para cada roto horizontal 
#y+80 para cada roto vertical

#1,6(x1=50,y1=40)
#1,5(x1=50,y1=120)
#1,4(x1=50,y1=200)
#1,3(x1=50,y1=280)
#1,2(x1=50,y1=360)
#1,1(x1=50,y1=440)

#2,6(x1=140,y1=40)
#2,5(x1=140,y1=120)
#2,4(x1=140,y1=200)
#2,3(x1=140,y1=280)
#2,2(x1=140,y1=360)
#2,1(x1=140,y1=440)

#3,6(x1=230,y1=40)
#3,5(x1=230,y1=120)
#3,4(x1=230,y1=200)
#3,3(x1=230,y1=280)
#3,2(x1=230,y1=360)
#3,1(x1=230,y1=440)

#4,6(x1=320,y1=40)
#4,5(x1=320,y1=120)
#4,4(x1=320,y1=200)
#4,3(x1=320,y1=280)
#4,2(x1=320,y1=360)
#4,1(x1=320,y1=440)

#5,6(x1=410,y1=40)
#5,5(x1=410,y1=120)
#5,4(x1=410,y1=200)
#5,3(x1=410,y1=280)
#5,2(x1=410,y1=360)
#5,1(x1=410,y1=440)

#6,6(x1=500,y1=40)
#6,5(x1=500,y1=120)
#6,4(x1=500,y1=200)
#6,3(x1=500,y1=280)
#6,2(x1=500,y1=360)
#6,1(x1=500,y1=440)

#7,6(x1=590,y1=40)
#7,5(x1=590,y1=120)
#7,4(x1=590,y1=200)
#7,3(x1=590,y1=280)
#7,2(x1=590,y1=360)
#7,1(x1=590,y1=440)
