from heapq import *
def sort_character_by_frequency(str):
  result=""
  freqDict={}
  maxHeap=[]
  for c in str:
      freqDict[c] = freqDict.get(c,0) + 1
  for c, f in freqDict.items():
      heappush(maxHeap,(-f,c))
  while len(maxHeap):
      f,c=maxHeap[0]
      result+=(c*(abs(f)))
      heappop(maxHeap)

  return result


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
