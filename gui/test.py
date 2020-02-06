import tkinter as tk
from tkinter import filedialog
from tkinter import *

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import pandas as pd

def show(option):
	print(option)


def browse():
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
	global dataframe
	dataframe = pd.read_csv(root.filename)
	print('dataframe loaded.')


def plot(self, filename):
	f = Figure(figsize=(5, 5), dpi=100)
	ax1 = f.add_subplot(111)
	ax1.plot(dataframe.col1, dataframe.col2)
	ax1.grid(1)

	canvas = FigureCanvasTkAgg(f, self)
	canvas.draw()
	canvas.get_tk_widget().pack(side=tk.TOP, fill='both', expand=True)

	toolbar = NavigationToolbar2Tk(canvas, self)
	toolbar.update()
	canvas._tkcanvas.pack(side=tk.TOP, fill='both', expand=True)


root = tk.Tk()

button2 = tk.Button(root, text='Upload',
	command=lambda: browse())
button2.pack()


plot_type = tk.StringVar()
radio1 = tk.Radiobutton(root, 
						text='Line', 
						variable=plot_type, 
						value='line',
						command=lambda: show('line'))
radio1.pack(anchor='w')

radio2 = tk.Radiobutton(root, 
						text='Scatter', 
						variable=plot_type, 
						value='scatter',
						command=lambda: show('scatter'))
radio2.pack(anchor='w')


button = tk.Button(root, text='Plot',
	command=lambda: plot(root, dataframe))
button.pack()





root.mainloop()