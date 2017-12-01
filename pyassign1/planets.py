# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 18:55:23 2017

@author: 张泽岳（1700011816）
"""

import turtle
import math

ss=turtle.Screen()
ss.screensize(1000,1000)
ss.bgcolor('black')

Mercury=turtle.Turtle()
Venus=turtle.Turtle()
Earth=turtle.Turtle()
Mars=turtle.Turtle()
Jupiter=turtle.Turtle()
Saturn=turtle.Turtle()
Sun=turtle.Turtle()

def solarsystem(Mercury,Venus,Earth,Mars,Jupiter,Saturn):
    Mercury.shape('circle')
    Venus.shape('circle')
    Earth.shape('circle')
    Mars.shape('circle')
    Jupiter.shape('circle')
    Saturn.shape('circle')
    Sun.shape('circle')

    Mercury.color('gray')
    Venus.color('gold')
    Earth.color('blue')
    Mars.color('red')
    Jupiter.color('brown')
    Saturn.color('white')
    Sun.color('orange')

    Mercury.shapesize(0.1)
    Venus.shapesize(0.4)
    Earth.shapesize(0.7)
    Mars.shapesize(0.5)
    Jupiter.shapesize(1.2)
    Saturn.shapesize(1)
    Sun.shapesize(2)

    Mercury.up()
    Mercury.goto(20,0)
    Mercury.down()
    
    Venus.up()
    Venus.goto(45*0.435,0)
    Venus.down()
    
    Earth.up()
    Earth.goto(90*0.667,0)
    Earth.down()
    
    Mars.up()
    Mars.goto(125*0.578,0)
    Mars.down()
    
    Jupiter.up()
    Jupiter.goto(200*0.716,0)
    Jupiter.down()
    
    Saturn.up()
    Saturn.goto(250*0.617,0)
    Saturn.down()
    
    for i in range(15000000000):
        Mercury.goto(-30+50*math.cos(math.radians(4*i)),30*math.sin(math.radians(4*i)))
        Venus.goto(-45+(45*1.435)*math.cos(math.radians(3*i)),(45*(1.435**2-1)**0.5)*math.sin(math.radians(3*i)))
        Earth.goto(-90+(90*1.667)*math.cos(math.radians(2.666*i)),(90*(1.667**2-1)**0.5)*math.sin(math.radians(2.666*i)))
        Mars.goto(-125+(125*1.578)*math.cos(math.radians(2.5*i)),(125*(1.578**2-1)**0.5)*math.sin(math.radians(2.5*i)))
        Jupiter.goto(-200+(200*1.716)*math.cos(math.radians(2*i)),(200*(1.716**2-1)**0.5)*math.sin(math.radians(2*i)))
        Saturn.goto(-250+(250*1.617)*math.cos(math.radians(1.8*i)),(250*(1.617**2-1)**0.5)*math.sin(math.radians(1.8*i)))
    
        
solarsystem(Mercury,Venus,Earth,Mars,Jupiter,Saturn)
ss.exitonclick()
