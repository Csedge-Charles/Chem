import random
import func



pressure = 1013 + random.randint(-20, 20)

volume = float(random.randint(40, 50))


def two_deci(x):
    x *= 100
    x = round(x)
    return x / 100

temp_list = [20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0,
             24.5, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0]
temp_dict = {
    20.0 : 23.4,
    20.5 : 24.1,
    21.0 : 24.9,
    21.5 : 25.7,
    22.0 : 26.4,
    22.5 : 27.2,
    23.0 : 28.1,
    23.5 : 29.0,
    24.0 : 29.8,
    24.5 : 31.0,
    25.0 : 31.7,
    26.0 : 33.6,
    27.0 : 35.7,
    28.0 : 37.8,
    29.0 : 40.1,
    30.0 : 42.5,
}

temp = random.choice(temp_list)

vapor_pressure = temp_dict[temp]

moles = ((pressure - vapor_pressure) / 1013) * (volume / 1000) / (0.0821 * (temp + 273))

moles *= 24.305

mass = two_deci(moles * 1000) + random.randint(-20, 20) / 100



R = ((pressure - vapor_pressure) / 1013 * (volume / 1000)) / (((mass / 1000)/ 24.305)* (temp + 273))



print()
print()
template_1 = f'In a chemical experiment, hydrogen gas is collected over water. The air pressure is {pressure}hpa at {temp}º celsius'
template_2 = f'During the reaction, pure magnesium, which weighs {mass}mg, reacts with hydrochloric acid to produce magnesium chloride.'
template_3 = f'It produced a biproduct of hydrogen gas with a volume of {volume}mL. Find the R value given that the' 
template_4 = f'molar mass of magnesium is 24.305 g/mol, and the water vapor pressure at {temp}ºC is {vapor_pressure}hpa'

print(template_1)
print()
print(template_2)
print()
print(template_3)
print()
input(template_4 + ': ')
print()
print()
print(R)
print()
print()
            
