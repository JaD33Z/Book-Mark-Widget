import os
from datetime import datetime
import json
import subprocess
from tkinter import *
from tkinter import messagebox
from tkmacosx import Button


############## Book_Mark Dev_Tool app #################

## main box for app window

window = Tk()
window.title("Book_Mark-Dev_Tool")
window.geometry('480x280')
window.configure(bg='gray4')
current_time = datetime.now()


## generated files to store info

json_file = "marks.json"
paste_file = 'paste_box.txt'
urls_file = "urls.txt"



# ---------------------------- Window Layout ----------------------------------------- #


name_lbl = Label(window, text="Project Name", bg='gray4', fg='green2')
name_lbl.grid(column=0, row=0, padx=10)
name_entry = Entry(window, width=25, bg='pale green', borderwidth=4, relief=SUNKEN)
name_entry.grid(column=1, row=0, padx=2, pady=8, ipady=3)

path_lbl = Label(window, text="File Path", bg='gray4', fg='green2')
path_lbl.grid(column=0, row=1, padx=10)
path_entry = Entry(window, width=25, bg='pale green', borderwidth=4, relief=SUNKEN)
path_entry.grid(column=1, row=1, padx=2, pady=8, ipady=3)

ref_lbl = Label(window, text="Reference URL", bg='gray4', fg='green2')
ref_lbl.grid(column=0, row=2)
ref_entry = Entry(window, width=25, bg='pale green', borderwidth=4, relief=SUNKEN)
ref_entry.grid(column=1, row=2, padx=2, pady=8, ipady=3)




# ----------------------- Button Functions -------------------------------------- #


## saves entry info to json file ('marks.json')
## takes entered text in fields, turns into dictionary, stores in file


def save_bookmark():
    project = name_entry.get()
    path_save = path_entry.get()
    ref_mat = ref_entry.get()
    saved_spots = {
        project: {
            'project directory': path_save,
            'references': [ref_mat],
            'on': f"{current_time}",
        }
    }
    if len(project) == 0 or len(path_save) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open(json_file, "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            # create file if not exist
            with open(json_file, "w") as data_file:
                json.dump(saved_spots, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(saved_spots)
            with open(json_file, "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # clear text entry windows
            name_entry.delete(0, END)
            path_entry.delete(0, END)
            ref_entry.delete(0, END)




## 'Paste_Box' button
## opens up a text window to copy + paste/ use as a general "scratch pad"
## to store any useful lines or info you could use later
## saves it in ('paste_box.txt'), access anytime by pressing button


def grab_paste_box():
    if not os.path.exists(paste_file):
        with open(paste_file, 'a+') as file:
            file.write('')
    subprocess.run(['open', paste_file], check=True)




## 'Show_List' button, opens a text editor file window
## to view all your saved data. See recent project names,
## directory locations, and reference material
## urls associated with the projects you are currently working on.


def show_recent():
    if os.path.exists(json_file):
        subprocess.run(['open', json_file], check=True)
    else:
        messagebox.showinfo(title="Error", message="No Data File Found. You Must Save An Entry First!")




## 'Find' button, enter name of project you are looking for, case and space sensitive.
## Opens up alert window with all of the queried project's info.


def search_project():
    project = name_entry.get()
    try:
        with open(json_file) as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if project in data:
            name = project
            path = data[project]["project directory"]
            ref = data[project]["references"]
            when = data[project]["on"]
            messagebox.showinfo(title=name, message=f"Directory: {path}\nReferences: {ref}\nFrom: {when}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {project} exists."
                                                       f" Search is Case and Space sensitive!")



## 'Add URLS' button
## "references" key in your saved entries dictionary is now a list of values.
## Store multiple url locations for your reference materials.
## Enter the project name and append your additional web addresses.


def add_ref_urls():
    if os.path.exists(json_file):
        name = name_entry.get()
        url = ref_entry.get()
        with open(json_file, "r+") as f:
            obj = json.load(f)
            for i in obj:
                if i == name:
                    obj[i]["references"].append(url)
                    f.seek(0)
                    json.dump(obj, f, indent=4)

            name_entry.delete(0, END)
            path_entry.delete(0, END)
            ref_entry.delete(0, END)



## 'URLS' button
## opens text window with a list of tuples containing project names
## with their url links you were using as reference

def bring_ref_links():
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            url_list = [(i[0:], j["references"]) for i, j in data.items()]
            with open(urls_file, "w") as url_file:
                url_file.write(str(url_list))
            subprocess.run(['open', urls_file], check=True)
    else:
        messagebox.showinfo(title="Error", message="No Data File Found. You Must Save An Entry First!")



## 'Delete All' button
## deletes the ('marks.json') file
## clears all your saved entries, start over with an empty file.
## This does NOT delete your paste box file.


def delete_all():
    if os.path.exists(json_file):
        res = messagebox.askquestion(title='Clear File', message='This will delete your saved entries file, are you sure you want a new one?')
        if res == 'yes':
            os.remove(json_file)
        elif res == 'no':
            pass
    else:
        messagebox.showinfo(title="Error", message="No Data File Found. You Must Save An Entry First!")




# ------------------------------ Buttons ---------------------------------------------- #


save_btn = Button(window, text="Save",  command=save_bookmark, fg='black', bg='green2', borderless=True)
save_btn.grid(column=2, row=0)

paste_btn = Button(window, text="Paste_Box", command=grab_paste_box, fg='black', bg='green2', borderless=True)
paste_btn.grid(column=1, row=3, padx=10, pady=10)

show_btn = Button(window, text="Show_List", command=show_recent, fg='black', bg='green2', borderless=True)
show_btn.grid(column=2, row=3)

search_btn = Button(window, text="Find", command=search_project, fg='black', bg='green2', borderless=True)
search_btn.grid(column=2, row=1)

urls_btn = Button(window, text="URLS", command=bring_ref_links, fg='black', bg='green2', borderless=True)
urls_btn.grid(column=0, row=3)

add_more_urls_btn = Button(window, text="Add+ urls", command=add_ref_urls, fg='black', bg='green2', borderless=True)
add_more_urls_btn.grid(column=2, row=2)

del_btn = Button(window, text="Delete All", command=delete_all, fg='black', bg='green2', borderless=True)
del_btn.grid(column=1, row=4, pady=20, padx=20)

window.mainloop()

