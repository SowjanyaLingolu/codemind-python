def isH(number):
    visited = set()
    while True:
        if number == 1:
            return 1
        elif number in visited:
            return 0
        else:
            visited.add(number)
            number = sum(int(digit)**2 for digit in str(number))
number = int(input())
if isH(number):
    print(True)
else:
    print(False)