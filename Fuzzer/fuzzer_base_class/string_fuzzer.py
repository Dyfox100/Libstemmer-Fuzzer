

class String_Fuzzer():

    def __init__(self, char_generation_strategy):
        self._char_generation_strategy = char_generation_strategy
        if self._char_generation_strategy == None:
            raise ValueError("Fuzzer Must Have a Strategy")

    def generate_fuzzy_string(self, length):
        """Generates a random (byte)string of <length> characters,
         using the char generation strategy to generate individual chars"""

        length = int(length)
        if length < 0:
            raise ValueError("Length must be greater than 0")

        byte_string = b""
        for __ in range(length):
            byte_string += self._char_generation_strategy.generate()

        return byte_string
