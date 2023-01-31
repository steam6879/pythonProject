# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#
#     def add(self):
#         result = self.first + self.second
#         return result
#
#     def mul(self):
#         result = self.first * self.second
#         return result
#
#     def sub(self):
#         result = self.first - self.second
#         return result
#
#     def div(self):
#         result = self.first / self.second
#         return result
#
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result
#
#
# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#
#         else:
#             return self.first / self.second
#
# # a = SafeFourCal(4,0)
# # print(a.div())
#
# class Family:
#     lastname = '김'
#
# print(Family.lastname)
# Family.lastname = '박'
# print(Family.lastname)

# add = lambda a, b: a+b
# print(add(5, 2))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b