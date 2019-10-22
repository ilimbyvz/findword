# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 02:22:49 2019

@author: DELL
"""

import tkinter as tk
import re
 


def kelimebulma():
    
    filename = 'text.txt' 
    fin=open(filename,'r')
    kelime=k.get()
    #s = fin.readline()
    for line in fin:
        line = line.rstrip()
    
        ke=re.findall("\S+"+kelime+"\S+|"+kelime+"\S+|"+"\S+"+kelime,line)
        
    sonuc.configure(text=ke)
    sonuc2.configure(text="Kelime sayısı: "+str(len(ke)))
    
    
    #Tkinter ile basit arayüz 
pencere = tk.Tk()

pencere.title("Kelime Bulma")
pencere.geometry('800x300')

kelime=tk.Label(text="Kelime:")
kelime.grid(row=0,column=0)

k=tk.Entry()
k.grid(row=0,column=1)

buton = tk.Button(text='Bul', command=kelimebulma)
buton.grid(row=1,column=1)

sonuc=tk.Label(text=" BOŞ")
sonuc.grid(row=2,column=1)

sonuc2=tk.Label(text=" BOŞ")
sonuc2.grid(row=3,column=1)


    

pencere.mainloop()
