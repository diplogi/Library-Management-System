# IMPORT DATACLASS FROM THE LIBRARY DATACLASSES
from dataclasses import dataclass

# DEFINE A CLASS LIST
booksList = []

# DEFINE A NOT BORROWED BOOKS LIST
notBorrowedList = []

# KEYWORD TO USE CLASSES AND DECLARE A "BOOK" CLASS
@dataclass
class Book:
    # BOOK CODE
    code: int
    # BOOK TITLE
    title: str
    # BOOK AUTHOR
    author: str
    # BOOK PUBLICATION YEAR
    publYear: int
    # BOOK EDITOR
    editor: str
    # BOOK ACTUAL OWNER
    actOwner: str
    # DAYS LEFT TO EXPIRING DATE
    daysLeft: int

# FUNCTION THAT RECEIVE A NUMBER OF BOOKS BY THE USER AND CONTROLS IF IT'S A VALID INPUT
def insertNBooks():
    # DEFINING A CONTAINER VARIABLE FOR THE TOTAL NUMBER OF BOOKS
    TotalNBooks = 0

    # INPUT VARIABLE FOR N BOOKS
    NBooks=int(input('How many books do you want to insert? '))

    # THIS CONDITION CONTROLS THAT NBOOKS IS >0 AND GET THAT NUMBER IN THE TOTAL CONTAINER VARIBLE
    if NBooks > 1:
        TotalNBooks += NBooks
        print()
        print(NBooks, ' books are being added to the library.')

    # PRINT 'ONE' IF NBooks INPUT IS 1 
    elif NBooks == 1:
        TotalNBooks += NBooks
        print()
        print('One book has been added to the library.')

    # THIS MAKES THE USER REWRITE NBOOKS IF IT'S <=0
    elif NBooks <= 0:
        while NBooks <= 0:
            NBooks=int(input('Re-write it. You have to insert a >0 number: '))

    return NBooks, TotalNBooks

# FUNCION THAT ADD INFOS TO
def booksInfo():
    code = int(input('Insert book code: '))
    title = input('Insert title:')
    author = input('Insert author name:')
    publYear = input('Insert publication year:')
    editor = input('Insert editor:')
    actOwner = input('Insert the actual owner:')
    daysLeft = int(input('Insert how many days are left from now to the expiring date:'))
    return  Book(code, title, author, publYear, editor, actOwner, daysLeft)

# FUNCTION THAT ORDER THE ELEMENTS IN booksList BY THE AUTHOR NAME
def orderListByAuthor(booksList:list[Book]):
    for i in range (len(booksList)-1):
        for j in range (i+1, len(booksList)):
            if booksList[i].author > booksList[j].author:
                booksList[i].author, booksList[j].author = booksList[j].author, booksList[i].author
    return booksList

# FUNCTION THAT ORDER THE ELEMENTS IN notBorrowedList BY THE CODE
def orderListByCode(notBorrowedList:list[Book]):
    for i in range (len(notBorrowedList)-1):
            for j in range (i+1, len(notBorrowedList)):
                if notBorrowedList[i].code > notBorrowedList[j].code:
                    notBorrowedList[i].code, notBorrowedList[j].code = notBorrowedList[j].code, notBorrowedList[i].code
    return notBorrowedList

# FUNCTION THAT FINDS AND PRINTS ALL EXPIRING BOOKS (UNDER 2 DAYS LEFT)
def findExpiringBooks(booksList:list[Book]):
    for i in range (len(booksList)):
        if booksList[i].daysLeft < 2:
            print(booksList[i])

# DEFINE A FLAG THAT MAKES SURE THE PROGRAM GOT AN INPUT FIRST
hasBooks = False

# DEFINE AN EXIT FLAG
exitConfirm=False
# REPEATING PRINTING THE MENU BY USING A WHILE WITH THE LAST BOOLEAN VARIABLE DEFINED AS A CONDITION
while exitConfirm == False:
    # THE WHOLE MENU
    print()
    print('1. Insert a number of books')
    print('-'*47)
    print('2. Print the total number of books')
    print('-'*47)
    print('3. Print every in-library book')
    print('-'*47)
    print('4. Print all books ordered by author name')
    print('-'*47)
    print('5. Print all non-borrowed books ordered by code')
    print('-'*47)
    print('6. Print all 2 days expiring books')
    print('-'*47)
    print('7. Exit')
    print('-'*47)
    print()

    # DEFINE A VARIABLE FOR THE MATCH CASE
    choose=int(input('Which option do you want to choose? '))

    match choose:

        # CASE 1 MAKES THE hasBooks BOOLEAN TRUE, SO THE SOFTWARE KNOWS THAT IT HAS BOTH hasBooks AND booksTotal VARIABLE
        case 1:
            hasBooks=True
            books, booksTotal = insertNBooks()
            for i in range (booksTotal):
                book1 = booksInfo()
                booksList.append(book1)
                askBorrow=input('Is this book in borrow? (Y/N)')
                if askBorrow == 'N':
                    notBorrowedList.append(book1)
                print('Book has been added.')

        # VERIFIES IF THE SOFTWARE GOT THE NECESSARY INPUT DONE AND THEN PRINT HOW MANY BOOKS THERE ARE
        case 2:
            if hasBooks != True:
                print("You have to insert books first.")
                print()
                books, booksTotal = insertNBooks()
                hasBooks = True

            if booksTotal == 1:
                    print("There's only one book.")

            else:
                print('There are', booksTotal, 'books')        
        # CASE THAT PRINTS ALL THE BOOKS IN THE TAB       
        case 3:
            print(notBorrowedList)
        # PRINTS ALL BOOKS ORDERED BY AUTHOR NAME        
        case 4:
            print(orderListByAuthor(notBorrowedList))
        # PRINTS ALL NON-BORROWED BOOKS ORDERED BY CODE
        case 5:
            print(orderListByCode(notBorrowedList))
        # PRINTS ALL EXPIRING BOOKS (IN 2 DAYS)
        case 6:
            findExpiringBooks(booksList)
        # EXIT CASE WITH CONFIRM
        case 7:
            # STRING VARIABLE TO CONFIRM USER EXIT
            dywExit=input('Are you sure you want to exit? (Y/N)')

            # 'WHILE' THAT CONTROLS THAT THE USER GIVES A VALID INPUT ANSWER
            while dywExit != 'N' and dywExit != 'Y':
                # USER HAS TO REWRITE THE ANSWER IF IT'S NOT VALID
                dywExit=input('Only options are Y and N. Write a valid one: ')
            
            # RECALL THE EXIT BOOLEAN IF USER GIVES CONFIRM
            if dywExit == 'Y':
                exitConfirm = True
        # DEFAULT CASE
        case _:
            print('Insert a valid option')