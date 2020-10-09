nums = [1,3,5,7,9]
def double_it(num):
    return num*2
doubled_nums = map(double_it,nums)
print(list(doubled_nums))
doubled_nums = map(lambda x: x*2,nums)
print(list(doubled_nums))
