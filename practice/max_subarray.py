
def max_cross_array(arr, low, high):
    mid = (low + high) / 2

    left_low = mid
    left_max = 0
    left_sum = 0
    for i in range(mid, low - 1, -1):
        left_sum += arr[i]
        if left_sum > left_max:
            left_max = left_sum
            left_low = i
        
    right_high = mid + 1
    right_max = 0
    right_sum = 0
    for j in range(mid + 1, high + 1):
        right_sum += arr[j]
        if right_sum > right_max:
            right_max = right_sum
            right_high = j
     

    return left_low, right_high, (left_max + right_max)

def max_sub_array(arr, low, high):
    mid = (low + high) / 2
    if low == high:
        return low, high, arr[low]
    else:
        left_low, left_high, left_max = max_sub_array(arr, low, mid)
        right_low, right_high, right_max = max_sub_array(arr, mid + 1, high)
        cross_low, cross_high, cross_max = max_cross_array(arr, low, high)
    
        if left_max >= right_max and left_max >= cross_max:
            return left_low, left_high, left_max
        elif right_max >= left_max and right_max >= cross_max:
            return right_low, right_high, right_max
        else:
            return cross_low, cross_high, cross_max


if __name__ == '__main__':
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print max_sub_array(arr, 0, len(arr) -1)
