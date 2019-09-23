from heapq import *
def find_k_frequent_numbers(nums, k):
  topNumbers = []
  minHeap=[]
  freqDic={}
  for n in nums:
      freqDic[n] =freqDic.get(n,0)+1
  for nums, frequency in freqDic.items():
      heappush(minHeap,(frequency,nums))
      if len(minHeap) > k:
          heappop(minHeap)
  # TODO: Write your code here
  while len(minHeap):
      topNumbers.append(heappop(minHeap)[1])
  return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

