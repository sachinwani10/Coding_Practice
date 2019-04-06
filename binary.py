data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 9

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = high - low / 2
	if target == data[mid]:
	    return True
	elif target < data[mid]:
	    high = mid - 1
	elif target > data[mid]:
	    low = mid + 1
    return False	