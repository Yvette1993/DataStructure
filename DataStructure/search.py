

def linear_search(dataset, val):
    for ind ,v in enumerate(dataset):
        if v == val:
            return ind
        else:
            return None

def binary_search(dataset, val):
    left = 0
    right = len(dataset)-1
    while left <= right:  #候选区有值
        mid = (left + right) // 2
        if dataset[mid] == val:
            return mid
        elif dataset[mid] > val: #待查找值在mid左侧
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

li = list(range(10))
binary_search(li,3)
linear_search(li,3)