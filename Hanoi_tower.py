"""
Solving the Tower of Hanoi problem.
https://en.wikipedia.org/wiki/Tower_of_Hanoi#:~:text=The%20Tower%20of%20Hanoi%20(also,thus%20approximating%20a%20conical%20shape
n - number of rings

Sample Input
2

Sample Output
1 - 2
1 - 3
2 - 3
"""

n = int(input())
l1 = [i + 1 for i in range(n)]
l2 = [0]
l3 = [0]
ring = n
while l3 != [i + 1 for i in range(n)]:
	if ring == 0:
		ring = n
	if ring % 2 == 0:
		if ring == l1[len(l1) - 1] and l2[len(l2) - 1] < ring:
			l1.remove(ring)
			l2.append(ring)
			print( '1 - 2')
			if not l1:
				l1 = [0]
			if 0 in l2:
				l2.remove(0)
		elif ring == l2[len(l2) - 1] and l3[len(l3) - 1] < ring:
			l2.remove(ring)
			l3.append(ring)
			print( '2 - 3')
			if not l2:
				l2 = [0]
			if 0 in l3:
				l3.remove(0)
		elif ring == l3[len(l3) - 1] and l1[len(l1) - 1] < ring:
			l3.remove(ring)
			l1.append(ring)
			print( '3 - 1')
			if not l3:
				l3 = [0]
			if 0 in l1:
				l1.remove(0)
		ring -= 1
	elif ring % 2 != 0:
		if ring == l1[len(l1) - 1] and l3[len(l3) - 1] < ring:
			l1.remove(ring)
			l3.append(ring)
			print( '1 - 3')
			if not l1:
				l1 = [0]
			if 0 in l3:
				l3.remove(0)
		elif ring == l3[len(l3) - 1] and l2[len(l2) - 1] < ring:
			l3.remove(ring)
			l2.append(ring)
			print( '3 - 2')
			if not l3:
				l3 = [0]
			if 0 in l2:
				l2.remove(0)
		elif ring == l2[len(l2) - 1] and l1[len(l1) - 1] < ring:
			l2.remove(ring)
			l1.append(ring)
			print( '2 - 1')
			if not l2:
				l2 = [0]
			if 0 in l1:
				l1.remove(0)
		ring -= 1
