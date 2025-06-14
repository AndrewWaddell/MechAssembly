class Compiler:
    def __init__(self) -> None:
        self.registers = {
        'R1':'',
        'R2':'',
        'R3':'',
        'R4':'',
        'R5':'',
        'R6':'',
        'R7':'',
        'R8':'',
        }

    def getRegisters(self):
        """
        Output the registers variable.
        """
        return list(self.registers.values())


    def interpretText(self, text):
        """
        Where text is initially input. Takes the text and starts to do some
        initial processing to decode it.
        """

        self.instructions = []  # Reset or initialize instruction list

        # Split text into lines and process each
        for line in text.strip().splitlines():
            parts = line.strip().split()
            if not parts:
                continue  # skip empty lines
            command = parts[0].lower()
            args = parts[1:]

            # Store as tuple (command, [args])
            self.instructions.append((command, args))
        
        self.runInstructions()

    def runInstructions(self):
        for cmd, args in self.instructions:
            if cmd == 'load':
                self.load_op(*args)
            elif cmd == 'and':
                self.and_op(*args)
            elif cmd == 'add':
                self.add_op(*args)
            elif cmd == 'xor':
                self.xor_op(*args)
            elif cmd == 'store':
                self.store_op(*args)
    
    
    def load_op(self, in1, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        self.registers[]

    def and_op(self, in1, in2, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        pass

    def add_op(self, in1, in2, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        pass

    def xor_op(self, in1, in2, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        pass

    def store_op(self, in1, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        pass