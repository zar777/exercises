import operator

from transaction import Transaction


class Store():

    def topReport(self, trans_list):
        # riportare i prodotti piu venduti in una lista dal piu venduto al meno venduto(i primi 10)
        occurrence = {}
        for el in trans_list:
            if el.description in occurrence:
                occurrence[el.description] += 1
            else:
                occurrence[el.description] = 1
        # lista di tuple (nome_prodotto, n-ocorrenze) ordinato secondo il n-occorrenze ( reverse order)
        sorted_tuple = sorted(occurrence.items(), key=operator.itemgetter(1), reverse=True)
        result = [i[0] for i in sorted_tuple]
        return result[:11]

    def topReport_cmp(self, trans_list):
        # stessa cosa con il comparatore pero e lambda function o comparator esterno(deve avere sempre variabili)
        # quindi per usare il dictionary occurrence devo per forza definirlo dentro questa funzione top_report_cmp
        occurrence = {}
        for el in trans_list:
            if el.description in occurrence:
                occurrence[el.description] += 1
            else:
                occurrence[el.description] = 1
        keys = occurrence.keys()
        # def comparator(v1, v2):
        #     return occurrence[v1] - occurrence[v2]
        result = sorted(keys, cmp=lambda v1, v2: occurrence[v1] - occurrence[v2], reverse=True)
        return result[:11]




if __name__ == '__main__':
    transactions = []
    transactions.append(Transaction('a', 500, 20))
    transactions.append(Transaction('a', 500, 20))
    transactions.append(Transaction('a', 500, 20))
    transactions.append(Transaction('a', 500, 20))
    transactions.append(Transaction('b', 500, 20))
    transactions.append(Transaction('b', 500, 20))
    transactions.append(Transaction('b', 500, 20))
    transactions.append(Transaction('c', 500, 20))
    transactions.append(Transaction('c', 500, 20))
    transactions.append(Transaction('d', 500, 20))
    transactions.append(Transaction('d', 500, 20))
    transactions.append(Transaction('e', 500, 20))
    transactions.append(Transaction('e', 500, 20))
    transactions.append(Transaction('f', 500, 20))
    transactions.append(Transaction('f', 500, 20))
    transactions.append(Transaction('zsef', 500, 20))
    transactions.append(Transaction('sdf', 500, 20))
    transactions.append(Transaction('sef', 500, 20))
    transactions.append(Transaction('sef', 500, 20))
    transactions.append(Transaction('zzzzz', 500, 20))
    transactions.append(Transaction('zzzzz', 500, 20))
    transactions.append(Transaction('zzzzz', 500, 20))
    transactions.append(Transaction('yyyyy', 500, 20))
    transactions.append(Transaction('yyyyy', 500, 20))
    transactions.append(Transaction('yyyyy', 500, 20))
    transactions.append(Transaction('yyyyy', 500, 20))
    transactions.append(Transaction('yyyyy', 500, 20))
    transactions.append(Transaction('poiuytrew', 500, 20))
    transactions.append(Transaction('hgfds', 500, 20))
    transactions.append(Transaction('bvcx', 500, 20))
    transactions.append(Transaction('qwera', 500, 20))
    transactions.append(Transaction('atufydrbgvf', 500, 20))
    store = Store()
    print store.topReport(transactions)
    print store.topReport_cmp(transactions)
