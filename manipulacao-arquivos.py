import tkinter as tk


def on_button_click():
    copiado = caixa1.get()
    colado = caixa2.get()
    
    with open(copiado) as texto, open(colado, 'w') as novo:
        novo.write(texto.read())
        
    caixa1.delete(0, tk.END)
    caixa2.delete(0, tk.END)
    
    
root = tk.Tk()
root.title('CLONADOR DE TEXTO')
root.geometry('600x400')

label = tk.Label(root, text='COLOQUE A EXTENSÃO DO ARQUIVO')
label.pack()

caixa1 = tk.Entry(root, width=50)
caixa1.pack(pady=20)
    
caixa2 = tk.Entry(root, width=50)
caixa2.pack(pady=20)
    
botao = tk.Button(root, text='ENVIAR', command=on_button_click)
botao.pack()


root.mainloop()
