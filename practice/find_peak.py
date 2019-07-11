
def find_1d_peak(arr, low, high):
    if len(arr) == 0:
        return None

    if low == high:
        return arr[low]

    mid = (low + high) // 2
    
    if (mid + 1) <= high and arr[mid] < arr[mid + 1]:
        return find_1d_peak(arr, mid + 1, high)
    elif (mid - 1) >= low and arr[mid] < arr[mid - 1]:
        return find_1d_peak(arr, low, mid)
    else:
       return arr[mid]

def find_2d_peak(arr, low, high):
    pass
    
if __name__ == '__main__':
    #arr = [9, 1, 2, 4, 7, 8, 5]
    arr = [1, 2, 3, 1]
    print arr
    print "peak is ", find_1d_peak(arr, 0, len(arr) - 1)
