import os,shutil
import tkinter as tk
from tkinter  import ttk
dict_extensions={
 'audio_extensions':('.mp3','.m4a','wav','flac'),
 'videos_extensions':('.mp4','.mkv','.MKV','.flv','.mpeg'),
 'image_extensions':('.jpeg','.png','.jpg','.gif'),
 'documents_extension':('.zip','.doc','.docx','.pdf','.pptx','.htm','.html','.ppt','.txt','.sql'),
}

def file_finder(folder_path,file_extension):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files
def move_file(folder_path):
    fileiter=os.walk(folder_path)
    for current_path,folder_names,file_names in fileiter:
        if current_path!=folder_path:
            for files in file_names:
                files_path=os.path.join(current_path,files)
                shutil.move(files_path,folder_path)
    return ''

def enter_func():
    folderpath=path_var.get()
    if checkbtn_var.get()==1:
        move_file(folderpath)
        for extension_type,extension_tuple in dict_extensions.items():
            folder_name=extension_type.split("_")[0] + '_files'
            folder_path = os.path.join(folderpath,folder_name)
            if os.path.exists(folder_path):
                pass
            else:
                os.mkdir(folder_path)
            for item in (file_finder(folderpath,extension_tuple)):
                item_path=os.path.join(folderpath,item)
                item_new_path=os.path.join(folder_path,item)
                shutil.move(item_path,item_new_path)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
        list_folder=os.listdir(folderpath)
        for folder in list_folder:
            folder_path=os.path.join(folderpath,folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
            else:
                pass
        path_entry_box.delete(0,tk.END)
        path_label.configure(foreground='Blue')



#starter code 
window=tk.Tk()
window.title('File Sorter')
#create label
title_label=ttk.Label(window,text='Welcome to file sorter ')
title_label.grid(row=0,column=0)
path_label=ttk.Label(window,text='Enter your path : ')
path_label.grid(row=1,column=0,sticky=tk.W)
# path_label.(side='top')
# create entry box
path_var=tk.StringVar() 
path_entry_box=ttk.Entry(window,width=16,textvariable=path_var)
path_entry_box.grid(row=1,column=1)
path_entry_box.focus()

#check button
checkbtn_var=tk.IntVar()
check_button=ttk.Checkbutton(window,text="If the path is successfully enterd ",variable=checkbtn_var)
check_button.grid(row=2,columnspan=3)

#create Button


enter_button=ttk.Button(window,text='Enter',command=enter_func)
enter_button.grid(row=3,column=0,sticky=tk.W)
window.mainloop()