# -*- coding: utf-8 -*-


import tkinter as tk
import re
 
def find():
    
    filename = 'text.txt' 
    fin=open(filename,'r')
    word=k.get()
    for line in fin:
        line = line.rstrip()
    
        worde=re.findall("\S+"+word+"\S+|"+word+"\S+|"+"\S+"+word,line)
        
    result.configure(text=worde)
    result2.configure(text="Number: "+str(len(worde)))
    
    
    #Basic interface with Tkinter
pencere = tk.Tk()

pencere.title("Find Word")
pencere.geometry('800x300')

wordTK=tk.Label(text="Word:")
wordTK.grid(row=0,column=0)

entry=tk.Entry()
entry.grid(row=0,column=1)

button = tk.Button(text='Bul', command=kelimebulma)
button.grid(row=1,column=1)

result=tk.Label(text="  ")
result.grid(row=2,column=1)

result2=tk.Label(text="  ")
resukt2.grid(row=3,column=1)


    

pencere.mainloop()
