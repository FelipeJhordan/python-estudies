## Get n largest or n smallest elemements in a list using the module heapq

import heapq

scores = [ 51, 33, 64, 87, 91, 75, 15, 49, 33, 82]

print(heapq.nlargest(3, scores))
print(heapq.nsmallest(5, scores))
