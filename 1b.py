import sys

current = 0
all_numbers = {}
input_ = sys.stdin.read().split('\n')
quit = False

while True:
    for line in input_:
        exec 'current = current ' + line
        try:
            x = all_numbers[current]
            print current
            quit = True
        except:
            all_numbers[current] = 0
        if quit:
            sys.exit(0)
