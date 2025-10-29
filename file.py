# import pandas as pd

# df = pd.read_csv("data.csv")
# print(df)

# from itertools import pairwise

# num = [20.5,50.5,30.0,10.5,55.0,150.9,100.9,80.9,90.9,79.9,60.0]
# diff = [num[i+1] - num[i] for i in range(len(num) - 1)]
# max_diff = max(diff)
# min_diff = min(diff)
# print(max_diff)
# print(min_diff)

# a = diff.index(max_diff)
# print(a)



# num = [20.5, 50.5, 30.0, 10.5, 55.0, 150.9, 100.9, 80.9, 90.9, 79.9, 60.0]

# diff = [num[i+1] - num[i] for i in range(len(num) - 1)]

# max_diff = max(num)
# min_diff = min(diff)
# max_index = diff.index(max_diff)
# min_index = diff.index(min_diff)
# print(max(num))
# print(diff)
# print(f"Maximum:{max_diff} between {max_index} to {max_index+1}")


num = [20.5, 50.5, 30.0, 10.5, 55.0, 200.9, 60.9, 80.9, 70.9, 79.9, 60.0]

average = sum(num) / len(num)
print(average) - (average)
for number in num:
    print(f"for {number} {number - average}")

