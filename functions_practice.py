def hello():
    print("hello")

def pack(x,y,z):
    return [x,y,z]

def eat_lunch(lunch):
    if len(lunch)==0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunch)):
            if i==0:
                print(f"First I eat {lunch[0]}")
            else:
                print(f"Next I eat {lunch[i]}")


hello()
print(pack("food", "snacks", "drinks"))
lunch1=[]
eat_lunch(lunch1)
lunch2=["apple", "sandwich", "cake"]
eat_lunch(lunch2)
