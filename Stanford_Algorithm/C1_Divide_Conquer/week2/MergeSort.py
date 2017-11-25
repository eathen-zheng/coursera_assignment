def merge_sort(lst):
    if len(lst) <= 1:
        return lst, 0
    else:
        mi = int(len(lst) / 2)
        left_list, left_cnt = merge_sort(lst[:mi])
        right_list, right_cnt = merge_sort(lst[mi:])
        merge_list, merge_cnt = merge(ll, lr)
        return merge_list, left_cnt + right_cnt + merge_cnt

def merge(l1, l2):
    res = []
    i, j = 0, 0
    cnt = 0
    while (i < len(l1)) and (j < len(l2)):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
            cnt += len(l1) - i
    res = res + l1[i:] + l2[j:]
    while j < len(l1):
        cnt += len(l1) - i
        j += 1
    return res, cnt

if __name__ == '__main__':
    with open('...') as f:
        arr = [int(x) for x in f]
        res = merge_sort(arr)
        print(res[1])