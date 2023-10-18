# DAA-TEST1-BSCS2

2. Analysis
THE INSERTION SORT
Starts iterating with the first element through the unsorted part of the array, considering one element at a time, starting from the second element (index 1). It compares the current element with the elements in the sorted part of the array, moving from right to left within the sorted subarray. If the current element is smaller than the element in the sorted part, it shifts the larger element to the right to make room for the current element. This process continues until the correct position for the current element is found within the sorted part. Once the correct position is determined, the current element is inserted into the sorted subarray at that position and it is repeated for all elements in the unsorted part,.

4. Comparison:
Best-case time complexity (Θ(n)): 
The best-case scenario occurs when the input array is already sorted or nearly sorted wherby it simply iterates through the elements once.
Average-case time complexity (Θ(n^2)): 
In the average case, the elements in the input array are in a random order. 
Worst-case time complexity (Θ(n^2)): 
The worst-case scenario occurs when the input array is sorted in reverse order. In this case, each element must be compared and potentially swapped with every element before it.

5. Practical Scenario:
Yes, Insertion Sort would be a good choice because itis efficient in the best-case scenario, which occurs when the input is already partially sorted or nearly sorted.






QUESTION 2

Linear search
Linear search is a simple search algorithm that checks every element in a list or array to find a specific value. It starts at the beginning of the list and examines each element in order until the target value is found or the entire list is searched.

Binary search
Binary search is a search algorithm that works on sorted data. It repeatedly divides the search interval in half and compares the target value with the middle element.

Merge sort
Merge Sort is a sorting algorithm that does the divide-and-conquer. It divides the list into smaller sublists, sorts them, and then merges the sorted sublists to produce the final sorted list.

Quick sort
Quick Sort also  follows the divide-and-conquer approach. It selects a "pivot" element and partitions the list into two sublists, one containing elements less than the pivot and the other containing elements greater than the pivot. 

PSEUDO CODE

function findMax(arr):
    max = arr[0]  // Initialize max to the first element of the array
    for i from 1 to length of arr - 1:
        if arr[i] > max:
            max = arr[i]
    return max


Complexity analysis
Time Complexity: O(n) 
Space Complexity: O(1) 




