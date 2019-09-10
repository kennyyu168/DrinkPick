# Filename: pythonPick
# Date: 9/9/19
# Description: Python command line program to select drink based on keywords

# SQLite3 to manipulate database
import sqlite3

# DiffLib to compare keywords with 
import difflib

# Constants
SURPRISE_ME = "surprise me"

# Surprise me to determine random drink
surprise_me = False

# Function Name: findDrink()
# Function Description: Matches keywords and provides a list
# Parameters: keywords - an array of keywords to be inserted
# Side Effects: Finds the drink that best matches keywords
# Return Value: Name of the drink

# Function Name: getKeywords()
# Function Description: Gets input from user
# Parameters: None
# Side Effects: Inputs get stored in an array
# Return Value: Array of strings
def getKeywords(): 
    
    # Array to store keywords
    drinkType = []

    # Beginning message
    print( "What are you feeling today? \n" )

    # Get main type of drink
    whatCategory = input( "Coffee, tea, etc. OR Surprise me? " )
    drinkType.append( whatCategory )

    # Check if it's surprise me
    if whatCategory.lower() == SURPRISE_ME:
        surprise_me = True
        return 

    # Sweetened or unsweetened
    sweetened = input( "Sweetened? " )
    drinkType.append( sweetened )

    # Iced or hot
    temp = input( "Iced or hot? " )
    drinkType.append( temp )

    # Any other specifics
    specifics = input( "Any specifics? " )
    drinkType.append( specifics )

    # return array and use to find drinks
    return drinkType

if __name__ == "__main__":
    keywordArray = getKeywords()
 


