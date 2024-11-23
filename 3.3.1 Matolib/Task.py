import numpy as np
from SelectionSort import selection_sort_numbers
import time
import matplotlib.pyplot as mp


start_time1 = time.perf_counter()
selection_sort_numbers(3)
end_time1 = time.perf_counter()
execution_time1 = end_time1 - start_time1


start_time2 = time.perf_counter()
selection_sort_numbers(30)
end_time2 = time.perf_counter()
execution_time2 = end_time2 - start_time2


start_time3 = time.perf_counter()
selection_sort_numbers(300)
end_time3 = time.perf_counter()
execution_time3 = end_time3 - start_time3

values = [4.3459003791213036e-05, 0.00010604201816022396, 0.007259540958330035]


print("Execution times we will plot are are:", execution_time1,execution_time2,execution_time3)

mp.xlabel("Time")
mp.ylabel("Time")
mp.title("Scatter Plot of Given Execution time")

x = range(1, len(values) + 1)
mp.scatter(x,values)

mp.show()