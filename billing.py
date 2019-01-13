# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:09:43 2019

@author: MY PC
"""

import numpy as np
def name_to_num(name):  #function to assign a no. againt name
    if name == "tea":
        res = 0
    elif name == "coffee":
        res = 1
    elif name == "samosa":
        res = 2
    elif name == "paratha":
        res = 3
    else:
        res = 4
    return res
def menu(): #menu card
    order=[] #null list to enter item
    num=[] #list to enter the no. of each item
    #menu to be displayed
    print("choose your items \n 1. tea \t\t Rs 5 \n 2. coffee \t\t Rs 7 \n 3. samosa \t\t Rs 10 \n 4. paratha \t\t Rs 20 \n 5. chowmien \t\t Rs 30")
    a=(input("would you like to order if yes please press y/yes")) #to ask isf he wants to order
    while a=='y' or a=='yes':
        print("give your order:")
        data=(input())
        t=name_to_num(data) #convet entered data into no.
        order.append(t) #append the order list for each item
        n=int(input("how much would u like to take"))
        num.append(n) #append the num list for its quantity
        a=(input("would you like to order more if yes please press y/yes"))
    print("thank u for ordering")
    print("you bill is Rs : ",bill_f(order,num)) #call the bill function for reqd amt
    b=input(("would you like to place your order(y/yes)")) #ask if he wants to take 
    if b=='y' or b=='yes':
        print("enjoy your meal \n thank u for visiting \n see you again")
    else:
        print('thank u')
def bill_f(order,num): #bill function
    total=0
    bill=[] #null bill list to take the amt for each item
    a=np.array((bill)) #convert list into array
    for i in range(len(order)): #loop to find the item
        if order[i]==0: #if tea
            bill.append(num[i]*5)
        elif order[i]==1: #if coffee
            bill.append(num[i]*7)
        elif order[i]==2: #if samosa
            bill.append(num[i]*10)
        elif order[i]==3: #if paratha
            bill.append(num[i]*20)
        else: #if chowmien
            bill.append(num[i]*30)
    s=sum(bill) #sum of the array
    return s
#main function
print("welcome to the restaurant")
ask=input("would you like to see the menu?? if yes please press y/yes") #ask if want to see menu
if ask=='y' or ask=='yes':
    menu() #call menu if yes
else:
    print('thank u')
y