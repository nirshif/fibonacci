students = []

def read_file():
    try:
        f = open ("students.txt", "r")
        for student in f.read_students(f):
            students.append(student)
        f.close()
    except Exeption:
        print("could not read file")
def read_students(f):
    for line in f:
        yield line

read_file()
print(students)