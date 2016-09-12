MONTHS = {
    'January': 0,
    'February': 1,
    'March': 2,
    'April': 3,
    'May': 4,
    'June': 5,
    'July': 6,
    'August': 7,
    'September': 8,
    'October': 9,
    'November': 10,
    'December': 11
}
LENGTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

DAYS = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}


def _is_leap(year):
    return year % 4 == 0

# calcolare il numero di settimane di un certo range (A, B)
def solution(Y, A, B, W):
    # giorni dell'inizio anno da togliere visto che il primo dell'anno non parte sempre da lunedi
    days_initial = (7 - DAYS[W]) % 7
    # giorni prima del primo mese del range (A, B)
    days_before = sum(LENGTHS[:MONTHS[A]]) - days_initial
    # giorni del periodo scelto
    days_period = sum(LENGTHS[MONTHS[A]:MONTHS[B]+1])
    # se bisestile e il mese A da calcolare e prima e` dopo febbraio aggiungi un giorno
    if _is_leap(Y):
        if MONTHS[A] >= 2:
            days_before += 1
        else:
            days_period += 1
    # giorni di inizio mese A da togliere se la settimana e` spezzata
    off_set = (7 - (days_before % 7)) % 7
    # numero settimane
    return (days_period - off_set) / 7


if __name__ == '__main__':
    print solution(2016, 'August', 'October', 'Friday')  # Leap
    print solution(2015, 'August', 'October', 'Thursday')  # Non leap