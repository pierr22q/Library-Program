#Qiana Pierre ASSIGNMENT 2
#Attribution for any sources used: Valarie Barr, geeksforgeeks
#Description:  library system dealing with only four types of lendable objects: Books, Journals, CDs, and DVDs.

class Resource(object):
    """
    Instance Variables:

    Title
    Publisher
    Type (what kind of resource it is)
    Is it electronic or not
    Is it checked-out or not
    Who it is checked-out t

    """

    def __init__(self,title,publisher,type,electronic):
        self.title = title
        self.publisher = publisher
        self.type = type
        self.electronic = electronic
        self.checkedOut = False
        self.checkedTo =  " "

    def getTitle(self):
        """
        grabs the title and returns it(title).
        """
        return self.title

    def getType(self):
        """
        grabs the type and return it(type)
        """
        return self.type

    def getCheckedOut(self):
        """
        grabs a boolean

        True = Checked Out
        False = Not Checked Out
        """
        return self.checkedOut

    def getCheckedTo(self):
        """
        grabs who it is checked to and return it
        """
        return self.checkedTo

    def checkIn(self):
        """
        set the check-out variable to False and who it’s checked out to is an empty string;
         it doesn’t need any parameters.
        """
        self.checkedOut = False # set to False
        self.checkedTo = " " # empty string


    def checkOut(self,checkedTo):
        """
        string of who it’s going to, set the check-out variable to True,
        and set who it’s checked out to to the appropriate name.
        """
        self.checkedOut = True # set to True
        self.checkedTo = checkedTo # set to appropriate name

    def __str__(self):
        """
        returns a string containing the variable information in an
        easy-to-read way.
        """
        outstring = 'Title : '+ self.title + '\n'
        outstring += 'Type : '  + self.type+ '\n'
        if self.electronic == True: # checking if it is electronic or not
            outstring += 'Electronic' + '\n'
        outstring += 'Physical' + '\n'
        if self.checkedOut == False: #checking if its checked out or not
            outstring += "Available" + '\n'
        else:
            outstring += "Checked Out To: " +  self.checkedTo + '\n'
        outstring += 'Publisher : '+ self.publisher + '\n'
        return outstring
