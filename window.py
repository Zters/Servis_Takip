import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import data
import enter_data
import on_service
import off_service
def window(mylocal):
    window = Tk()
    window.title("SERVIS TAKIP")
    window.geometry("800x600") 
    
    frame = Frame(window)
    frame.pack()
    button_frame = Frame(window)
    button_frame.pack(fill=BOTH,padx=20,pady=20)
    
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
    title_combobox = Combobox(service_info_frame,value=['ONAYLANDI','SERVISTE','TAMAMLANDI'])
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
    button = Button(frame, text="SERVIS EKLE", command=lambda: enter_data.enter_data(
        company_name_entry,
        store_name_entry,
        title_combobox,
        responsible_entry,
        notionality_conbobox,
        mylocal
    ))  # Increase width and height as per your requirement
    button.grid(row=2,column=0,sticky="news",padx=2,pady=2,)

    button = Button(frame,text="SERVISLER",command=lambda: data.data(mylocal))
    button.grid(row=3,column=0,sticky="news",padx=2,pady=2)


    button = Button(button_frame,text="SERVISTE OLANLAR",command=lambda: on_service.on_service(mylocal))
    button.pack(side=LEFT,fill=BOTH,expand=1,padx=10,pady=2)

    # button.grid(row=4,column=0,sticky="news",padx=2,pady=2)
    
    button = Button(button_frame,text="SERVISI TAMAMLANANLAR",command=lambda: off_service.off_service(mylocal))
    button.pack(side=RIGHT,fill=BOTH,expand=1,padx=10,pady=2)
    # button.grid(row=4,column=1,sticky="news",padx=2,pady=2)
    window.mainloop()