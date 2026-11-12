# Accept an integer and determine whether it is even or odd using the % operator. Example:
# Enter number: 25 Output: 25 is Odd

number = int(input("Enter number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:print(f"{number} is Odd")