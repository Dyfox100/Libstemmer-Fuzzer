import random
from binascii import unhexlify

from Fuzzer.fuzzing_strategies.base_strategy.base_strategy import Abstract_Strategy

class English_Valid_UTF8_Strategy(Abstract_Strategy):

    def generate(self):
        #valid range for standard ascii enligsh chars is
        #0x20 to 0x7e.
        first_hex_num = random.choice('234567')
        second_hex_num = random.choice('0123456789abcdef')

        result = unhexlify(first_hex_num + second_hex_num)
        #0x7f is control reserved char, so get new char if 0x7f generated.
        while result == b'\x7f':
            result = self.generate()

        return result
