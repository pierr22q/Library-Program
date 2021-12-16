#Qiana Pierre ASSIGNMENT 2
#Attribution for any sources used: Valarie Barr, geeksforgeeks
#Description:  library system dealing with only four types of lendable objects: Books, Journals, CDs, and DVDs.

from Resource import Resource


class DVD(Resource):
    """
    Instance Variables
    Title
    Publisher
    Performers
    Year
    Length
    Genre
    Is it electronic or not: All DVDs are assumed to be NOT electronic -> False
    """
    def __init__(self,title,publisher,performers,year,length,genre):
        super().__init__(title,publisher,'DVD',"False")
        self.performers = performers
        self.year = year
        self.length = length
        self.genre = genre

#getters
    def getPerformers(self):
        return self.performers

    def getYear(self):
        return self.year

    def getLength(self):
        return self.length
#setters
    def setYear(self,newYear):
        self.year = newYear

    def setLength(self,newLength):
        self.length = newLength

#str returns a string containing the variable information in aneasy-to-read way.

    def __str__(self):
        outstring5 = 'Year:' + str(self.year) + '\n'
        outstring5 += 'Length(min):' + str(self.length) + '\n'
        outstring5 += 'Performers:'+  self.performers + '\n'
        outstring5 += 'Genre:'+ self.genre + '\n'
        #del self.publisher
        return  super().__str__() + outstring5
