#Take a full name as input. Print it in uppercase, in lowercase, reversed, and print its length. Use at least three different string methods.
name=input("Enter your name:")
print("Uppercase:",name.upper())
print("Lowercase:",name.lower())
print("Reversed:",name[::-1])
print("Length:",len(name))