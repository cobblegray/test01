def add_and_return_binary(a, b):
    result = a + b
    return bin(result)

if __name__ == "__main__":
    print(add_and_return_binary(6, 4))