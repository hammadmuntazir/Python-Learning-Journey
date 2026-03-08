"""1. Two Loops
Outer loop (i): Current position jahan hum chhota element rakhna chahte hain

Inner loop (j): Baaki unsorted elements mein se minimum dhondta hai

2. min_index Variable
Minimum element ka index store karta hai

Initially current position ko maanta hai

Update hota hai jab chhota element milta hai

3. Swap Operation
python
arr[i], arr[min_index] = arr[min_index], arr[i]"""
def selectionSort(arr):
    n=len(arr)
    # outer loop traverse karta hai array ke har element ko
    for i in range(n):
        min_index=i
    #inner loop compare karta hai current element se baaki unsorted elements ko
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        # swap karta hai current element ko minimum element ke saath
        arr[i],arr[min_index]=arr[min_index],arr[i]
# Driver code
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print(f"Original array: {arr}")
    selectionSort(arr)
    print(f"Sorted array: {arr}")
