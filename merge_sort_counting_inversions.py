# Use PyPy3 to get a congratulations because if you
# use python you will get time limit exceeded
def mergeSort(arr):
    inversion_count = 0
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        inversion_count += mergeSort(L)
 
        # Sorting the second half
        inversion_count += mergeSort(R)
        
        # Merge into one array
        inversion_count += merge(arr, L, R)
        
        return inversion_count
    else:
        return 0
        
def merge(arr, L, R):
    inversion_count = 0
    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            inversion_count += len(L) - i
        k += 1

    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    return inversion_count

def countInversions(arr):
    # Write your code here
    return mergeSort(arr)