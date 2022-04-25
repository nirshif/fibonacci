"""
my_list = [x for x in range(1,10)]

#without generator
def process_list(my_list):
    for i in range(len(my_list)):
        my_list[i] *= 2
    return my_list
for item in process_list(my_list):
    print(" ")
"""

def gen():
    yield 1
    yield 2
    yield 3

def gen2():
    yield 9000
    yield from range(12)
    for thing in gen():
        yield thing

    yield 9001

for thing in gen2():
    print(f'got thing: {thing}')


