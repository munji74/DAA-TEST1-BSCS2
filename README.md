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


