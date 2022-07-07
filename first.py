import tkinter as tk
from tkcalendar import *
from tkinter import ttk
import time
import sqlite3
import calendar
import datetime
from plyer import notification 
root = tk.Tk()

conn = sqlite3.connect('reminders_db')
c = conn.cursor()

# c.execute("CREATE TABLE reminders(event_name text,from_time text,to_time text,location text)")
# c.execute("CREATE TABLE users(isLoggedIn integer,username text,password text)")


conn.commit()
conn.close()


def reminder():
    present_date = display_cal.get_date()
    newWindow = tk.Toplevel(root)
    newWindow.title("Set a reminder for " + present_date)
    newWindow.geometry("500x300")
    newWindow.configure(bg="#323232")
    heading = tk.Label(newWindow,text="Set a reminder for " + present_date,width=500,height=2,font=10,bg='#ec4646',fg="white")
    heading.pack()

    def clear_search(event):
        input1.delete(0, tk.END)
    def clear_search2(event):
        input2.delete(0, tk.END)

    Font_input = ("MS Sans Serif", 15)

    input1 = tk.Entry(newWindow)
    input1.insert(0, "Event Name")
    input1.bind("<Button-1>", clear_search)
    input1.place(x=100,y=60,height=30,width=300)
    input1.configure(bg='#323232',bd=1,font=Font_input,fg="white",borderwidth=1)
    input1.focus_set()

    input2 = tk.Entry(newWindow)
    input2.insert(0, "Location")
    input2.bind("<Button-1>", clear_search2)
    input2.place(x=100,y=160,height=30,width=300)
    input2.configure(bg='#323232',bd=1,font=Font_input,fg="white")

    tkvar = tk.StringVar(newWindow)
    choices = [ '12:00 am','1:00 am','2:00 am','3:00 am','4:00 am','5:00 am','6:00 am','7:00 am','8:00 am','9:00 am','10:00 am','11:00 am','12:00 pm','1:00 pm','2:00 pm','3:00 pm','4:00 pm','5:00 pm','6:00 pm','7:00 pm','8:00 pm','9:00 pm','10:00 pm','11:00 pm',]
    tkvar.set(choices[0])

    popupMenu = ttk.Combobox(newWindow, value=choices)
    popupMenu.current(0)
    popupMenu.place(x=100,y=110,width=80)

    popupMenu2 = ttk.Combobox(newWindow, value=choices)
    popupMenu2.current(0)
    popupMenu2.place(x=300,y=110,width=80)

    def save():
        save_input1=input1.get()
        save_input2=input2.get()
        save_combo1=popupMenu.get()
        save_combo2=popupMenu2.get()
        # save_combo3=popupMenu3.get()
        save_date = present_date

        conn = sqlite3.connect('reminders_db')
        c = conn.cursor()

        c.execute("INSERT INTO reminders VALUES(:event_name,:from_time,:to_time,:location)",
            {
                'event_name': input1.get(),
                'from_time': popupMenu.get(),
                'to_time': popupMenu2.get(),
                'location': input2.get(),
                # 'remind_before': popupMenu3.get()
            }
        )

        conn.commit()
        conn.close()

        notification.notify(
        title="Reminder Set",
        message="You set a reminder for " + save_input1 + ' at ' + save_combo1,
        timeout=5
        )

        newWindow.destroy()

    Font_button = ("MS Sans Serif", 10)

    save_button = tk.Button(newWindow, text="SAVE", command = save)
    save_button.place(x=300,y=260,width=100)
    save_button.configure(bg="#ec4646",fg="white",font=Font_button)

# reminder end

def view_reminders():
    present_date = display_cal.get_date()
    newWindow = tk.Toplevel(root)
    newWindow.title("Showing all reminders")
    newWindow.geometry("600x400")
    newWindow.configure(bg="#323232")
    heading = tk.Label(newWindow,text="Showing all reminders ",width=500,height=2,font=10,bg='#ec4646',fg="white")
    heading.pack()

    conn = sqlite3.connect('reminders_db')
    c = conn.cursor()    

    c.execute("SELECT *,oid FROM reminders")
    records = c.fetchall()

    i=len(records)
    


    def create_frame():

        frame3 = tk.Frame(newWindow,width=600,height=120, bg="#323232",border=5)
        frame3.pack()

        my_text = tk.Text(frame3)
        my_text.place(x=0,y=0,width=200,height=120)
        my_text.insert(1.0,print_records)
        Font_tuple = ("Comic Sans MS", 10)
        my_text.configure(bg="#323232",fg="white",border=0,font=Font_tuple)

        def delete():
            conn = sqlite3.connect('reminders_db')
            c = conn.cursor() 

            text1 = my_text.get('1.0','end')
            textx = text1.split()

            c.execute("DELETE from reminders WHERE oid =" + textx[0])

            frame3.destroy()

            conn.commit()
            conn.close()

 

        delete_button = tk.Button(frame3, text="DONE", command = delete)
        delete_button.place(x=300,y=50)
        delete_button.configure(bg="#ec4646",fg="white",font=Font_button)


    print_records = ''
    for record in records:
        print_records = ''
        print_records += str(record[4]) + '\n' + 'Reminder for:    ' + str(present_date) + '\n' + 'Event Name:      ' + str(record[0]) + '\n' + 'from:                ' +str(record[1])+ '\n'  + 'to:                    ' + str(record[2])+ '\n'  + 'Location:          ' + str(record[3])+ '\n' 
        create_frame()


    conn.commit()
    conn.close()

country = ''

def login_screen():
    newWindow = tk.Toplevel(root)
    newWindow.title("Login")
    newWindow.geometry("600x600")
    newWindow.configure(bg="#323232")
    heading = tk.Label(newWindow,text="Login",width=500,height=2,font=10,bg='#ec4646',fg="white")
    heading.pack()

    conn = sqlite3.connect('reminders_db')
    c = conn.cursor() 
    
    submit = tk.Button(newWindow, text="Submit", command = delete)
    submit.place(x=30,y=50)
    submit.configure(bg="#ec4646",fg="white",font=Font_button)

    conn.commit()
    conn.close()
    






def show_holidays():
    newWindow = tk.Toplevel(root)
    newWindow.title("Showing all holidays")
    newWindow.geometry("800x500")
    heading = tk.Label(newWindow,text="Showing all holidays ",width=500,height=2,font=10,bg='#ec4646',fg="white")
    heading.pack()
    

    file = open("holidays.txt",'r')
    stuff = file.read()
    my_text = tk.Text(newWindow,padx=50)
    my_text.place(x=0,y=50,width=1000,height=445)
    my_text.insert(1.0,stuff)
    Font_tuple = ("Helvetica", 12, "bold")
    my_text.configure(bg="#323232",fg="white",border=0,font=Font_tuple,spacing2=100)


on = 1

def hide():
    global on
    if on:
        frame1.pack_forget()
        on=0
    else:
        frame1.pack(side="left",fill=tk.BOTH,expand=0)
        top_frame.pack()
        on=1
    return 0

def show_year():
    newWindow = tk.Toplevel(root)
    newWindow.title("Showing all holidays")
    newWindow.geometry("600x600")

    cal_year = calendar.calendar(2021)
    label3 = tk.Text(newWindow,width=1000,height=800,bg="#323232",fg="white",padx=10,pady=10)
    label3.insert(1.0,cal_year)
    label3.pack()




Font_button = ("MS Sans Serif", 10, "bold")

side_frame = tk.Frame(root,width=30,height=2000,bg="#323232")
side_frame.pack(side="left")

top_frame = tk.Frame(root,width=2000,height=60,bg='#323232')
top_frame.pack(side="top")
heading = tk.Label(top_frame,text="Calender App",width=500,height=2,font=10,bg='#323232',fg="white")
heading.pack()

def on_enter1(e):
    year_button['background'] = '#9e9d89'

def on_leave1(e):
    year_button['background'] = '#323232'

# ----

def on_enter2(e):
    dash_button['background'] = '#9e9d89'

def on_leave2(e):
    dash_button['background'] = '#323232'

# ----

def on_enter3(e):
    reminder_button['background'] = '#9e9d89'

def on_leave3(e):
    reminder_button['background'] = '#555555'

# ----

def on_enter4(e):
    holiday_button['background'] = '#9e9d89'

def on_leave4(e):
    holiday_button['background'] = '#555555'

# ----

def on_enter6(e):
    hide_button['background'] = '#9e9d89'

def on_leave6(e):
    hide_button['background'] = '#323232'

# ----

def on_enter5(e):
    open_cal['background'] = '#9e9d89'

def on_leave5(e):
    open_cal['background'] = '#555555'

# ----

def on_enter7(e):
    login['background'] = '#9e9d89'

def on_leave7(e):
    login['background'] = '#555555'

year_button = tk.Button(top_frame,text="Year",command=show_year)
year_button.place(x=1085,y=20,width=50)
year_button.configure(bg="#323232",fg="white",font=Font_button,border=0)
year_button.bind("<Enter>", on_enter1)
year_button.bind("<Leave>", on_leave1)

dash_button = tk.Button(top_frame,text="...")
dash_button.place(x=1135,y=20)
dash_button.configure(bg="#323232",fg="white",font=Font_button,border=0)
dash_button.bind("<Enter>", on_enter2)
dash_button.bind("<Leave>", on_leave2)


frame1 = tk.Frame(root,width=250,height=800,bg="#555555")
frame1.pack(side="left",fill=tk.BOTH,expand=0)

frame2 = tk.Frame(root, width = 100, height =800 , bg="#323232")
frame2.pack(side="right",fill=tk.BOTH,expand=1)


reminder_button = tk.Button(frame1, text="Show  Reminders", command=view_reminders)
reminder_button.place(x=23,y=310,width=150)
reminder_button.configure(bg="#555555",fg="white",font=Font_button,border=0)
reminder_button.bind("<Enter>", on_enter3)
reminder_button.bind("<Leave>", on_leave3)

label5= tk.Label(frame1,text=">",font=10,bg="#555555",fg="white")
label5.place(x=10,y=310,height=25,width=25)

holiday_button = tk.Button(frame1, text="Show  holidays", command=show_holidays)
holiday_button.place(x=15,y=360,width=155)
holiday_button.configure(bg="#555555",fg="white",font=Font_button,border=0)
holiday_button.bind("<Enter>", on_enter4)
holiday_button.bind("<Leave>", on_leave4)

label5= tk.Label(frame1,text=">",font=10,bg="#555555",fg="white")
label5.place(x=10,y=360,height=25,width=25)

hide_button = tk.Button(root, text='----\n----', command=hide,height=2,width=4)
hide_button.place(x=30,y=15)
hide_button.bind('<Button-1>', hide)
hide_button.configure(bg="#2b2b28",fg="white",border=0)
hide_button.bind("<Enter>", on_enter6)
hide_button.bind("<Leave>", on_leave6)

display_cal = Calendar(frame1,showweeknumbers = False,firstweekday = 'sunday' , setmode='day', date_pattern='d/m/yy',weekendbackground="#2b2b28",othermonthwebackground="#555555" ,othermonthweforeground="white",weekendforeground="white",othermonthforeground="white" ,othermonthbackground ="#555555",background="#555555", disabledbackground="#2b2b28", bordercolor="#323232", headersbackground="#555555", normalbackground="#2b2b28", foreground='white', normalforeground='white', headersforeground='white')
display_cal.place(x=10,y=120)

cal_2 = Calendar(frame2,showweeknumbers = False,firstweekday = 'sunday', setmode='day', date_pattern='d/m/yy',weekendbackground="#323232",othermonthwebackground="#2b2b28" ,othermonthweforeground="white",weekendforeground="white",othermonthforeground="white" ,othermonthbackground ="#2b2b28",background="#323232", disabledbackground="#323232", bordercolor="#2b2b28", headersbackground="#323232", normalbackground="#323232", foreground='white', normalforeground='white', headersforeground='white')
cal_2.pack(fill="both", expand=True)
cal_2.configure()
display_cal.bind('<Double-1>', reminder)

d = datetime.datetime.now()

open_cal = tk.Button(frame1, text ='SET  REMINDER', command = reminder)
open_cal.place(x=20,y=70,width=150)
open_cal.configure(bg="#555555",fg="white",font=Font_button,border=0)
open_cal.bind("<Enter>", on_enter5)
open_cal.bind("<Leave>", on_leave5)

label4= tk.Label(frame1,text="+",font=10,bg="#555555",fg="white")
label4.place(x=10,y=69,height=25,width=25)

# login = tk.Button(frame1,text="Login",command=login_screen)
# login.configure(bg="#555555",fg="white",font=Font_button,border=0)
# login.place(x=20,y=600,width=100)
# login.bind("<Enter>", on_enter7)
# login.bind("<Leave>", on_leave7)

# label4= tk.Label(frame1,text="#",font=10,bg="#555555",fg="white")
# label4.place(x=10,y=600,height=25,width=25)

root.geometry('1200x800')
root.title('CALENDAR')
root.mainloop()
