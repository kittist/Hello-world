from turtle import *;from math import *;from random import *
##print(dcc);print(pgr)
color = ['yellow','orange','red','violet','pink','blue','purple','green']
speed(0);pensize(5)

def body(x,y,pgr,dcc,hg,num,rs):
    pu();poss(x,y);pd()
    for i in range(num):
        fillcolor(color[i%7])
        begin_fill();rt(dcc);fd(pgr)
        circle(rs,180+(dcc*2))
        fd(pgr);rt(180-dcc);end_fill()
    pu();poss(x,y);pd();dot((hg*1.3)+10, 'black')
    dot((hg*1.3), 'yellow');pu()

def poss(x,y):home();goto(x,y)

def eye(r):     
    lt(45)
    for i in range(2):
        fillcolor('black');begin_fill()
        circle(r,90);circle(r/2,90)
        end_fill()
    lt(45);fd(r/5);dot(r/2,'white')
    pu();lt(30);fd(r);pd();dot(r,'white')

def eyes(x,y,hg):
    poss(x,y);fd(hg/3.6);lt(90);fd(hg/5);rt(90)
    pd();eye(hg/12);pu()
    poss(x,y);bk(hg/3.6);lt(90);fd(hg/5);rt(90)
    pd();eye(hg/12)
    

def mouth(x,y,r):
    pu();poss(x,y);pd()
    fillcolor('red');begin_fill()
    pu();fd(r);pd();lt(165)
    circle(r*4,30)
    lt(90+15);fd(r)
    circle(r*0.60,120);fd(r)
    end_fill()

def mura(x1,y1,hg):
    rs = hg/3.75;x=100;y=100
    pgr = sqrt( pow(rs,2) + pow(hg,2) )
    dcc = int(round(degrees(atan2(rs, hg))))
    num = ceil(360/(dcc*2))
    body(x1,y1,pgr,dcc,hg,num,rs)
    eyes(x1,y1,hg)
    mouth(x1,y1,hg/2.25)

min = -500;max = 500;num = 70
for i in range(num):
    mura(randint(min, max),randint(min, max),randint(30,150))
