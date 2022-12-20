import math
import csv


def cr2(q, selection, average):
    def standard_deviation():
        sm = 0
        for i in selection:
            sm += (i - average)**2
        std = math.sqrt(sm/(len(selection)-1.5))
        return std

    def opening_file():
        with open('p_for_z.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if str(len(selection)) == row[0]:
                    nums = int(row[1])
                    if q == 0.01:
                        prob = float(row[2])
                    elif q == 0.02:
                        prob = float(row[3])
                    elif q == 0.05:
                        prob = float(row[4])
        return nums, prob

    def compare():
        with open('vals_of_z.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if p == float(row[0]):
                    z_val = float(row[1])
        return z_val

    def count():
        cnt = 0
        for i in selection:
            if i - average > z * s:
                cnt += 1
        return cnt

    s = standard_deviation()
    m, p = opening_file()
    z = compare()
    counter = count()
    if counter <= m:
        return True
    else:
        return False
