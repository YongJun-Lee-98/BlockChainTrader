def print_ntimes(*values, n=2):
	for i in range(n):
		print(values)
print_ntimes("Hello","Python","World", 3)

print_ntimes(1, 3, n=5)