#1. Arithmetic Operators
a = 10
b = 5

print("Addition:", a + b)        # Output: 15
print("Subtraction:", a - b)     # Output: 5
print("Multiplication:", a * b)  # Output: 50
print("Division:", a / b)        # Output: 2.0
print("Floor Division:", a // b) # Output: 2
print("Modulus:", a % b)        # Output: 0
print("Exponentiation:", a ** b) # Output: 100000

#2. Comparison Operators

x = 10
y = 20
print("Equal to:", x == y)       # Output: False
print("Not equal to:", x != y)   # Output: True
print("Greater than:", x > y)    # Output: False
print("Less than:", x < y)       # Output: True
print("Greater than or equal to:", x >= y) # Output: False
print("Less than or equal to:", x <= y)    # Output: True

#3. Logical Operators

p = True
q = False
print("Logical AND:", p and q)  # Output: False
print("Logical OR:", p or q)    # Output: True
print("Logical NOT:", not p)    # Output: False

#4. Assignment Operators

c = 10
c += 5  # Equivalent to c = c + 5
print("After += operator:", c)  # Output: 15
c -= 3  # Equivalent to c = c - 3
print("After -= operator:", c)  # Output: 12
c *= 2  # Equivalent to c = c * 2
print("After *= operator:", c)  # Output: 24
c /= 4  # Equivalent to c = c / 4
print("After /= operator:", c)  # Output: 6.0
c //= 2 # Equivalent to c = c // 2
print("After //= operator:", c) # Output: 3.0
c %= 2  # Equivalent to c = c % 2
print("After %= operator:", c)  # Output: 1.0
c **= 3 # Equivalent to c = c ** 3
print("After **= operator:", c) # Output: 1.0

#5. Bitwise Operators

m = 5  # In binary: 0101
n = 3  # In binary: 0011
print("Bitwise AND:", m & n)  # Output: 1 (In binary: 0001)
print("Bitwise OR:", m | n)   # Output: 7 (In binary
print("Bitwise XOR:", m ^ n)  # Output: 6 (In binary: 0110)
print("Bitwise NOT:", ~m)     # Output: -6 (In binary:
print("Left Shift:", m << 1) # Output: 10 (In binary: 1010)
print("Right Shift:", m >> 1) # Output: 2 (In binary:


#6. Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b:", a is b)  # Output: True
print("a is c:", a is c)  # Output: False
print("a == c:", a == c)  # Output: True

#7. Membership Operators

fruits = ["apple", "banana", "cherry"]
print("Is 'banana' in fruits?", "banana" in fruits)  # Output: True
print("Is 'grape' in fruits?", "grape" in fruits)    #
print("Is 'grape' not in fruits?", "grape" not in fruits)  # Output: True


#8. Operator Precedence
result = 10 + 5 * 2  # Multiplication has higher precedence than addition
print("Result of 10 + 5 * 2:", result)  # Output:
result = (10 + 5) * 2  # Parentheses change the precedence
print("Result of (10 + 5) * 2:", result)  # Output


#9. Ternary Operator

age = 18
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)  # Output: Adult

#10. Walrus Operator (Python 3.8+)

n = 5
if (squared := n ** 2) > 20:
    print("Squared value is greater than 20:", squared)  # Output: Squared value is greater than 20: 25


#11. Augmented Assignment Operators

x = 10
x += 5  # Equivalent to x = x + 5
print("After += operator:", x)  # Output: 15
x -= 3  # Equivalent to x = x - 3
print("After -= operator:", x)  # Output: 12
x *= 2  # Equivalent to x = x * 2
print("After *= operator:", x)  # Output: 24
x /= 4  # Equivalent to x = x / 4
print("After /= operator:", x)  # Output: 6.0
x //= 2 # Equivalent to x = x // 2
print("After //= operator:", x) # Output: 3.0
x %= 2  # Equivalent to x = x % 2
print("After %= operator:", x)  # Output: 1.0
x **= 3 # Equivalent to x = x ** 3
print("After **= operator:", x) # Output: 1.0

