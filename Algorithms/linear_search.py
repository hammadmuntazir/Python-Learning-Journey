def search(arr,x):
    n=len(arr)
    for i in range(0,n):
        if(arr[i]==x):
            return i
    return -1

if __name__ =="__main__":
    arr=[1,4,0,2,9]
    x=2

    result=search(arr,x)
    if(result==-1):
        print("Element not found in array")
    else:
        print("Element is present at index",result)
