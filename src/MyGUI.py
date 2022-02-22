# -*- coding: utf-8 -*-

from tkinter import *
import tkinter as tk
from tkinter.font import Font
import os

from MySearcher import MySearcher
from CustomText import CustomText

def search():
    output_box.delete('1.0', tk.END)
    query_text = query_entry.get()
    genre_text = genre.get()
    k = int(k_option.get())
    if genre_text in ["None", "Both"]:
        genre_text = None
    output_text = ""
    if not query_text == "":
        parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dataset_path = parent_path + "/dataset/dataset.txt"
        lexitron_path = parent_path + "/lexitron/lexitron.txt"
        my_searcher = MySearcher(dataset_path, lexitron_path)
        print('query: ', query_text)
        print('genre: ', genre_text)
        print('k: ', k)
        result = my_searcher.TFIDFSearch(query_text, k, genre=genre_text)
        if not result:
            output_text = '\"{}\"\nSorry, Not Found!!!'.format(query_text)
        else:
            output_text += '{} Result(s) found: \"{}\"\n\n'.format(len(result), query_text)
            for idx, item in enumerate(result):
                output_text += '[{}] {}\n\n'.format((idx + 1), item.printOutputFormat())
                print(item)
    else:
        output_text = "Please enter your keyword first!!!"
    output_box.insert(tk.END, output_text)
    scrollbar.grid(row=7, column=2, sticky='ns')
    output_box.tag_configure("yellow", foreground="black", background="yellow")
    output_box.highlight_pattern(query_text, "yellow")


if __name__ == '__main__':

    window = tk.Tk()
    thai_font = Font(family="TH Baijam", size=16)
    window.title("Search Engine for Thai Traditional Songs")
    # window.geometry("720x480")

    genre = StringVar(window)
    genre.set(None)

    w = tk.Label(window, text='Traditional Thai Song Search Engine', font="50") 
    w.grid(row=0, columnspan=2, pady=15)

    tk.Label(window, text="Keyword:").grid(row=1, pady=8)
    query_entry = tk.Entry(window, font=thai_font)
    query_entry.grid(row=1, column=1, pady=8)

    tk.Label(window, text="Type:").grid(row=2)
    type_1 = tk.Radiobutton(window, text="Both", variable=genre, value="Both")
    type_1.deselect()
    type_1.grid(row=2, column=1)
    type_2 = tk.Radiobutton(window, text="เพลงไทยเดิม", variable=genre, value="เพลงไทยเดิม")
    type_2.deselect()
    type_2.grid(row=3, column=1)
    type_3 = tk.Radiobutton(window, text="เพลงสุนทราภรณ์", variable=genre, value="เพลงสุนทราภรณ์")
    type_3.deselect()
    type_3.grid(row=4, column=1)

    k_list = [i for i in range(1, 11)]
    k_option = StringVar(window)
    k_option.set(k_list[0]) # default value

    tk.Label(window, text="Max Result:").grid(row=5, pady=8)
    k_dropdown = OptionMenu(window, k_option, *k_list)
    k_dropdown.grid(row=5, column=1, pady=10)

    tk.Button(window, text='Quit', command=window.quit).grid(row=6, column=0, pady=8)
    tk.Button(window, text='Search', command=search).grid(row=6, column=1, pady=8)

    output_box = CustomText(window)
    scrollbar = tk.Scrollbar(window, orient='vertical', command=output_box.yview)
    output_box.configure(height=20, width=60, font=thai_font, yscrollcommand=scrollbar.set)
    output_box.configure()
    output_box.grid(row=7, columnspan=2)

    window.mainloop()
