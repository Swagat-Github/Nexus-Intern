# CLASS OF LINKEDLIST
class ListNode(object):
  def __init__(self,val=0,Next=None):
    self.val = val
    self.Next = Next
# CREATION OF LINKEDLIST
def  CreateLinkedList(values):
  if not values:
    return None
  Head = ListNode(values[0])
  Cuurent = Head
  for val in values[1:]:
    Cuurent.Next = ListNode(val)
    Cuurent = Cuurent.Next
  return Head
# TRAVERSAL OF LINKEDLIST
def LinkedListTraversal(Head):
  Temp = Head
  while Temp:
    if(Temp.val is not None):
      print(Temp.val,end='')
      Temp = Temp.Next
      if Temp:
        print('->', end='')

# MAIN FUNCTION
values = list(map(int,input("Enter the values with spaces:").split()))
LLList = CreateLinkedList(values)
print("LinkedList:")
LinkedListTraversal(LLList)
