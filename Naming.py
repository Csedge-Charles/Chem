import random
polyatomic_name = ['acetate', 'perbromate', 'bromate', 'bromite', 'hypobromite',
                   'perchlorate', 'chlorate', 'chlorite', 'hypochlorite', 'cyanide',
                  'dihydrogen phosphate', 'bicarbonate', 'hydrogen sulfate', 
                  'hydroxide', 'ammonium', 'dimercury', 'nitrate', 'nitrite', 
                  'permanganate', 'carbonate', 'chromate', 'dichromate','hydrogen phosphate', 'oxalate',
                  'sulfate', 'sulfite', 'arsenate', 'phosphate']
#   ₂   ₃   ₄

# polyatomic_name = ['acetate', 'perbromate', 'hypobromite',
#                    'perchlorate', 'cyanide',
#                   'dihydrogen phosphate', 'bicarbonate', 'hydrogen sulfate', 
#                   'hydroxide', 'ammonium', 'dimercury', 
#                   'permanganate', 'carbonate', 'chromate', 'dichromate','hydrogen phosphate', 'oxalate',
#                    'sulfite', 'arsenate']
# polyatomic_name = ['ammonium', 'dimercury']
polyatomic_dictionary = {
    'acetate': ['acetate','CH₃COO', -1],
    'perbromate': ['perbromate', 'BrO₄', -1],
    'bromate': ['bromate', 'BrO₃', -1], 
    'bromite': ['bromite', 'BrO₂', -1], 
    'hypobromite': ['hypobromate', 'BrO', -1], 
    'perchlorate': ['perchlorate', 'ClO₄', -1],
    'chlorate': ['chlorate', 'ClO₃', -1], 
    'chlorite': ['chlorite', 'ClO₂', -1], 
    'hypochlorite': ['hypochlorate', 'ClO', -1],
    'cyanide': ['cyanide', 'CN', -1],
    'dihydrogen phosphate': ['dihydrogen phosphate', 'H₂PO₄', -1],
    'bicarbonate' : ['bicarbonate','HCO₃', -1],
    'hydrogen sulfate' : ['hydrogen sulfate', 'HSO₄', -1],
    'hydroxide' : ['hydroxide', 'OH', -1],
    'ammonium' : ['ammonium', 'NH₄', 1],
    'dimercury' : ['dimercury', 'Hg₂', 2],
    'nitrate' : ['nitrate', 'NO₃', -1],
    'nitrite' : ['nitrite', 'NO₂', -1],
    'permanganate' : ['permanganate', 'MnO₄', -1],
    'carbonate' : ['carbonate', 'CO₃', -2],
    'chromate' : ['chromate', 'CrO₄', -2],
    'dichromate' : ['dichromate', 'Cr₂O₇', -2],
    'hydrogen phosphate': ['hydrogen phosphate', 'HPO₄', -2],
    'oxalate' : ['oxalate', 'C₂O₄', -2],
    'sulfate' : ['sulfate', 'SO₄', -2],
    'sulfite' : ['sulfite', 'SO₃', -2],
    'arsenate' : ['arsenate', 'AsO₄', -3],
    'phosphate' : ['phosphate', 'PO₄', -3],
}

minus_1_list = ['fluoride', 'chloride', 'bromide', 'iodide',
                'acetate', 'perbromate', 'bromate', 'bromite',
                'hypobromite', 'perchlorate', 'chlorate',
                'hypochlorite', 'chlorite', 'cyanide',
                'dihydrogen phosphate', 'bicarbonate',
                'hydrogen sulfate', 'hydroxide']

f_block = ['lanthanum', 'cerium', 'praseodymium', 'niodymium', 'promethium', 'samarium', 'europium', 'gadolinium',
           'terbium', 'Dysprosium', 'holmium', 'erbium', 'thulium', 'ytterbium', 'lutetium',
           'actinium', 'thorium', 'protactinium', 'uranium', 'neptunium', 'plutonium', 'americium', 'curium', 'berkelium',
           'californium', 'einsteinium', 'fermium', 'mendelevium', 'nobelium', 'lawrencium']
properties = [3, 'many', 'many', 3, 3, 'many', 'many', 3, 'many', 3, 3, 3, 'many', 'many', 3, 
              3, 4, 'many', 'many', 'many', 'many', 'many', 'many', 'many', 'many', 3, 3, 3, 'many', 3]

charge_minus_1 = {
    'fluoride' : 'F',
    'chloride' : 'Cl',
    'bromide' : 'Br',
    'iodide' : 'I',
    'acetate': 'CH₃COO',
    'perbromate': 'BrO₄',
    'bromate': 'BrO₃', 
    'bromite': 'BrO₂', 
    'hypobromite': 'BrO', 
    'perchlorate': 'ClO₄',
    'chlorate': 'ClO₃', 
    'chlorite': 'ClO₂', 
    'hypochlorite': 'ClO',
    'cyanide': 'CN',
    'dihydrogen phosphate': 'H₂PO₄',
    'bicarbonate' : 'HCO₃',
    'hydrogen sulfate' : 'HSO₄',
    'hydroxide' : 'OH',
}

minus_2_list = ['Oxide', 'Sulfide', 'Selenide', 'carbonate',
                'chromate', 'dichromate', 'hydrogen phosphate',
                'oxalate', 'sulfate', 'sulfite']

charge_minus_2 = {
    'Oxide' : 'O',
    'Sulfide' : 'S',
    'Selenide' : 'Se',
    'carbonate' : 'CO₃',
    'chromate' : 'CrO₄',
    'dichromate' : 'Cr₂O₇',
    'hydrogen phosphate': 'HPO₄',
    'oxalate' : 'C₂O₄',
    'sulfate' : 'SO₄',
    'sulfite' : 'SO₃',
    

}

plus_1_list = ['Hydrogen', 'Lithium', 'Sodium', 
               'Potassium', 'Rubidium', 'Cesium', 
               'Francium', 'Copper(I)', 'Silver(I)', 
               'Gold(I)',  'Mercury(I)', 'Silver']
charge_plus_1 = {
    'Hydrogen' : 'H',
    'Lithium' : 'Li',
    'Sodium' : 'Na',
    'Potassium' : 'K',
    'Rubidium' : 'Rb',
    'Cesium' : 'Cs',
    'Francium' : 'Fr',
    'Copper(I)' : 'Cu',
    'Silver(I)' : 'Ag',
    'Gold(I)' : 'Au',
    'Mercury(I)' : 'Hg',
    'Silver' : 'Ag',
}
plus_2_list = ['Beryllium', 'Magnesium', 'Calcium', 
               'Strongtium', 'Rubidium', 'Barium', 
               'Radium', 'Vanadium(II)', 'Chromium(II)', 
                'Manganese(II)', 'Platinum(II)', 'Copper(II)', 
                'Cadmium', 'Zinc']
charge_plus_2 = {
    'Beryllium' : 'Be',
    'Magnesium' : 'Mg',
    'Calcium' : 'Ca',
    'Strongtium' : 'Sr',
    'Rubidium' : 'Rb',
    'Barium' : 'Ba',
    'Radium' : 'Ra',
    'Vanadium(II)' : 'V',
    'Chromium(II)' : 'Cr',
    'Manganese(II)' : 'Mn',
    'Platinum(II)' : 'Pt',
    'Copper(II)' : 'Cu',
    'Cadmium' : 'Cd',
    'Zinc' : 'Zn',
    
}

plus_3_list = ['Boron', 'Aluminum', 'Gallium',
               'Indium', 'Scandium', 'Yttrium', 
               'Iron(III)', 'Vanadium(III)',
               'Iridium(III)', 'Osmium(III)',
               'Tungsten(III)', 'Gold(III)',  'Niobium(III)',
               'Manganese(III)']

charge_plus_3 = {
    'Boron' : 'B',
    'Aluminum' : 'Al',
    'Gallium' : 'Ga',
    'Indium' : 'In',
    'Scandium' : 'Sc',
    'Yttrium' : 'Y',
    'lanthanum' : 'la',
    'Iron(III)' : 'Fe',
    'Vanadium(III)' : 'V',
    'Iridium(III)' : 'Ir',
    'Osmium(III)' : 'Os',
    'Tungsten(III)' : 'W',
    'Gold(III)' : 'Au',
    'Niobium(III)' : 'Nb',
    'Manganese(III)' : 'Mn',
    
}
number_list = ['', '','₂', '₃', '₄']
number_list_2 = ['', '','2', '3', '4']
atom_list = [plus_1_list, plus_2_list, plus_3_list]
minus_list = [minus_1_list, minus_2_list]
dict_list = [charge_plus_1, charge_plus_2, charge_plus_3]
dict_list_2 = [charge_minus_1, charge_minus_2]



for i in range(100):
    charge_number = random.randint(1, 3)
    greater_charge = random.randint(1, 2)
    ionic_list = atom_list[charge_number - 1]
    ion = random.choice(ionic_list)
    dic = dict_list[charge_number - 1]
    atom = dic[ion]
    
    ionic_list_2 = minus_list[greater_charge - 1]
    ion_2 = random.choice(ionic_list_2)
    dic_2 = dict_list_2[greater_charge - 1]
    atom_2 = dic_2[ion_2]
    
    number_1 = ''
    parentheses_1 = ''
    parentheses_2 = ''
    parentheses_3 = ''
    parentheses_4 = ''
    number_2 = ''
    polyatomic_atom = random.choice(polyatomic_name)
    polyatomic_info = polyatomic_dictionary[polyatomic_atom]
    choice = random.randint(2, 3)

    if choice == 1:
        print()
        print()
        input(f'What is the charge of {random.choice([polyatomic_atom, polyatomic_info[1]])}: ')
        print()
        print(polyatomic_info[2])
        print()
        print()
        
    if choice == 2:
        
        
        
        if polyatomic_info[2] < 0:
            if round(-1 * polyatomic_info[2]) < charge_number:
                parentheses_1 = '('
                parentheses_2 = ')'
                number_2 = number_list[int(-1 * charge_number / polyatomic_info[2])]
                if polyatomic_info[2] == -2 and charge_number == 3:
                    number_2 = '₃'
                    number_1 = '₂'
            if round(-1 * polyatomic_info[2]) > charge_number:
                number_1 = number_list[int(-1 * polyatomic_info[2]/ charge_number)]
                if polyatomic_info[2] == -3 and charge_number == 2:
                    number_2 = '₂'
                    number_1 = '₃'
        
            print()
            print()
            ans = input(f'{atom}{number_1}{parentheses_1}{polyatomic_info[1]}{parentheses_2}{number_2}: ')
            print()
            if ans.upper() == f'{ion} {polyatomic_atom}'.upper():
                print('Correct')
            else:
                print(f'Wrong: {ion} {polyatomic_atom}')
            print()
        else:
            if round(polyatomic_info[2]) < greater_charge:
                if atom_2 != 'F' and atom_2 != 'Cl' and atom_2 != 'Br' and atom_2 != 'I' and atom_2 != 'O' and atom_2 != 'S' and atom_2 != 'Se':
                    parentheses_1 = '('
                    parentheses_2 = ')'
                number_2 = number_list[int(greater_charge / polyatomic_info[2])]
            if round(polyatomic_info[2]) > greater_charge:
                parentheses_3 = '('
                parentheses_4 = ')'
                number_1 = number_list[int(polyatomic_info[2]/ greater_charge)]
                
            print()
            print()
            ans = input(f'{parentheses_1}{polyatomic_info[1]}{parentheses_2}{number_2}{parentheses_3}{atom_2}{parentheses_4}{number_1}: ')
            print()
            if ans.upper() == f'{polyatomic_atom} {ion_2}'.upper():
                print('Correct')
            else:
                print(f'Wrong: {polyatomic_atom} {ion_2}')
            print()
    if choice == 3:
        
        
        
        if polyatomic_info[2] < 0:
            if round(-1 * polyatomic_info[2]) < charge_number:
                parentheses_1 = '('
                parentheses_2 = ')'
                number_2 = number_list[int(-1 * charge_number / polyatomic_info[2])]
                if polyatomic_info[2] == -2 and charge_number == 3:
                    number_2 = '₃'
                    number_1 = '₂'
            if round(-1 * polyatomic_info[2]) > charge_number:
                number_1 = number_list[int(-1 * polyatomic_info[2]/ charge_number)]
                if polyatomic_info[2] == -3 and charge_number == 2:
                    number_2 = '₂'
                    number_1 = '₃'
        
            print()
            print()     
            print('Use ₂ ₃ ₄ ₇ to write out the formula for')
            print()
            print()
            ans = input(f'{ion} {polyatomic_atom}: ')
            print()
            print()
            if ans.upper() == f'{atom}{number_1}{parentheses_1}{polyatomic_info[1]}{parentheses_2}{number_2}'.upper():
                print('Correct')
            else:
                print(f'Wrong: {atom}{number_1}{parentheses_1}{polyatomic_info[1]}{parentheses_2}{number_2}')
            print()
        else:
            if round(polyatomic_info[2]) < greater_charge:
                if atom_2 != 'F' and atom_2 != 'Cl' and atom_2 != 'Br' and atom_2 != 'I' and atom_2 != 'O' and atom_2 != 'S' and atom_2 != 'Se':
                    parentheses_1 = '('
                    parentheses_2 = ')'
                number_2 = number_list[int(greater_charge / polyatomic_info[2])]
            if round(polyatomic_info[2]) > greater_charge:
                parentheses_3 = '('
                parentheses_4 = ')'
                number_1 = number_list[int(polyatomic_info[2]/ greater_charge)]
                
            print()
            print()
            print('Use ₂ ₃ ₄ to write out the formula for')
            print()
            print()
            ans = input(f'{polyatomic_atom} {ion_2}: ')
            print()
            print()
            if ans.upper() == f'{parentheses_1}{polyatomic_info[1]}{parentheses_2}{number_2}{parentheses_3}{atom_2}{parentheses_4}{number_1}'.upper():
                print('Correct')
            else:
                print(f'Wrong: {parentheses_1}{polyatomic_info[1]}{parentheses_2}{number_2}{parentheses_3}{atom_2}{parentheses_4}{number_1}')
            print()
    
    
    if choice == 4:
        pick = random.randint(0, 29)
        print()
        print()
        ans = input(f'Write the charge of {f_block[pick]}. If there are multiple, write "many": ')
        print()
        print()
        if ans == str(properties[pick]):
            print('Correct')
        else:
            print(f'Wrong: {properties[pick]}')          
        