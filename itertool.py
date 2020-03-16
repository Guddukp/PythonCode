from itertools import count,accumulate,takewhile,product
for i in count(3):
    print(i)
    if i>=11:
        break

nums=list(accumulate(range(8)))  ##accumulate is factorial...nums
print(nums)

num_takewhile=list(takewhile(lambda x: x<=6,nums))
print(num_takewhile)

letter=['a','b']
print(list(product(letter,range(3))))
