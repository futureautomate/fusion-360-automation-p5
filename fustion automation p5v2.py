# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:05:36 2021

@author: Tejas
"""

import pyautogui
import time

#while True:
#    time.sleep(1)    
#    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#    print(currentMouseX, currentMouseY)    

def moveToExCoMenu(keys):
    pyautogui.moveTo(MenuExCoLocation[keys][0],MenuExCoLocation[keys][1],1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    
def hideMenu(keys):
    pyautogui.moveTo(MenuHideLocation[keys][0],MenuHideLocation[keys][1],1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    
bodyx = 57
bodyy = 355

bodyhx = 89
bodyhy = 354

MenuOrder = {'Body':1,'Sketches':2,'Constructions':3}
MenuExCoLocation = {'Body':[bodyx,bodyy],'Sketches':[bodyx,(bodyy+30*(MenuOrder['Sketches']-1))],'Constructions':[bodyx,(bodyy+30*(MenuOrder['Constructions']-1))]}
MenuHideLocation = {'Body':[bodyhx,bodyhy],'Sketches':[bodyhx,(bodyhy+30*(MenuOrder['Sketches']-1))],'Constructions':[bodyhx,(bodyhy+30*(MenuOrder['Constructions']-1))]}

mainOpt = 1

while mainOpt < 3 or mainOpt > 0:
    mainOpt = int(input("Enter the selection\n1)Menu Selection\n2)Hide Menu\n3)Exit\n"))
    
    if mainOpt == 1:
        print("Selet Menu for navigatin --\n")
        for i,j in MenuOrder.items():
            print('%d:%s' % (j,i))
        opt = int(input())
        menu = list(MenuExCoLocation.keys())[opt-1]
        moveToExCoMenu(menu)
        
    elif mainOpt == 2:
        print("Selet Menu for navigatin --\n")
        for i,j in MenuOrder.items():
            print('%d:%s' % (j,i))
        opt = int(input())
        menu = list(MenuHideLocation.keys())[opt-1]
        hideMenu(menu)
        
    elif mainOpt == 3:
        break
        
    else:
        print("Dude wrong input check the menu and select correct one...")