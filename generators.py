import time

def fibo_gen(limit):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            if not limit or aux <= limit:
                yield aux
            else:
                raise StopIteration


if __name__ == "__main__":
    
    limit = input("Please insert the limit:\n")
    try:
        limit = int(limit)
    except:
        print("The limit should be a number")
        exit()

    fibonacci = fibo_gen(limit)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)
