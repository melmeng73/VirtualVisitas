import pandas as pd
import random

def createGroups(allEmails, desired):
    # returns a list of the subgroups (which are also lists) of the emails.
    random.shuffle(allEmails)
    #desired = int(input("How many people would you like in a group: "))
    subgroups = [allEmails[x:x + desired] for x in range(0, len(allEmails), desired)]
    # if there's a group with less than desired number of people, evenly distribute amongst the other groups
    lastLen = len(subgroups[-1])
    if lastLen < desired:
        for x in range(lastLen):
            # if the remainder in the last group is larger than the number of subgroups, then it will add multiple people to the other groups.
            # Ex:
            subgroups[x % len(subgroups)].append(subgroups[-1][x])
            subgroups[-1][x] = 0

    subgroups = [x for x in subgroups if x != []]
    counter = 0
    for i in subgroups:
        for x in i:
            if x == 0:
                counter += 1
    if counter != 0:
        subgroups.pop(-1)
    return subgroups

def get_category_emails(All_Summary,allEmailsNoDuplicates,category):

#    category = input("Do groups by which category?")
    #get relevant category column
    category_Summary=All_Summary[category]
    
    #go through each category value
    category_strs=category_Summary.drop_duplicates()
    #list of category lists
    by_category=[]
    #relevant category value
    for category_val in category_strs:
        # print(major)
        #index of correct category values in category column
        category_yes=category_Summary[category_Summary==category_val].index
        category_yes=pd.Index.tolist(category_yes)
        # print(category_yes)
        
        #get specific emails that are correct e.g. 'History' in 'Major' column emails
        specific_emails = [allEmailsNoDuplicates[i] for i in category_yes]
        # print(specific_emails)
        by_category.append(specific_emails)
    print(by_category)
    return by_category

