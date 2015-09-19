# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 08:26:09 2015

@author: MakMN
"""
# із числами, які повторюються: або щоб не повторювались, або щоб замінювались при попаданні

import random

a_number = {x: x for x in range(1, 76)}

line1 = [x for x in range(1, 16)]
line2 = [x for x in range(16, 31)]
line3 = [x for x in range(31, 46)]
line4 = [x for x in range(46, 61)]
line5 = [x for x in range(61, 76)]

#all = [(x, y, z, q, s) for x in line1 for y in line2 for z in line3 for q in line4 for s in line5] # генератор усіх варіантів послідовності чисел

table = []  #таблиця випадкових чисел для 1 стовпця лотереї
for i in range(5):
        row = [random.choice(line1), random.choice(line2), random.choice(line3), random.choice(line4), random.choice(line5)]
        table += [row]

def popadannya(table, n, count):
    for i in range(len(table)):
            for g in range(len(table)):
                if table[i][g] == n:
                    print('Happy', count1, 'ball!')                    
                    print('Position in tables ['+str(i) +']' + '[' + str(g) +']')
                    table[i][g] = 0
                    print(table)
                    return table

def deleteline(table, nline):
    table = table.remove(table[nline])
    return table

print(table)                

balls = []  #генератор випадкових чисел із можливістю відсікання тих, які вже були раніше
ballsintable = [] #попадання кульки в масив випадкових чисел

count1 = 1  # кульки, що попали у діапазон
count2 = 0  # кількість кульок, що випали
count3 = 0  # лінії, що склалася

for j in range(1000):  # довільна кількість майбутніх спроб випадання кульок
    if not a_number:
            break
    confirm = input('Give the ball? (Y/N)\n =>')
    if confirm.capitalize() == 'Y':
        ball = random.randint(1, 75)
        if ball in balls:
            print('Випала кулька, яка випадала раніше... тра фіксити')
            continue
        else:
            count2 += 1
            balls += [a_number.pop(ball)]
            print('The', count2, 'ball is:', ball)
            ballsintable = popadannya(table, ball, count1)
            if ballsintable:
                count1 += 1
                for i in range(len(ballsintable)):
                    if sum(ballsintable[i]) == 0:
                        ballsintable = deleteline(ballsintable, i)
                        count3 += 1
                        print('Yuo got the', count3, 'line!!!', i, 'row')
                        print(ballsintable)
                        break
            else:
                print('No ball in lines...')
    else:
        print('Кульки, що попали у діапазон:', count1-1, '\nКількість кульок, що випали:', count2, '\nЛінії, що склалася:', count3, '\nБувайте!')
        break
