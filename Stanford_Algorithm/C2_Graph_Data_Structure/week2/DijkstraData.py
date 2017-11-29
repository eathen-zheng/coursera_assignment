import heapq
import sys

class Graph:
    
    def __init__(self):
        self.vertices = {}

    def get_vertices(self, filename):
        with open(filename) as f:
            for line in f.readlines():
                edges = line.split()
                if len(edges) <= 1: continue
                v = int(edges[0])
                self.vertices[v] = {}
                for edge in edges[1:]:
                    tmp = edge.split(',')
                    self.vertices[v][int(tmp[0])] = int(tmp[1])

    def shortest_path(self, v_s, v_t):
        distances = {} # distance from v_s to vertex
        v_pre = {} # previous vertex
        v_heap = [] # heapq of all vertices in graph

        for v in self.vertices:
            if v == v_s:
                distances[v] = 0
                v_pre[v] = None
                heapq.heappush(v_heap, [0, v])
            else:
                distances[v] = sys.maxsize
                v_pre[v] = None
                heapq.heappush(v_heap, [sys.maxsize, v])

        while v_heap:
            v_min = heapq.heappop(v_heap)[1]
            if v_min == v_t:
                path = []
                while v_pre[v_min]:
                    path.append(v_min)
                    v_min = v_pre[v_min]
                print('path of ' + str(v_t) + ' : ' + str(path))
                print('distance of ' + str(v_t) + ' : ' + str(distances[v_t]))
                return distances[v_t]
            if distances[v_min] == sys.maxsize:
                break
            for v_adj in self.vertices[v_min]:
                alt = distances[v_min] + self.vertices[v_min][v_adj]
                if alt < distances[v_adj]:
                    distances[v_adj] = alt
                    v_pre[v_adj] = v_min
                    for n in v_heap:
                        if n[1] == v_adj:
                            n[0] = alt
                            break
                    heapq.heapify(v_heap)
                    
        print('distance of' + str(v_t) + ':' + str(distances[v_t]))
        return distances[v_t]

if __name__ == '__main__':
    
    g = Graph()
    g.get_vertices('DijkstraData.txt')

    v_s = 1
    for v_t in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
        g.shortest_path(v_s, v_t)