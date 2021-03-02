# 문제 1
print("hello\n"*10)

# 문제 2
a,b,c,d = 10,100,20,300
print("{},{},{},{}\n".format(a,b,c,d))
a,b,c,d = b,c,d,a
print("{}, {}, {}, {}".format(a,b,c,d))

# 문제 3
print(max(a,b,c,d))

# 문제 4
inp = int(input())
print("{}{}".format(inp%10, inp//10))

# 문제 5
def show():
    for i in range(100):
        print(i, end=" ")
        if i % 10 and i != 0:
            print("\n")

# 매개 변수
# 반환값

# 문제 6
def p(*args):
    print(sum(args))

p(1,2,3)
p(1,2,3,4)

# 파일 입출력



filename = 'data/poem.txt'
with open(filename, 'r', encoding='utf-8') as f:
    for i in f:
        print(i.strip())
    line = f.readlines()
    print(line)
    for i in line:
        print(i.strip())

temp = '\t\t\n\n apple \t\t\n'
t = temp.strip()

print("[{}]".format(temp))

with open('data/write.txt', 'r', encoding='utf-8') as f:
    print(f.readline())


a = 'aa,bb,cc'
print(a.split(','))
b = a.split(',')
print('*'.join(b))

import random

print(sum([random.randrange(100) for _ in range(10)]))
