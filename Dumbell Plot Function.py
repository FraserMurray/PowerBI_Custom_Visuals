import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# This is a user defined function which will create a Dumbell plot within power BI
# Column A represents the categories on the Y axis and Columns B and C are the two values which will be displayed as a dumbell on the X
# This function assumes that a percentage is shown along the x axis (Numerics ranging from 0-1 ideally)

# Note that each value you assign to the function must have single quotation marks between them.
#i.e dumbellplot('Assets','Assets Lost','Assets Recovered','Assets','Lost','Recovered')

def dumbellplot(columnA,columnB,columnC,x_header,y_header,y1_name,y2_name):

    filtered_dataset = dataset.dropna(subset=[columnB, columnC])

    a = filtered_dataset[columnA].astype(str)
    b = filtered_dataset[columnB]
    c = filtered_dataset[columnC]

    plt.figure(figsize=10,6)
    plt.scatter(b, a, color="darkblue", label=y1_name,marker='o',s=100)
    plt.scatter(c,a,color='teal',label=y2_name,marker='o', s=100)

    for var_y,var_x,var_z in zip(a,b,c):
        plt.plot([var_x, var_z],[var_y,var_y], color="black")

    plt.xlabel(x_header,fontsize = 14)
    plt.ylabel(y_header, fontsize = 12)
    plt.title(y1_name + " vs " + y2_name,fontsize = 18)

    plt.legend()

    plt.yticks(rotation = 45)

    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))

    plt.grid(visible=True, linestyle='-', color='lightgray', linewidth=0.8)

    plt.show()
    