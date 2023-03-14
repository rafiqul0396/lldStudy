from multiprocessing import Process

def print_even(limit, exit_prog, number):
    while not exit_prog and number <= limit:
        if(number % 2 == 0):
            print(number)
        number = number + 1

def print_odd(limit, exit_prog, number):
    while not exit_prog and number <= limit:
        if(number % 2 == 1):
            print(number)
        number = number + 1

if __name__ == "__main__":

    limit = 10
    exit_prog = False
    number = 0

    t1 = Process(target=print_even, args=(limit, exit_prog, number))
    t1.start()
    t2 = Process(target=print_odd, args=(limit, exit_prog, number))
    t2.start()

    t1.join()
    t2.join()