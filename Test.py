class Publication:
    def __init__(self, title, authors, year, status="available"):
        self.title = title
        self.authors = authors
        self.year = year
        self.status = status

    def __str__(self):
        authors_str = ', '.join([f"'{author}'" for author in self.authors])
        return f"{self.title} - [{authors_str}] ({self.year})"

class Book(Publication):
    def __init__(self, title, authors, year, isbn, pages):
        super().__init__(title, authors, year)
        self.isbn = isbn
        self.pages = pages
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}"

class Journal(Publication):
    def __init__(self, title, authors, year, edition_number, periodicity):
        super().__init__(title, authors, year)
        self.edition_number = edition_number
        self.periodicity = periodicity
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.pubs = []

    def lend_pub(self, publication):
        if publication.status == "available":
            self.pubs.append(publication)
            publication.status = "borrowed"
            print(f"The {publication.title} has been lent to {self.name}.")
        else:
            print(f"The {publication.title} is not available.")

    def return_pub(self, publication):
        if publication in self.pubs:
            self.pubs.remove(publication)
            publication.status = "available"
            print(f"The {publication.title} was returned by {self.name}.")
        else:
            print(f"The {publication.title} was not borrowed by {self.name}.")
    
    def __str__(self):
        return '[' + ', '.join(str(pub) for pub in self.pubs) + ']'

class Professor(User):
    def __init__(self, name, user_id, department, employee_id, max_pubs=2):
        super().__init__(name, user_id)
        self.department = department
        self.employee_id = employee_id
        self.max_pubs = max_pubs

    def lend_pub(self, publication):
        if len(self.pubs) < self.max_pubs:
            super().lend_pub(publication)
        else:
            print(f"{self.name} has reached the maximum limit of borrowed items.")

class Student(User):
    def __init__(self, name, user_id, grade, student_id, max_pubs=1):
        super().__init__(name, user_id)
        self.grade = grade
        self.student_id = student_id
        self.max_pubs = max_pubs

    def lend_pub(self, publication):
        if len(self.pubs) < self.max_pubs:
            super().lend_pub(publication)
        else:
            print(f"{self.name} has reached the maximum limit of borrowed items.")

class Library:
    def __init__(self, name):
        self.name = name
        self.catalogue = []
        self.users = []

    def show_catalogue(self):
        print(f"Catalogue of the library: {self.name}")
        print("-" * 50)
        for pub in self.catalogue:
            print(pub)
        print("-" * 50)

    def add_publication(self, publication):
        self.catalogue.append(publication)

    def register_user(self, user):
        self.users.append(user)

    def lend_pub(self, user, publication):
        if user in self.users and publication in self.catalogue:
            user.lend_pub(publication)
        else:
            print("The user or publication is not registered.")

    def return_pub(self, user, publication):
        if user in self.users and publication in self.catalogue:
            user.return_pub(publication)
        else:
            print("The user or publication is not registered.")


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
