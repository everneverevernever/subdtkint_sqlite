from tkinter import *
from tkinter import ttk
import  backend as back

window = Tk()
window.title('subd')
frame_change = Frame(window, width = 150, height = 150, bg='red') #блок для функционала субд
frame_view = Frame(window, width = 150, height = 150, bg='blue') #блок для просмотра базы данных
frame_change.place(relx=0, rely=0, relwidth=1, relheight=1)
frame_view.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
window.geometry('300x250')

# кнопка измененить
but_change = Button(frame_change, text='Изменить', width = 10, height = 1, bg = 'white', font = 'Arial 15')
but_change.bind('<Button-1>', back.cnangeDB)
but_change.grid(row = 4, column = 4)

# порядок элементов
heads = ['id', 'name', 'expenses']
table = ttk.Treeview(frame_view, show='headings') # дерево выполняющее свойство таблицы
table['columns'] = heads # длина таблицы

# заголовки столбцов и их расположение
for header in heads:
    table.heading(header, text=header, anchor='center')
    table.column(header, anchor='center')

# добавление из бд в приложение
for row in back.information():
    table.insert('', END, values=row )
table.pack(expand=YES, fill=BOTH)

window.mainloop()