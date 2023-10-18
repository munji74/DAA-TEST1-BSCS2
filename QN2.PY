def max(arr):
    if not arr:
        return None  # FOR empty arrays

    maxVal = arr[0]  #first element of the array
    for i in range(1, len(arr)):
        if arr[i] > maxVal:
            maxVal = arr[i]
    return maxVal

list = [
    [],               
    [10],             
    [6, 3, 10, 2, 6, 7], 
    [10, 20, 30, 40, 50, 60, 70], 
    [70, 60, 50, 40, 30, 20, 10],  
]

for i, lst in enumerate(list):
    maxVal = max(lst)
    if maxVal is not None:
        print(f"Case {i + 1}: {lst} and MaxVal= {maxVal}")
    else:
        print(f"Case {i + 1}: {lst} is an empty array")

