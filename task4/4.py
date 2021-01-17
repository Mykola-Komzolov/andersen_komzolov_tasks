print ('Введите скобочную последовательность:')
x = input()
x = str(x)
k = 0
k = int(k)
c = 0
c = int(c)
ch = 0
ch = int(ch)
g = 1
g = int (g)
for i in range (len(x)):
    if x[i] == '[':
        k = k + 1
    elif x[i] == ']':
        k = k - 1
    elif x[i] == '(':
        c = c + 1
    elif x[i] == ')':
        c = c - 1
    if k < 0:
        k = k + 1
        g = 0
        print ('Нет открывающейся скобки для ]')
    elif c < 0:
        c = c + 1
        g = 0
        print ('Нет открывающейся скобки для )')
if (k > 0):
    g = 0
    print ("Не закрытая скобка [")
elif (c > 0):
    g = 0
    print ("Не закрытая скобка (")
if g == 1:
    print ('Всё верно.')
input ('Press enter to exit')