1
*********************************************************************************************
Extreme Points:
	a point can be obtaind by mixing others iif it lies inside a trangle in color space.

In triangle test:
	Mark all poins of S as EXTREME
	for each triangle (p,q,r)
	  for each s in S\(p,q,r)
	    if s in triangle (p,q,r) then
	      mark s as NO_EXTREME

to left test:
	to test if a point s lies inside a given triangle(p,q,r)

Complexity: O(n^4)

2
**********************************************************************************************
Exteme Edges:
	e=(s,t) is an EE of CH(p) iif all points in S\(s,t) lie to the same side of e.


Identifying Extreme Edges:
	Let EE=Empty
	for each directed segment pq
	  if points in S\(p,q) lies to the same side of pq then let EE=EE U (pq)

