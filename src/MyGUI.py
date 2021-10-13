
import tkinter as tk
import os

from MySearcher import MySearcher

query = ""

def getQuery():
    query = query_entry.get()
    parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = parent_path + "\dataset\dataset.txt"
    lexitron_path = parent_path + "\lexitron\lexitron.txt"
    my_searcher = MySearcher(dataset_path, lexitron_path)
    result = my_searcher.TFIDFSearch(query, 5)

    for res in result:
        print(res)

window = tk.Tk()
# Code to add widgets will go here...

tk.Label(window, 
         text="First Name").grid(row=0)
tk.Label(window, 
         text="Last Name").grid(row=1)

query_entry = tk.Entry(window)
e2 = tk.Entry(window)

query_entry.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(window, 
          text='Quit', 
          command=window.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(window, 
          text='Show', command=getQuery).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

window.mainloop()
