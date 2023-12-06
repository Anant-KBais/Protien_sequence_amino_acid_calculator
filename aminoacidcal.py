import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
from matplotlib import pyplot as plt
root = tk.Tk()
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    # function to open file
def open_file():
    global file
    file = filedialog.askopenfile(initialdir="C:/Users/ANANT KRISN BAIS/Desktop/", filetypes=(
        ("PDB file", "*.pdb"), ("All files", "*.*"), ("All documents file", "*.doc")),
                                    title="Choose a protein data file")
    lines = open(file.name, "r")

    t = scrolledtext.ScrolledText(root)

    prev = 0
    for line in lines:

        if line.startswith("ATOM"):

                column = line.split(" ")
                while column.count('') != 0:
                    column.remove('')

                if prev != column[5]:
                    prev = column[5]
                    t.insert(index='current', chars=line)
                    t.place(x=600,y=100)
    lines.close()


# function to calculate percentage of amino acid
def calculator(res):
    lines = open(file.name, "r")
    prev = 0
    count = 0
    total = 0

    for line in lines:
        if line.startswith("ATOM"):
            column = line.split(" ")
            while column.count('') != 0:
                column.remove('')

            if prev != column[5]:
                total += 1
                prev = column[5]
                if column[3] == res:
                    count += 1
    percent = (count / total) * 100
    lines.close()
    return percent, total


# calculate percentage of all amino acid
def t_perc():
    residue = ['GLY', 'PRO', 'ALA', 'VAL', 'LEU',
                'ILE', 'MET', 'CYS', 'PHE', 'TYR',
                'TRP', 'HIS', 'LYS', 'ARG', 'GLN',
                'ASN', 'GLU', 'ASP', 'SER', 'THR']
    total_percent = 0
    x = 0
    for res in residue:
        percent,total = calculator(res)
        tk.Label(text=res[0:4] + "  :     " + str(percent)[0:5] + "%",font=8).place(x=75,y=100+x)
        x += 25
        total_percent += percent
        graph_res[res]= percent
    tk.Label(text="total amino acids : "+str(total),font=8).place(x=350,y=200)


# calculate percentage of specific amino acid
def sp_perc():
    residue = res.get()
    percent,total = calculator(residue)
    tk.Label(text=residue+" :  "  +str(percent)[0:5]+ "%"+ "    ", font=12).place(x=650,y=30)

# create graph
graph_res={}
def graph_it():
    plt.title("Amino acid composition")
    plt.bar(graph_res.keys(), graph_res.values())
    plt.ylabel("Percentage")
    plt.xlabel("Amino acids")

    x = -0.4
    for y in graph_res.values():
        plt.text(x, y, str(y)[0:4]+"%")
        x += 1
    plt.show()


tk.Label(root, text="Amino acid percentage calculator", font=32, bg ="pink").grid(column=20, row=2)

# add menu to add load file
menu = tk.Menu(root)
menu.add_command(label="Load Database", command=open_file)

# calculate buttons
scal = tk.Button(root, text="Calculate selected Percentage",font=8, command=sp_perc)
scal.place(x=350, y=30)

cal = tk.Button(root, text="Calculate total Percentage",font=8, command=t_perc)
cal.place(x=350, y=70)

# graph button
graph = tk.Button(root, text="Create graph",font=8, command=graph_it)
graph.place(x=350,y=110)

# enter the amino acid
tk.Label(text="Enter the amino acid", font=16).grid(column=11, row=9)
res = tk.StringVar()
amino = ttk.Combobox(root, textvar=res)
amino['values'] = ['GLY', 'PRO', 'ALA', 'VAL', 'LEU',
                    'ILE', 'MET', 'CYS', 'PHE', 'TYR',
                    'TRP', 'HIS', 'LYS', 'ARG', 'GLN',
                    'ASN', 'GLU', 'ASP', 'SER', 'THR']
amino.grid(column=19, row=9)

# Creator button
from tkinter import messagebox as msg
def message():
    msg.showinfo("Created by anant","Anant Rocks!!")
tk.Button(root,text="Creator", command=message, font=12).place(x=350,y=550)

root.config(menu=menu)
root.title("Amino acid calculator")
root.mainloop()
