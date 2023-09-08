def solution(k, dungeons):
    def dfs(p, n, path):
        max_depth = n  # 최대 깊이를 따로 변수로 관리합니다.
        for i in range(len(dungeons)):
            if dungeons[i][0] > p or i in path:
                continue
            p -= dungeons[i][1]
            path.append(i)
            max_depth = max(max_depth, dfs(p, n + 1, path))  # 깊이를 최대값으로 업데이트합니다.
            p += dungeons[i][1]
            path.pop()
        return max_depth  # 최대 깊이를 반환합니다.

    answer = dfs(k, 0, [])
    return answer
