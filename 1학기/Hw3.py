# def radix_to_radix(n, radix1, radix2):
#     result = []
#     if radix1 == 10 and radix2 == 2:
#         while not n//2 == 1 or 0:
#             result.append(n%2)
#             n = n//2
#
#         result.append(n%2)
#         result.append(n//2)
#     result.reverse()
#     result = [str(x) for x in result]
#     result = ''.join(result)
#
#
#     return print(result)
#
# radix_to_radix(140, 10, 2)






# def radix_to_radix(n, radix1, radix2):  #10진수 to 2진수 only
#     result = []
#     while not n//radix2 < radix2:
#         result.append(n%radix2)
#         n = n//radix2
#
#     result.append(n%radix2)
#     result.append(n//radix2)
#
#     result.reverse()
#     result = [str(x) for x in result]
#     result = ''.join(result)
#
#
#     return print(result)
#
# radix_to_radix(175, 8, 2)




# print()
# print(base_to_dec(5, 8))


# def radix_to_radix(n, radix1, radix2):
#     result = []
#     if radix1 > radix2:
#         while not n//radix2 < radix2:
#             result.append(n%radix2)
#             n = n//radix2
#
#         result.append(n%radix2)
#         result.append(n//radix2)
#     result.reverse()
#     result = [str(x) for x in result]
#     result = ''.join(result)
#
#
#     return print(result)

# radix_to_radix(80, 10, 8)




#number를 decimal로 convert하는 함수
def convert_to_dec(num_str,base):
    if not num_str.isdigit() and not num_str in 'A' or 'B' or 'C' or 'D' or 'E' or 'F':    #잘못된 알파벳 입력시 Error messege
        return 'worng'

    else:
        num_str = str(num_str)
        num_str = num_str[::-1]     #reverse the string
        num = 0

        for k in range(len(num_str)):
            dig = num_str[k]
            if dig.isdigit():
                dig = int(dig)

            else:
                dig = ord(dig.upper())-ord('A')+10
            num += dig*(base**k)
        return num

#decimal을 원하는 base number로 convert하는 함수
def convert_to_base(num,base):
    base_num = ""

    if num.isdigit() and num < 0:
        return 'wrong'

    while num.isdigit() and num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #uppercase letters 사용

        num //= base

    base_num = base_num[::-1]

    return base_num

number = input('Enter a number : ')
radix1 = int(input('Enter a radix1 : '))
radix2 = int(input('Enter a radix2 : '))

dec_num = convert_to_dec(number, radix1)                #input된 number를 decimal로 convert
result = convert_to_base(dec_num, radix2)               #converting된 decimal(dec_num)을 radix2의 base number로 convert

if result == 'wrong' or dec_num == 'wrong':             #positive number가 아니거나 잘못된 알파벳 입력시 Error messege
    print('Wrong Input')
elif not radix1 and radix2 == 2 or 8 or 10 or 16:       #between 2 and 16 이 아닐경우 Error messege
    print('Wrong Input')

#formatting operator % 사용
else:
    print('[radix_to_radix] %s in based %s is %s in base %s' % (number, radix1, result, radix2))

# if radix1 == 16 and radix2 == 2 or 8 or 10 or 16:
#     print('[radix_to_radix] %s in based %s is %s in base %s' % (number, radix1, result, radix2))
#
# elif radix1 == 2 or 8 or 10 and radix2 == 2 or 8 or 10 or 16:
#     if int(number) < 0:
#         print('Wrong Input')
#
#     else:
#         print('[radix_to_radix] %s in based %s is %s in base %s' % (number, radix1, result, radix2))
#
# else:
#     print('Wrong Input')