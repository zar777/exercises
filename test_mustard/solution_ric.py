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
    'Thursdat': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}


def _is_leap(year):
    return year % 4 == 0


def solution(Y, A, B, W):
    a_index = MONTHS[A]
    b_index = MONTHS[B]
    days_to_month = sum(LENGTHS[0:a_index+1])
    if _is_leap(Y) and A > 2:
        days_to_month += 1
    days_to_month -= DAYS[W]
    month_offset = 7 - (days_to_month % 7)
    total_days = sum(LENGTHS[a_index:b_index+1]) - month_offset
    return total_days / 7