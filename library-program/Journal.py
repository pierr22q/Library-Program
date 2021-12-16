#Qiana Pierre ASSIGNMENT 2
#Attribution for any sources used: Valarie Barr, geeksforgeeks
#Description:  library system dealing with only four types of lendable objects: Books, Journals, CDs, and DVDs.

from Resource import Resource

class Journal(Resource):

    """
    Instance Variables
    Title
    Publisher
    Range of years published
    How often they are published (publishing frequency -- could be monthly, quarterly, etc.)
    Is it electronic or not: All Journals are assumed to be electronic -> True
    """
    def __init__(self,title,publisher,rangeOfYears,publishingFrequency):
        super().__init__(title, publisher,'Journal','True')
        self.rangeOfYears = rangeOfYears
        self.publishingFrequency = publishingFrequency

#getters
    def getRangeOfYears(self):
        return rangeOfYears

    def getPublishingFrequency(self):
        return publishingFrequency
#setters
    def setRangeOfYears(self, newRangeOfYears):
        self.rangeOfYears = newRangeOfYears

    def setPublishingFrequency(self, newPublishingFrequency):
        self.publishingFrequency = newPublishingFrequency

#str returns a string containing the variable information in aneasy-to-read way.
    def __str__(self):
        outstring3 = 'Year Range:'+ str(self.rangeOfYears) + '\n'
        outstring3 += 'Frequency:' + self.publishingFrequency + '\n'
        return  super().__str__() + outstring3
