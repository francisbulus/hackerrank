def pairs(k, arr):
    # This satisfies the constraint of each integer being unique unique
    unique_nums = set(arr)
    # This keeps track of the number of element pairs
    count = 0

    for num in arr:
        '''
        Get what would be the subtrahend if you were subtracting the upper element from the smaller in a pair, and 
        check to see if it's present in the unique set
        '''
        subtrahend = num - k
        count = count + 1 if subtrahend in unique_nums else count

    return count
