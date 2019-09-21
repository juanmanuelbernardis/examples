
# listas

```
# UNI

m | 0, 1, 2, 3
---------------
0 | A, B, C, D

A = m[0]
C = m[2]
D = m[3]

# MULTI

m | 0, 1, 2, 3 x
--------------
0 | A, B, C, D
1 | E, F, G, H
2 | I, J, K, L
3 | M, N, O, P
y

F = m[1][1]
M = m[3][0]
P = m[3][3]
```
## example

```python
a = [
	0 ['A', 'B', 'C', 'D'],
	1 ['E', 'F', 'G', 'H'],
	2 ['I', 'J', 'K', 'L'],
	3 ['M', 'N', 'O', 'P']
]

print('F', a[1][1])
print('M', a[3][0])
```