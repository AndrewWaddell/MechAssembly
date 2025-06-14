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

        expected_argument_counts = {
            'load': 2,
            'and' : 3,
            'add' : 3,
            'xor' : 3,
            'store':2
        }

        # Split text into lines and process each
        for line in text.strip().splitlines():
            parts = line.strip().split()
            if not parts:
                continue  # skip empty lines
            command = parts[0].lower()
            args = parts[1:]

            # Validate command and argument count
        if command in expected_argument_counts:
            expected = expected_argument_counts[command]
            
            # Handle both single number and range of valid arg counts
            if isinstance(expected, int):
                # Exact number required
                if len(args) == expected:
                    self.instructions.append((command, args))
                # else: silently ignore - wrong number of args
        
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
        self.registers[in1.upper()] = out.upper()

    def and_op(self, in1, in2, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        output = 'and-'+in1+'-'+in2
        self.registers[out.upper()] = output.upper() # g for gear

    def add_op(self, in1, in2, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        self.registers[out.upper()] = 'G'

    def xor_op(self, in1, in2, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        pass

    def store_op(self, in1, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        self.registers[in1.upper()] = ''