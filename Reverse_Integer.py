def reverse_int(nums):
    a=str(nums)
    if 0<nums<=(1<<31)-1:
        return int(a[::-1])
    elif(-1<<31)<=nums<0:
        return-(int(a[:-len(a):-1]))
    else:
        return 0
n=int(input())
print(reverse_int(n))