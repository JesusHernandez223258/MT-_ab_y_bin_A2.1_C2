import tkinter as tk

class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)  # Convert input to a list to represent the tape
        self.head_position = 0
        self.state = 'start'

    def step(self):
        """
        Executes one step of the Turing machine.
        """
        if self.state == 'start':
            if self.head_position < len(self.tape) and self.tape[self.head_position] == '1':
                self.state = 'odd'
                self.head_position += 1
            elif self.head_position < len(self.tape) and self.tape[self.head_position] == '0':
                self.state = 'even'
                self.head_position += 1
            else:
                self.state = 'check_parity'

        elif self.state == 'odd':
            if self.head_position < len(self.tape) and self.tape[self.head_position] == '1':
                self.state = 'even'
                self.head_position += 1
            elif self.head_position < len(self.tape) and self.tape[self.head_position] == '0':
                self.head_position += 1
            else:
                self.state = 'check_parity'

        elif self.state == 'even':
            if self.head_position < len(self.tape) and self.tape[self.head_position] == '1':
                self.state = 'odd'
                self.head_position += 1
            elif self.head_position < len(self.tape) and self.tape[self.head_position] == '0':
                self.head_position += 1
            else:
                self.state = 'check_parity'

    def run(self):
        """
        Runs the Turing machine until it reaches the final state.
        """
        while self.state != 'check_parity':
            self.step()

        # Add '1' if state is odd (indicating odd parity); '0' if state is even
        if self.state == 'check_parity':
            if self.state == 'odd':
                self.tape.append('1')
            else:
                self.tape.append('0')

        return ''.join(self.tape)  # Return the final tape as a string

# GUI for Turing Machine
def run_turing_machine():
    input_string = entry.get()
    # Check if the input only contains 0's and 1's
    if not set(input_string).issubset({'0', '1'}):
        result_label.config(text="Please enter a valid binary string (0's and 1's only).")
        return

    # Initialize and run the Turing Machine
    machine = TuringMachine(input_string)
    result = machine.run()
    result_label.config(text=f"Result: {result}")

# GUI setup
root = tk.Tk()
root.title("Turing Machine - Parity Checker")

# Entry field for binary input
label = tk.Label(root, text="Enter a binary string:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Run button
run_button = tk.Button(root, text="Run Turing Machine", command=run_turing_machine)
run_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()
