import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox


root = tk.Tk()
a = tk.IntVar()
root.geometry("600x400")
root.title("Flight planner 1.0")



#----ROW 1----

departlabel = tk.Label(root, text="Departure:", font=('Arial', 14))
departlabel.grid(row = 2, column = 0, pady = 2)

depart = tk.Entry(root, width=5, font=('Arial', 12))
depart.grid(row = 2, column = 1, pady = 2)

arrivelabel = tk.Label(root, text="Arrival:", font=('Arial', 14))
arrivelabel.grid(row = 2, column = 2, pady = 2)

arrive = tk.Entry(root, width=5, font=('Arial', 12))
arrive.grid(row = 2, column = 3, pady = 2)

#----ROW 2----

aircraftlabel = tk.Label(root, text="Aircraft:", font=('Arial', 14))
aircraftlabel.grid(row = 3, column = 0)

aircraft = tk.Entry(root, width=8, font=('Arial', 12))
aircraft.grid(row = 3, column = 1, pady=2)

callsignlabel = tk.Label(root, text="Callsign:", font=('Arial', 14))
callsignlabel.grid(row=3, column=2)

callsign = tk.Entry(root, width=10, font=('Arial', 12))
callsign.grid(row=3,column=3)

#----ROW 3----

cruiselabel = tk.Label(root, text="Cruise(FL):", font=('Arial', 14))
cruiselabel.grid(row = 4, column = 0)

cruise = tk.Entry(root, width=8, font=('Arial', 12))
cruise.grid(row = 4, column = 1, pady=2)

#----ROW 4----

flightrulelabel = tk.Label(root, text="Flight Rule: ", font=('Arial', 14))
flightrulelabel.grid(row = 5, column = 0)

ifr = tk.Radiobutton(root, text="IFR", variable=a, value=1).grid(row=5, column=1)
vfr = tk.Radiobutton(root, text="VFR", variable=a, value=2).grid(row=5, column=2)

#----ROW 5----

deprunlabel = tk.Label(root, text="Departure Runway: ", font=('Arial', 14))
deprunlabel.grid(row = 6, column = 0)

deprun = tk.Entry(root, width=4, font=('Arial', 12))
deprun.grid(row = 6, column = 1, pady=2)

arrrunlabel = tk.Label(root, text="Arrival Runway: ", font=('Arial', 14))
arrrunlabel.grid(row = 6, column = 2)

arrrun = tk.Entry(root, width=4, font=('Arial', 12))
arrrun.grid(row = 6, column = 3, pady=2)


def getdata():
    if (callsign.get() == "" or depart.get() == "" or arrive.get() == "" or aircraft.get() == ""):
        messagebox.askretrycancel("Message", "Please fill in all pieces of information...")
        return
    if (a.get() == 1):
        fr = 'IFR'
    elif(a.get() == 2):
        fr = 'VFR'
    else:
        fr = "None Assigned"
    print(depart.get(), "/", arrive.get())
    print("Aircraft: ", aircraft.get())
    print("Callsign: ", callsign.get())
    print("Cruise alt: ", cruise.get())
    print("Departure Runway: ", deprun.get())
    print("Arrival Runway: ", arrrun.get())
    with open('Flights.txt','a') as flightplan:
        flightplan.write(f"Callsign: {callsign.get()}\n{depart.get()}/{arrive.get()}\nAircraft: {aircraft.get()}\nCruise alt: FL{cruise.get()}\nFlight Rule:{fr}\nDeparture Runway:{deprun.get()}\tArrival Runway: {arrrun.get()}\n========================================\n")
    clear_text()

def clear_text():
        depart.delete(0, 'end')
        arrive.delete(0, 'end')
        aircraft.delete(0, 'end')
        callsign.delete(0, 'end')
        cruise.delete(0, 'end')
        deprun.delete(0, 'end')
        arrrun.delete(0, 'end')
        return

def SaveToFile1(filename):
    # The file saving logic will now be inside this function
    if (a.get() == 1):
        fr = 'IFR'
    elif(a.get() == 2):
        fr = 'VFR'
    else:
        fr = "None Assigned"

    with open(f'{filename}.txt', 'w') as flightplan:
        flightplan.write(f"Callsign: {callsign.get()}\n{depart.get()}/{arrive.get()}\nAircraft: {aircraft.get()}\nCruise alt: FL{cruise.get()}\nFlight Rule:{fr}\nDeparture Runway:{deprun.get()}\tArrival Runway: {arrrun.get()}\n")

    print(f"File saved as {filename}.txt")
    clear_text()

def Saveas():
    if (callsign.get() == "" or depart.get() == "" or arrive.get() == "" or aircraft.get() == ""):
        messagebox.askretrycancel("Message", "Please fill in all pieces of information...")
        return
    newWindow = tk.Toplevel(root)
    newWindow.title("Save As...")
    newWindow.geometry("400x200")

    filelabel = tk.Label(newWindow, text="Enter file name: ", font=('Arial', 14))
    filelabel.grid(row=1, column=0)

    filename = tk.Entry(newWindow, width=20, font=('Arial', 12))
    filename.grid(row=2, column=1, pady=2)

    # Define the button to trigger the save operation
    def on_save():
        UserFileName = filename.get()
        if UserFileName:  # Only proceed if the user entered a filename
            SaveToFile1(UserFileName)
            newWindow.destroy()  # Optionally close the "Save As" window after saving
        else:
            print("No filename entered.")

    enterbutton = tk.Button(newWindow, text="Save", command=on_save)
    enterbutton.grid(column=1)

def helpmenuwindow():
    helpWindow = tk.Toplevel(root)
    helpWindow.title("Help - User Guide")
    helpWindow.geometry("600x400")

    helpText = """Flight Planner User Guide:

    1. Enter your flight details in the fields.
    - Departure: Enter the departure airport.
    - Arrival: Enter the arrival airport.
    - Aircraft: Enter the aircraft type.
    - Callsign: Enter your flight's callsign.
    - Cruise: Enter the cruise altitude in FL (e.g., FL350).
    - Flight Rule: Select either IFR or VFR.

    2. To save your flight details:
    - Click 'Save' to append the details to the default file (Flights.txt).
    - Click 'Save As...' to specify a custom file name to save the flight details.

    3. The program will generate a text file with the flight details in the following format:
    - Callsign: [callsign]
    - Departure: [departure airport]
    - Arrival: [arrival airport]
    - Aircraft: [aircraft]
    - Cruise altitude: FL[altitude]
    - Flight rule: [IFR/VFR]
    - Runways: [departure/arrival runway]

    4. You can clear the text fields by selecting 'New' in the File menu.

    """
    helpLabel = tk.Label(helpWindow, text=helpText, font=('Arial', 10), justify="left")
    helpLabel.grid(row=0,column=0)


menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=clear_text)
filemenu.add_command(label='Save', command=getdata)
filemenu.add_command(label='Save As...', command=Saveas)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Guide', command=helpmenuwindow)

enterbutton = tk.Button(root, text="Enter", command=getdata)
enterbutton.grid(column = 1)

root.mainloop()
