import time
start_time = time.time()
d = 0
for i in range(10000000):
    d += i*294908757
# print('Enter an integer value between 5 and 10')
# while True:
#     try:
#         # value = int(input())
#         value = int("6")
#         if value >= 5 and value <= 10:
#             print(f"Your input value ({value}) has been accepted.")
#             break
#         else:
#             print(f"You entered {value}. Please enter a number between 5 and 10.")
#     except:
#         print("Sorry, you entered an invalid number, please try again.")
print("--- %s seconds ---" % (time.time() - start_time))