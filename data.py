import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import update_data
def data(mylocal):
    window = Tk()
    window.title("SERVIS TAKIP")
    window.geometry("800x600") 
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
    
    title_name_label = Label(another_frame, text="Durum")
    title_name_label.grid(row=0,column=2)

    maid_name_label = Label(another_frame, text="MAID")
    maid_name_label.grid(row=0,column=3)

    responsible_name_label = Label(another_frame, text="RESPONSIBLE")
    responsible_name_label.grid(row=0, column=4)
    i = 1
    arr = []
    for data in mylocal.find({'service': 'ONAYLANDI'}):
    
        company_data_label = Label(another_frame, text=data['company'])
        company_data_label.grid(row=i, column=0)

        store_name_label = Label(another_frame, text=data['store'])
        store_name_label.grid(row=i,column=1)
        
        title_name_combobox = Combobox(another_frame, value=['ONAYLANDI','SERVISTE','TAMAMLANDI'])
        title_name_combobox.set(data['service'])
        title_name_combobox.grid(row=i,column=2)

        maid_name_label = Label(another_frame, text=data['maid'])
        maid_name_label.grid(row=i,column=3)

        responsible_name_label = Label(another_frame, text=data['responsible'])
        responsible_name_label.grid(row=i, column=4)

        arr.append([mylocal, title_name_combobox,data['_id']])

        button_data = Button(another_frame,text="UPDATE",command=lambda i = i: update_data.update_data(arr[i-1][0],arr[i-1][1],arr[i-1][2] ))
        button_data.grid(row=i,column=5)
        i += 1
    
    for  widget  in another_frame.winfo_children():
        widget.grid_configure(padx=10,pady=5)

      