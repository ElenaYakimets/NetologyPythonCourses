residence_limit = 90
schengen_constraint = 180


def date_difference(leave, arrive):
    result = leave - arrive + 1
    return result


def visit_length(visit):
    return date_difference(visit[1], visit[0])


def get_days_for_visits(visits):
    days_for_visits = []
    for visit in visits:
        days_for_visit = 0
        for past_visit in visits:
            if visit[0] - schengen_constraint < past_visit[0] < visit[0]:
                days_for_visit += visit_length(past_visit)
        days_for_visit += visit_length(visit)
        days_for_visits.append(days_for_visit)
    return days_for_visits


def print_days_future_visit(visits, date_in_future):
    visits_for_future = visits + [[date_in_future, date_in_future]]
    days_for_future_visits = get_days_for_visits(visits_for_future)
    days_in_es = residence_limit - days_for_future_visits[len(days_for_future_visits) - 1] + 1
    print('Если въедем %s числа, сможем провести в шенгене %s дней' % (date_in_future, days_in_es))

    assert days_in_es == 90 - 20 - 20


def print_residence_limit_violation(visits):
    days_for_visits = get_days_for_visits(visits)

    for visit, total_days in zip(visits, days_for_visits):
        if total_days > residence_limit:
            overstay_time = total_days - residence_limit
            print('Во время визита', visit, 'количество время пребывания превышено на', overstay_time, 'дней')


visits = [[1, 10], [61, 90], [101, 140], [141, 160], [271, 290]]

# бесконечный цикл
while True:
    # выбор режима
    print('Введите v, чтобы добавить визит')
    user_input = input()
    if user_input == 'v':
        print('Начало (введите номер календарного дня):')
        start = int(input())
        print('Конец (введите номер календарного дня):')
        end = int(input())
        visits.append([start, end])
    print_residence_limit_violation(visits)