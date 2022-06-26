ans = 0

edges = [[] for _ in range(10)]


def add_edge(u, v):
    global edges
    edges[u].append(v)
    edges[v].append(u)


def minTimeToColor(node, parent, arrival_time):

    global ans

    # Starting from time = 0,
    # for all the child edges
    current_time = 0

    for x in edges[node]:

        # If the edge is not visited yet.
        if x != parent:

            # Time of coloring of
            # the current edge
            current_time += 1

            # If the parent edge has
            # been colored at the same time
            if current_time == arrival_time:
                current_time += 1

            # Update the maximum time
            ans = max(ans, current_time)

            # Recursively call the
            # function to its child node
            minTimeToColor(x, node, current_time)


if __name__ == "__main__":
    n = int(input())
    A = []
    for _ in range(n - 1):
        A.append(list(map(int, input().split())))

    for i in A:
        add_edge(i[0], i[1])

    minTimeToColor(1, -1, 0)

    print(ans)
