import pandas as pd
import matplotlib.pyplot as plt

# Plotting Class
class Plot:
    def __init__(self, data):
        self.data = data

    # Parent Function that calls the required plotting function
    def plot(self, type, col1, col2):
        if type.lower() == 'scatter':
            self._scatter(col1, col2)
        elif type.lower() == 'line':
            self._line(col1, col2)
        elif type.lower() == 'bar':
            self._bar(col1, col2)

        self.__labels__(col1, col2)


    # Scatter Plot function
    def _scatter(self, col1, col2):
        plt.scatter(self.data[col1], self.data[col2])


    # Line Plot function
    def _line(self, col1, col2):
        plt.plot(self.data[col1], self.data[col2])


    def _bar(self, col1, col2):
        plt.bar(self.data[col1], self.data[col2])

    # Function to put labels on the plot
    def __labels__(self, col1, col2):
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.title(f'{col1} v/s {col2}')
        plt.grid(1)
        plt.show()


keys = Plot.__dict__.keys()
available_plots = [plot[1:] for plot in keys if plot[0]=='_' and plot[1]!='_'] 

# print(plots)
