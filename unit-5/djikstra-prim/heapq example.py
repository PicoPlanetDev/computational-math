import heapq

h=[]
heapq.heappush(h,(9,(1,2)))
print(h)
heapq.heappush(h,(3,(5,2)))
print(h)
heapq.heappush(h,(11,(1,9)))
print(h)
heapq.heappush(h,(1,(3,6)))
print(h)
heapq.heappush(h,(8,(5,7)))
print(h)
z=heapq.heappop(h)
print(z,h)
z=heapq.heappop(h)
print(z,h)
