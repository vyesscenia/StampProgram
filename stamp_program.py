"""
start 
get the number of sheets
sheets / 5
round answer to next number
output the result to the user
end
"""

import math

def calculate(sheet):
    answer = sheet/5
    rounded = math.ceil(answer)
    print("shet is : ", sheet)
    print("The answer is: ", answer)
    print("rounded is: ", rounded)
    print("=============================")    
    return rounded

output = calculate(16)

print("the return statement is: ", output)

