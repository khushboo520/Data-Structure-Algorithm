from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result=[]
  q=deque()
  q.append(root)
  while q:
      levelSize=len(q)
      currentLevel=[]
      for i in range(levelSize):
          currenttNode=q.pop()
          currentLevel.append(currenttNode.val)
          if currenttNode.left:
              q.appendleft(currenttNode.left)
          if currenttNode.right:
              q.appendleft(currenttNode.right)
      result.append(currentLevel)


  return result

def creatArray(root,r,level):
    if root == None:
        return None
    if len(r) == level:
        a=[root.val]
        r.append(a)
    else:
        a=r[level]
        a.append(root.val)
    creatArray(root.left,r,level+1)
    creatArray(root.right,r,level+1)
    return r

def main():
  result=[]
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  #print("Level order traversal: " + str(creatArray(root,result,0)))
  print("Level order traversal: " + str(traverse(root)))


main()