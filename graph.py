import numpy as np
import scipy.stats as stats
import pylab as pl


def draw(filename):
    f = open(filename, 'r')
    ls = []
    for line in f:
        line = line.replace(',', '.')
        ls.append(float(line[:-1]))

    h = sorted(ls)  # sorted

    fit = stats.norm.pdf(h)  # this is a fitting indeed

    pl.plot(h, fit, '0.01')

    pl.hist(h)  # use this to draw histogram of your data

    pl.savefig('plot.png')
