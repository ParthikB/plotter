import matplotlib
matplotlib.use('TkAgg')

from matplotlib import style
style.use('ggplot')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import pandas as pd



LARGE_FONT = ('Verdana', 12)

f = Figure(figsize=(5, 5), dpi=100)
ax1 = f.add_subplot(111)

class Command:

	def update_graph(self, plot_type):
		ax1.clear()
		if plot_type == 'line':
			print('plotting line')
			ax1.plot(dataframe.col1, dataframe.col2)
		elif plot_type == 'scatter':
			print('plotting scatter')
			ax1.scatter(dataframe.col1, dataframe.col2)
		ax1.grid(1)

		canvas.draw()


	def browse_file(self, root):
		root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
		global dataframe
		dataframe = pd.read_csv(root.filename)
		print('dataframe loaded.')


	def plot(self, root, filename, plot_type):

		ax1.clear()
		if plot_type == 'line':
			print('plotting line')
			ax1.plot(dataframe.col1, dataframe.col2)
		elif plot_type == 'scatter':
			print('plotting scatter')
			ax1.scatter(dataframe.col1, dataframe.col2)
		ax1.grid(1)

		global canvas
		canvas = FigureCanvasTkAgg(f, root)
		canvas.get_tk_widget().pack(side=tk.RIGHT, fill='both', expand=True)
		print('Canvas created.')
		canvas.draw()

		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill='both', expand=True)
		



class App(tk.Tk):

	def __init__(self, *arg, **kwargs):
		tk.Tk.__init__(self, *arg, **kwargs)

		# tk.Tk.iconbitmap(self, default='path_to_icon.ico')
		tk.Tk.wm_title(self, 'Quick Plotter')

		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames={}

		for F in [StartPage]:
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='ew')

		self.show_frame(StartPage)


	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()





class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self, 
						text='Now this is where it starts!', 
						font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text='Upload',
							command=lambda: command.browse_file(self))
		button1.pack()


		global plot_type
		plot_type = tk.StringVar()
		radio1 = tk.Radiobutton(self, 
								text='Line', 
								variable=plot_type, 
								value='line',
								command=lambda: command.update_graph('line'))
		radio1.pack(anchor='w')

		radio2 = tk.Radiobutton(self, 
								text='Scatter', 
								variable=plot_type, 
								value='scatter',
								command=lambda: command.update_graph('scatter'))
		radio2.pack(anchor='w')


		button2 = ttk.Button(self, text='Plot',
							command=lambda: command.plot(self, dataframe, plot_type.get()))
		button2.pack()


command = Command()
app = App()
app.mainloop()