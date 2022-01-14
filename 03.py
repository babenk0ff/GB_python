def school(names, classes):
    classes_iter = iter(classes)
    for name in names:
        yield name, next(classes_iter, None)


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']

gen = school(tutors, klasses)

i = 1
while i <= len(tutors):
    print(type(next(gen)))
    i += 1
