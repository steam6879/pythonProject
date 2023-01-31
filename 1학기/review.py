# position = (1, 2, 3)
# print(position, 'and',  type(position))
#
# x, y, z = position
#
# print(y)
#
# a, b = ('aa', 'bb')
# a, b = b, a
# print(n)


# from cs1media import*
#
# img = load_picture('photos/geowi.jpg')
# w, h = img.size()
# for y in range(h):
#     for x in range(w):
#         r, g, b = img.get(x, y)
#         r, g, b = 255-r, 255-g, 255-b
#         img.set(x, y, (r, g, b))
#
# img.show()


# from cs1media import *
#
# threshold = 100
# white = (255,255,255)
# black = (0,0,0)
#
# img = load_picture('photos/yuna1.jpg')
#
# w, h = img.size()
# for y in range(h):
#     for x in range(w):
#         r, g, b = img.get(x,y)
#         v = (r+g+b) // 3
#         if v > threshold:
#             img.set(x, y, white)
#
#         else:
#             img.set(x,y,black)
#
# img.show()


# from cs1media import *
#
# yellow = (255,255,0)
# blue = (0,0,255)
# green = (0,255,0)
#
# img = load_picture('photos/yuna1.jpg')
#
# w, h = img.size()
# for y in range(h):
#     for x in range(w):
#         r, g, b = img.get(x,y)
#         v = (r+g+b) // 3
#         if v < 85:
#             img.set(x, y, blue)
#
#         elif v > 170:
#             img.set(x, y, green)
#
#         else:
#             img.set(x, y, yellow)
#
# img.show()

# import math
#
# def to_radians(deg):
#     return (deg/180.0)*math.pi
#
# # a = input('write degrees')
# # a = int(a)
# # b = to_radians(a)
# # print(b)
#
# sin = math.sin
# pi = math.pi
# degrees = 45
# radians = degrees / 360*2*pi
#
# print(sin(radians))

# def tt():
#     print('hi')
#
# s = tt()
# print(s)
# import math
# print(math.pi)

# while (True):
#     name = input('What is your name?')
#
#     if name == 'finish':
#         break
#
#     print('Welcome' + name)


# import math
#
# a = input('side a : ')
# b = input('side b : ')
# c = input('side c : ')
#
# a = int(a)
# b = int(b)
# c = int(c)
#
# def is_triangle():
#     if a + b > c:
#         return print('Yes')
#
#     else:
#         return print('No')
#
# is_triangle()

# def avg(data, start = 0, end = None):
#     if not end:
#         end = len(data)
#
#     return sum(data[start:end]) / float(end - start)
#
# d = (1, 2, 3, 4, 5)
#
# print(avg(d, 2, 4))

# from cs1graphics import *
# Canvas(400, 300)
# def create_sun(radius, color):
#     sun = Circle(radius)
#     sun.setFillColor(color)
#     sun.setBorderColor(color)
#     sun.moveTo(100, 100)
#
# create_sun(30, 'yellow')


# from cs1graphics import *
#
# canvas = Canvas(400, 300)
# canvas.setBackgroundColor('light blue')
# canvas.setTitle('inha.Univ')
#
# sq = Square(100)
# sq.moveTo(100, 100)
# canvas.add(sq)
#
# sq.setFillColor('red')
# sq.setBorderColor('red')
# # sq.moveTo(100, 100)
# import time
#
# for i in range(100):
#     time.sleep(0.05)
#     sq.move(10, 0)

# import time
#
# print('안녕하세요.')
# time.sleep(1)
#
# print('오리가 신발끈을 어떻게 묶을까요?')
# time.sleep(5)
#
# print('꽉꽉.')

# korea = [1, 2, (3, 4, 5)]
#
# korea[2] = (7, 8, 9)
#
# print(korea[2])

# countries = ["Australia", "Austria", "Belarus", "Belgium", "Canada", "China", "Czech Republic", "Finland", "France", "Germany", "Great Britain", "Hungary", "Italy", "Japan", "Netherlands", "New Zealand", "Norway", "Poland", "Russia", "Slovakia", "Slovenia", "South Korea", "Sweden", "Switzerland", "Ukraine", "United States"]
#
# gold = [0, 5, 2, 0, 11, 1, 2, 1, 5, 14, 1, 1, 3, 4, 8, 0, 14, 1, 2, 1, 0, 5, 7, 5, 1, 9]
#
# silver = [2, 3, 1, 1, 8 ,6, 2, 1, 4, 10, 0, 0, 2, 5, 6, 0, 14, 0, 6, 2, 1, 8, 6, 6, 0 ,8]
#
# bronze = [1, 6, 0, 0, 10, 2, 3, 4, 6, 7, 4, 0, 5, 4, 6, 2, 11, 1, 9, 0, 1, 4, 1, 4, 0, 6]
#
# madals = []
# for i in range(len(countries)):
#   madals.append((countries[i], gold[i], silver[i], bronze[i]))
#
#
# def print_total():
#   for country, g, s, b in madals:
#     print(country + ' : ',  g + s + b)
#
# print_total()

# for country in countries:
#     print(country)

# l = list(range(1,11))
# print(l)
#
# for i in range(len(l)):
#     l[i] *= l[i]
#
# print(l)

# for i in range(len(countries)):
#     print(countries[i], gold[i] + silver[i] + bronze[i])

# totals = []
#
# for i in range(len(countries)):
#     madals = gold[i] + silver[i] + bronze[i]
#     totals.append((madals, countries[i]))
#
# # print(totals)
#
# totals.sort()
# print(totals)
# totals.reverse()
# print(totals)
#
# top_ten = totals[:10]
# # print(top_ten)
#
# # for p in top_ten:
# #     madals, country = p
# #     print(madals, country)
#
# def no_madals(country, a1, b1):
#     result = []
#
#     for i in range(len(countries)):
#         if a1[i] == 0 and b1[i] == 0:
#             result.append(countries[i])
#
#     return result
#
# only_gold = no_madals(countries, silver, bronze)
# print(only_gold)
#
# a = 'Hello World'
# for i in a:
#     print(i)

# L = ['a', 'b', 10, 1, 1]
# M = [12, 13, 15]
# L.extend('balal')
# print(L)

# x0 = 500
# x1 = 70
# va1 = max(x0, x1)
# print('Max between %d and %d is %d' % (x0, x1, va1))

# print('5.24'%d)

# a = '  App le '
#
# print(a.rstrip())

# text = 'my Mirthday is 2003/9/6'
# result1 = text.split()
# result2 = text.split('/')
# print(result1)
# print(result2)
#
# print('\n')
#
# result3 = ' '.join(result1)
# result4 = '/'.join(result2)
# print(result3)
# print(result4)

# set = {5: 5, 1, 2, 3, 3}
# # odd = {1,2}
# # print(set.intersection(odd))
# # print(set)
#
# # d1 = dict()
# # print(d1)
# print(5 in set)
# set.

# f = open('planets.txt', 'r')
# print(type(f))
# s = f.readline()
# print(s)
# s = f.readline()
# print(s)

# for l in f:
#     s = l.strip()
#     print(s, end=' and ')

# planets = []
#
# for line in f:
#     planets.append(line.strip())
#
# print(planets)

# planets2 = f.readline()
# print(planets2)

# current = 0
# earth = 0
#
# for line in f:
#     current += 1
#     planet = line.strip()
#
#     if planet == 'Earth':
#         earth = current
#         break
#
# print('Earth is planet %dth' % earth)
#
#
# f.close()

# f = open('words.txt', 'r')

# for line in f:
#     if len(line) > 20:
#         print(line, end=' ')

# current = 0
# for line in f:
#     if not 'a' in line:
#         current += 1
#
# print("%d words have no 'e'" % current)

# def is_abecedarian(word):
#     for i in range(1, len(word)):
#         if word[i-1].lower() > word[i].lower():
#             return False
#
#     return True
#
# for line in f:
#     word = line.strip()
#     if is_abecedarian(word):
#         print(word)
#
# f.close()

# f = open('note.txt', 'w')
# f.write('Hello world\n\n')
#
# for i in range(5):
#     f.write(str(i))
#     f.write('\n')
#
# f.close()



#Task at Week 13
# f = open('result.txt', 'w')
# input1 = open('input1.txt', 'r')
# input2 = open('input2.txt', 'r')
# input3 = open('input3.txt', 'r')

#Sol_1 : my code
# def merge(input, result):
#     f = open(result, 'w')
#     list = []
#
#     for i in range(len(input)):
#         globals()['input_'+str(i)] = open(input[i], 'r')        #input_i 'r'로 만들어서 열기
#
#         for globals()['list'+str(i)] in globals()['input_'+str(i)]:
#             list.append(globals()['list'+str(i)].strip())
#
#     for write in list:
#         f.write(write)
#         f.write('\n')
#
# merge(['input1.txt', 'input3.txt'], 'result.txt')

# #Sol_2 : Professor's code
# def merge(txt_list, output_name):
#     f_output = open(output_name, 'w')
#
#     line_list = []
#     for input in txt_list:
#         f_input = open(input, 'r')
#         line_list.append(f_input.readlines())
#
#     f_input.close()
#
#     for line in line_list:
#         for str in line:
#             f_output.write(str)
#
#     f_output.close()
#
# merge(['input1.txt', 'input3.txt'], 'result.txt')



# merge('input1.txt', 'result.txt')
#
# list = []
# for line1 in input1:
#     list.append(line1.strip())
#
# for line2 in input2:
#     list.append(line2.strip())
#
#
# for write in list:
#     f.write(write)
#     f.write('\n')
#
# f.close()
# input1.close()
# input2.close()
# input3.close()








# merge(['hello', 'world'])
# print(list)

# a = ''
# for i in range(5):
#     a += str(i)
#
# print(a)
#
# a = list(a)
# a.reverse()
# a = ''.join(a)
#
# print(a)

# def jinsu(a,b):
#     convertString="0123456789ABCDEF"
#     sol=''
#     if a<b :
#         return convertString[a]
#     while a>=b:
#         n=divmod(a,b)
#         a //= b
#         sol += convertString[n[1]]
#     sol += convertString[n[0]]
#     return sol[::-1]
#
# # 재귀법 버전
# def jinsu_rec(a,b):
#     convertString="0123456789ABCDEF"
#     if a <b :
#         return convertString[a]
#     n = divmod(a,b)
#     return jinsu_rec(a//b, b)+ convertString[n[1]]
#
#
# a = int(input("진수를 변환하고 싶은 숫자를 입력하세요: "))
# b = int(input("몇 진수로 변환하고 싶습니까?"))
# print("반복문으로 구한 %d 의 %d 진수 변환 : %s" %(a,b,jinsu(a,b)))
# print("재귀법으로 구한 %d 의 %d 진수 변환 : %s" %(a,b,jinsu_rec(a,b)))


# def convert(a):
#     a = "{}".format(a)
#     print(a)
#
# convert(a)
# a = 5
# print(type(a) == str)

# a = 'apple'
# print(len(a))

# from cs1media import *
# # img = create_picture(480, 480, 'red')
# a = load_picture('photos/geowi.jpg')
# threshold = 125
# (w, h) = a.size()
# for y in range(h):
#     for x in range(w):
#         r, g, b = a.get(x, y)
#         ave = (r + g + b)//3
#
#         if ave > threshold:
#             a.set(x, y, (255, 255, 255))
#
#         else:
#             a.set(x, y, (0, 0, 0))
#
# a.show()


# from cs1robots import *
#
# create_world()
# hubo = Robot('yellow')
# hubo.move()
# ami = hubo
# ami.turn_left()
# hubo.move()
# print(ami == hubo)

# from cs1graphics import *
#
# def create_sun(radius, color):
#     sun = Circle(radius)
#     sun.setFillColor(color)
#     sun.setBorderColor(color)
#     sun.moveTo(100, 100)
#     return sun
#
# # canvas = Canvas(400, 300)
# sun = create_sun(30, 'yellow')
# Canvas(400, 300).add(sun)
# import time
# for i in range(100):
#     sun.move(1, 0)
#     sun.setFillColor((255, 255 - i, i*2))
#
#     time.sleep(0.05)

# f = open('planets.txt', 'r')
# list = []
# for i in f:
#
#     list.append(i.strip())
# f.close()
# print(list)
# print('\n')
#
# for i in range(len(list)):
#     list[i] = list[i].upper()
#
# print(list)

# print(set('Hello world'))


#
# list.extend('apple')
# print(list)

# x = 3.946
# print('Formatting - %.2f' % x)



# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# thisdict.get('aaa', default=None)
# print(thisdict['brand'])

# print(1964 in thisdict)

# f = open('planets.txt', 'r')

# print(f.readlines())

# current = 0
# earth = 0
#
# for line in f:
#   current += 1
#   planet = line.strip().lower()
#
#   if planet == 'earth':
#     earth = current
# print('Earth is planet %s' % earth)
# f.close()

# f = open('words.txt', 'r')

# count = 0
# for line in f:
#   word = line.strip()
#   if not 'e' in word:
#     count += 1
#
#
# print(count)

#Q1
# def is_abecedarian(word):
#   for i in range(1, len(word)):
#     if word[i-1] > word[i]:
#       return False
#
#   return True
#
# for line in f:
#   word = line.lower().strip()
#   if is_abecedarian(word):
#     print(word)
#
# f.close()

#Q2
# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
#
# def print_five():
#   a_five = []
#   for i in a:
#     if len(i) == 5:
#       a_five.append(i)
#
#   print(a_five)
#
# print_five()

#Q3
# text1 = 'a:b:c:d'
#
# list = text1.split(':')
# text2 ='#'.join(list)
# print(text2)

#Q4
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
#
# above_50 = []
# for i in range(len(A)):
#   if int(A[i]) >= 50:
#     above_50.append(A[i])
#
# print(sum(above_50))

#Q5
# def fibonacci(n):
#   if n == 0:
#     return 0
#
#   elif n == 1:
#     return 1
#
#   else:
#     return fibonacci(n-2) + fibonacci(n-1)
#
# for i in range(10):
#   print(fibonacci(i))
# input = int(input('enter a number'))
# print(fibonacci(input))

#Q6
# a = input('enter a number')
# list = a.split(',')
#
# list_int = []
# for i in range(len(list)):
#   list_int.append(int(list[i]))
#
# print(sum(list_int))

#Q7
# n = int(input('구구단을 출력할 숫자를 입력하세요(2~9): '))
# for i in range(9):
#   print(n*(i+1), end=' ')

#Q8
# f = open('result.txt', 'r')
# # list = []
# # for i in f:
# #     list.append(i.strip())
# list = f.readlines()
#
#
# f.close()
# list.reverse()
#
# f = open('result2.txt', 'w')
# for i in list:
#     i = i.strip()
#     f.write(i)
#     f.write('\n')
# print(list)

#Q9
# f = open('sample.txt', 'r')
#
# list = []
# for i in f:
#     list.append(int(i.strip()))
# f.close()
# mean = sum(list)/len(list)
# print(mean)
# f = open('result.txt', 'w')
# f.write(str(mean))
#
# f.close()

#Q11
num = input('enter a number')
list = list(num)
print(list)
list_int = []
for i in range(len(list)):
    list_int.append(int(list[i]))
print(list_int)

for i in range(len(list)-2):
    if list_int[i]%2 == 1 and list_int[i+1]%2 == 1:
        list_int.insert(i+1, '-')

    elif list_int[i]%2 == 0 and list_int[i+1]%2 == 0:
        list_int.insert(i+1, '*')

    else:
        continue

print(list_int)