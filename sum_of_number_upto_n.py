

def sum_of_num_upto_n(num):
    output = 0
    for i in range(1, num+1):
        output += i

    return output

if __name__ == "__main__":
    print("hi")
    for i in range(1,11):
        print(f"sum of numbers upto {i} = {sum_of_num_upto_n(i)}")

