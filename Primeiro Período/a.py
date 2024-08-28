l = [x*y for x in [1,0,2] for y in (2,1,0) if y>x and x%y != 2]
print(l)