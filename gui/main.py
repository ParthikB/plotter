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

	def update_graph(self, plot_type, plot_val_x, plot_val_y):
		ax1.clear()
		if plot_type == 'line':
			print('plotting line')
			ax1.plot(dataframe[plot_val_x], dataframe[plot_val_y])
		elif plot_type == 'scatter':
			print('plotting scatter')
			ax1.scatter(dataframe[plot_val_x], dataframe[plot_val_y])
		ax1.grid(1)
		ax1.set_xlabel(plot_val_x)
		ax1.set_ylabel(plot_val_y)
		
		canvas.draw()


	def browse_file(self, root):
		root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
		global dataframe, feature_list, plot_val_x, plot_val_y
		
		dataframe = pd.read_csv(root.filename)
		
		feature_list = []
		for col in dataframe.columns:
			feature_list.append(col)
		
		plot_val_x  = tk.StringVar()
		plot_val_x.set(feature_list[0])
		popupMenu_x = tk.OptionMenu(root, plot_val_x, *feature_list)
		popupMenu_x.pack()
		# plot_val_x  = plot_val_x.get()
		
		plot_val_y  = tk.StringVar()
		plot_val_y.set(feature_list[0])
		popupMenu_y = tk.OptionMenu(root, plot_val_y, *feature_list)
		popupMenu_y.pack()
		# plot_val_y  = plot_val_y.get()

		print(plot_val_x, plot_val_y)
		# print(plot_val_x.get(), plot_val_y.get())
		print('dataframe loaded.')
		# print(plot_val_x.get(), plot_val_y.get())


	def plot(self, root, filename, plot_type, plot_val_x, plot_val_y):
		print('*****************************************')
		print("********************", plot_val_x, plot_val_y)
		ax1.clear()
		if plot_type == 'line':
			print('plotting line')
			ax1.plot(dataframe[plot_val_x], dataframe[plot_val_y])
		elif plot_type == 'scatter':
			print('plotting scatter')
			ax1.scatter(dataframe[plot_val_x], dataframe[plot_val_y])
		ax1.grid(1)
		ax1.set_xlabel(plot_val_x)
		ax1.set_ylabel(plot_val_y)

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

		# feature_list = ['none']		
		# plot_vals = tk.StringVar()
		# popupMenu = tk.OptionMenu(self, plot_vals, *feature_list)
		# popupMenu.pack()

		global plot_type
		plot_type = tk.StringVar()
		radio1 = ttk.Radiobutton(self, 
								text='Line', 
								variable=plot_type, 
								value='line',
								command=lambda: command.update_graph('line', plot_val_x.get(), plot_val_y.get()))
		radio1.pack(anchor='w')

		radio2 = ttk.Radiobutton(self, 
								text='Scatter', 
								variable=plot_type, 
								value='scatter',
								command=lambda: command.update_graph('scatter', plot_val_x.get(), plot_val_y.get()))
		radio2.pack(anchor='w')


		button2 = ttk.Button(self, text='Plot',
							command=lambda: command.plot(self, dataframe, plot_type.get(), plot_val_x.get(), plot_val_y.get()))
		button2.pack()



command = Command()

app = App()
app.mainloop()