X=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
Y=[1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]
Z=[1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0]

def maj(x, y, z):
	if x==y:
		X_func()
		Y_func()
	elif y==z:
		Y_func()
		Z_func()
	elif z==x:
		Z_func()
		X_func()

def X_func():
	global X
	t=(X[13]+X[16]+X[17]+X[18])%2
	for i in range(18, 0, -1):
		X[i]=X[i-1]
	X[0]=t

def Y_func():
	global Y
	t=(Y[20]+Y[21])%2
	for i in range(21, 0, -1):
		Y[i]=Y[i-1]
	Y[0]=t

def Z_func():
	global Z
	t=(Z[7]+Z[20]+Z[21]+Z[22])%2
	for i in range(22, 0, -1):
		Z[i]=Z[i-1]
	Z[0]=t

print('키 스트림 : ', end='')
for i in range(0, 32):
	maj(X[8], Y[10], Z[10])
	print((X[18]+Y[21]+Z[22])%2, end='')
print()
print('X: ', X)
print('Y: ', Y)
print('Z: ', Z)
