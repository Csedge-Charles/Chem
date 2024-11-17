import random
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def string(x):
    string = ''
    for i in x:
        if i != 1:
            string += str(i)
    return string


def gather(reactant_list):
    empt = []
    iterator = 0
    for i in reactant_list:
        if type(i) is str:
            if i not in empt:
                empt.append(i)
        if type(i) is int:
            if reactant_list[iterator - 1] == empt[len(empt) - 1]:
                empt.append(i)
            else:
                for x in range(len(empt)):
                    if empt[x] == reactant_list[iterator - 1]:
                        empt[x + 1] += reactant_list[iterator]
                        break
        iterator += 1
    return empt
        
def string(x):
    y = ''
    for i in x:
        y += i
    return y
      
def list_removal(x):
    new = []
    for i in x:
        if i != '':
            new.append(i)
    return new
     

def repiece(reactant):
    new_list = []
    num = ''
    element = ''
    iterator = 0
    for i in reactant:
        if i in num_list:
            num += i
            if iterator == len(reactant) - 1:
                new_list.append(int(num))
                num = ''
            if iterator + 1 < len(reactant):
                if reactant[iterator + 1] not in num_list:
                    new_list.append(int(num))
                    num = ''
        if i == '(':
            new_list.append('(')
        if i == ')':
            new_list.append(')')
        if i.isupper() and i not in num_list and i != '(' and i != ')':
            element += i
            if iterator + 1 < len(reactant):
                if reactant[iterator + 1].isupper() or reactant[iterator + 1] == '(' or reactant[iterator + 1] == ')' or reactant[iterator + 1] in num_list:
                    new_list.append(element)
                    element = ''
            if iterator == len(reactant) - 1:
                new_list.append(element)
                new_list.append(1)
                element = ''
        if i.isupper() == False and i not in num_list and i != '(' and i != ')':
            element += i
            new_list.append(element)
            element = ''
        iterator += 1
    return new_list


            
def seperate(reactant):
    new_list = []
    reactant = repiece(reactant)
    iterator = 0
    multiplier_2 = 1
    parenthasis = False
    multiplier = 1
    for i in range(len(reactant)):
        if reactant[i] == ')':
            multiplier_2 = reactant[i + 1]
            break
    for i in reactant:
        if i == '(':
            parenthasis = True
        if i == ')':
            break
        if type(i) is int:
            if iterator == 0:
                multiplier = i
            if parenthasis and iterator != 0:
                new_list.append(i * multiplier * multiplier_2)
            if iterator != 0 and parenthasis == False:
                new_list.append(i * multiplier)
        if type(i) is str and i != ')' and i != '(':
            new_list.append(i)
            if iterator + 1 < len(reactant):
                if type(reactant[iterator + 1]) is str and reactant[iterator + 1] != ')' and reactant[iterator + 1] != '(':
                    if parenthasis:
                        new_list.append(multiplier * multiplier_2)
                    else:
                        new_list.append(multiplier)
            if iterator == len(reactant) - 1:
                if parenthasis:
                    new_list.append(multiplier * multiplier_2)
                else:
                    new_list.append(multiplier)
        iterator += 1
        
    return new_list
 


def split(reaction):
    part_1 = ''
    part_2 = ''
    switch = False
    for i in reaction:
        if i == ' ' or i == '+':
            switch = True
        else:
            if switch:
                part_2 += i
            else:
                part_1 += i
    return part_1 + part_2

def lcm(a):
    modulo = 1
    mass = 0
    tell = True
    for i in a:
        mass += i
    for x in range(1, mass):
        tell = True
        for y in a:
            if y % x != 0:
                tell = False
        if tell:
            modulo = x
    return modulo

def match(a, b):
    remake = []
    iteration = 0
    for i in b:
        for n in a:
            if type(i) is str:
                if i == n:
                    remake.append(i)
                    remake.append(a[iteration + 1])
            iteration += 1
        iteration = 0
    return remake
            
def combustion(reactant_1, reactant_2):
    a = reactant_1
    b = reactant_2
    c = 'H2O'
    d = 'CO2'
    reactant_1 = seperate(reactant_1)
    reactant_2 = seperate(reactant_2)
    reactant_3 = seperate('H2O')
    reactant_4 = seperate('CO2')
    coeff_1 = 1
    coeff_2 = 1
    coeff_3 = 1
    coeff_4 = 1
    if 'C' in reactant_1:
        coeff_4 = reactant_1[1]
        if reactant_1[3] % 2 != 0:
            coeff_4 *= 2
            coeff_1 *= 2
            coeff_3 = int(reactant_1[3])
        else:
            coeff_3 = int(reactant_1[3] / 2)
        
        if 'O' in reactant_1:
            if (coeff_4 * 2 + coeff_3 - coeff_1 * reactant_1[5]) % 2 != 0:
                coeff_2 = int(coeff_4 * 2 + coeff_3 - coeff_1 * reactant_1[5])
                coeff_1 *= 2
                coeff_4 *= 2
                coeff_3 *= 2
            else:
                coeff_2 = int((coeff_4 * 2 + coeff_3 - coeff_1 * reactant_1[5]) / 2)
        else:
            if (coeff_4 * 2 + coeff_3) % 2 != 0:
                coeff_2 = int(coeff_4 * 2 + coeff_3)
                coeff_1 *= 2
                coeff_4 *= 2
                coeff_3 *= 2
            else:
                coeff_2 = int((coeff_4 * 2 + coeff_3) / 2)
    if coeff_1 == 1:
        coeff_1 = ''
    if coeff_2 == 1:
        coeff_2 = ''
    if coeff_3 == 1:
        coeff_3 = ''
    if coeff_4 == 1:
        coeff_4 = ''
    return f'{coeff_1}{a} + {coeff_2}{b} -> {coeff_4}{d} + {coeff_3}{c}'
                


def balance(reactant_1, reactant_2, product_1, product_2):
    r_1 = reactant_1
    r_2 = reactant_2
    p_1 = product_1
    p_2 = product_2
    d_r_1 = seperate(r_1)
    d_r_2 = seperate(r_2)
    d_p_1 = seperate(p_1)
    d_p_2 = seperate(p_2)
    while match(gather(d_r_1 + d_r_2), gather(d_p_1 + d_p_2)) != gather(d_p_1 + d_p_2):
        r_1 = reactant_1
        r_2 = reactant_2
        p_1 = product_1
        p_2 = product_2
        coeff_2 = ''
        coeff_4 = ''
        coeff_1 = random.randint(1, 100)
        if reactant_2 != '':
            coeff_2 = random.randint(1, 100)
        coeff_3 = random.randint(1, 100)
        if product_2 != '':
            coeff_4 = random.randint(1, 100)
        r_1 = str(coeff_1) + reactant_1
        r_2 = str(coeff_2) + reactant_2
        p_1 = str(coeff_3) + product_1
        p_2 = str(coeff_4) + product_2
        d_r_1 = seperate(r_1)
        d_r_2 = seperate(r_2)
        d_p_1 = seperate(p_1)
        d_p_2 = seperate(p_2)
    if reactant_2 != '' and product_2 == '':
        factor = lcm([coeff_1, coeff_2, coeff_3])
        coeff_1 = int(coeff_1 / factor)
        coeff_2 = int(coeff_2 / factor)
        coeff_3 = int(coeff_3 / factor)
        if coeff_1 == 1:
            coeff_1 = ''
        if coeff_2 == 1:
            coeff_2 = ''
        if coeff_3 == 1:
            coeff_3 = ''
        return f'{coeff_1}{reactant_1} + {coeff_2}{reactant_2} -> {coeff_3}{product_1}'
    
    if reactant_2 == '' and product_2 != '':
        factor = lcm([coeff_1, coeff_3, coeff_4])
        coeff_1 = int(coeff_1 / factor)
        coeff_4 = int(coeff_4 / factor)
        coeff_3 = int(coeff_3 / factor)
        if coeff_1 == 1:
            coeff_1 = ''
        if coeff_3 == 1:
            coeff_3 = ''
        if coeff_4 == 1:
            coeff_4 = ''
        return f'{coeff_1}{reactant_1} -> {coeff_3}{product_1} + {coeff_4}{product_2}'
    factor = lcm([coeff_1, coeff_2, coeff_3, coeff_4])
    coeff_1 = int(coeff_1 / factor)
    coeff_2 = int(coeff_2 / factor)
    coeff_3 = int(coeff_3 / factor)
    coeff_4 = int(coeff_4 / factor)
    if coeff_1 == 1:
        coeff_1 = ''
    if coeff_2 == 1:
        coeff_2 = ''
    if coeff_3 == 1:
        coeff_3 = ''
    if coeff_4 == 1:
        coeff_4 = ''
    return f'{coeff_1}{reactant_1} + {coeff_2}{reactant_2} -> {coeff_3}{product_1} + {coeff_4}{product_2}'

print(combustion('C26H12O32', 'O2'))

def sigfig(num):
    sigfig = 0
    zero = 0
    count = 0
    deci_count = False
    start = False
    lead = 'none'
    for i in num:
        if deci_count == False:
            if i != '0' and i != '.':
                sigfig += 1
            else:
                if i == '0':
                    zero += 1
                    if count + 1 < len(num):
                        if num[count + 1] != '0':
                            sigfig += zero
                            zero = 0
                else:
                    deci_count = True
                    if count == 0:
                        lead = '0'
                        
                    else:
                        if count == 1:
                            if num[count - 1] == '0':
                                lead = '0'
                                sigfig -= 1
                            else:
                                lead = 'any'
                        else:
                            lead = 'any'
        else:
            if lead == 'any':
                sigfig += 1
            else:
                if i != '0':
                    start = True
                    sigfig += 1
                else:
                    if start == True:
                        sigfig += 1
                    
                
        count += 1
    return sigfig
#If input is a float, then 1.00000 will be considered 1.0 messing up the sig fig count

