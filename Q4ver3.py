tup = [('a', 4, 2), ('a', 4, 3), ('a', 7, 2), ('a', 7, 3), ('b', 4, 2), ('b', 4, 3), ('b', 7, 2), ('b', 7, 3)]
ans = sorted(tup, key=lambda tup: (tup[len(tup)-1]))
print(ans)