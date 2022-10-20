from cProfile import label
from cgitb import text
from lzma import is_check_supported
from multiprocessing.sharedctypes import Value
from pydoc import cli
import log
import model_div as m_div
import model_sub as m_sub
import model_sum as m_sum
import model_mult as m_mult
import tkinter as tk


root = tk.Tk()

root.title("Калькулятор")
root.geometry("500x250+100+100")
root.resizable(False, False)
create_rb_number = tk.IntVar()
create_rb_operation = tk.IntVar()
create_rb_operation.set(0)
text_input_field_1 = tk.Label(text="Введите перое число:", font=10).grid(
    row=0, column=0, stick="w")
text_input_field_2 = tk.Label(text="Введите второе число:", font=10).grid(
    row=1, column=0, stick="w")

input_field_1 = tk.Entry(root)
input_field_1.grid(row=0, column=1)
input_field_2 = tk.Entry(root)
input_field_2.grid(row=1, column=1)
input_field_3 = tk.Entry(root)
input_field_3.grid(row=0, column=2)
input_field_4 = tk.Entry(root)
input_field_4.grid(row=1, column=2)
root.grid_columnconfigure(0, minsize=130)

info_label_1 = tk.Label(text="Выберите тип числа:", font=10).place(x=0, y=60)
rb_r = tk.Radiobutton(root, text="Рацианольные",
                      variable=create_rb_number, value=1, font=10)
rb_r.grid(row=4, column=1, stick="w")
rb_k = tk.Radiobutton(root, text="Комплексные", variable=create_rb_number,
                      value=2, font=10)
rb_k.grid(row=5, column=1, stick="w")

info_label_2 = tk.Label(text="Выберите операцию:", font=10).place(x=0, y=120)
rb_sum = tk.Radiobutton(root, text="+", variable=create_rb_operation,
                        value=1, font=10)
rb_sum.place(x=170, y=120)
rb_sub = tk.Radiobutton(root, text="-", variable=create_rb_operation,
                        value=2, font=10)
rb_sub.place(x=210, y=120)
rb_mult = tk.Radiobutton(
    root, text="*", variable=create_rb_operation, value=3, font=10)
rb_mult.place(x=250, y=120)
rb_div = tk.Radiobutton(
    root, text="/", variable=create_rb_operation, value=4, font=10)
rb_div.place(x=290, y=120)
rb_rem_div = tk.Radiobutton(
    root, text="%", variable=create_rb_operation, value=5, font=10)
rb_rem_div.place(x=330, y=120)

label1 = tk.Label(root, text="", font=10)
label1.place(x=180, y=160)

info_label_result = tk.Label(
    text="Результат вычисления:", font=10).place(x=0, y=160)


def single_click():
    value1 = input_field_1.get()
    value2 = input_field_2.get()
    value3 = input_field_3.get()
    value4 = input_field_4.get()

    if create_rb_number.get() == 1 and create_rb_operation.get() == 1:
        label1['text'] = f"{m_sum.Sum(int(value1),int(value2),0,0,1)}"
        log.sum_logger(f"{value1},{value2},0,0,1\n")

    elif create_rb_number.get() == 2 and create_rb_operation.get() == 1:
        label1['text'] = f"{m_sum.Sum(int(value1),int(value2),int(value3),int(value4),2)}"
        log.sum_logger(f"{value1},{value2},{value3},{value4},2\n")

    elif create_rb_number.get() == 1 and create_rb_operation.get() == 2:
        label1['text'] = f"{m_sub.Subtraction(int(value1),int(value2),0,0,1)}"
        log.sub_logger(f"{value1},{value2},0,0,1\n")

    elif create_rb_number.get() == 2 and create_rb_operation.get() == 2:
        label1['text'] = f"{m_sub.Subtraction(int(value1),int(value2),int(value3),int(value4),2)}"
        log.sub_logger(f"{value1},{value2},{value3},{value4},2\n")

    elif create_rb_number.get() == 1 and create_rb_operation.get() == 3:
        label1['text'] = f"{m_mult.Multiplication(int(value1),int(value2),0,0,1)}"
        log.mult_logger(f"{value1},{value2},0,0,1\n")

    elif create_rb_number.get() == 2 and create_rb_operation.get() == 3:
        label1['text'] = f"{m_mult.Multiplication(int(value1),int(value2),int(value3),int(value4),2)}"
        log.mult_logger(f"{value1},{value2},{value3},{value4},2\n")

    elif create_rb_number.get() == 1 and create_rb_operation.get() == 4:
        label1['text'] = f"{m_div.Division(int(value1),int(value2),0,0,1)}"
        log.div_logger(f"{value1},{value2},0,0,1\n")

    elif create_rb_number.get() == 1 and create_rb_operation.get() == 5:
        label1['text'] = f"{m_div.Division(int(value1),int(value2),0,0,2)}"
        log.div_logger(f"{value1},{value2},0,0,1\n")

    else:
        label1['text'] = "Некорректное значение ввода"
    return


tk.Button(root, text="Вывести результат",
          command=single_click, font=10).place(x=150, y=200)

root.mainloop()
