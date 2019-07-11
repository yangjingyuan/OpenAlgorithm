import os
import sys

def swap(arr, p, q):
    temp = arr[p]
    arr[p] = arr[q]
    arr[q] = temp

def partition(arr, low, high):
    x = arr[low]
    p = low
    for q in range(low + 1, high + 1):
        if arr[q] <= x:
            p += 1
            swap(arr, p, q)
    swap(arr, low, p)
    return p

def quick_sort(arr, low, high):
    if low < high:
        pviot = partition(arr, low, high)
        quick_sort(arr, low, pviot -1)
        quick_sort(arr, pviot + 1, high)

def insert_sort(arr, low, high):
    for q in range(low + 1, high + 1):
        key = arr[q]
        while q > 0 and arr[q - 1] > key:
            arr[q] = arr[q - 1]
            q -= 1
        arr[q] = key

if __name__ == '__main__':
    arr = [7, 8, 10, 1, 6, 2, 11, 2, 3, 4]
    print arr
    low = 0
    high = len(arr) - 1
    quick_sort(arr, low, high)
    print "quick sort ", arr
    insert_sort(arr, low, high)
    print "insert sort", arr
