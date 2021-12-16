#Qiana Pierre ASSIGNMENT 2
#Attribution for any sources used: Valarie Barr, geeksforgeeks
#Description:  library system dealing with only four types of lendable objects: Books, Journals, CDs, and DVDs.


from Resource import Resource


class CD(Resource):
    """
    Instance Variables
    Title
    Publisher
    Artist
    Recording company (used as Publisher field)
    Year
    Length
    Is it electronic or not: All CDs are assumed to be NOT electronic -> False
    """
    def __init__(self,title,publisher,artist,year,length):
        super().__init__(title,publisher,'CD',"False")
        self.artist = artist
        self.year = year
        self.length = length
#getters
    def getArtist(self):
        return self.artist

    def getYear(self):
        return self.year

    def getLength(self):
        return self.length
#setters
    def setArtist(self,newArtist):
        self.artist = newArtist

    def setYear(self,newYear):
        self.year = newYear

    def setLength(self,newLength):
        self.length = newLength
##str returns a string containing the variable information in aneasy-to-read way.

    def __str__(self):
        outstring4 = 'Artist:'+ self.artist + '\n'
        outstring4 += 'Year:' + str(self.year) + '\n'
        outstring4 += 'Length:' + str(self.length) + '\n'
        return  super().__str__() + outstring4
