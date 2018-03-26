import random


class Dictogram(dict):
    def __init__(self, iterable=None):
        # Инициализируем наше распределение как новый объект класса,
        # добавляем имеющиеся элементы
        dict.__init__(self)
        self.types = 0  # число уникальных ключей в распределении
        self.tokens = 0  # общее количество всех слов в распределении
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        # Обновляем распределение элементами из имеющегося
        # итерируемого набора данных
        for item in iterable:
            if item in self:
                self[item] += 1
                self.tokens += 1
            else:
                self[item] = 1
                self.types += 1
                self.tokens += 1

    def count(self, item):
        # Возвращаем значение счетчика элемента, или 0
        if item in self:
            return self[item]
        return 0

    def return_random_word(self):
        return random.sample(self, 1)[0]

    def return_weighted_random_word(self):
        # Сгенерировать псевдослучайное число между 0 и (n-1),
        # где n - общее число слов
        random_int = random.randint(0, self.tokens-1)
        index = 0
        list_of_keys = list(self.keys())
        # вывести 'случайный индекс:', random_int
        for i in range(0, self.types):
            index += self[list_of_keys[i]]
            # вывести индекс
            if(index > random_int):
                # вывести list_of_keys[i]
                return list_of_keys[i]


def make_higher_order_markov_model(markov_model, order, data):
    if markov_model is None:
        markov_model = dict()

    for i in range(0, len(data)-order):
        # Создаем окно
        window = tuple(data[i: i+order])
        # Добавляем в словарь
        if window in markov_model:
            # Присоединяем к уже существующему распределению
            markov_model[window].update([data[i+order]])
        else:
            markov_model[window] = Dictogram([data[i+order]])


def generate_random_sentence(length, markov_model):
    # print(markov_model) (Для отладки)
    current_word = random.choice(list(markov_model))
    sentence = [current_word]
    for i in range(length - 1):
        if current_word in set(markov_model):
            current_dictogram = markov_model[current_word]
        else:
            current_dictogram = markov_model[random.choice(list(markov_model))]
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0][0].capitalize()
    return ' '.join(sentence) + '.'
    #return sentence


'''def main():
    print(generate_random_sentence(length, markov_model))


if __name__ == "__main__":
    main()'''
