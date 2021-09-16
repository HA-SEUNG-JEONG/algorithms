# 순위
# n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.
# 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 선수의 수는 1명 이상 100명 이하입니다.
# 경기 결과는 1개 이상 4,500개 이하입니다.
# results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
# 모든 경기 결과에는 모순이 없습니다.

# 입출력 예
# n	    results	                                        return
# 5	    [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	    2
# 2번 선수는 [1, 3, 4] 선수에게 패배했고 5번 선수에게 승리했기 때문에 4위입니다.
# 5번 선수는 4위인 2번 선수에게 패배했기 때문에 5위입니다.

# cf) 플로이드 와샬 알고리즘(모든 지점에서 다른 모든 지점까지의 최단거리) : Dxz = min(Dxz, Dxy + Dyz)

# 나의 정답 - 플로이드 와샬 응용 - 모든 상대방에 대한 승패 추측이 가능한 선수들만 순위 확정된 것으로 간주
def solution(n, results):
    answer = 0
    
    graph = [([0] * (n+1)) for _ in range(n+1)]
    
    for r in results:
        a, b = r
        graph[a][b] = 1 # a가 승리
        graph[b][a] = -1 # b가 패배
    
    print(graph)
    # [[0, 0, 0, 0, 0, 0], 
    # [0, 0, 1, 0, 0, 0], 
    # [0, -1, 0, -1, -1, 1], => (y=2) 2는 1,3,4에게 패배, 5에게 승리
    # [0, 0, 1, 0, -1, 0], 
    # [0, 0, 1, 1, 0, 0], 
    # [0, 0, -1, 0, 0, 0]]
    
    for mid in range(1, n+1):
        for y in range(1, n+1):
            for x in range(1, n+1):
                if graph[x][mid] == 1 and graph[mid][y] == 1:
                    graph[x][y] = 1 # (승) x > mid > y (패)
                    # graph[y][x] = -1 # 반대 경우는 (y,x)일 때 자동으로 추가됨
                if graph[x][mid] == -1 and graph[mid][y] == -1:
                    graph[x][y] = -1 # (승) y > mid > x (패)
                    # graph[y][x] = 1
    print(graph)   
    # [[0, 0, 0, 0, 0, 0], 
    # [0, 0, 1, 0, 0, 1], 
    # [0, -1, 0, -1, -1, 1], 
    # [0, 0, 1, 0, -1, 1], 
    # [0, 0, 1, 1, 0, 1], 
    # [0, -1, -1, -1, -1, 0]] => (y=5) 5는 1,2,3,4에게 패배 (x=2일때도 동일)

    for player in graph[1:]:
        if player.count(0) == 2:
            answer += 1
    
    return answer

# =================================================================