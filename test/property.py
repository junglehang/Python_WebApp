

class Person(object):
    _instance = None

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if(cls._instance == None):
            cls._instance = object.__new__(cls)
        return cls._instance

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def set_name(self,new_name):
        self.name = new_name

    @classmethod
    def show(self):
        print("show")


def main():
    person = Person("薇薇",21)
    person2 = Person("lili",20)
    print(person)
    print(person2)
    print(person.get_name)
    person.set_name = "小雅"
    print(person.get_name)
    Person.show()

if __name__ == '__main__':
    main()