def solution(today, terms, privacies):
    to_year, to_month, to_days = map(int,today.split("."))
    termDict = dict()
    targets = []
    answer = []
    for line in terms:
        key, val = line.split()
        termDict[key] = int(val)
    for lines in privacies:
        line, key = lines.split()
        add_month = termDict[key]
        year, month, days = map(int,line.split("."))
        month += add_month
        days -= 1
        if days == 0:
            days = 28
            month -= 1
            if month == 0:
                month = 12
                year -=1
        add_year = 0
        if month > 12:
            month -= 1
            add_year = month//12
            month %= 12
            month += 1
        year += add_year
        targets.append((year, month, days))
    i = 1
    for y, m, d in targets:
        if y < to_year:
            answer.append(i)
        elif y == to_year and m < to_month:
            answer.append(i)
        elif y == to_year and m == to_month and d < to_days:
            answer.append(i)
        i += 1
    return answer
