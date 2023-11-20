# CLASS OF A LINKEDLIST
class ListNode(object):
  def __init__ (self,val=0,next=None):
    self.val  = val
    self.next = next
# LINKEDLIST CLASS WITH MIDDLENUMBER FUNCTION
class LinkedList(object):
  def MiddleNumberofList(self,Head):
    First = Second = Head
    while Second and Second.next:
      First  = First.next
      Second = Second.next.next
    return First 
# CREATION OF LINKEDLIST
def CreateLinkedList():
  values = list(map(int,input("Enter the values with space:").split()))
  if not values:
    return None
  Head = ListNode(values[0])
  Current = Head
  for val in values[1:]:
    Current.next = ListNode(val)
    Current = Current.next
  return Head
# MAIN FUNCTION
InputValues = CreateLinkedList()
LinkedListSolution = LinkedList()

if InputValues:
  Result = LinkedListSolution.MiddleNumberofList(InputValues)
  print("Middle Value of the LinkedList:",Result.val)
else:
  print("Empty LinkedList")