import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
from pymongo import *

import window

uri="URL EKLENECEK"
myclient = MongoClient(uri,tls=True,tlsAllowInvalidCertificates=True)
mydb = myclient["SERVIS"]
mylocal = mydb["DATA"]

if __name__ == "__main__":
    window.window(mylocal)