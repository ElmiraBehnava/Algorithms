class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def print_matrix(self):
        for row in self.adjMatrix:
            print("".join(map(str, row)))


def main():
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        v, w = map(int, input().split(" "))
        g.add_edge(v - 1, w - 1)

    g.print_matrix()


if __name__ == "__main__":
    main()
