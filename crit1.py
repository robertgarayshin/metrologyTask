import csv
import math


def cr1(q):
    def openfile():
        f = open('22_var28_Sost_GOST.txt', 'r')
        ls = []
        for line in f:
            line = line.replace(',', '.')
            ls.append(float(line[:-1]))
        return ls

    def average_count():
        a = 0
        for elem in lst:
            a += elem / len(lst)
        return a

    def offset_standard_deviation():
        res = 0
        for i in lst:
            res += (i - avg) ** 2
        return math.sqrt(res / len(lst))

    def counting_d():
        a = 0
        std = offset_standard_deviation()
        for i in lst:
            a += abs(i - avg) / (len(lst) * std)
        return a

    def filling_n():
        ls = []
        for i in range(16, 52, 5):
            ls.append(i)
        return ls

    def inserting_to_dict(fname):
        with open(fname, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if fname == 'q1_1.csv':
                    for i in range(len(n)):
                        q1_1[n[i]] = float(row[i])
                elif fname == 'q1_5.csv':
                    for i in range(len(n)):
                        q1_5[n[i]] = float(row[i])
                elif fname == 'q1_99.csv':
                    for i in range(len(n)):
                        q1_99[n[i]] = float(row[i])
                elif fname == 'q1_95.csv':
                    for i in range(len(n)):
                        q1_95[n[i]] = float(row[i])

    def finding_interval():
        val = len(lst)
        i = 0
        if val >= 51:
            print('over')
        else:
            while not (n[i] < val < n[i + 1]):
                i += 1
            lft = n[i]
            rght = n[i + 1]
            return lft, rght

    def interpolation(x1, y1, x2, y2, x):
        return y1 - (y1 - y2) * (x - x1) / (x2 - x1)

    lst = openfile()
    avg = average_count()
    d = counting_d()
    n = filling_n()

    if q == 0.02:
        q1_1 = dict.fromkeys(n)
        q1_99 = dict.fromkeys(n)

        inserting_to_dict('q1_1.csv')
        inserting_to_dict('q1_99.csv')

        left, right = finding_interval()

        bigger = interpolation(left, q1_1[left], right, q1_1[right], len(lst))
        lower = interpolation(left, q1_99[left], right, q1_99[right], len(lst))

    else:

        q1_5 = dict.fromkeys(n)
        q1_95 = dict.fromkeys(n)

        inserting_to_dict('q1_5.csv')
        inserting_to_dict('q1_95.csv')

        left, right = finding_interval()

        bigger = interpolation(left, q1_5[left], right, q1_5[right], len(lst))
        lower = interpolation(left, q1_95[left], right, q1_95[right], len(lst))

    if lower < d <= bigger:
        print(lower, '<', d, '≤', bigger, 'is True')
        return lst, avg, True
    else:
        print('decline')
        return None, None, False
