import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *

import os
import openpyxl

def enter_data():
    company = company_name_entry.get()
    store = store_name_entry.get()
    service =title_combobox.get()
    responsible =responsible_entry.get()
    if(len(company) != 0 and len(store) != 0 and len(service) != 0 and len(responsible) != 0):
        print("basarili")

        filepath = "C:\\Users\\Teknik\\Desktop\\Servis_Takip\\data.xlsx"

        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = ["Company", "Store", "service", "responsoble"]
            sheet.append(heading)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([company,store,service,responsible])
        workbook.save(filepath)
    else:
        print("hata")
        tkinter.messagebox.showwarning(title="Error",message="Lutfen gerekli bilgileri doldurunuz")

    # print("First Name = ",company,"\nLast Name = ",store,"\nDurum = ",service,"\nResponsible",responsible)
window = Tk()
window.title("SERVIS TAKIP")

frame = Frame(window)
frame.pack()

service_info_frame = LabelFrame(frame,text="Servis Bilgileri")
service_info_frame.grid(row= 0 , column=0,padx=20,pady=20)

company_name_label = Label(service_info_frame, text="Company")
company_name_label.grid(row=0, column=0)
store_name_label = Label(service_info_frame, text="Store")
store_name_label.grid(row=0, column=1)

company_name_entry = Entry(service_info_frame)
store_name_entry = Entry(service_info_frame)
company_name_entry.grid(row=1, column=0)
store_name_entry.grid(row=1, column=1)


title_label = Label(service_info_frame, text="Title")
title_combobox = Combobox(service_info_frame,values=["Onaylandi","Devam Ediyor","Tamamlandi"])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)


# age_label = Label(service_info_frame, text="Age")
# age_spinbox = Spinbox(service_info_frame)
# age_label.grid(row=2,column=0)
# age_spinbox.grid(row=3,column=0)
responsible_label = Label(service_info_frame, text="Responsible")
responsible_label.grid(row=2, column=1)

responsible_entry = Entry(service_info_frame)
responsible_entry.grid(row=3,column=1)

notionality_label = Label(service_info_frame,text="notionality")
notionality_conbobox = Combobox(service_info_frame, value=["Africa","antartica","asia"])
notionality_label.grid(row=2,column=0)
notionality_conbobox.grid(row=3,column=0)


for  widget  in service_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#saving course info
courses_frame = LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)


registered_label = Label(courses_frame,text="Registered Status")
registered_check = Checkbutton(courses_frame,text="Curretly Registered")
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

#button
button = Button(frame,text="ender data", command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=20)

window.mainloop()
