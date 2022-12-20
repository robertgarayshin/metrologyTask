from tkinter import *
import crit1
import crit2

q = 0.02

selection, average, is_correct = crit1.cr1(q)
is_correct2 = crit2.cr2(q, selection, average)
print(is_correct2)
