"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/

"""
import sys
import heapq
from typing import List


class DestState:
    def __init__(self, city_id, cost, stop):
        self.city_id = city_id
        self.cost = cost
        self.stop = stop

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost


# da ji sa si 居然超时? not sure why yet
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # visited = [sys.maxsize] * n
        graph = self.build_graph(flights, n)
        min_heap: List[DestState] = []
        heapq.heappush(min_heap, DestState(city_id=src, cost=0, stop=0))

        while min_heap:
            cur_city = heapq.heappop(min_heap)
            # print('processing node :', cur_city.city_id, 'current step: ', cur_city.stop)
            if cur_city.city_id == dst and cur_city.stop <= k + 1:
                return cur_city.cost

            if cur_city.stop > k:
                continue

            for n_city in graph[cur_city.city_id]:
                indent = '  ' * cur_city.stop
                print(f'{indent}{cur_city.city_id}: processing neighbours: ', n_city[0])
                # if visited[n_city[0]] > cur_city.cost + n_city[1]:
                #     visited[n_city[0]] = cur_city.cost + n_city[1]
                heapq.heappush(min_heap,
                               DestState(city_id=n_city[0], cost=cur_city.cost + n_city[1], stop=cur_city.stop + 1))

        return -1

    def build_graph(self, flights, n):
        graph = {}
        for i in range(n):
            graph[i] = []

        for edge in flights:
            # source : (city_id, cost)
            graph[edge[0]].append((edge[1], edge[2]))

        return graph


from collections import deque

# 朴素BFS
# 更为简单, 而且更好理解!
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = [sys.maxsize] * n
        graph = self.build_graph(flights, n)
        queue = deque()
        queue.appendleft(DestState(city_id=src, cost=0, stop=0))
        level = 0

        # break when level exceeds required stop
        while queue and level <= k:
            # essential: drain queue (current level)
            # using deque, not a heap
            for i in range(len(queue)):
                cur_city = queue.pop()

                for n_city in graph[cur_city.city_id]:
                    # only process nodes that it's either
                    # 1. has not been visited
                    # 2. has a smaller cost than previous visit
                    if visited[n_city[0]] > cur_city.cost + n_city[1]:
                        indent = '  ' * cur_city.stop
                        print(f'{indent}{cur_city.city_id}: processing neighbours: ', n_city[0])
                        visited[n_city[0]] = cur_city.cost + n_city[1]
                        queue.appendleft(DestState(city_id=n_city[0], cost=cur_city.cost + n_city[1],
                                                   stop=cur_city.stop + 1))
            # track level
            level += 1

        return -1 if visited[dst] == sys.maxsize else visited[dst]

    def build_graph(self, flights, n):
        graph = {}
        for i in range(n):
            graph[i] = []

        for edge in flights:
            # source : (city_id, cost)
            graph[edge[0]].append((edge[1], edge[2]))

        return graph


# flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
flights = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]

print(Solution2().findCheapestPrice(n=5, flights=flights, src=0, dst=2, k=2))

print('dajisasi')
print(Solution().findCheapestPrice(n=5, flights=flights, src=0, dst=2, k=2))
