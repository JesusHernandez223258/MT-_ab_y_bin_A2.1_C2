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
        self.tape = list(input_string) + ["_"]  # Usamos '_' como marcador del final de la cinta
        self.head = 0
        self.state = "q0"

    def step(self):
        """ Ejecuta un paso de la máquina de Turing """
        if self.state == "q0":
            # Verifica que haya una 'a' al inicio de cada nuevo patrón 'abb'
            if self.tape[self.head] == 'a':
                self.head += 1
                self.state = "q1"
            elif self.tape[self.head] == "_":
                self.state = "accepted"  # Acepta si está en el final sin más caracteres
            else:
                self.state = "rejected"  # Rechaza si no es 'a' o '_' en q0

        elif self.state == "q1":
            # Verifica que la 'a' esté seguida de la primera 'b'
            if self.tape[self.head] == 'b':
                self.head += 1
                self.state = "q2"
            else:
                self.state = "rejected"  # Si no encuentra 'b', rechaza la cadena
        
        elif self.state == "q2":
            # Verifica que la primera 'b' esté seguida de una segunda 'b'
            if self.tape[self.head] == 'b':
                self.head += 1
                self.state = "q0"  # Reinicia para buscar otro 'abb' si existe
            else:
                self.state = "rejected"  # Si encuentra algo que no es 'b', rechaza la cadena

    def run(self, input_string):
        """ Ejecuta la máquina en una cadena de entrada completa """
        self.reset(input_string)
        while self.state not in ["accepted", "rejected"]:
            self.step()
        
        # Al finalizar, se acepta la cadena si estamos en el estado 'accepted'
        return self.state == "accepted"

class TuringMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Turing Machine Validator for 'abb' Pattern")
        
        self.label = tk.Label(root, text="Ingrese una cadena de 'abb':")
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
