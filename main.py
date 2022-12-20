from tkinter import Frame, Tk, BOTH, Label, Listbox, END, Variable
from tkinter import filedialog, ttk
from tkinter.messagebox import showerror
import crit1
import crit2
import graph


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
        cntbtn = ttk.Button(text="Рассчитать", command=self.count)
        cntbtn.place(relheight=0.07, relwidth=0.28, x=180, y=110)
        self.listbox = Listbox()
        self.listbox.place(relheight=0.35, relwidth=0.45, x=10, y=150)
        label1 = Label(text="Критерий 1:")
        label1.place(relheight=0.065, relwidth=0.45, x=270, y=145)
        self.label_res1 = Label(text="Not counted", background="#808080")
        self.label_res1.place(relheight=0.065, relwidth=0.45, x=270, y=185)
        label2 = Label(text="Критерий 2:")
        label2.place(relheight=0.065, relwidth=0.45, x=270, y=225)
        self.label_res2 = Label(text="Not counted", background="#808080")
        self.label_res2.place(relheight=0.065, relwidth=0.45, x=270, y=265)
        label_result = Label(text="Result", font=("Helvetica", 20))
        label_result.place(relheight=0.07, relwidth=0.28, x=180, y=300)
        self.label_acceptance = Label(text="Not counted", background="#808080", font=("Helvetica", 20))
        self.label_acceptance.place(relheight=0.07, relwidth=0.28, x=180, y=330)

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
        self.fl = dlg.show()
        if self.fl != '':
            self.file(self.fl)

    def file(self, filename):
        self.fentry.insert(0, filename)
        f = open(filename, 'r')
        ls = []
        for line in f:
            line = line.replace(',', '.')
            ls.append(float(line[:-1]))
        ls_var = Variable(value=ls)
        self.listbox = Listbox(listvariable=ls_var)
        self.listbox.place(relheight=0.35, relwidth=0.45, x=10, y=150)
        f.close()

    def count(self):
        def cnt():
            if is_first_correct:
                self.label_res1 = Label(text="Accepted", background="#008000")
                self.label_res1.place(relheight=0.065, relwidth=0.45, x=270, y=185)
                is_second_correct = crit2.cr2(self.q, selection, average)
                if is_second_correct:
                    self.label_res2 = Label(text="Accepted", background="#008000")
                    self.label_res2.place(relheight=0.065, relwidth=0.45, x=270, y=265)
                    self.label_acceptance = Label(text="Accepted", background="#008000", font=("Helvetica", 20))
                    self.label_acceptance.place(relheight=0.07, relwidth=0.28, x=180, y=330)
                    self.graph_button = ttk.Button(text="График", command=self.show_graph)
                    self.graph_button.place(relheight=0.07, relwidth=0.28, x=180, y=370)
                else:
                    self.label_res2 = Label(text="Declined", background="#ff0000")
                    self.label_res2.place(relheight=0.065, relwidth=0.45, x=270, y=265)
                    self.label_acceptance = Label(text="Declined", background="#ff0000", font=("Helvetica", 20))
                    self.label_acceptance.place(relheight=0.07, relwidth=0.28, x=180, y=330)
                    self.graph_button = ttk.Button(text="График", command=self.show_graph)
                    self.graph_button.place(relheight=0.07, relwidth=0.28, x=180, y=370)
            else:
                self.label_res1 = Label(text="Declined", background="#ff0000")
                self.label_res1.place(relheight=0.065, relwidth=0.45, x=270, y=185)
                self.label_acceptance = Label(text="Declined", background="#ff0000", font=("Helvetica", 20))
                self.label_acceptance.place(relheight=0.07, relwidth=0.28, x=180, y=330)
                self.graph_button = ttk.Button(text="График", command=self.show_graph)
                self.graph_button.place(relheight=0.07, relwidth=0.28, x=180, y=370)

        if self.q == 0:
            self.q = 0.02
            self.qentry.insert(0, '0.02')
            try:
                selection, average, is_first_correct = crit1.cr1(self.q, self.fl)
                cnt()
            except AttributeError:
                showerror("No file selected", "Нужно открыть файл с исходной выборкой")
        else:
            try:
                selection, average, is_first_correct = crit1.cr1(self.q, self.fl)
                cnt()
            except AttributeError:
                showerror("No file selected", "Нужно открыть файл с исходной выборкой")

    def show_graph(self):
        graph.draw(self.fl)


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
