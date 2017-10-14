from ll import HashTable
from nltk.corpus import words

table = HashTable(10)

for i in range(20):
	table.add(words.words()[i], 1)
table.add("foo", 1)
print(table)

print(table["foo"])