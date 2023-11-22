
def update_data(mylocal, title_name_combobox,id):
    print(id, " " ,title_name_combobox.get())
    mylocal.update_one({"_id":id},{"$set":{"service":title_name_combobox.get()}})
 
    print("update_data")   
