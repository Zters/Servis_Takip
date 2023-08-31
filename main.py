import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import pymongo
from pymongo import *

uri="buraya url yazılacak"
myclient = MongoClient(uri,tls=True,tlsAllowInvalidCertificates=True)
mydb = myclient["SERVIS"]
mylocal = mydb["DATA"]
def enter_data():
    company = company_name_entry.get()
    store = store_name_entry.get()
    service = title_combobox.get()
    maid = notionality_conbobox.get()
    responsible = responsible_entry.get()
    mydata = {"company": company,"store": store, "service": service,"responsible": responsible,"maid":maid}
    x = mylocal.insert_one(mydata)
    print(x.inserted_id)

def data():
    window = Tk()
    window.title("SERVIS TAKIP")
    
    frame = Frame(window)
    frame.pack(fill=BOTH, expand=1)
    
    service_info_frame = LabelFrame(frame, text="Servis Bilgileri")
    service_info_frame.pack()
    
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    another_frame = Frame(canvas)
    another_frame.pack()

    canvas.create_window((0,0), window=another_frame, anchor=NW)

    company_name_label = Label(another_frame, text="COMPANY")
    company_name_label.grid(row=0,column=0)
    
    store_name_label = Label(another_frame, text="STRORE")
    store_name_label.grid(row=0,column=1)
    
    title_name_label = Label(another_frame, text="TITLE")
    title_name_label.grid(row=0,column=2)

    maid_name_label = Label(another_frame, text="MAID")
    maid_name_label.grid(row=0,column=3)

    responsible_name_label = Label(another_frame, text="RESPONSIBLE")
    responsible_name_label.grid(row=0, column=4)
    i = 1


    for data in mylocal.find({},{"_id":0}):
    
        company_data_label = Label(another_frame, text=data['company'])
        company_data_label.grid(row=i, column=0)

        store_name_label = Label(another_frame, text=data['store'])
        store_name_label.grid(row=i,column=1)
        
        title_name_label = Label(another_frame, text=data['service'])
        title_name_label.grid(row=i,column=2)

        maid_name_label = Label(another_frame, text=data['maid'])
        maid_name_label.grid(row=i,column=3)

        responsible_name_label = Label(another_frame, text=data['responsible'])
        responsible_name_label.grid(row=i, column=4)

        i += 1

    another_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    for  widget  in another_frame.winfo_children():
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