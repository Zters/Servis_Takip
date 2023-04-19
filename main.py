import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import pymongo
from pymongo import *

uri="MONGOURL"
myclient = MongoClient(uri,tls=True,tlsAllowInvalidCertificates=True)
mydb = myclient["SERVIS"]
mylocal = mydb["DATA"]
def enter_data():
    company = company_name_entry.get()
    store = store_name_entry.get()
    service = title_combobox.get()
    responsible = responsible_entry.get()
    mydata = {"company": company,"store": store, "service": service,"responsible": responsible}
    x = mylocal.insert_one(mydata)
    print(x.inserted_id)
def data():
    window = Tk()
    window.title("SERVIS TAKIP")

    frame = Frame(window)
    frame.pack()

    service_info_frame = LabelFrame(frame, text="Servis Bilgileri")
    service_info_frame.grid(row=0, column=0,padx=20,pady=20)
# FOR KULLANILARAK DATALAR CEKILIP DEF DATA GIRILECEK
    
    for data in mylocal.find({},{"_id":0}):
        company_name_label = Label(service_info_frame, text="COMPANY")
        company_name_label.grid(row=0,column=0)
        
        store_name_label = Label(service_info_frame, text="STRORE")
        store_name_label.grid(row=0,column=1)
        
        title_name_label = Label(service_info_frame, text="TITLE")
        title_name_label.grid(row=0,column=2)

        maid_name_label = Label(service_info_frame, text="MAID")
        maid_name_label.grid(row=0,column=3)

        responsible_name_label = Label(service_info_frame, text="RESPONSIBLE")
        responsible_name_label.grid(row=0, column=4)
        
# ===========================================================================

        company_data_label = Label(service_info_frame, text="TEST")
        company_data_label.grid(row=1, column=0)

        store_data_label = Label(service_info_frame, text="TEST")
        store_data_label.grid(row=1, column=1)

        title_data_label = Label(service_info_frame, text="TEST")
        title_data_label.grid(row=1, column=2)

        maid_data_label = Label(service_info_frame, text="TEST")
        maid_data_label.grid(row=1, column=3)

        responsible_data_label = Label(service_info_frame, text="TEST")
        responsible_data_label.grid(row=1, column=4)

    
    for  widget  in service_info_frame.winfo_children():
        widget.grid_configure(padx=10,pady=5)
        

window = Tk()
window.title("SERVIS TAKIP")

frame = Frame(window)
frame.pack()

service_info_frame = LabelFrame(frame, text="Servis Bilgileri")
service_info_frame.grid(row=0, column=0,padx=20,pady=20)

company_name_label = Label(service_info_frame, text="Company")
company_name_label.grid(row=0, column=0)
store_name_label = Label(service_info_frame, text="Store")
store_name_label.grid(row=0, column=1)


company_name_entry = Entry(service_info_frame)
store_name_entry = Entry(service_info_frame)
company_name_entry.grid(row=1, column=0)
store_name_entry.grid(row=1, column=1)


title_label = Label(service_info_frame, text="Title")
title_combobox = Combobox(service_info_frame,value=["1","2","3"])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)


responsible_label = Label(service_info_frame, text="Responsible")
responsible_label.grid(row=2,column=1)

responsible_entry = Entry(service_info_frame)
responsible_entry.grid(row=3,column=1)


notionality_label = Label(service_info_frame,text="Maid")
notionality_conbobox = Combobox(service_info_frame, value=["Africa","antartica","asia"])
notionality_label.grid(row=2,column=0)
notionality_conbobox.grid(row=3,column=0)


# for  widget  in service_info_frame.winfo_children():
#     widget.grid_configure(padx=10,pady=5)


#button
button = Button(frame,text="enter",command=enter_data)
button.grid(row=2,column=0,sticky="news",padx=2,pady=2)
button = Button(frame,text="data",command=data)
button.grid(row=3,column=0,sticky="news",padx=2,pady=2)

window.mainloop()
