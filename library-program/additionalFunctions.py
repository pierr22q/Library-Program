#Qiana Pierre ASSIGNMENT 2
#Attribution for any sources used: Valarie Barr, geeksforgeeks
#Description:   several additional functions that perform different tasks on an array

from Resource import Resource

def getAllCheckedOut(list):
    """
    takes an array of R​esource ​objects,
    and returns a smaller array of ​Resource​ objects.
    """
    allcheckedOut = []
    for i in range(0,len(list)):
        if Resource.getCheckedOut(list[i]) == True:
            allcheckedOut.append(list[i])
    return allcheckedOut

def getAllUserHasCheckedOut(list,user):
    """
    takes an array of ​Resource ​objects and a String,
    and returns a smaller array of ​Resource​ objects
    """
    allUsercheckedOut = []
    for i in range(0,len(list)):
        if Resource.getCheckedTo(list[i]) == user:
            allUsercheckedOut.append(list[i])
    return allUsercheckedOut


def getAllOfType(list,type):
    """
    takes an array of ​Resource ​objects and a String,
     and returns a smaller array of ​Resource​ objects
    """
    allOfType = []
    for i in range(0,len(list)):
        if Resource.getType(list[i]) == type:
            allOfType.append(list[i])
    return allOfType
