class library:
    #constructor method assign values to class
    def __init__(self, list, name):
        self.booklist=list
        self.name=name
        #dictionary to dispaly the lended books
        self.lenddict={}
    #method to display books
    def displayBooks(self):
        print(f"These are the books that are available:{self.name}") 
        #display each book in the booklist
        for book in self.booklist:
            print(book)
    #method to lend book
    def lendBook(self,user,book):
        #check if the book is not in the lab
        if book is not self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Book lended successfully")
        else:
            print(f"Book is alreay lended by {self.lenddict[book]}")    
    #method to add a book
    def addBook(self, book):
        self.booklist.append(book)
        print("Book added successfully")   
    #method to return a book
    def returnBook(self,book):
        self.lenddict.pop(book)
        print("Book returned successfully")        
#main function-run the program
def main():
    #create the book list
    books=library(['Thinking,fast and slow','The Handmaids Tale','The diary of a young girl'], "Blades of light")
    #user menu
    while(True):
        print(f"Welcome to the {books.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. lend a Book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue # display the menu again
        else:
            #convert binto int
            user_choice=int(user_choice)
        if user_choice==1:
            books.displayBooks() 
        elif user_choice==2:
            book=input("Enter the name of the book you want to lend:")
            user=input("Enter your name:")
            books.lendBook(user,book)
        elif user_choice==3:
            book=input("Enter the name of the book you want to add:")
            books.addBook(user,book) 
        elif user_choice==4:
            book=input("Enter the name of the book you want to return:")
            books.returnBook(user,book)
        else:
            print("Not a valid option") 
        print("Press q to quit") 
        user_choice2=input("Enter the letter q to quit:")
        if user_choice2=="q":
            break #stop code from execution
#run the main program
if __name__=="__main__":
    main()                  
                   
    
