# Importing tkinter module
from tkinter import *
import datetime
# importing calendar module
import calendar


def findDay():
    gui = Tk()
    gui.config(background='light blue')
    gui.title("Calender for the year")
    gui.geometry("750x200")
    day = day_field.get()
    dayy = datetime.datetime.strptime(day, '%d-%m-%Y').weekday()
    gui_content = calendar.day_name[dayy]
    calday = Label(gui, text=gui_content, font="Consolas 100 bold")
    calday.grid(row=10, column=4, padx=38)
    gui.mainloop()


# function to show calendar of the given year
def showCalender():
    gui = Tk()
    gui.config(background='light blue')
    gui.title("Calender for the year")
    gui.geometry("550x550")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop()


# Driver code
if __name__ == '__main__':
    new = Tk()
    new.config(background='#8ED5EC')
    new.title("Calender")
    new.geometry("950x500")
    cali = Label(new, text="Calender", bg='#8ED5EC', font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='#8ED5EC', font=("ariel", 15, "bold"), height=3, width=15)
    day = Label(new, text="Enter date", bg='#8ED5EC', font=("ariel", 15, "bold"), height=3, width=15)
    year_field = Entry(new, font='Arial 18')
    day_field = Entry(new, font='Arial 18')
    Showday = Button(new, text='Show Day', font=("consolas", 20, "bold"), fg='Black', bg='#7D5074', height=3, width=20,command=findDay)
    Showcal = Button(new, text='Show Calender', font=("consolas", 20, "bold"), fg='Black', bg='#7D5074', height=3,width=20, command=showCalender)
    Exit = Button(new, text='Exit', fg='Black', font=("consolas", 20, "bold"), bg='#7D5074', height=3, width=20,command=new.destroy)
      
    # putting widgets in position
    cali.grid(row=1, column=1)
    year.grid(row=10, column=8)
    day.grid(row=10, column=7)
    year_field.grid(columnspan=4, padx=10, pady=10, ipadx=20, ipady=15, row=20, column=8)
    day_field.grid(columnspan=4, padx=10, pady=10, ipadx=20, ipady=15, row=20, column=4)
    Showday.grid(row=25, column=7, pady=10)
    Showcal.grid(row=25, column=8)
    Exit.grid(row=45, column=7, padx=10)
    new.mainloop()
