"""Test"""
import turtle as t
from random import random

t1 = t.Turtle()
t2 = t.Turtle()

wn = t.Screen()
wn.bgcolor("lightgreen")

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t1.right(angle)
    t1.fd(steps)
    t2.left(angle)
    t2.bk(steps)
