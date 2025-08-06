# # print("Hellow world")
# # print ("Kiran Gawade")
# # print(23)
# # print(23+4)
# # name="kiran"
# # print(name)
# # print(7%2)
# # print("My name is :",name)
# # print("")
# # print(name+" this is my name")
# # a=23
# # print(a)

# a=2
# b=5
# sum=a+b
# print(sum)
# print("The sum of",a,"and",b,"is",sum)
# print(a+b)
# def reverse_string(s):
#     reversed_str = ''
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str

# user_input = input("Enter a string to reverse: ")
# print("Reversed string:", reverse_string(user_input))

# a="kiran is my name"
# print(type(a))
# print(a[0:5])
# print(a[0:1:2])
# aeiou
# user_input = input("Enter a string to reverse: ")
# print("Reversed string:", reverse_string(user_input))
# user_input= input("Enter a string: ")
# print("Number of vowels in the string:", counnt_vowels(user_input))

#to find the number of vowels in a string using a loop
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

user_input = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(user_input))

def count_vowels(s):
    vowels="aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
user_input = input("enter a sring")
    