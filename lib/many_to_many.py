class Author:

    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    def contracts(self):
        relevant_contracts = []
        for contract in Contract.all:
            if contract.author == self:
                relevant_contracts.append(contract)
            else:
                pass
        return relevant_contracts
    
    def books(self):
        relevant_books = []
        for contract in Contract.all:
            if contract.author == self:
                relevant_books.append(contract.book)
            else:
                pass
        return relevant_books
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for contract in Contract.all:
            if contract.author == self:
                total += contract.royalties
            else:
                pass
        return total



class Book:

    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)

    def contracts(self):
        relevant_contracts = []
        for contract in Contract.all:
            if contract.book == self:
                relevant_contracts.append(contract)
            else:
                pass
        return relevant_contracts
    
    def authors(self):
        relevant_authors = []
        for contract in Contract.all:
            if contract.book == self:
                relevant_authors.append(contract.author)
            else:
                pass
        return relevant_authors


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("Author must be an instance of the 'Author' class.")
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("Book must be an instance of the 'Book' class.")
        if type(date) is str:
            self.date = date
        else:
            raise Exception("Date must be a valid string.")
        if type(royalties) is int:
            self.royalties = royalties
        else:
            raise Exception("Royalties must be a valid number.")
        Contract.all.append(self)

    def contracts_by_date(date):
        relevant_contracts = []
        for contract in Contract.all:
            if contract.date == date:
                relevant_contracts.append(contract)
            else:
                pass
        return relevant_contracts