list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list2 = []
for sym in list1:
    if sym.replace('+', '').replace('-', '').isdigit():
        if sym.isdigit():
            sym = f'"{int(sym):02d}"'
        else:
            sym = f'"{sym[0]}{int(sym[1:]):02d}"'
    list2.append(sym)

print(' '.join(list2))
