from consts import rus_day_of_week_short, rus_day_of_week

__all__ = ['row_prettier', 'week_schedule_prettier', 'day_of_week_to_short']


def day_of_week_to_short(day_of_week: str) -> str:
    return rus_day_of_week_short[rus_day_of_week.index(day_of_week.capitalize())]


def week_schedule_prettier(d: dict) -> str:
    res_str = ''
    for weekday, subjects in d.items():
        res_str += weekday + '\n'
        res_str += ('_' * 12) + '\n'

        if not subjects:
            continue

        for subject in subjects:
            res_str += subject + '\n'

        res_str += ('_' * 12) + '\n\n'

    return res_str


def row_prettier(row: tuple) -> str:
    time = row[1]
    subject = row[2]
    room = row[3]
    teacher = row[4]

    return f'{subject} {room} {time.strftime("%X")} {teacher}'
