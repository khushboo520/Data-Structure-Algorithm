from heapq import *
def find_Kth_smallest(lists, k):
  number = -1
  minheap = []
  for l in lists:
      if l is not None:
          heappush(minheap, (l[0],l[1:]))
  counter=0
  while minheap is not None:
      v,l = heappop(minheap)
      if len(l) !=0:
          heappush(minheap,(l[0],l[1:]))
      if counter == k-1:
          return v
      counter += 1
  return number


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
