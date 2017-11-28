import sys,threading  
sys.setrecursionlimit(3000000)  
threading.stack_size(67108864)  

def first_dfs(v_idx):
    global order_idx, rev_edge_dict, isexplored_first, visit_order
    if len(rev_edge_dict[v_idx]) > 0:
        for idx in rev_edge_dict[v_idx]:
            if not isexplored_first[idx - 1]:
                isexplored_first[idx - 1] = True
                first_dfs(idx)
    visit_order[order_idx - 1] = v_idx
    order_idx = order_idx - 1

def second_dfs(v_idx):
    global edge_dict, isexplored_second, visit_order, scc_list, scc_idx
    if len(edge_dict[v_idx]) == 0 : return
    for idx in edge_dict[v_idx]:
        if not isexplored_second[idx - 1]:
            isexplored_second[idx - 1] = True
            second_dfs(idx)
    scc_list[scc_idx - 1] += 1

def load_dataset(filename):
    global edge_length, edge_dict, rev_edge_dict
    with open(filename, 'r') as f:
        edge_length = len(f.readlines())
    with open(filename, 'r') as f:
        edge_dict = {x:[] for x in range(1, edge_length + 1)}
        rev_edge_dict = {x:[] for x in range(1, edge_length + 1)}
        for line in f.readlines():
            edge=[int(x) for x in line.split()]
            edge_dict[edge[0]].append(edge[1])
            rev_edge_dict[edge[1]].append(edge[0])

def scc_main(filename = 'SCC.txt'):
    global edge_length, edge_dict, rev_edge_dict, isexplored_first, isexplored_second,\
    visit_order, order_idx, scc_list, scc_idx

    load_dataset(filename)

    isexplored_first = [False for x in range(1, edge_length + 1)]
    isexplored_second = [False for x in range(1, edge_length + 1)]
    visit_order = [0 for x in range(1, edge_length + 1)]
    scc_list = [0 for x in range(1, edge_length + 1)]
    order_idx = edge_length
    
    print("first dfs")
    for idx in range(1, edge_length + 1):
        if not isexplored_first[idx - 1]:
            isexplored_first[idx - 1] = True
            first_dfs(idx)
    
    print("second dfs")
    for idx in visit_order:
        if not isexplored_second[idx - 1]:
            scc_idx = idx
            isexplored_second[idx - 1] = True
            second_dfs(idx)
    
    scc_list.sort(reverse = True)
    print(scc_list[:10]) # [434821, 968, 459, 313, 211, 205, 197, 177, 162, 152]

if __name__ == '__main__':
    thread = threading.Thread(target = scc_main)
    thread.start()