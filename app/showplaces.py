def get_showplaces(from_place, to_place, width, max_time, nodes_number):

    MAXN = 10
    pos = None

    dp = [None]*MAXN
    parent = [None]*MAXN

    for i in range(MAXN):
        dp[i] = [1061109567]*MAXN
        parent[i] = [0]*MAXN

    ans = [None]*MAXN

    dp[1][1] = 0

    for i in range(2, nodes_number+1, 1):
        
        for j in range(0, len(from_place), 1):
            if dp[i-1][from_place[j]] + width[j] < dp[i][to_place[j]]:
                dp[i][to_place[j]] = dp[i-1][from_place[j]] + width[j]
                parent[i][to_place[j]] = from_place[j]

        if dp[i][nodes_number] <= max_time:
            pos = i

    id = nodes_number
    # print(dp)

    for i in range(pos, 0, -1):
        ans[i] = id
        id = parent[i][id]
        # print(ans)
        # print(i)

    return ans[1:pos+1]


if __name__ == "__main__":

    from_place = [1, 2, 2]
    to_place = [2, 3, 4]
    width = [5, 7, 8]

    max_time = 13
    nodes_number = 4

    # from_place = [1, 1, 3, 2, 4, 6]
    # to_place = [2, 3, 6, 4, 6, 5]
    # width = [2, 3, 3, 2, 2, 1]

    # max_time = 7
    # nodes_number = 6

    # from_place = [1, 3, 1, 2, 4]
    # to_place = [3, 5, 2, 4, 5]
    # width = [3, 3, 2, 3, 2]

    # max_time = 6
    # nodes_number = 5

    print(get_showplaces(from_place, to_place, width, max_time, nodes_number))