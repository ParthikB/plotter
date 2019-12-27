# Importing the Plotting Class
from plots import *

# Function to take the column name from the user
def input_col_name(idx):
    col_name = input(f'Enter {idx} col      : ')
    if col_name not in columns:
        print('Invalid Columns. Try again.\n')
        col_name = input_col_name(idx)
    return col_name


# Reading the data file
data = pd.read_csv('datasets/BTC_USD.csv')
columns = [col for col in data.columns]


if __name__ == '__main__':

    # Printing the details
    print(
        f'''
        Available Columns : {columns}
        Available Plots   : line, scatter, bar
        '''
    )

    # Taking INPUTS from the user
    col1 = input_col_name('x')
    col2 = input_col_name('y')
    type = input('Enter Plot type  : ')

    # PLOTTING
    # try:
    plot = Plot()
    plot.plot(type, col1, col2)

    # except:
    #     print("\nSomething's not cool!")