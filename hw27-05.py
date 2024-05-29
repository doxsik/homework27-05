weight = int(input('Ваш вес(кг):'))           #вес

height = int(input('Ваш рост(см):'))          #рост

bmi = int(weight/(height/100)**2)             #индекс массы тела

print(f'Ваш индекс массы тела: {bmi}')

rnge = list(f'16{'='*(40-16)}40')             #шкала

rnge[bmi-16] = '|'                            #добавление палочки в шкалу

print("".join(rnge))
