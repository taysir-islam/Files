import csv
class student:
    grade = 6
    print('hi i am a student of grade', grade)

ob = student()    

class student2:
    grade2 = 6
    name='taysir'

    def intro(self):
        print('hi i am a student ')

    def detail(self):
        print('my name is', self.name)
        print('i study in grade', self.grade2)

ob2 = student2()
ob2.intro()
ob2.detail()



class parrot:
    species = 'bird'
    def __init__(self, name, age):
        self.name = name
        self.age = age


blu = parrot('blu', 10)
woo = parrot('woo', 15)

print('blu is a {}'.format(blu.species))
print('woo is a {}'.format(woo.species))

print('{} is {} years old'.format(blu.name, blu.age))
print('{} is {} years old'.format(woo.name, woo.age))   


def add_book(filename='book.csv'):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    genre = input("Enter genre: ")

    with open(filename, 'a',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([title, author, isbn, genre])
    print('Book added successfully')    

add_book()


class parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)
    
blu = parrot('blu', 10)
print(blu.sing('happy'))
print(blu.dance())