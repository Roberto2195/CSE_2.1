string_list = ["W", "or", "l", "d!"]
int_list = [5, 15, -67, 191, 88, -23]
float_list = [2.2, -101.9, 60.0]
boolean_list = [False, False, True, False, True]
mixed_list = ["Hello", 2, "the", string_list]
empty = []

print(int_list[5])
int_list[5] = 23
print(int_list[5])

if "Hello" in mixed_list:
    print("It was there!")
    print("Condition")