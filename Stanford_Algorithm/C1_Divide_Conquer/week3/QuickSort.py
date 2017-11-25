def choose_pivot_first(lst):
    return 0

def choose_pivot_last(lst):
    return -1

def choose_pivot_median(lst):
    if len(lst) % 2 == 0:
        mid_index = int(len(lst) / 2) - 1
    else:
        mid_index = int(len(lst) / 2)
    tmp_lst = sorted([lst[0], lst[mid_index], lst[-1]])
    return lst.index(tmp_lst[1])

def partition(lst, pivot):
    if lst[0] != lst[pivot]:
        lst[0], lst[pivot] = lst[pivot], lst[0]
    i = 1
    for j in range(1, len(lst)):
        if lst[j] < lst[0]:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[0], lst[i-1] = lst[i-1], lst[0]
    return lst[:i-1], lst[i:]

def quick_sort(lst, choose_pivot_func):
    num_comparison = len(lst) - 1
    if len(lst) <= 1:
        return lst, 0
    pivot = choose_pivot_func(lst)
    p_val = lst[pivot]
    less_part, greater_part = partition(lst, pivot)
    result1 = quick_sort(less_part, choose_pivot_func)
    result2 = quick_sort(greater_part, choose_pivot_func)
    return result1[0] + [p_val] + result2[0], num_comparison + result1[1] + result2[1]

if __name__ == '__main__':
    with open("./QuickSort.txt","r") as f:
        arr = [int(l) for l in f]
    print(quick_sort(arr,choose_pivot_first)[1])

    with open("./QuickSort.txt","r") as f:
        arr = [int(l) for l in f]
    print(quick_sort(arr,choose_pivot_last)[1])
    
    with open("./QuickSort.txt","r") as f:
        arr = [int(l) for l in f]
    print(quick_sort(arr,choose_pivot_median)[1])