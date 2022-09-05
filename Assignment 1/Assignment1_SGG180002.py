from ast import Return
import sys
import csv
import re
import pathlib
import pickle
from unicodedata import digit

class Person:
    def __init__(self, Last_Name, First_Name, Mid_Initial, ID, Phone_Num):
         self.Last_Name = Last_Name
         self.First_Name = First_Name
         self.Mid_Initial = Mid_Initial
         self.ID = ID
         self.Phone_Num = Phone_Num     

    def Display(self):
        #A neat displat of the dictionary
        print("Employee ID:  ", self.ID)
        print("\t\t", self.First_Name, self.Mid_Initial, self.Last_Name)
        print("\t\t", self.Phone_Num) 
#End of class Person:

def ProcessFile(self):
    #Our sub string list to mess with
    NoSpecialChars = []
    
    #Our dictionary to store and return everything
    Employee_Diction = {}

    #We must remove any unwanted chars from the user input
    for index in range(0, len(self)):
        NoSpecialChars.append(re.sub(r'[.:;/?-_\n\t"\s"]', '-',self[index].lower()))
        index += 1

    #Double checking the file context from our dictionary
    for wordIndex in range(0,len(NoSpecialChars)):
        
        #Spliting each string element one at a time
        StringELE = NoSpecialChars[wordIndex].split(",")

        #Seeing if there is a Middle inital
        if StringELE[2] == "" or StringELE[2] == " ":
                StringELE[2] = 'X'
        else:
            StringELE[2] = StringELE[2].upper()

        #Captializing only the first letter in last_Name & First_Name
        StringELE[0] = StringELE[0].capitalize() 
        StringELE[1] = StringELE[1].capitalize()

        """ 
        Format of the NoSpecialChars = 
        ['Lastname' 'Firstname' 'Mid_Initial' 'ID3042' '123-456-7890']
        """
        #Splicing only ID section of StringELE
        StringELE[3] = ID_verified(StringELE[3])

        #Standerizing phone numbers
        StringELE[4] = phoneNum_verified(StringELE[4])

        #Create the dictionary for the fixed string input
        createDic = Person(StringELE[0], StringELE[1], StringELE[2], StringELE[3], StringELE[4])
        Employee_Diction[wordIndex] = createDic.__dict__ 
        #Employee_Diction = createDic.__dict__ 

    #End of FOR wordIndex in range loop

    return Employee_Diction
#End of def ProcessFile(self):

def ID_verified(self):
        loopEnder = True
        print(self)

        while loopEnder:
            #Variable for the 2 letters
            letter2 = re.findall("[A-Za-z][A-Za-z]", self)
            
            #Variable for the 4 numbers
            numbers4 = re.findall("[0-9][0-9][0-9][0-9]", self)

            if len(letter2) == 0 or len(numbers4) == 0:
                print("\nThere is nothing inputted for this ID: ", self)
                self = input("Please enter the correct ID!")

            elif len(letter2[-1]) != 2:
                print("\nThere is not enough letters in this ID: ", self)
                self = input("Please enter the correct ID!")

            elif len(numbers4[-1]) != 4:
                print("\nThere is not enough numbers in this ID: ", self, "Please enter the correct ID!")
                self = input("Please enter the correct ID!")

            else: 
                loopEnder = False
        #End of WHILE loopEnder:

        return self.upper()
#End of def ID_verified(self):

def phoneNum_verified(self):

    #making sure the phone number length is correct
    while len(self) != 12:
        print("There is not enough numbers in ", self, 
            ". Please ener the correct phone number!\n")
            
        #getting the fixed phone num 
        self = input("Reminder that the proper format is 123-456-7890:")
    #End of WHILE len(self) != 12:

    return self
#End of def phoneNum_verified(self):

if __name__ == '__main__':

    if len(sys.argv) > 2:
        print("You need to enter a valid filename. \nPlease try again.")
        quit()
                
    Filename = sys.argv[1]

    #Reading and storing the file content into an list
    #pathlib.Path.cwd().joinpath(Filename)
    with open( Filename, 'r')  as csvFile:
        #skipping the 1st line of reader
        reader = csvFile.read().splitlines()[1:]
    #End of reading the file and skipping the 1st line
    print("\n",len(reader),"\n")   
    print("I have just read:\n\n", reader)
    
    #Method call ProcessFile to read data.csv
    EmployeeReport = ProcessFile(reader)
    
    #pickle the EmployeeReport
    pickle.dump(EmployeeReport, open('EmployeeReport.pickle', 'wb'))

    #reading the pickle back in
    EmployeeReport_In = pickle.load(open('EmployeeReport.pickle', 'rb'))

    print("\nHere is our revised employee list.")
    for index in range(0, len(EmployeeReport_In)):

        #A dict sample for Person Class
        dictELE = EmployeeReport_In[index]

        #Displaying the diction one at a time
        human = Person(dictELE['Last_Name'], dictELE['First_Name'], dictELE['Mid_Initial'], dictELE['ID'], dictELE['Phone_Num'])
        human.Display()
        index += 1
        print("\n")
    
#End of Main?
