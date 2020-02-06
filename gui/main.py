import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use('TkAgg')

from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


LARGE_FONT = ('Verdana', 12)


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

		for F in (StartPage, PageOne):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='ew')

		self.show_frame(StartPage)


	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# def upload(name):
# 	print(f'{name} > File uploaded!')

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self, text='Now this is where it starts!', font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text='Upload',
			command=lambda: controller.show_frame(PageOne))
		button1.pack()

		

class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text='Page two', font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text='Home',
			command=lambda: controller.show_frame(StartPage))
		button1.pack()
		
		f = Figure(figsize=(5, 5), dpi=100)
		ax1 = f.add_subplot(111)
		ax1.plot(range(10))

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill='both', expand=True)

		toolbar = NavigationToolbar2Tk(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill='both', expand=True)

app = App()
app.mainloop()