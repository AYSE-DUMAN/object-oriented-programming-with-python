def my_generator():
    n = 1
    print("The value of n is 1")

    yield n

    n += 1
    print("The value of n is 2")
    yield n

    n += 1
    print("The value of ne is 3")
    yield n

# for loop using generator 
for item in my_generator():
    print(item)

def reverse_str(given_str):
    length = len(given_str)
    for i in range(length - 1, -1, -1):
        yield given_str[i]

# for loop to reverse string
for char in reverse_str("hello world"):
    print(char)

my_list = [1, 2, 3, 4]
list_ = [x**2 for x in my_list]

generator = (x**2 for x in my_list)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print(sum(x ** 2 for x in my_list))
print(max(x ** 2 for x in my_list))


if __name__ == "__main__":

    x = my_generator()
    print(next(x))
    print(next(x))
    print(next(x))

