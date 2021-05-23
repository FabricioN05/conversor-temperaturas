from tkinter import *
from tkinter import ttk
from conversoes import *

AZUL_CLARO = 'lightblue'
AZUL_CLARO2 = '#0f44b8'
CINZA = 'grey'

conversoes_combo_1 = ['Celsius', 'Fahrenheit', 'Kelvin']
conversoes_combo_2 = ['Fahrenheit', 'Celsius', 'Kelvin']


def checar_numeros(entrada):
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    return all(caractere in numeros for caractere in str(entrada))


def deletar_placeholder(Input):
    if Input.get() == 'Insira o valor':
        Input.delete(0, END)
        Input.configure(fg='black')


def inserir_placeholder(Input):
    if not Input.get():
        Input.insert('0', 'Insira o valor')
        Input.configure(fg=CINZA)


def calcular(combo1, combo2,  valor, label):

    if checar_numeros(valor):
        valor = int(valor)

        if combo1.get() == 'Celsius':
            if combo2.get() == 'Fahrenheit':
                label.configure(text=f'{celsius_fahrenheit(valor):.2f} °F')

            if combo2.get() == 'Kelvin':
                label.configure(text=f'{celsius_kelvin(valor):.2f} K')

        if combo1.get() == 'Fahrenheit':
            if combo2.get() == 'Celsius':
                label.configure(text=f'{fahrenheit_celsius(valor):.2f} °C')

            if combo2.get() == 'Kelvin':
                label.configure(text=f'{fahrenheit_kelvin(valor):.2f} K')

        if combo1.get() == 'Kelvin':
            if combo2.get() == 'Celsius':
                label.configure(text=f'{kelvin_celsius(valor):.2f} °C')

            if combo2.get() == 'Fahrenheit':
                label.configure(text=f'{kelvin_fahrenheit(valor):.2f} °F')


window = Tk()
window.title('Conversor Temperaturas')
window.geometry('400x300')
window.resizable(False, False)
window.configure(bg=AZUL_CLARO)

titulo = Label(window, text='Conversor de Temperaturas', font='Arial 20', bg=AZUL_CLARO)
titulo.pack(pady=10)

combo_medida1 = ttk.Combobox(window, values=conversoes_combo_1, state='readonly')
combo_medida1.current(0)
combo_medida1.bind('<FocusIn>', lambda evento: window.focus())
combo_medida1.pack(pady=5)

texto = Label(window, text='para', font='Arial 12', bg=AZUL_CLARO)
texto.pack(pady=10)

combo_medida2 = ttk.Combobox(window, values=conversoes_combo_2, state='readonly')
combo_medida2.current(0)
combo_medida2.pack(pady=5)

input_valor = Entry(window, fg=CINZA, relief='flat', width=20)
input_valor.insert(0, 'Insira o valor')
input_valor.bind('<FocusIn>', lambda evento: deletar_placeholder(input_valor))
input_valor.bind('<FocusOut>', lambda evento: inserir_placeholder(input_valor))
input_valor.pack(padx=80, pady=35, anchor='w')

botao = Button(window, text='Calcular', relief='flat', bg=AZUL_CLARO2,
               command=lambda: calcular(combo_medida1, combo_medida2, input_valor.get(), label_resultado))
botao.place(x=240, y=199, width=55, height=20)

label2 = Label(window, text='Resultado:', font='Arial 12', bg=AZUL_CLARO)
label2.place(x=78, y=237)

label_resultado = Label(window, text='', font='Arial 12', bg=AZUL_CLARO)
label_resultado.place(x=178, y=237)

window.mainloop()
