# You are completely free to change this variables to check your algorithm.
num1 = 6
num2 = 28


# Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    num1_sum = 0
    num2_sum = 0
    if num1 == num2 or num1 < 1 or num2 < 1:
        return "Invalid"
    elif type(num1) == int and type(num2) == int:
        pass
    else:
        return "Invalid"
    for i in range(1, int(num1 / 2 + 1)):
        if num1 % i == 0:
            #num1_divisor.append(i)
            num1_sum += i
    num1_sum += num1
    for i in range(1, int(num2 / 2 + 1)):
        if num2 % i == 0:
            num2_sum += i
    num2_sum += num2
    if num1_sum / num1  == num2_sum / num2:
        return True
    else:
        return False


# This line prints your method's return so that you can check your output.
print(isFriendlyPair())