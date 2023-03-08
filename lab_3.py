from math import inf


class Graph:
    @classmethod
    def check_for_cycle(cls, edges):
        visited = []
        for edge in edges:
            if edge[2] in visited:
                return True
            visited.append(edge[1])
        return False

    @classmethod
    def kruskal(cls, edges):
        sorted_edges = sorted(edges, key=lambda x: x[0])
        if sorted_edges[0][0] < 0:
            raise ValueError("Numbers have to be positive")
        mst = []
        for edge in sorted_edges:
            if not Graph.check_for_cycle(mst+[edge]):
                mst.append(edge)
        return mst

    @classmethod
    def prims(cls, edges):
        nodes = {}
        for i in edges:
            nodes[i[2]] = []
            nodes[i[1]] = []
        n = len(nodes)
        set_mst = {1}
        mst = []
        edges.insert(0, (inf, -1, -1))

        while len(set_mst) < n:
            min_edge = (inf, -1, -1)
            for node in set_mst:
                min_ = min(edges, key=lambda x: x[0] if (x[1] == node or x[2] == node) and (
                            x[1] not in set_mst or x[2] not in set_mst) else inf)
                if min_edge[0] > min_[0]:
                    min_edge = min_

            if min_edge[0] == inf:
                break

            mst.append(min_edge)
            set_mst.add(min_edge[1])
            set_mst.add(min_edge[2])

        return mst


if __name__ == '__main__':
    graph = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6), (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]
    print(f'Graph: {graph}\nKruskal: {Graph.kruskal(graph)}\nPrim: {Graph.prims(graph)}')
