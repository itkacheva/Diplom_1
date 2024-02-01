import random
import string


def generate_random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(random.randint(1, 255)))
