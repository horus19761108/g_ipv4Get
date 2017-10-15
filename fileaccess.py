# -*- coding: utf-8 -*-

import tkinter
import tkinter.filedialog

def read_file():
    tk = tkinter.Tk()
    tk.withdraw()  
    filename = tkinter.filedialog.askopenfilename()
    print(filename)

    with open (filename, 'r', encoding='utf8') as input:
        data = input.read()
        data = data.split("\n")

    return data

def file_view():
    list = read_file()
    print("読み込んだ行数 =",len(list))
    for i,l in enumerate(list):
        print(i+1,l)