# Assignment Overview

In my program, I was able to read in a csv file and automatically correct the user inputs For 
most of the attributes

## How to run the code.
  
  First, make sure you have a compatible IDE for python 3.8 or higher.
  Once you have you system ready, please download the data file and the 
    python program named Assignment1_SGG180002 
  
 By opening the python file to your respected IDE, in the console
    type in this: python Assignment1_SGG180002.py 'data/data.csv'
  
## How does the code work?
  
  This code functions on if the user inputs the exact file name.
  The code will read in the file name and store the information into the 'reader' list.
  
  The reader list will the sent to our main method: ProcessFile, where most of the automation happens
  
  ### What happens in the ProcessFile method
    
    The method starts off by initionaizing a list to hold in our strings and a 
    dictionary to store the corrected information
    
    **Most of the FOR loops will iterate the dictionary's elements**
    
    The 1st FOR loop removes all known special character and lowercases every elemnent that contains
    a letter string.
    
    The 2nd FOR loop has the most action. StringELE stores the concatinate
      each element in the list one at a time. That way, we can use the 
      capitalize and upper string operates to specific indexes
       
       It is the ID and Phone numbers that were a bit more difficult to correctly implement as
       as I needed to create two seprate methods to neatly identify if the elements follows the 
       input regulations
       
       From there, I know that the elemnets follow their protocal and we send each element 
       of StringELE to the Person class to easily add into our Employee_Diction with 
       'createDic.__dict__'
       
  ## Where does this code fail in
    
    One huge flaw in my design is that there is very little check to see if first name, 
    last name, and middle initial are really letters. Secondly, the verification of the phone number
    realise on the length of the phone number instead of a deeper analysis such number placement. 
    The same kind of goes with ID, but I check to see if there is only 2 letters and 4 numbers.
    Just not in a particular order 
   
 ## Lessons learned
    
    This assignment served me as a great reminder of how unpractice I have been in python.
    Creating the class has allows been confusing to me and the usage of sysarg took the 
    longest to understand and implement correctly. I am a bit ashamed that most of 
    my FOR loops are still interated by numbers, but I am sure that I will grow out of that
    as I progress in this course
    
