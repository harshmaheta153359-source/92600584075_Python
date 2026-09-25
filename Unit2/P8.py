
x = 10

def outer():
    
    y = 20

    def inner():
        # Local variable
        z = 30

    
        print("Global variable:", x)
        print("Nonlocal variable:", y)
        print("Local variable:", z)

    inner()

outer()
