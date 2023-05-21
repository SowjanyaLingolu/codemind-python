def is_ugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1

num=int(input())
result=is_ugly(num)
if result==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")
