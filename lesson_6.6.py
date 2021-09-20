from sys import argv

with open("bakery.csv", "a", encoding="utf-8") as bak_a:
    with open("bakery.csv", "r", encoding="utf-8") as bak_r:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace(".", "").isdigit()]:
            if len(argv) == 3:
                start, finish = map(int, argv[1:])
                print(*(v for i, v in enumerate(bak_r) if start - 1 <= i < finish), sep="")
            if "," in argv[1] or "." in argv[1]:
                if round(float(argv[1].replace(",", ".")), 3) <= 99999.999:
                    print(f'{round(float(argv[1].replace(",", ".")), 3):>010}', file=bak_a)
                else:
                    print("Number must be less than 99 999,999")
            else:
                print(*(v for i, v in enumerate(bak_r) if i >= int(argv[1]) - 1))
        else:
            print(bak_r.read())