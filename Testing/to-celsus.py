#placing a float tin front of input makes it a number vlaue
f = float(input("what tempure you like to convert? "))

# this is the formula to convert the 2 temps
c = (f -32) * 5 / 9

#round make the float to be rounded  an the 2 is for the element
print(f, "f is", round(c ,2), "c'")s