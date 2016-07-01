# license: GPLv3
__author__ = "Александр Мангазеев"

import turtle
from math import sin

print("""Данная программа умеет рисовать цифры, заданного десятичного числа
   для этого необходимо ввести число с клавиатуры и нажать Enter


   """)

num = input('Enter number: ')

t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(2)
t.speed(10)


def main():
    t.penup()
    t.backward(300)
  
    number(num)
    
    t.hideturtle()
    
def number(num):
    for h in str(num):
        if h == '1':
            digit_one(50)
            t.forward(30)
        elif h == '2':
            digit_two(50)
            t.forward(30)
        elif h == '3':
            digit_three(50)
            t.forward(30)
        elif h == '4':
            digit_four(50)
            t.forward(30)
        elif h == '5':
            digit_five(50)
            t.forward(30)
        elif h == '6':
            digit_six(50)
            t.forward(30)
        elif h == '7':
            digit_seven(50)
            t.forward(30)
        elif h == '8':
            digit_eight(50)
            t.forward(30)
        elif h == '9':
            digit_nine(50)
            t.forward(30)
        elif h == '0':
            digit_zero(50)
            t.forward(30)
        
            
def digit_one(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    t.penup()
    t.forward(length / 2)
    t.pendown()
    t.left(90)
    t.forward(length)
    t.left(90 + 45)
    t.forward(length * sin(45 * 3.141592 / 180))
    # обратный ход
    t.backward(length * sin(45 * 3.141592 / 180))
    t.right(90 + 45)
    t.backward(length)
    t.right(90)
    t.penup()


def digit_two(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length / 2
    L2 = (length / 2) * 2 ** 0.5
    B = [180, -135, 45, 90]
    A = [L1, L2, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()

def digit_three(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length / 2
    L2 = (length / 2) * 2 ** 0.5
    B = [-135, 135, -135, 135]
    A = [L2, L1, L2, L1]

    t.penup()
    t.forward(L1)
    t.left(180)
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.left(180)
    t.penup()
    t.forward(L1)

def digit_four(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length / 2
    L2 = (length / 2) * 2 ** 0.5
    B = [90, 0, 180, -90, -90]
    A = [L1, L1, L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()

def digit_five(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length / 2
    L2 = (length / 2) * 2 ** 0.5
    B = [180, 180, 90, 90, -90, -90]
    A = [L1, L1, L1, L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()

def digit_six(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length / 2
    L2 = (length / 2) * 2 ** 0.5
    B = [180, -90, -90, -90, -90, -90, -45]
    A = [L1, L1, L1, L1, L1, L1, L2]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    
def digit_seven(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length / 2
    L2 = (length / 2) * 2 ** 0.5
    B = [-90, -45, 135]
    A = [L1, L2, L1]

    t.penup()
    t.forward(L1)
    t.left(180)
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.left(180)
    t.forward(L1)

def digit_eight(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length / 2
    L2 = (length / 2) * 2 ** 0.5
    B = [180, -90, 0, -90, -90, -90, 180, -90]
    A = [L1, L1, L1, L1, L1, L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()

def digit_nine(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length / 2
    L2 = (length / 2) * 2 ** 0.5
    B = [-135, 135, -90, -90, -90]
    A = [L2, L1, L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.left(180)
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.left(180)
    t.penup()
    t.forward(L1)

def digit_zero(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length / 2
    L2 = (length / 2) * 2 ** 0.5
    B = [180, -90, 0, -90, -90, 0
         ]
    A = [L1, L1, L1, L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()

main()
