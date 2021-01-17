print ('Введите скобочную последовательность:')
x = input()
x = str(x)
K = 0
K = int(K)
C = 0
C = int(C)
Ch = 0
Ch = int(Ch)
g = 1
g = int (g)
for i in range (len(x)):
    if x[i] == '[':
        K = K + 1
    elif x[i] == ']':
        K = K - 1
    elif x[i] == '(':
        C = C + 1
    elif x[i] == ')':
        C = C - 1
    if K < 0:
        K = K + 1
        g = 0
        print ('Нет открывающейся скобки для ]')
    elif C < 0:
        C = C + 1
        g = 0
        print ('Нет открывающейся скобки для )')
if (K > 0):
    g = 0
    print ("Не закрытая скобка [")
elif (C > 0):
    g = 0
    print ("Не закрытая скобка (")
if g == 1:
    print ('Всё верно.')
input ('Press Enter to exit')
