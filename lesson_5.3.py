from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

str = (n for n in zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(*islice(str, 7))
print(type(str))

print(next(str)) #StopIteration
