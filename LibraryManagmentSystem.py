def LMS():      #function declared for Library Management System
    print("Welcome to Skill Circle Library Management System")
    print("Press 1 for 101 Book Information.")
    print("Press 2 for 102 Book Information.")
    print("Press 3 for 103 Book Information.")
    print("Press 4 for 104 Book Information.")
    print("Press 5 for 105 Book Information.")
    Info()        #function call to display book information based on user input in LMS function

def Book101():        #function declared for book information 101
    print("Displaying information for Book 101...")
    print("Book Title:- Introduction to Python Programming")
    print("Author: Dr. Thyagaraju G. S ")
    print("Book Price:- Rs. 600.00")
    print("Description:-  This book will take you on a journey to master the basics of Python and explore its powerful features. ")
    print("Book Launch Date :- 14 November 2023")

def Book102():          #function declared for book information 102
    print("Book Title:- Statistics for Absolute Beginners")
    print("Author: Oliver Theobald ")
    print("Book Price:- Rs. 1731.00")
    print("Description:- Statistics for Absolute Beginners is the ultimate crash course for anyone looking to conquer statistics, even if you've never touched a textbook before. ")
    print("Book Launch Date :- 24 February 2020")

def Book103():          #function declared for book information 103 
    print("Book Title:- INTRODUCTION TO ARTIFICIAL INTELLIGENCE")
    print("Author: CHARNIAK")
    print("Book Price:-  Rs. 549.00")
    print("Description:- This book provides a comprehensive introduction to the field of artificial intelligence, covering key concepts and techniques.")
    print("Book Launch Date :- 1 January 2002")

def Book104():              #function declared for book information 104
    print("Book Title:- An Introduction to Machine Learning")
    print("Author: Miroslav Kubat")
    print("Book Price:- Rs. 4792.00")
    print("Description:- This textbook presents fundamental machine learning concepts in an easy to understand manner by providing practical advice, using straightforward examples, and offering engaging discussions of relevant applications.")
    print("Book Launch Date :- 18 August 2018")

def Book105():          #function declared for book information 105
    print("Book Title:- Introduction to SQL: Mastering the Relational Database Language")
    print("Author: Rick van der Lanse")
    print("Book Price:-  Rs. 5913.00")
    print("Description:-  This edition brings it up to date for the most recent SQL standard, as well as with the most recent versions of Microsoft SQL Server, Oracle, DB2, and MySQL. The author is an insider on the SQL standard committee.")
    print("Book Launch Date :- 5 October 2006 ")

def Info():        #function declared for userinput and to call realted book information functions
    a=int(input())
    if (a==1):
        Book101()       #Calling function for book 101 information in INFO function
        print("Do you want to continue?")
        print("Press 1 for continue")
        print("Press 2 for exit")
        c=int(input())
        if (c == 1):
            LMS()      #Calling LMS function in INFO function
        elif (c==2):
            print("Thank you for visiting SkillCircle Library Management System")
        else:
            print("Invalid input, please try again.")
            LMS()           #Calling LMS function in INFO function
    elif (a==2):
        Book102()       #Calling function for book 102 information in INFO function
        print("Do you want to continue?")
        print("Press 1 for continue")
        print("Press 2 for exit")
        c=int(input())
        if (c == 1):
            LMS()           #Calling LMS function in INFO function
        elif (c==2):
            print("Thank you for visiting SkillCircle Library Management System")
        else:
            print("Invalid input, please try again.")
            LMS()               #Calling LMS function in INFO function
    elif (a==3):        
        Book103()    #Calling function for book 103 information in INFO function
        print("Do you want to continue?")
        print("Press 1 for continue")
        print("Press 2 for exit")
        c=int(input())
        if (c == 1):
            LMS()    #Calling LMS function in INFO function
        elif (c==2):
            print("Thank you for visiting SkillCircle Library Management System")
        else:
            print("Invalid input, please try again.")
            LMS()    #Calling LMS function in INFO function

    elif (a==4):
        Book104()       #Calling function for book 104 information in INFO function
        print("Do you want to continue?")
        print("Press 1 for continue")
        print("Press 2 for exit")
        c=int(input())
        if (c == 1):
            LMS()   #Calling LMS function in INFO function
        elif (c==2):
            print("Thank you for visiting SkillCircle Library Management System")
        else:
            print("Invalid input, please try again.")
            LMS()   #Calling LMS function in INFO function

    elif (a==5):
        Book105()       #Calling function for book 105 information in INFO function
        print("Do you want to continue?")
        print("Press 1 for continue")
        print("Press 2 for exit")
        c=int(input())
        if (c == 1):
            LMS()   #Calling LMS function in INFO function
        elif (c==2):
            print("Thank you for visiting SkillCircle Library Management System")
        else:
            print("Invalid input, please try again.")
            LMS()   #Calling LMS function in INFO function
    else:
        print("Please Press valid key")
        print("Press 1 for continue")
        print("Press 2 for exit")
        c=int(input())
        if (c == 1):
            LMS()   #Calling LMS function in INFO function
        elif (c==2):
            print("Thank you for visiting SkillCircle Library Management System")
        else:
            print("Invalid input, please try again.")
            LMS()   #Calling LMS function in INFO function

LMS()       #Calling LMS function to start the program
