def is_perfect_square(number):
    if number<0:
        return False
    square_root=int(number**0.5)
    return square_root * square_root == number
num=int(input())
if is_perfect_square(num):
    print("True")
else:
    print("False")