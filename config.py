def init():
    import pandas as pd

    global All_Summary
    All_Summary = pd.read_excel("Virtual Visitas (Responses).xlsx")
    global allEmailsNoDuplicates
    global desired

    #remove all rows with duplicate emails except last
    All_Summary=All_Summary.drop_duplicates(subset=['Email Address'], keep='last').reset_index(drop=True)
    
    # make sure the exact name of the column is Email
    Summary = All_Summary["Email Address"]
    Summary = Summary.dropna()
    # Putting all the data into a pandas dataframe
    desired = int(input("How many people would you like in a group? "))
    allEmails1 = []
    for i in Summary:
        allEmails1.append(i)
    
    allEmailsNoDuplicates=list(allEmails1)
    # to test that all emails work
    # print(allEmailsNoDuplicates)
    # allEmails now contains all of the emails from the Excel file with all NaN values dropped
