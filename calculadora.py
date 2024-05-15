from tkinter import *
from tkinter import ttk

# Cores
cor1 = "#000000"  # Preta
cor2 = "#ffffff"  # Branca
cor3 = "#464747"  # Cinza escuro
cor4 = "#fa0f0f"  # Vermelho
cor5 = "#a7a9ab"  # Cinza
cor6 = "#f77539"  # Laranja

# Configuração da janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")  # Largura x Altura
janela.config(bg=cor1)

# Criando os frames
frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(janela, width=235, height=265)
frame_corpo.grid(row=1, column=0)

# Variável para armazenar todos os valores
todos_valores = ""

# Função para adicionar valores
def colocar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

# Função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# Função para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Criando label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Criando botões
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda: colocar_valores('%'), text="%", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command=lambda: colocar_valores('/'), text="/", width=5, height=2, bg=cor6, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_8 = Button(frame_corpo, command=lambda: colocar_valores('7'), text="7", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=52)
b_9 = Button(frame_corpo, command=lambda: colocar_valores('8'), text="8", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=52)
b_10 = Button(frame_corpo, command=lambda: colocar_valores('9'), text="9", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=52)
b_11 = Button(frame_corpo, command=lambda: colocar_valores('*'), text="*", width=5, height=2, bg=cor6, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=52)

b_12 = Button(frame_corpo, command=lambda: colocar_valores('4'), text="4", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=104)
b_13 = Button(frame_corpo, command=lambda: colocar_valores('5'), text="5", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=104)
b_14 = Button(frame_corpo, command=lambda: colocar_valores('6'), text="6", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=104)
b_15 = Button(frame_corpo, command=lambda: colocar_valores('-'), text="-", width=5, height=2, bg=cor6, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=104)

b_16 = Button(frame_corpo, command=lambda: colocar_valores('1'), text="1", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=156)
b_17 = Button(frame_corpo, command=lambda: colocar_valores('2'), text="2", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=59, y=156)
b_18 = Button(frame_corpo, command=lambda: colocar_valores('3'), text="3", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=118, y=156)
b_19 = Button(frame_corpo, command=lambda: colocar_valores('+'), text="+", width=5, height=2, bg=cor6, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_19.place(x=177, y=156)

b_20 = Button(frame_corpo, command=lambda: colocar_valores('0'), text="0", width=11, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_20.place(x=0, y=208)
b_21 = Button(frame_corpo, command=lambda: colocar_valores('.'), text=".", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_21.place(x=118, y=208)
b_22 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor6, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_22.place(x=177, y=208)

janela.mainloop()
