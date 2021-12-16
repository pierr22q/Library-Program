#Qiana Pierre ASSIGNMENT 2
#Attribution for any sources used: Valarie Barr, geeksforgeeks
#Description:  library system dealing with only four types of lendable objects: Books, Journals, CDs, and DVDs.

from Resource import Resource

class Book(Resource):
    """
    Instance Variables:
    Title
    Publisher
    Is it electronic or not
    Number of Pages
    Publication Year
    Genre

    """
    def __init__(self,title,publisher,electronic,author,numOfPages,publicationYear,genre):
        super().__init__(title,publisher,'Book',electronic)
        self.author = author
        self.numOfPages = numOfPages
        self.publicationYear = publicationYear
        self.genre = genre

#getters
    def getAuthor(self):
        return self.author

    def getNumOfPages(self):
        return self.numOfPages

    def getPublicationYear(self):
        return self.publicationYear

    def getGenre(self):
        return self.genre
#setters
    def setAuthor(self,newAuthor):
        self.author = newAuthor

    def setNumOfPages(self,newNumOfPages):
        self.numOfPages = newNumOfPages

    def setPublicationYear(self,newPublicationYear):
        self.publicationYear = newPublicationYear

    def setGenre(self,newGenre):
        self.genre = newGenre

#str returns a string containing the variable information in aneasy-to-read way.
    def __str__(self):
        outstring2 = 'Author : '+ self.author + '\n'
        outstring2 += 'Number of Pages : '+ str(self.numOfPages) + '\n'
        outstring2 += 'Publication Year : '+ str(self.publicationYear) + '\n'
        outstring2 += 'Genre :' + self.genre + '\n'
        return  super().__str__() + outstring2
