import random
correct=0
##print (random.randint(6,100))
life=5
while life>0:
    quest=random.randint(1,4)
    
    #===========сложение===========
    if quest==1:
        random1=random.randint(1,10+correct*3)
        random2=random.randint(1,10+correct*3)
        otvet=int(input( f"{random1} + {random2} = "))
        if otvet==random1+random2:
            print("правильно (╯°□°）╯︵ ┻━┻ ")
            correct=correct+1
        else:
            print("неправильно ( •_•)>⌐■-■ ")
            life=life-1
        print()
    #===========умножение===========
    elif quest==2:
        random1=random.randint(1,10+correct)
        random2=random.randint(1,10+correct)
        
        otvet=int(input( f"{random1} * {random2} = "))
        if otvet==random1*random2:
            print("правильно ( ´･･)ﾉ(._.`) ")
            correct=correct+1
        else:
            print("неправильно (┬┬﹏┬┬) ")
            life=life-1
        print()
    #===========вычитание===========        
    elif quest==3:
        random1=random.randint(1,10+correct*2)
        random2=random.randint(1,10+correct*2) 
        
        if random1<random2:
            dop=0
            dop=random2
            random2=random1
            random1=dop
            
        otvet=int(input(f"{random1} - {random2} = "))
        
        if otvet==random1-random2:
            print("правильно (❁´◡`❁)")
            correct=correct+1
        else:
            print("неправильно :-( ")
            life=life-1 
        print()
   #===========деление===========                       
    elif quest==4:
        random1=random.randint(1,10+correct)
        random2=random.randint(1,10+correct)
        dop2=random1*random2
    
        otvet=int(input(f"{dop2} / {random1} = "))
        if otvet==dop2/random1:
            print("правильно ༼ つ ◕_◕ ༽つ")
            correct=correct+1
        else:
            print("неправильно ಥ_ಥ")
            life=life-1
        print()
print (f"количество правильных ответов: {correct} ")
