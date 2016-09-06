import random


def secret_santa(elements):
    tmp = elements[:]
    result = []*len(elements)
    i = 0
    while len(tmp) > 0:
        # randint ritorna un numero random
        x = random.randint(0, len(tmp)-1)
        # finche 2 elementi di due liste diverse sono uguali continua ad estrarre numeri random( come se fossero degli
        # if ripetuti in cascata
        while tmp[x] == elements[i]:
            x = random.randint(0, len(tmp)-1)
        # rimuovi l'elemento dal bussolotto tmp
        popEl = tmp.pop(x)
        # crea la lista di tuple randomiche
        result.append((elements[i], popEl))
        i += 1
    return result


def extract_one(bussolotto):
    return random.randint(0, len(bussolotto) - 1)


def is_valid(extracted, element):
    if extracted == element:
        return False
    else:
        return True


def remove_from(bussolotto, index):
    return bussolotto.pop(index)


def append_result(result, pop_el, element):
    result.append((element, pop_el))


def secret_santa_2(elements):
    bussolotto = elements[:]
    result = [] * len(elements)
    i = 0
    while len(bussolotto) > 0:
        extracted_index = extract_one(bussolotto)
        extracted = bussolotto[extracted_index]
        if len(bussolotto) == 2 and not is_valid(bussolotto[-1], elements[-1]):
            append_result(result, bussolotto[0], elements[-1])
            append_result(result, bussolotto[1], elements[i])
            del bussolotto[:]
            break
        if is_valid(extracted, elements[i]):
            pop_el = remove_from(bussolotto, extracted_index)
            append_result(result, pop_el, elements[i])
            i += 1
    return result

if __name__ == '__main__':
    elements = ['a', 'b', 'c', 'd']
    print secret_santa(elements)
