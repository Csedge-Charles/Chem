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
            if parenthasis:
                new_list.append(i * multiplier * multiplier_2)
            else:
                new_list.append(i * multiplier)
        if type(i) is str and i != ')' and i != '(':
            new_list.append(i)
            if type(reactant[iterator + 1]) is str and reactant[iterator + 1] != ')' and reactant[iterator + 1] != '(':
                if parenthasis == True:
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


def reaction(reaction_type, reactant_1, reactant_2):
    reactant_1_copy = seperate(reactant_1)
    reactant_2_copy = seperate(reactant_2)
    total = gather(reactant_1_copy + reactant_2_copy)
    if reaction_type == 'synthesis':
        if 'N' in reactant_1 and 'H' in reactant_2:
            pass
        else:
            count = []
            empt = []
            for i in range(len(total)):
                if type(total[i]) is int:
                    count.append(i)
                    empt.append(total[i])
            factor = lcm(empt)
            for x in range(len(empt)):
                empt[x] = int(empt[x] / factor)
            for i in range(len(count)):
                total[count[i]] = empt[i]
            if factor == 1:
                factor = ''
            return f'{factor}{string(total)}'

def balance(reactant_1, reactant_2, product_1, product_2):  
    multiplier_1 = 1
    multiplier_2 = 2
    if reactant_2 == '':
        reactant_2 = ''
        multiplier_1 = 0
    if product_2 == '':
        product_2 = ''
        multiplier_2 = 0
    coeff_1 = 1
    coeff_2 = 1
    coeff_3 = 1
    coeff_4 = 1
    reactant_1_save = str(coeff_1)+reactant_1
    reactant_2_save = str(coeff_2)+reactant_2
    product_1_save = str(coeff_3)+product_1
    product_2_save = str(coeff_4)+product_2
    
    reactant_1_copy = seperate(reactant_1_save)
    reactant_2_copy = seperate(reactant_2_save)
    reactant_total = gather(reactant_1_copy + reactant_2_copy)
    product_1_copy = seperate(product_1_save)
    product_2_copy = seperate(product_2_save)
    product_total = match(gather(product_1_copy + product_2_copy), reactant_total)
    count = []
    empt = []
    for i in range(len(reactant_total)):
        if type(reactant_total[i]) is int:
            count.append(i)
            empt.append(reactant_total[i])
    count_2 = []
    empt_2 = []
    for i in range(len(product_total)):
        if type(product_total[i]) is int:
            count_2.append(i)
            empt_2.append(product_total[i])
    while reactant_total != product_total:
        reactant_1_save = reactant_1
        reactant_2_save = reactant_1
        product_1_save = product_1
        product_2_save = product_2
        coeff_1 = random.randint(1, 9)
        if reactant_2 != '':
            coeff_2 = random.randint(1, 9)
        coeff_3 = random.randint(1, 9)
        if product_2 != '':
            coeff_4 = random.randint(1, 9)
        reactant_1_save = str(coeff_1)+reactant_1
        reactant_2_save = str(coeff_2)+reactant_2
        product_1_save = str(coeff_3)+product_1
        product_2_save = str(coeff_4)+product_2
        
        reactant_1_copy = seperate(reactant_1_save)
        reactant_2_copy = seperate(reactant_2_save)
        reactant_total = gather(reactant_1_copy + reactant_2_copy)
        product_1_copy = seperate(product_1_save)
        product_2_copy = seperate(product_2_save)
        product_total = match(gather(product_1_copy + product_2_copy), reactant_total)
        count = []
        empt = []
        for i in range(len(reactant_total)):
            if type(reactant_total[i]) is int:
                count.append(i)
                empt.append(reactant_total[i])
        count_2 = []
        empt_2 = []
        for i in range(len(product_total)):
            if type(product_total[i]) is int:
                count_2.append(i)
                empt_2.append(product_total[i])
                
    factor = lcm([coeff_1, coeff_2, coeff_3, coeff_4])
    if reactant_2 == '' and product_2 == '':
        factor = lcm([coeff_1, coeff_3])
        coeff_1 = int(coeff_1 / factor)
        coeff_3 = int(coeff_3 / factor)
        if coeff_1 == 1:
            coeff_1 = ''
        if coeff_3 == 1:
            coeff_3 = ''
        return f'{coeff_1}{reactant_1} -> {coeff_3}{product_1}'
    if reactant_2 == '':
        factor = lcm([coeff_1, coeff_3, coeff_4])
        coeff_1 = int(coeff_1 / factor)
        coeff_3 = int(coeff_3 / factor)
        coeff_4 = int(coeff_4 / factor)
        if coeff_1 == 1:
            coeff_1 = ''
        if coeff_3 == 1:
            coeff_3 = ''
        if coeff_4 == 1:
            coeff_4 = ''
        return f'{coeff_1}{reactant_1} -> {coeff_3}{product_1} + {coeff_4}{product_2}'
    if product_2 == '':
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

