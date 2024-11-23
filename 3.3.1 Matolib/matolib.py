import matplotlib.pyplot as mp

a=[1,2,3,4,5]

figure, axis = mp.subplots()

axis.plot(a,a, label='"a" array, plotted', c='r')  # Plot some data.

axis.scatter(a, a, label='"a" array, scattered')  # Plot some more data

axis.set_xlabel('x label')  # Add an x-label to the axes.

axis.set_ylabel('a values')  # Add a y-label to the axes.

axis.set_title("Plot vs Scatter")  # Add a title to the axes.

axis.legend()  # Add a legend

mp.show()


