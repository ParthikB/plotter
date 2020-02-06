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


# Initializing few Constants
LARGE_FONT = ('Verdana', 12)

f = Figure(figsize=(5, 5), dpi=100)
ax1 = f.add_subplot(111)


# Main GUI Base-Class
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


# Helper Class that carries various commands.
class Command:

	# Update the graph with every new selection
	def update_graph(self, plot_type, plot_val_x, plot_val_y):
		ax1.clear() # clears out the previous data on the graph so that it doesn't get rendered again
		
		# Plotting the graph according the the type of plot
		if plot_type == 'line':
			# print('Plotting line')
			ax1.plot(dataframe[plot_val_x], dataframe[plot_val_y])
		elif plot_type == 'scatter':
			# print('Plotting scatter')
			ax1.scatter(dataframe[plot_val_x], dataframe[plot_val_y])
		
		ax1.grid(1)
		ax1.set_xlabel(plot_val_x)
		ax1.set_ylabel(plot_val_y)
		
		# Rendering the graph onto the GUI
		canvas.draw()


	# Browses the file on the local machine
	def browse_file(self, root):

		root.filename =  filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("csv files","*.csv"), ("all files", "*.*")))
		
		# Initializing some global variables that are needed afterward in the program
		global dataframe, feature_list, plot_val_x, plot_val_y
		
		dataframe = pd.read_csv(root.filename) # Reading the .csv dataset file
		
		# Creating a feature list of the columns of the dataset to be fed to the dropdown menu
		feature_list = []
		for col in dataframe.columns:
			feature_list.append(col)
		
		# Selecting the X-AXIS feature
		plot_val_x  = tk.StringVar()
		plot_val_x.set(feature_list[0]) # Setting the default value for the variable
		popupMenu_x = tk.OptionMenu(root, plot_val_x, *feature_list)
		popupMenu_x.pack()
		
		# Selecting the Y-AXIS feature
		plot_val_y  = tk.StringVar()
		plot_val_y.set(feature_list[0])
		popupMenu_y = tk.OptionMenu(root, plot_val_y, *feature_list)
		popupMenu_y.pack()

		# print(plot_val_x, plot_val_y)
		print('Dataframe loaded.')
		
		# Creating a Blank Canvas for the matplotlib graphs
		global canvas
		canvas = FigureCanvasTkAgg(f, root)
		canvas.get_tk_widget().pack(side=tk.RIGHT, fill='both', expand=True)
		print('Canvas created.')
		canvas.draw()

		toolbar = NavigationToolbar2Tk(canvas, root)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill='both', expand=True)



# The HOMEPAGE of the GUI
class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		

		label = tk.Label(self, 
						text='Now this is where it begins!', 
						font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		# the UPLOAD button
		button1 = ttk.Button(self, text='Upload',
							command=lambda: command.browse_file(self))
		button1.pack()


		# Options to select the PLOT TYPE
		radio1 = ttk.Radiobutton(self, 
								text='Line', 
								value='line',
								command=lambda: command.update_graph('line', plot_val_x.get(), plot_val_y.get()))
		radio1.pack(anchor='w')

		radio2 = ttk.Radiobutton(self, 
								text='Scatter', 
								value='scatter',
								command=lambda: command.update_graph('scatter', plot_val_x.get(), plot_val_y.get()))
		radio2.pack(anchor='w')




if __name__ == '__main__':
	
	command = Command()

	app = App()
	app.mainloop()