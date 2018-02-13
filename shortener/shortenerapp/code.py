import random

def code_generator(size , char ):
    new_code = ''
    for i in range(size):
        new_code += random.choice(char)
    return new_code

new_code = code_generator(6, 'afuhufxrkerwcklbvds')
print(new_code)