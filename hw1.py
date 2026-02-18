def check(men_prefs, women_prefs, matching):
    # делаем двухсторонний словарь для удобства {m1: w1, w1: m1} и тд
    partner = {}
    for m, w in matching.items(): # с помощью items превращаем словарь в список с кортежами [(ключ, знач), (ключ, знач)]
        partner[m] = w # мужчине соответсвует женщина
        partner[w] = m # женщине соответствует мужчина
    for man in men_prefs.keys():
        wife = partner[man] # женщина, котрая сейчас у мужчины
        for woman in men_prefs[man]:
            if woman == wife:
                break
            husband = partner[woman]
            # проверка: женщина предпочитает этого мужчину своему текущему партнёру или нет и наоборот
            if women_prefs[woman].index(man) < women_prefs[woman].index(husband) and men_prefs[man].index(woman) < men_prefs[man].index(wife):
                return "Неустойчивое"
    return "Устойчивое"

# таблица распределения женщин по предпочтениям у мужчин
men_prefs = {'M1': ['W1', 'W2', 'W3'],
             'M2': ['W2', 'W1', 'W3'],
             'M3': ['W1', 'W2', 'W3']}

# таблица распределения мужчин по предпочтениям у женщин
women_prefs = {'W1': ['M2', 'M1', 'M3'],
               'W2': ['M1', 'M2', 'M3'],
               'W3': ['M1', 'M2', 'M3']}


matching1 = {'M1': 'W3', 'M2': 'W1', 'M3': 'W2'}
print(f'Проверка паросочетания 1: {matching1}, Вывод: {check(men_prefs, women_prefs, matching1)}')

matching2 = {'M1': 'W1', 'M2': 'W2', 'M3': 'W3'}
print(f'\nПроверка паросочетания 2: {matching2}, Вывод: {check(men_prefs, women_prefs, matching2)}')
