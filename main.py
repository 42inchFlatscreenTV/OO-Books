# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.



class Book:
    def __init__(self, title, author, year, numPages):
        self.title = title
        self.author = author
        self.year = year
        self.numPages = numPages

    def displayDetails(self):
        return f"'{self.title}' by {self.author} ({self.year}), {self.numPages} pages"
    
    def rateBook(self, rating):
        self.rating = rating
        return f"Rating for '{self.title}': {self.rating}/5"
    
    def reviewBook(self, review):
        self.review = review
        return f"Review for '{self.title}': {self.review}"

class Novel(Book):
    def __init__(self, title, author, year, numPages, genre, numChapters):
        super().__init__(title, author, year, numPages)
        self.genre = genre
        self.numChapters = numChapters
    
    def calcReadTime(self, readSpeed):
        readTime = self.numPages / readSpeed
        return f"Estimated read time for '{self.title}': {readTime} hours"
    
class Magazine(Book):
    def __init__(self, title, author, year, numPages, issueNumber):
        super().__init__(title, author, year, numPages)
        self.issueNumber = issueNumber
    
    def getArticleByTitle(self, title):
        return f"Article '{title}' found in '{self.title}' magazine, Issue Number: {self.issueNumber}"