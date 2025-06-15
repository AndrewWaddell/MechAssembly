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
        self.axis = []
        self.counter = 0 # what column are we up to in the drawing

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

        # each time we draw, we have to draw from scratch
        self.instructions = []  # Reset or initialize instruction list
        self.gridInstructions = [] # this is instruction list for actual drawing onto grid
        self.counter = 0 # reset counter

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
        if len(out) != 2:
            return # ignore if not in the format of "R1"
        self.registers[out.upper()] = in1.upper()
        self.gridInstructions.append((int(out[1]),self.counter,in1.upper()))
        self.counter += 1
        self.instructions.pop(0)

    def and_op(self, in1, in2, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        output = 'and-'+in1+'-'+in2
        self.registers[out.upper()] = output.upper()
        self.gridInstructions.append((int(in1[1]),self.counter,''))
        self.gridInstructions.append((int(in2[1]),self.counter,''))
        self.gridInstructions.append((int(out[1]),self.counter,''))
        self.axis.append((self.counter,self.counter+1,''))
        

    def add_op(self, in1, in2, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        output = 'add-'+in1+'-'+in2
        self.registers[out.upper()] = output

    def xor_op(self, in1, in2, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        output = 'xor-'+in1+'-'+in2
        self.registers[out.upper()] = output

    def store_op(self, in1, out):
        """
        Manages the registers in the same way the AND operator would.
        """
        self.registers[out.upper()] = ''