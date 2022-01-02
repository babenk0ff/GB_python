from random import sample, randint


def get_jokes(number, repeat=True) -> list[str]:
    """Функция, генерирующая number шуток из трех списков исходных слов.
    По умолчанию (repeat=True) разрешены повторы слов при генерации шуток"""

    # Исходные списки слов
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []  # Итоговый список

    if repeat:
        # В случае разрешения повторяемости слов
        i = 1
        while i <= number:
            joke = list(zip(sample(nouns, 1), sample(adverbs, 1), sample(adjectives, 1)))
            for elem in joke:
                result.append(' '.join(elem))
            i += 1
    else:
        # При запрете повторяемости слов
        if number > 5:  # Ограничение number длиной списков исходных слов
            number = 5
        i = 1
        while i <= number:
            # Ограничение повторяемости слов путем удаления их из списков
            word_1 = nouns.pop(randint(0, len(nouns) - 1))
            word_2 = adverbs.pop(randint(0, len(adverbs) - 1))
            word_3 = adjectives.pop(randint(0, len(adjectives) - 1))
            # Добавление шутки в итоговый список
            result.append(f'{word_1} {word_2} {word_3}')
            i += 1

    return result


print(get_jokes(repeat=False, number=3))
