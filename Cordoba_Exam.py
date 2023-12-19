from abc import ABC, abstractmethod

class Publication(ABC):
    def __init__(self, title: str, authors, year_of_pub: int):
        self.title = title
        if isinstance(authors, list) and all(isinstance(author, str) for author in authors):
            self.authors = authors
        else:
            raise ValueError("Los autores deben ser una lista de cadenas")
        self.year_of_pub = year_of_pub
        self.status = "available"
    
    def change_status(self, new_status):
        self.status = new_status

class Book(Publication):
    def __init__(self, title, authors, year_of_pub, isbn, n_pages):
        super().__init__(title, authors, year_of_pub)
        if isbn.isdigit() and len(isbn) == 13:
            self.isbn = isbn
        else:
            raise ValueError("El ISBN debe ser una cadena de 13 dígitos")
        self.n_pages = n_pages
    
class Journal(Publication):
    def __init__(self, title, authors, year_of_pub, edition_n, periodicity):
        super().__init__(title, authors, year_of_pub)
        self.edition_n = edition_n
        self.periodicity = periodicity

class User(ABC):
    def __init__(self, name: str, user_id: str):
        self.name = name
        if user_id.isdigit() and len(user_id) == 9:
            self.user_id = user_id
        else:
            raise ValueError("El UserID debe ser una cadena de 9 dígitos")
        self.pubs = []
    
    def lend_pub(self, publication):
        publication.change_status("borrowed")
        self.pubs.append(publication)

    def return_pub(self, publication):
        publication.change_status("available")
        self.pubs.remove(publication)

class Professor(User):
    def __init__(self, name: str, user_id: str, department: str, employee_id: str):
        super().__init__(name, user_id)
        self.department = department
        if len(employee_id) == 6:
            self.employee_id = employee_id
        else:
            raise ValueError("El EmployeeID debe ser de 6 números")
        self.max_pubs = 2

class Student(User):
    def __init__(self, name: str, user_id: str, grade: str, student_id: str):
        super().__init__(name, user_id)
        self.grade = grade
        if len(student_id) == 6:
            self.student_id = student_id
        else:
            raise ValueError("El StudentID debe ser de 6 números")
        self.max_pubs = 1

class Library:
    def __init__(self, name: str):
        self.name = name
        self.catalogue = []
        self.users_list = []

    @property 
    def text_catalogue(self):
        return "\n".join(str(elemento) for elemento in self.catalogue)
        
    def show_catalogue(self):
        print("Catalogue of the library: " + self.name +
              "\n--------------------------------------------------\n" +
              self.text_catalogue +
              "\n--------------------------------------------------")
    def add_publication(self, publication):
        self.catalogue.append(publication)
    
    def register_user(self, user):
        self.users_list.append(user)
    
    def lend_pub(self, user, publication):
        if user in self.users_list and publication in self.catalogue:
            if len(user.pubs) < user.max_pubs:
                if publication.status == "available":
                    user.lend_pub(publication)
                    print(f'The {type(publication).__name__} "{publication.title}" has been lent to {user.name}')
                else:
                    print(f'The {type(publication).__name__} "{publication.title}" is not available')
            else:
                print(f'{user.name} has reached the maximum limit of borrowed items')
        else:
            print("The user or publication is not registered")
    
    def return_pub(self, user, publication):
        if user in self.users_list and publication in user.pubs:
            user.return_pub(publication)
            print(f'The {type(publication).__name__} "{publication.title}" was returned by {user.name}')
        else:
            print("The user or publication is not registered")
    
if __name__ == "__main__":

    library = Library("Loyola Andalucía Library")
    book1 = Book("Learning Python II",
    ["Javier Perez", "Daniel Muñoz"],
    2023, "1234567890123", 300)
    journal1 = Journal("Technology Journal",
    ["Stephen Curry", "LeBron James"],
    2022, 7, "Annual")
    journal2 = Journal("Medical Journal",
    ["Michael Jordan", "Larry Bird"],
    2023, 5, "Monthly")
    professor1 = Professor("Professor Tija", "123456789", "Philosophy", "123456")
    student1 = Student("Ashkabos Teberio", "987654321", "DAN", "654321")
    student2 = Student("Rachel Tonali", "656565656", "ADE+DAN", "454322")
    library.add_publication(book1)
    library.add_publication(journal1)
    library.add_publication(journal2)
    library.register_user(professor1)
    library.register_user(student1)
    library.show_catalogue()
    library.lend_pub(professor1, book1)
    library.lend_pub(student1, book1) # the book should be borrowed
    print(student1.pubs) # empty list
    library.return_pub(professor1, book1)
    library.lend_pub(student1, book1) # the book should be available now
    library.lend_pub(student1, journal2)
    print(student1.pubs)
    library.lend_pub(student2, journal1) # User not registred
