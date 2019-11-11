import random
from binascii import unhexlify

from Fuzzer.fuzzing_strategies.base_strategy.base_strategy import Abstract_Strategy

class Random_Non_Valid_UTF8_Strategy(Abstract_Strategy):

    def generate(self):
        #valid range for standard ascii enligsh chars is
        #0x20 to 0x7e.
        num_bytes = random.randint(1, 4)
        result = b""
        for __ in range(num_bytes):
            first_hex_num = random.choice('0123456789abcdef')
            second_hex_num = random.choice('0123456789abcdef')
            result += unhexlify(first_hex_num + second_hex_num)

        return result
