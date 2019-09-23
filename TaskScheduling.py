from collections import deque
def is_scheduling_possible(tasks, prerequisites):
  inDegree={i :0 for i in range(tasks)}
  graph={i:[] for i in range(tasks)}
  q=deque()
  sortedOrder=[]
  for t in prerequisites:
      parent,child=t[0],t[1]
      graph[parent].append(child)
      inDegree[child]+=1


  for node in inDegree.keys():
      if inDegree[node] == 0:
          q.append(node)

  while q:
      node=q.popleft()
      sortedOrder.append(node)
      for c in graph[node]:
          inDegree[c]-=1
          if inDegree[c] == 0:
              q.append(c)
  if len(sortedOrder) != tasks:
      return False
  return True



def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
