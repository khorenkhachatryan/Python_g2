matrix = [[1 for k in range(3)] for m in range (3)]
for col in range(3):
	for row in range(3):
		value = int(input())
		matrix[col][row] = value
print("this is your matrix now",matrix)
rotated_matrix = [ 
	[0,0,0],
	[0,0,0],
	[0,0,0]
]
for i in range(3):
	for j in range(3):
		rotated_matrix[i][j] = matrix[2 - i][2 - j]
print("this is the rotated matrix now",rotated_matrix)

	
