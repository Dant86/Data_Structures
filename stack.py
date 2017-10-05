from ll import LinkedList, Stack
import sys

def put_ll_into_arr(ll):
	arr = []
	for i in range(len(ll)):
		arr.append(ll.itemAt(i))
	return arr

expr = "([])"


prev_seen = LinkedList()
openings = ["[", "(", "{"]
closings = ["]", ")", "}"]
complements = {}
for opening, closing in zip(openings, closings):
	complements[opening] = closing

bracs = Stack()
for char in expr:
	if bracs.values.head is None:
		bracs.add(char)
	elif char in closings and openings.index(bracs.itemAt(0)) == closings.index(char):
		bracs.remove()
	else:
		bracs.add(char)

if len(bracs) == 0:
	print(True)
else:
	print(False)