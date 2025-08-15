from math import * 

import subprocess

startimage = '【﻿Ｄａｎｋ　ＯＳ】'

menulist = [ 'videos', ' wisdom', 'logic', 'nano']

videolist = 'IDK'

wisdom = 'Cheese'

def nano():
      subprocess.Popen(["/usr/bin/nano"])

#def logic():
 #    sub = input('Subject: ')
  #   pred = input('predicate: ')
   #  singpl = input('is the subject Singular or plural? Sing / PL: ')
    # if singpl == 'Sing':
   #  copula = 'is'
    # elif singpl == 'PL':
 #    copula = 'are'
  #   sel = input('Which statement do you wish to use? A E I O: ')
   #  if sel == 'A':
    # statement0 = str('all ' + sub + ' ' + copula + ' ' + pred)
  #if_statments below might need to become elif_  
 # if sel == 'E':
  #  statement0 = str('no ' + sub + ' ' + copula + ' ' + pred)
 # if sel == 'I':
  #  statement0 = str('some ' + sub + ' ' + copula + ' ' + pred)
 # if sel == 'O':
  # statement0 = str('some ' + sub + ' ' + copula + ' not  ' + pred)
 # print(statement0)
  
 # sub1 = input('Subject: ')
 # pred1 = input('predicate: ')
 # singpl1 = input('is the subject Singular or plural? Sing / PL: ')
 # if singpl1 == 'Sing':
 #   copula1 = 'is'
 # elif singpl1 == 'PL':
 #   copula1 = 'are'

 # sel1 = input('Which statement do you wish to use? A E I O: ')
 # if sel1 == 'A':
 #   statement1 = str('all ' + sub1 + ' ' + copula1 + ' ' + pred1)
 # if sel1 == 'E':
 #   statement1 = str('no ' + sub1 + ' ' + copula1 + ' ' + pred1)
 # if sel1 == 'I':
 #   statement1 = str('some ' + sub1 + ' ' + copula1 + ' ' + pred1)
 # if sel1 == 'O':
  #    statement1 = str('some ' + sub1 + ' ' + copula1 + ' not  ' + pred1)
 # if pred == sub1:
  #  statement2 = str('all ' + sub + ' ' + copula + ' ' + pred1)
 # print(statement0 + '\n' + statement1 + '\n' + statement2)
#  sel2 = input('Menu or back to logic? M/L: ')
 # if sel2 == 'M':
  #  menu()
 # elif sel2 == 'L':
  #  logic()



def screensaver():
     print(startimage)
     print('Loading...')


def password():
     password = input('Whats The Password: ')
     if password == "69":
      print('Access Granted')
     pass

     else:
     print('Access Denied')
     password()
     menu()

def returntomenu():
     print('Would you like to continue?: Yes/No\n')
     selection1 = input()
     if selection1 == 'Yes':
     menu()
     else:
     print('okie')
     startup()

def menu():
     print('Menu ' + str(menulist))
     selection = input()
     if selection == "videos":
     print(videolist)
     returntomenu()
     elif selection == "wisdom":
     print(wisdom)
     returntomenu()
     elif selection == 'logic':
     logic()
     elif selection == 'nano':
     nano()
     else:
     print(selection + " is not a valid entry")
     menu()

def startup():
     screensaver()
     password()

startup()
