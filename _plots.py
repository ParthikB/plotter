import pandas as pd
import matplotlib.pyplot as plt
from main import data

# Plotting Class
class Plot:

    # Parent Function that calls the required plotting function
    def plot(self, type, col1, col2):
        if type.lower() == 'scatter':
            self._scatter(col1, col2)
        elif type.lower() == 'line':
            self._line(col1, col2)
        elif type.lower() == 'bar':
            self._bar(col1, col2)

        self._labels(col1, col2)


    # Scatter Plot function
    def _scatter(self, col1, col2):
        plt.scatter(data[col1], data[col2])


    # Line Plot function
    def _line(self, col1, col2):
        plt.plot(data[col1], data[col2])


    def _bar(self, col1, col2):
        plt.bar(data[col1], data[col2])

    # Function to put labels on the plot
    def _labels(self, col1, col2):
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.title(f'{col1} v/s {col2}')
        plt.grid(1)
        plt.show()