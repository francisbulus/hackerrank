def minDiff(arr,n,k): 
    result = +2147483647

    # Sorting the array. 
    arr.sort()    
    # Find minimum value among 
    # all K size subarray. 
    for i in range(n-k+1): 
        result = int(min(result, arr[i+k-1] - arr[i])) 
   
    return result 