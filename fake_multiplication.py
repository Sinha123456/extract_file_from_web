import random
def wrongMul(number):
    wrong = random.randint(0,9)
    table = [i*number  for i in range(1,11)]
    table[wrong] = table[wrong]+ random.randint(0,10)
    return table

def correctMul(table,number):
    for i in range(1,11):
        if table[i-1] != i*number:
           return i-1
           return None


if __name__ == '__main__':
    #print(wrongMul(8))
    number = int(input("Enter the number: "))
    myTable = wrongMul(number)
    print(myTable)
    wrongIndex = correctMul(myTable, number)
    print(f" The table is wrong at index {wrongIndex}")
