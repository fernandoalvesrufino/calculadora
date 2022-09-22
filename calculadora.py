# importando tkinter
from tkinter import *
from tkinter import ttk
from tkinter import _Relief
from turtle import width

# cores
cor_1 = "#3b3b3b"     # preta
cor_2 = "#feffff"     # branco
cor_3 = "#38576b"     # azul
cor_4 = "#ECEFF1"     # cinza
cor_5 = "#FFAB40"     # laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor_1)

# criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor_3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Criando label
app_label = label(frame_tela, text='123456789', width=16, height=2, padx=7, _Relief=FLAT, anchor="e")
app_label.place(x=0, y=0)

# criando botões
botao_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_1.place(x=0, y=0)
botao_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=118, y=0)
botao_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=177, y=0)

botao_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_4.place(x=0, y=52)
botao_5 = Button(frame_corpo, text="8", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_5.place(x=59, y=52)
botao_6 = Button(frame_corpo, text="9", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_6.place(x=118, y=52)
botao_7 = Button(frame_corpo, text="*", width=5, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_7.place(x=177, y=52)

botao_8 = Button(frame_corpo, text="4", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_8.place(x=0, y=104)
botao_9 = Button(frame_corpo, text="5", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_9.place(x=59, y=104)
botao_10 = Button(frame_corpo, text="6", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_10.place(x=118, y=104)
botao_11 = Button(frame_corpo, text="-", width=5, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_11.place(x=177, y=104)

botao_12 = Button(frame_corpo, text="1", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_12.place(x=0, y=156)
botao_13 = Button(frame_corpo, text="2", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_13.place(x=59, y=156)
botao_14 = Button(frame_corpo, text="3", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_14.place(x=118, y=156)
botao_15 = Button(frame_corpo, text="+", width=5, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_15.place(x=177, y=156)

botao_16 = Button(frame_corpo, text="0", width=11, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_16.place(x=0, y=208)
botao_17 = Button(frame_corpo, text=".", width=5, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_17.place(x=118, y=208)
botao_18 = Button(frame_corpo, text="=", width=5, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_18.place(x=177, y=208)


janela.mainloop()
