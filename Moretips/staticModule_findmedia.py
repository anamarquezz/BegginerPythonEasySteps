import statistics

marks = [1, 6, 9, 23, 2]
print(f"Mean: {marks} :  {statistics.mean(marks)} ")
print(f"Median: {marks}: {statistics.median(marks)}")

marks1 = [1, 6, 9, 23, 2, 7]
print(f"Median_high: {marks1} : {statistics.median_high(marks1)} ")
print(f"Median_low: {marks1} : {statistics.median_low(marks1)} ")
print(f"variance: {marks1} : {statistics.variance(marks1)} ")
