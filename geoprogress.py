b=int(input("Введите превый элемнт прогрессии"))
q=int(input("Введите множитель прогрессии"))
n=int(input("Введите номер последнего элемента"))
if b>= -10000 and b<=10000:
    if  q>=1 and q<= 50:
        if n>=2 and n<=100:
            print( b * (q**n - 1) // (q - 1))
        else : 
            print ("Ошибка в переменной")
    elif q==1:
        if n>=2 and n<=100:
            print(b*n)
        else: print ("Ошибка в переменной") 
    else : print ("Ошибка в переменной") 
else : print ("Ошибка в переменной")          
   
           
















