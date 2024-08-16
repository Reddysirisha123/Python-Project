
from print_statement import repeat_hello, hello_name

def print_even_up_to_number(input_number):
    list_of_numbers= list(range(1, input_number+1))
    print(list_of_numbers)
    for number in list_of_numbers:
        if number % 2 ==0:
            print(number)


if __name__ == "__main__":
    print("Hello world")
    repeat_hello( somename= "Class", n_times= 5)
    hello_name("Class")

    list_of_names = ["Rahul", "Nav", "Abhi", "Jack"]
    for name in list_of_names:
        hello_name(name)

    number_list = [1,2,3,4,5]
    print(number_list)

    for num in number_list:
        print(num)

    print_even_up_to_number(25)

