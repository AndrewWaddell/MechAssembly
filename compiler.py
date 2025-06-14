class Compiler:
    def __init__(self) -> None:
        self.registers = ['','','','','','','','']

    def interpretText(self,text):
        """
        Where text is initially input. Takes the text and starts to do some
        initial processing to decode it.
        """
        self.registers[0] = 'A1'
        self.registers[1] = 'A2'