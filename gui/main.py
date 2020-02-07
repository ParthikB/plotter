import matplotlib
matplotlib.use('TkAgg')

from matplotlib import style
# style.use('ggplot')
style.use('seaborn')


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
import tkinter.ttk as ttk

import pandas as pd


# Initializing few Constants
LARGE_FONT = ('Verdana', 12)
BACKGROUND_COLOR = '#42f498'


f = Figure(figsize=(15, 5), dpi=100)
ax1 = f.add_subplot(111)



# Main GUI Base-Class
class App(tk.Tk):

    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)

        # tk.Tk.iconbitmap(self, default='path_to_icon.ico')
        tk.Tk.wm_title(self, 'Quick Plotter')

        container = tk.Frame(self, 
                             bg=BACKGROUND_COLOR)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}
        


        for F in [StartPage]:
            frame = F(container, self)      # Parent, Controller
            self.frames[F] = frame
            # frame.grid(row=0, column=0, sticky='ew')
            frame.pack()

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
    def browse_file(self, parent):

        # S = ttk.Style()
        # S.configure('Wild.TRadioButton',
        #     background = BACKGROUND_COLOR)

        parent.filename =  tk.filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("csv files","*.csv"), ("all files", "*.*")))
        
        # Initializing some global variables that are needed afterward in the program
        global dataframe, feature_list, plot_val_x, plot_val_y
        
        dataframe = pd.read_csv(parent.filename) # Reading the .csv dataset file
        
        # Creating a feature list of the columns of the dataset to be fed to the dropdown menu
        feature_list = []
        for col in dataframe.columns:
            feature_list.append(col)

#####################################################################################################################################
        
        INFO = tk.Frame(parent, bg=BACKGROUND_COLOR)


        
        FEATURES = tk.Frame(INFO, bg=BACKGROUND_COLOR)

        tk.Label(FEATURES, text='Features :', bg=BACKGROUND_COLOR).grid(row=0, columnspan=2)

        # Selecting the X-AXIS feature
        plot_val_x  = tk.StringVar()
        plot_val_x.set(feature_list[0]) # Setting the default value for the variable
        tk.Label(FEATURES, text='X-Axis :', bg=BACKGROUND_COLOR).grid(row=1, column=0)
        popupMenu_x = tk.OptionMenu(FEATURES, plot_val_x, command=lambda x: command.update_graph('line', plot_val_x.get(), plot_val_y.get()), *feature_list).grid(row=1, column=1)
        
        # Selecting the Y-AXIS feature
        plot_val_y  = tk.StringVar()
        plot_val_y.set(feature_list[0])
        tk.Label(FEATURES, text='Y-Axis :', bg=BACKGROUND_COLOR).grid(row=2, column=0)
        popupMenu_y = tk.OptionMenu(FEATURES, plot_val_y, command=lambda x: command.update_graph('line', plot_val_x.get(), plot_val_y.get()), *feature_list).grid(row=2, column=1)
        
        FEATURES.pack(pady=30)


        OPTIONS = tk.Frame(INFO, bg=BACKGROUND_COLOR)
        
        s = ttk.Style()                     # Creating style element
        s.configure('Wild.TRadiobutton',    # First argument is the name of style. Needs to end with: .TRadiobutton
                background=BACKGROUND_COLOR,             # Setting background to our specified color above
                foreground='black')      
        

        tk.Label(OPTIONS, text='Plot Type :', bg=BACKGROUND_COLOR).grid(row=0)

        # Options to select the PLOT TYPE
        button1 = ttk.Radiobutton(OPTIONS, 
                        text='Line', 
                        value='line',
                        # style='Wild.TRadioButton',
                        command=lambda: command.update_graph('line', plot_val_x.get(), plot_val_y.get()))
        # button1.configure(background =BACKGROUND_COLOR)
        button1.grid(row=1, sticky='w')
        
        button2 = ttk.Radiobutton(OPTIONS, 
                        text='Scatter', 
                        value='scatter',
                        # style='Wild.TRadioButton',
                        command=lambda: command.update_graph('scatter', plot_val_x.get(), plot_val_y.get()))
        # button2.configure(background =BACKGROUND_COLOR)
        button2.grid(row=2, sticky='w')

        OPTIONS.pack(pady=30)



        INFO.pack(side='left', padx=15)
#####################################################################################################################################


#####################################################################################################################################
        GRAPH = tk.Frame(parent)

        # Creating a Blank Canvas for the matplotlib graphs
        global canvas
        canvas = FigureCanvasTkAgg(f, parent)
        canvas.get_tk_widget().pack(side=tk.LEFT, fill='both', expand=True)
        print('Canvas created.')
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, parent)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill='both', expand=True)


        GRAPH.pack(side='right', fill='both', expand=True)
#####################################################################################################################################



# The HOMEPAGE of the GUI
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        label = tk.Label(parent, 
                        text='It begins here!', 
                        font=LARGE_FONT,
                        bg=BACKGROUND_COLOR).pack()

        # the UPLOAD button
        button1 = ttk.Button(parent, text='Upload',
                            command=lambda: command.browse_file(parent)).pack()




if __name__ == '__main__':
    
    command = Command()

    app = App()
    app.mainloop()
