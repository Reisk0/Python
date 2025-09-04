#MODULO WEB

"""
Answer = "Hello, World!"
print (Answer)
"""

n = 3

if n % 2 != 0:  # n impar
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")