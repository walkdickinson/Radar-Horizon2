#Radar Horizon Calculation

import tkinter as tk
from tkinter import *
import math

root=Tk()
root.title("Radar Horizon")
root.geometry("500x400")

def Calculation():
    target=int(target_radar_heightvalue.get())
    total=(round(math.sqrt(target) + math.sqrt(3.6) * 1.23))
    Label(text=f"{total}", font="arial 15 bold").place(x=250,y=170)


#subject
sub1=Label(root,text="Target Radar Height in ft", font="arial 10")
total=Label(root,text="Radar Horizon in NM", font="arial 10")
sub3=Label(root, text='Radar Horizon = Square Root of Target Height + Square Root of USV Height *1.23', font='arial 10')


sub1.place(x=50,y=20)
total.place(x=50,y=70)
sub3.place(x=50,y=120)

target_radar_heightvalue=StringVar()


target_radar_heightvalue=Entry(root,textvariable=target_radar_heightvalue,font="arial 15", width=15)


target_radar_heightvalue.place(x=250,y=20)


Button(text="Calculate", font="arial 15", bg="white", bd=10,command=Calculation).place(x=50,y=300)
Button(text="Exit", font="arial 15", bg="white", bd=10,width=8,command=lambda:exit()).place(x=350,y=300)

root.mainloop()