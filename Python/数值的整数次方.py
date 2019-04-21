# 貌似简单的一道题，其实是一个大坑！考察边界条件思考是否全面。 O(n), O(1)
# 0的0次方数学上没有任何意义，做除法的时候需要单独考虑。返回0或者1都可以接受。
def offer16(base, exponent):
    if exponent == 0: return 1
    if exponent == 1: return base
    if exponent < 0:
        exponent = -exponent
        base = 1 / base if base != 0 else 0
    res = base
    while exponent > 1:
        res *= base
        exponent -= 1
    return res


# 根据奇数和偶数的乘方性质优化代码。 O(logn),O(1)
# 彻底优化代码，位运算和位移运算比除法和取余运算更加高效。
def offer16_1(base, exponent):
    if exponent == 0: return 1
    if exponent == 1: return base
    if exponent < 0:
        exponent = -exponent
        base = 1 / base if base != 0 else 0
    flag = False
    if exponent & 1 == 1: flag = True
    res = base
    while exponent > 1:
        res *= res
        exponent = exponent >> 1
    return res * base if flag else res

-----

print(offer16_1(-2, -9))
print(offer16_1(2, 0))
