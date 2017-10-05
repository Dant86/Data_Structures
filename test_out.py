from ll import Binary_Search_Tree

foo = Binary_Search_Tree()
foo.add(5)
foo.add(7)
foo.add(3)
print(len(foo))
print(foo.height())
foo.delete(3)
print(len(foo))