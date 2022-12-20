# import tkinter
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog, ttk
import crit1
import crit2


class SostCrit(Frame):
    q = 0.0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Домашнаяя работа по метрологии")
        fbtn = ttk.Button(text="Выбрать файл", command=self.onOpen)
        fbtn.place(relheight=0.07, relwidth=0.28, x=350, y=30)
        self.fentry = ttk.Entry()  # state=["disabled"])
        self.qentry = ttk.Entry()
        self.fentry.place(relheight=0.07, relwidth=0.68, x=10, y=30)
        self.qentry.place(relheight=0.07, relwidth=0.68, x=10, y=70)
        qbtn = ttk.Button(text="Задать q", command=self.qentry_get)
        qbtn.place(relheight=0.07, relwidth=0.28, x=350, y=70)

    def qentry_get(self):
        try:
            self.q = float(self.qentry.get())
            if self.q != 0.02:
                self.q = 0.02
                self.qentry.delete(0, END)
                self.qentry.insert(0, '0.02')
        except ValueError:
            self.q = 0.02
            self.qentry.insert(0, '0.02')

    def onOpen(self):
        ftypes = [('Текстовые файлы', '*.txt')]
        dlg = filedialog.Open(self, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            self.count_first(fl)

    def count_first(self, filename):
        self.fentry.insert(0, filename)
        if self.q == 0:
            self.q = 0.02
            self.qentry.insert(0, '0.02')
            crit1.cr1(self.q, filename)
        else:
            crit1.cr1(self.q, filename)


def main():
    root = Tk()
    ex = SostCrit()
    root.geometry("500x400+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()

# q = 0.02

# selection, average, is_correct = crit1.cr1(q)
# is_correct2 = crit2.cr2(q, selection, average)
# print(is_correct2)
