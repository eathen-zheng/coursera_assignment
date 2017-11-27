from random import choice

def get_edges(filename):
    edges = []
    with open(filename) as f:
        for line in f.readlines():
            tmp = line.strip().split()
            if len(tmp) < 1: continue
            for i in range(1, len(tmp)):
                edge = (tmp[0], tmp[i])
                edges.append(tmp_edge)
    return edges

def get_minCut(edges):
    while len(set(edges)) > 2:
        current_edge = choice(edges)
        edges.remove(current_edge)
        edges = map(lambda x: (current_edge[0] if x[0] == current_edge[1] else x[0],
                               current_edge[0] if x[1] == current_edge[1] else x[1]),
                    edges)
        edges = list(filter(lambda x: x[0] != x[1], edges))
    edges = list(filter(lambda x: x[0] < x[1], edges))
    return len(edges)

if __name__ == '__main__':
    min_egde = 1000
    edges = get_edges('./KargerMinCut.txt')
    for i in range(100):
        x = get_minCut(edges)
        if x < min_egde:
            min_egde = x
    print(min_egde)