#Ecuacion recta perpendicular en punto (0,1) 
def recta(a,b):
    pendientex=b[0]-a[0] 
    pendientey=b[1]-a[1]
    print("y=",-pendientex/pendientey,"(x-",a[0],")","+",a[1]) 
    return 

recta([0,1],[1,2])


#Ecuacion recta perpendicular en punto (1,5) 

# recta([1,5],[3,-1])