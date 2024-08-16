
print("Hello World")

myname = "Sirisha"

print(f"Hello {myname}! How are you?")

def hello_name(somename):
    print(f"Hello {somename}! This is a function. ")


def repeat_hello(somename, n_times):
    for i in range(n_times):
        print(f"Hello there {somename}! This is print statement number: {i+1}")


if __name__ == "__main__":
    hello_name("Class")
    hello_name("Abhi")
    hello_name("Nav")

    repeat_hello( somename= "Abhi", n_times= 5)






