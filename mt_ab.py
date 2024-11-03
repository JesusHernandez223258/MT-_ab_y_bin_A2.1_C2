import tkinter as tk
from tkinter import messagebox

class TuringMachineAB:
    def __init__(self):
        # Definimos los estados de la máquina y la cinta
        self.tape = []
        self.head = 0
        self.state = "q0"

    def reset(self, input_string):
        """ Inicializa la cinta y el cabezal para una nueva entrada """
        self.tape = list(input_string) + ["_"]
        self.head = 0
        self.state = "q0"

    def step(self):
        """ Ejecuta un paso de la máquina de Turing """
        if self.state == "q0":
            if self.tape[self.head] == 'a':
                self.tape[self.head] = 'X'
                self.head += 1
                self.state = "q1"
            else:
                self.state = "rejected"
        elif self.state == "q1":
            if self.tape[self.head] == 'b':
                self.tape[self.head] = 'Y'
                self.head += 1
                self.state = "q2"
            else:
                self.state = "rejected"
        elif self.state == "q2":
            if self.tape[self.head] == '_':
                self.state = "accepted"
            elif self.tape[self.head] == 'a':
                self.state = "q0"
            else:
                self.state = "rejected"
                
    def run(self, input_string):
        """ Ejecuta la máquina en una cadena de entrada completa """
        self.reset(input_string)
        while self.state not in ["accepted", "rejected"]:
            self.step()
        return self.state == "accepted"

class TuringMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Turing Machine Validator for 'ab'")
        
        self.label = tk.Label(root, text="Ingrese una cadena de 'ab':")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.button = tk.Button(root, text="Validar", command=self.validate)
        self.button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        self.machine = TuringMachineAB()

    def validate(self):
        input_string = self.entry.get()
        is_valid = self.machine.run(input_string)
        if is_valid:
            self.result_label.config(text="Cadena válida")
            messagebox.showinfo("Resultado", "La cadena es válida.")
        else:
            self.result_label.config(text="Cadena no válida")
            messagebox.showerror("Resultado", "La cadena no es válida.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TuringMachineApp(root)
    root.mainloop()
