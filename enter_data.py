
def enter_data(company_name_entry,store_name_entry,title_combobox,responsible_entry,notionality_conbobox,mylocal):
    company = company_name_entry.get()
    store = store_name_entry.get()
    service = title_combobox.get()
    maid = notionality_conbobox.get()
    responsible = responsible_entry.get()
    mydata = {"company": company,"store": store, "service": service,"responsible": responsible,"maid":maid}
    x = mylocal.insert_one(mydata)
    print(x.inserted_id)