print ('Массив:')
import random
Array = ([random.randint(0, 100) for i in range(15)])
print (Array)
print ('Числа кратные 3')
for i in range(len(Array)):
        if (Array[i]%3==0):
            print(Array[i])
input ('Press Enter to exit')
