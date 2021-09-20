with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    lines = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
    for n in lines:
        print(n)
