import math

def isPrime(x:int):
    ctrl = True
    for i in range(2, int(math.sqrt(x)) +1):
        if x%i == 0: ctrl = False
    return ctrl

'''
Does not work well with exponents that are power of 2
'''
def squareNMultiply(base:int, exp:int, modulo:int):
    exp_list = []
    temp_mult = 1
    while exp != 0:
        power = getGreatestPower(exp, 2)
        exp_list.insert(0,power)
        exp -= power

    for index, i in enumerate(exp_list):
        if index == 0: l = math.pow(base,i) %modulo
        else: l = (l*l) %modulo
        temp_mult = (temp_mult* l) % modulo
        if index != len(exp_list)-1:
            sliding = i
            while (exp_list[index+ 1] /sliding) != 2:
                sliding *= 2
                l = (l*l) %modulo
    return int(temp_mult)

def getGreatestPower(num:int, base:int):
    return int(math.pow(base, int(math.log(num, base))))


def Bezout(a:int, b:int):
    sn1 = 1
    sn = 0
    tn1 = 0
    tn = 1
    temp = 0
    while (r := a%b) != 0:
        #Calculation
        temp = r
        q = int(a/b)
        s = -sn*q + sn1
        t = -tn*q + tn1

        #Substitution
        a = b
        b = r
        sn1 = sn
        tn1 = tn
        sn = s
        tn = t
    return (temp,s,t)

def getGCD(a:int, b:int): return Bezout(a,b)[0]

def getMCM(a:int, b:int): return int((a*b)/getGCD(a,b))


#TODO : Incomplete and really confusing
def isGenerator(seed:int, base:int):
    count = 0
    temp:int = 1
    while count < base - 1:
        if ((temp := temp * seed) % base) not in [1, seed]:
            count += 1
        else:
            return False if count < base - 2 else True
    return True
    pass

def point_sum(modulo,a, x1,y1):
    l = Bezout((2* y1)%modulo, modulo)
    x = (((3* (x1**2) +a)*(l[1]))**2 -2*x1 )%modulo
    y = (-y1 +(((3*(x1**2)+a)*(l[1]))*(x1 -x)))%modulo
    return x,y


def points_sum(modulo, x1,y1, x2,y2):
    l = Bezout((x1-x2)%modulo, modulo)
    x = (((y1-y2)*(l[1]))**2 -x1 -x2 )%modulo
    y = ((y1-y2)*(l[1])*(x1 -x) -y1)%modulo
    return x,y

def point_multiples(modulo, a, x,y, mul):
    print("({},{})^{} = ({},{})".format(x,y,1,x,y))
    xnew = x
    ynew = y
    for i in range(2,mul+1):
        if(x == xnew and (x,y) !=(xnew,ynew)):
            if i == 1:
                continue
            else:
                print("Si arriva solo a {}*({},{})".format(i, x, y))
                break
        else:
            xnew, ynew = point_sum(modulo,a,x,y) if (x,y) == (xnew,ynew) else points_sum(modulo,x,y,xnew, ynew)
            print("({},{})^{} = ({},{})".format(x,y,i,xnew, ynew))


def rho(n):
    counter = 1
    x = 2
    x = ((x**2)%n +1)%n
    last_square = (((x**2 +1)**2 )%n +1)%n
    print(counter)
    counter+=1
    while((d := getGCD(abs(x -last_square),n)) == 1):
        print(counter)
        counter+=1
        x = ((x**2)%n +1)%n
        last_square = (((x**2 +1)**2)%n +1)%n
        pass
    return d, int(n/d)
