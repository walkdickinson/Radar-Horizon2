import tkinter as tk
from tkinter import *
from tkinter import ttk
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from mpl_toolkits.basemap import Basemap


root = tk.Tk()
root.title("Radar Calculations")
root.geometry("800x600")


#Functions for tabs

def CalculationERP():
    try:
        power=float(radar_power_in_dBMentry.get())
        gain=float(antenna_Gain_in_dBmvalue.get())
        loss=float(antenna_Loss_in_dBmvalue.get())
        total=(power+gain-loss)
        ttk.Label(tab1, text=f"{total}", font="arial 15 bold").grid(row=20, column=15)
    except ValueError:
        ttk.Label(tab1,text="Invalid input. Please enter numerical values.", font="arial 10").grid(row=20, column=15)

def CalculationHorizon():
    try:
        latitude=float(latitude_entry.get())
        longitude=float(longitude_entry.get())
        target=int(target_radar_heightvalue.get())
        total=(round(math.sqrt(target) + math.sqrt(3.6) * 1.23))
        totalCH=total*1852
        ttk.Label(tab1, text=f"{total}", font="arial 15 bold").grid(row=55, column=15, pady=10)
        # Display the result in the GUI
        result_var = StringVar()
        result_var.set(f'Max Detection Range: {totalCH:.2f} meters')

        # Plot the circle on a world map
        fig, ax = plt.subplots()
        m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
        m.drawcoastlines()
        m.drawcountries()

        # Plot the circle
        circle = Circle(m(longitude, latitude), totalCH, fill=False, edgecolor='r')
        ax.add_patch(circle)
        plt.scatter(m(longitude, latitude), m(latitude, longitude), color='blue')  # Mark user-provided location

        plt.title('Radar Detection Range')
        plt.show()
    except ValueError:
        ttk.Label(tab1, text="Invalid input. Please enter numerical values.", font="arial 10").grid(row=55, column=15, pady=10)   
    
def CalculationMaxrange():
    try:
        latitude=float(latitude_entry.get())
        longitude=float(longitude_entry.get())
        power2=float(radar_power_in_dBMentry2.get())
        expo1=int(topowerA.get())
        expo2=int(topowerB.get())
        gain2=float(antenna_Gain_in_dBmvalue2.get())
        wavelength=float(soi_wavelength_in_meters.get())
        rcs=float(rcs_in_metersq.get())
        echo=float(echo_strength_inwatts.get())
        sumofloss=float(sum_of_loss_in_db.get())
        total=(((power2*10**(expo1))*gain2**2*wavelength**2*rcs)/(((4*math.pi)**3)*(echo*10**(expo2))*sumofloss))**(1/4)
        ttk.Label(tab2, text=f"{total}", font="arial 15 bold").grid(row=35, column=15)
        totalNM=(total/1852)
        ttk.Label(tab2, text=f"{totalNM}", font="arial 15 bold").grid(row=40, column=15)
        # Display the result in the GUI
        result_var = StringVar()
        result_var.set(f'Max Detection Range: {total:.2f} meters')

        # Plot the circle on a world map
        fig, ax = plt.subplots()
        m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
        m.drawcoastlines()
        m.drawcountries()

        # Plot the circle
        circle = Circle(m(longitude, latitude), total, fill=False, edgecolor='r')
        ax.add_patch(circle)
        plt.scatter(m(longitude, latitude), m(latitude, longitude), color='blue')  # Mark user-provided location

        plt.title('Radar Detection Range')
        plt.show()
    except ValueError:
        ttk.Label(tab2, text="Invalid input. Please enter numerical values.", font="arial 10").grid(row=35, column=15)


# def display_map_tab3():
    # Display the result in the GUI
    #result_var.set(f'Max Detection Range: {max_detection_range:.2f} meters')

    # Plot the circle on a world map
    #fig, ax = plt.subplots()
   #m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    #m.drawcoastlines()
    #m.drawcountries()

    # Plot the circle
    #circle = Circle(m(longitude, latitude), max_detection_range, fill=False, edgecolor='r')
    #ax.add_patch(circle)
    #plt.scatter(m(longitude, latitude), m(latitude, longitude), color='blue')  # Mark user-provided location

    #plt.title('Radar Detection Range')
    #plt.show()
            
    
#Creating Tabs and Tab labels via Notebook
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook, width=800, height=600)
notebook.add(tab1, text = "ERP/ Radar Horizion")

#Not 100% sure if these are needed
frame=LabelFrame(tab1, text="ERP", padx=5, pady=5)
frame.grid(padx=10, pady=10)

#ERP for some reason all the columns had to be switched to 0 vs 1 
#This is all in tab1. Tab2 was moved to the bottom to keep it all together
sub1=Label(tab1,text="Radar Power in dBm", font="arial 10")
sub2=Label(tab1,text="Antenna Gain in dBm", font="arial 10")
sub3=Label(tab1,text="Antenna Loss in dBm", font="arial 10")
total=Label(tab1,text="Calculate ERP", font="arial 10")

#these actually place the defined variables
sub1.grid(row=5, column=0, pady=10)
sub2.grid(row=10, column=0, pady=10)
sub3.grid(row=15, column=0, pady=10)
total.grid(row=20, column=0, pady=10)

radar_power_in_dBMvalue=StringVar()
antenna_Gain_in_dBmvalue=StringVar()
antenna_Loss_in_dBmvalue=StringVar()

#Creatinon of the user input feilds variables
radar_power_in_dBMentry=Entry(tab1,textvariable=radar_power_in_dBMvalue,font="arial 15", width=15)
antenna_Gain_in_dBmvalue=Entry(tab1,textvariable=antenna_Gain_in_dBmvalue,font="arial 15", width=15)
antenna_Loss_in_dBmvalue=Entry(tab1,textvariable=antenna_Loss_in_dBmvalue,font="arial 15", width=15)

#placement of the user input varible 
radar_power_in_dBMentry.grid(row=5, column=15, pady=10)
antenna_Gain_in_dBmvalue.grid(row=10, column=15, pady=10)
antenna_Loss_in_dBmvalue.grid(row=15, column=15, pady=10)




#Target Radar height equation user input fields and variables. Snet to above function
sub1=ttk.Label(tab1,text="Target Radar Height in ft", font="arial 10")
sub1.grid(row=50, column=0, pady=10)

total=ttk.Label(tab1,text="Radar Horizon in NM", font="arial 10")
total.grid(row=55, column=0, pady=10)

sub3=ttk.Label(tab1, text='(Radar Horizon = Square Root of Target Height + Square Root of USV Height *1.23)', font='arial 10')
sub3.grid(row=60, column=0, pady=10)

target_radar_heightvalue=StringVar()
#Had to create new Variables in the notebook format 'tkk.button' then used .grid on next line to place them.
target_radar_heightvalue=ttk.Entry(tab1,textvariable=target_radar_heightvalue,font="arial 15", width=15)
target_radar_heightvalue.grid(row=50, column=15, pady=10)


ERP_Button = Button(tab1, text="Calculate ERP", font="arial 15", bg="white", bd=10,command=CalculationERP)
ERP_Button.grid(row=30, column=0, pady=10)
         
Button_RH = Button(tab1, text="Calculate Radar Horizon", font="arial 15", bg="white", bd=10, command=CalculationHorizon)
Button_RH.grid(row=80, column=0, pady=10)


# Buttons for closing. beacuse there will be one on the second tab and it has to be double coded.
exit_button = Button(tab1, text="Exit",font="arial 15", bg="white", bd=10,width=8, command=root.destroy)
exit_button.grid(row=85, column=0, pady=20)


#Begin coding of Tab2 intial parts are creating the tab and naming it "MDR"
tab2 = ttk.Frame(notebook, width=800, height=600)
notebook.add(tab2, text = "MDR")
    
frame2=LabelFrame(tab2,text="MDR", pady=5, padx=5)
frame2.grid(padx=10, pady=10)    
    


#subject Max range labels for user input boxs. Same layout as before but with leading 2s to make thme unique to tab1
sub21=Label(tab2,text="Radar Power in Watts",font="arial 10")
sub22=Label(tab2,text="Antenna Gain in Watts", font="arial 10")
sub23=Label(tab2,text="SOI wavelength in Meters", font ="arial 10")
sub24=Label(tab2,text="RCS in Meters Squared", font ="arial 10")
sub25=Label(tab2,text="Echo strength in Watts", font="arial 10")
sub26=Label(tab2,text="Sum of Loss in Watts", font="arial 10")
sub27=Label(tab2,text="X 10 to the power of", font="arial 10")
sub28=Label(tab2,text="X 10 to the power of", font="arial 10")
total2=Label(tab2,text="Calculated Max Range in Meters", font="arial 10")
total2NM=Label(tab2,text="Calculated Max Range in Nautical Miles", font="arial 10")

#placement of labels
sub21.grid(row=5, column=1, pady=10)
sub22.grid(row=10, column=1, pady=10)
sub23.grid(row=15, column=1, pady=10)
sub24.grid(row=20, column=1, pady=10)
sub25.grid(row=25, column=1, pady=10)
sub26.grid(row=30, column=1, pady=10)
sub27.grid(row=5, column=20, pady=10)
sub28.grid(row=25, column=20, pady=10)
total2.grid(row=35, column=1, pady=10)
total2NM.grid(row=40, column=1, pady=10)

#creates User input boxs for colculations to occur

radar_power_in_dBMvalue2=StringVar()
antenna_Gain_in_dBmvalue2=StringVar()
soi_wavelength_in_meters=StringVar()
rcs_in_metersq=StringVar()
echo_strength_inwatts=StringVar()
sum_of_loss_in_db=StringVar()
topowerA=StringVar()
topowerB=StringVar()

#defines input variable and sets font for boxes
radar_power_in_dBMentry2=Entry(tab2,textvariable=radar_power_in_dBMvalue2,font="arial 15", width=15)
antenna_Gain_in_dBmvalue2=Entry(tab2,textvariable=antenna_Gain_in_dBmvalue2,font="arial 15", width=15)
soi_wavelength_in_meters=Entry(tab2,textvariable=soi_wavelength_in_meters,font="arial 15", width=15)
rcs_in_metersq=Entry(tab2,textvariable=rcs_in_metersq,font="arial 15", width=15)
echo_strength_inwatts=Entry(tab2,textvariable=echo_strength_inwatts,font="arial 15", width=15)
sum_of_loss_in_db=Entry(tab2,textvariable=sum_of_loss_in_db,font="arial 15", width=15)
topowerA=Entry(tab2,textvariable=topowerA,font="arial 15", width=15)
topowerB=Entry(tab2,textvariable=topowerB,font="arial 15", width=15)


#places user input boxes in GUI
radar_power_in_dBMentry2.grid(row=5, column=15, pady=10)
antenna_Gain_in_dBmvalue2.grid(row=10, column=15, pady=10)
soi_wavelength_in_meters.grid(row=15, column=15, pady=10)
rcs_in_metersq.grid(row=20, column=15, pady=10)
echo_strength_inwatts.grid(row=25, column=15, pady=10)
sum_of_loss_in_db.grid(row=30, column=15, pady=10)
topowerA.grid(row=5, column=30, pady=10)
topowerB.grid(row=25, column=30, pady=10)


#Calculation Button
MDR_Button = Button(tab2,text="Calculate Max Detection Range", font="arial 15", bg="white", bd=10,command=CalculationMaxrange)
MDR_Button.grid(row=50, column=1, pady=10)


#Second Exit button
exit_button = Button(tab2, text="Exit",font="arial 15", bg="white", bd=10,width=8, command=root.destroy)
exit_button.grid(row=85, column=1, pady=20)


#Begin coding of Tab2 intial parts are creating the tab and naming it "MDR"
tab3 = ttk.Frame(notebook, width=800, height=600)
notebook.add(tab3, text = "MAP")


# Latitude input
Label(tab3, text='Latitude:').grid(row=0, column=0)
latitude_entry = Entry(tab3)
latitude_entry.grid(row=0, column=1)

# Longitude input
Label(tab3, text='Longitude:').grid(row=1, column=0)
longitude_entry = Entry(tab3)
longitude_entry.grid(row=1, column=1)

#Third Exit button
exit_button = Button(tab3, text="Exit",font="arial 15", bg="white", bd=10,width=8, command=root.destroy)
exit_button.grid(row=85, column=1, pady=20) 

notebook.grid()

root.mainloop()
