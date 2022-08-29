def displaying(table):
	for i in range(len(table)):
		print(i, '=>', end='')
		for j in table[i]:
			print(j, end='')
		print()


hash_table = [[] for _ in range(5)]


def hashing(key_value):
	return key_value % len(hash_table)


def insert(my_table, key_val, value):
	hashing_key = hashing(key_val)
	my_table[hashing_key].append(value)


if __name__ == "__main__":
	insert(hash_table, 11, 'Selim')
	insert(hash_table, 12, 'Hamza')
	insert(hash_table, 13, 'Samara')
	insert(hash_table, 14, 'Ahmed')
	insert(hash_table, 14, 'Mohamed')

displaying(hash_table)
