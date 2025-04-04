x= 0
y=False

match x :
    case 0 if y:
        print("x is zero")
    case 0 if not y:
        print ("x is one")
    case _:
        print("x is something else")