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
    def __init__(self, title, author, year, numPages, getArticleByTitle):
        super().__init__(title, author, year, numPages)
        self.getArticleByTitle = getArticleByTitle
    
    def getArticleByTitle(self, title):
        return f"Article '{title}' found in '{self.title}' magazine, Issue Number: {self.getArticleByTitle}"
    

# Example usage
novel = Novel("The Great Gatsby", "F. Scott Fitzgerald", 1925, 180, "Fiction", 9)
print(novel.displayDetails())
print(novel.calcReadTime(30))
print(novel.rateBook(5))
print(novel.reviewBook("A classic tale of love and loss."))
magazine = Magazine("National Geographic", "Various", 2023, 100, 5)
print(magazine.displayDetails())        