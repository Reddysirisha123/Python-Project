def product_of_numbers_up_to_n(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product



def factors_of_numbers(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


def check_for_primes(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def check_for_prime_up_to_n(num):
    for num in range(1, 11):
        if check_for_primes(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")


def multiply_primes_up_to_n(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = 1
    for num in range(2, n+1):
        if is_prime(num):
            result *= num
    return result


import math


def calculate_distance(x, y, z):
    return math.sqrt(x ** 2 + y ** 2 + z ** 2)





if __name__ == '__main__':
    for n in range(1, 11):
        print(f"product_of_numbers_up_to_n = {product_of_numbers_up_to_n(n)}")

if __name__ == '__main__':
    for n in range(1, 101):
        print(f"factors_of_numbers = {factors_of_numbers(n)}")

if __name__ == '__main__':
    for num in range(1, 11):
        print(f"check_for_primes = {check_for_primes(num)}")

if __name__ == "__main__":
    for num in range(1, 12):
        print(f"multiply_primes_up_to_n (num) = {multiply_primes_up_to_n(num)}")

if __name__ == "__main__":
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))
    z = float(input("Enter the z-coordinate: "))

    distance = calculate_distance(x, y, z)

    print(f"The distance of the vector ({x}, {y}, {z}) from the origin (0, 0, 0) is {distance:.2f}")