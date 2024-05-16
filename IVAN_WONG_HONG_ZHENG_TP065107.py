#Ivan Wong Hong Zheng
#TP065107
#Joshua Jeshruen
#TP064585


EXIT_MESSAGE = "Exitting to Main Menu..."

#Register Users
def register():
    Username, Password, Password1 = "", "", ""
    Username = input("Create username:")
    Password = input("Create password:")
    Password1 = input("Confirm password:")
    data = {}
    usernames = []

    with open('database.txt', 'r') as db:
        for line in db.readlines():
            db_username, db_password = line.split(',')
            data[db_username] = db_password
            usernames.append(db_username)

    if Password != Password1:
        print("Password does not match, restart")
        register()
    else:
        if len(Password) <= 6:
            print("Password too short, restart:")
            register()
        elif Username in usernames:
            print("Username exists")
            register()
        else:
            with open('database.txt', 'a') as db:
                db.write(','.join([Username, Password]) + '\n')
            print("Success")


# Login
def access():
    Username = input("Enter username:")
    Password = input("Enter Password:")
    usernames = []
    data = {}

    if len(Username) > 0 and len(Password) > 0:

        data = {}
        with open('database.txt', 'r') as db:

            for line in db.readlines():
                db_username, db_password = line.strip('\n').split(',')
                data[db_username] = db_password
            usernames = data.keys()

        if Username in usernames:

            if Password == data[Username]:
                print("Login Successful")
                print("Hi", Username)
                mainMenu()
            else:
                print("Password or Username incorrect")

        else:
            print("Username or password doesn't exist")
    else:
        print("Please enter a value")

#Choose to login or signup
def home(option=None):
    option = input("Login | Signup: ")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter an option")


# main routine
#mainMenu()

def mainMenu():

    while True:
        print("1. Insert Data")
        print("2. Remove Data")
        print("3. Modify Data")
        print("4. View Data")
        print("5. Search Data")
        print("6. Quit")

        selection = int(input("Enter choice: "))
        if selection == 1:
            InsertData()
        elif selection == 2:
            RemoveData()
        elif selection == 3:
            ModifyData()
        elif selection == 4:
            ViewData()
        elif selection == 5:
            SearchData()
        elif selection == 6:
            print("Exitting...")
            exit(0)
        else:
            print("Invalid choice. Enter 1-6")
            mainMenu()


def InsertData():
    print("1. Insert Tenant Data")
    print("2. Insert Apartment Data")
    print("3. Return to main menu")

    selection = int(input("Enter choice: "))
    if selection == 1:
        insert_new_tenant_data()
    elif selection == 2:
        insert_new_apartment_details()
    elif selection == 3:
        print(EXIT_MESSAGE)
    else:
        print("Invalid choice. Enter 1-3")
        InsertData()


def RemoveData():
    print("1. Remove Tenant Data")
    print("2. Remove Apartment Data")
    print("3. Return to main menu")

    selection = int(input("Enter choice: "))
    if selection == 1:
        delete_tenant_data()
    elif selection == 2:
        delete_apartment_data()
    elif selection == 3:
        print(EXIT_MESSAGE)
    else:
        print("Invalid choice. Enter 1-3")
        RemoveData()



def ModifyData():
    print("1. Modify Tenant Data")
    print("2. Modify Apartment Data")
    print("3. Return to main menu")

    selection = int(input("Enter choice: "))
    if selection == 1:
        Modify_Tenant_Data()

    elif selection == 2:
        Modify_Apartment_Details()

    elif selection == 3:
        print(EXIT_MESSAGE)
    else:
        print("Invalid choice. Enter 1-3")
        ModifyData()




def ViewData():
    print("1. View Tenant Data")
    print("2. View Apartment Data")
    print("3. Return to main menu")

    selection = int(input("Enter choice: "))
    if selection == 1:
        View_Tenant_Data()

    elif selection == 2:
        View_Apt_Data()

    elif selection == 3:
        print(EXIT_MESSAGE)

    else:
        print("Invalid choice. Enter 1-3")
        ViewData()






def SearchData():
    print("1. Search Tenant Data")
    print("2. Search Apartment Data")
    print("3. Return to main menu")

    selection = int(input("Enter choice: "))
    if selection == 1:
        Search_Tenant_Data()

    elif selection == 2:
        Search_Apt_Details()

    elif selection == 3:
        print(EXIT_MESSAGE)

    else:
        print("Invalid choice. Enter 1-3")
        SearchData()






#Entering new tenant data
def insert_new_tenant_data():                       #define this function for admin to insert all the tenant data
    tenant_detail = []                              #set tenant detail as a array for store data inside
    while True:                                     #executes the loop body while the input evaluates to True
        Tenant_aptID = inputforValidation("Please enter tenant apartment ID: ", validate_tenantaptID)
        if Tenant_aptID == False:
            return

        Tenant_name = inputforValidation("Please enter tenant name: ", validate_CharacterName)
        if Tenant_name == False:
            return

        Tenant_identitynumber = inputforValidation("Please enter tenant identity number without dashes: ", validate_number)
        if Tenant_identitynumber == False:
            return

        Tenant_contactnumber = inputforValidation("Please enter tenant contact number without dashes: ", validate_number)
        if Tenant_contactnumber == False:
            return 

        Tenant_placeofbirth = inputforValidation("Please enter tenant place of birth: ", validate_CharacterName)
        if Tenant_placeofbirth == False:
            return

        Tenant_cityofbirth = inputforValidation("Please enter tenant city of birth: ", validate_CharacterName)
        if Tenant_cityofbirth == False:
            return 

        Tenant_workhistory = inputforValidation("Please enter tenant work history: ", validate_CharacterName)
        if Tenant_workhistory == False:
            return

        Tenant_currentwork = inputforValidation("Please enter tenant current employer: ", validate_CharacterName)
        if Tenant_currentwork == False:
            return

        #after input above each of the data, then set tenant data as a data storage for letting all the data to store inside  
        tenant_data = [Tenant_aptID, Tenant_name, Tenant_identitynumber, Tenant_contactnumber, Tenant_placeofbirth,
                    Tenant_cityofbirth, Tenant_workhistory, Tenant_currentwork]
        tenant_detail.append(tenant_data)                #append the data in tenant data storage to tenant detail list     


        options = input("Continue enter tenant data?(Y/N): ")   
        if options == "Y":
            continue
        elif options == "y":
            continue
        else:
            with open("tenant_data.txt","a") as fhand:       
                for record in tenant_detail:
                    for item in record:
                        fhand.write(item + ",")
                    fhand.write("\n")
            
                print(tenant_detail)                           #after all the data has append to the text file, it will display the data again
                print("Tenant data has been stored")
                break


def delete_tenant_data():

    while True:

        # Get Tenant ID from user
        Tenant_aptID = inputforValidation("Please enter tenant apartment ID that you wan to delete: ", validate_tenantaptID)
        if Tenant_aptID == False:
            return

        # Opening and reading tentant data.txt file
        with open("tenant_data.txt","r") as fhand:
            tenant_details = fhand.readlines()

        # Ensuring tenant details exists
        if len(tenant_details) == 0:
            print("No Tenant Data Found")
            return

        # iterate thru 'tenant_details' and extract only tenants that don't
        # match the apartment id
        new_tenant_details = []
        for record in tenant_details:

            # split each line into a list, so we can check the apartment ID
            tenant_split = record.split(",") 

            # if the first element (apartmentID) does NOT match the requested "Tenant_aptID"
            # then we add the record to the 'new_tenant_details' variable
            if tenant_split[0] != Tenant_aptID:

                new_tenant_details.append(','.join(tenant_split))
                continue

            # if the first element (apartmentID) does indeed match the requested "Tenant_aptID"
            # then we 'transfer' that record to the 'past_tenant_data.txt'
            if tenant_split[0] == Tenant_aptID:

                with open('past_tenant_data.txt', 'a') as fhand:
                    fhand.write(','.join(tenant_split))
                continue

        # write the 'new_tenant_details' to the filesystem
        # (we will overwrite the 'tenant_data.txt' with the contents of the 'new_tenant_details' variable)
        with open('tenant_data.txt', 'w') as fhand:

            fhand.writelines(new_tenant_details)

        # check with the user to see if they want to continue deleting tenant data
        options = input("Continue deleting tenant data?(Y/N): ")
        if options == "Y":
            continue
        elif options == "y":
            continue
        else:
            return

#View tenant data
def View_Tenant_Data():                                     #define this function for view all the tenant data
    with open("tenant_data.txt","r") as fhand:  
        for records in fhand:
            #display the tenant data and return a copy of the string with trailing characters removed                                
            print (records.rstrip().rstrip(","))            #separate one string into a records of multiple ones, based on the comma       

    while True:                                             #executes the loop body while the input is not 'E' or 'e'
            options = input("Press [E] to exit: ")
            if options == "E":
                break
            elif options == "e":
                break
            else:
                print("Invalid key, Press [E] again to exit: ")
                continue


#Search tenant data
def Search_Tenant_Data():                                   #define this function for search specific tenant data
    ID = input("Please enter tenant apartment ID: ")

    found = False                                          #the line will be printed out as found is always false, so when the input is false it will set to default at the beginning of each search
    with open("tenant_data.txt","r") as Data:              
        DataLine = Data.readlines()                        #after open the text files in read mode, read all the lines at a single go and then return them as each line a string element in a list
        for line in DataLine:
            list = line.strip("\n").split(",")             
            Tenant_aptID = list[0]                          #set tenant apartment ID as 0 in list, so that when admin entered the ID, it wont display the ID again
            Tenant_name = list[1]
            Tenant_identitynumber = list[2]
            Tenant_contactnumber = list[3]
            Tenant_placeofbirth = list[4]
            Tenant_cityofbirth = list[5]
            Tenant_workhistory = list[6]
            Tenant_currentwork = list[7]

            if ID == Tenant_aptID:
                #display all list 1-7 that are already set data as list from above
                print("1.Tenant_name:" ,Tenant_name)          #when the options has print the output, it, will display the list[1] that are declared as Tenant_name
                print("2.Tenant_identitynumber:" ,Tenant_identitynumber)
                print("3.Tenant_contactnumber:" ,Tenant_contactnumber)
                print("4.Tenant_placeofbirth:" ,Tenant_placeofbirth)
                print("5.Tenant_cityofbirth:" ,Tenant_cityofbirth)
                print("6.Tenant_workhistory:" ,Tenant_workhistory)
                print("7.Tenant_currentwork:" ,Tenant_currentwork)  
                found = True                                #if the input is exist in the data storage, it will set at true and will break the false loop
                break

        if found:                                           #if its true, it will print the data of the tenant ID that has been entered
            print 
        else:
            print("There is no data")

        while True:
            options = input("Press [E] to exit: ")
            if options == "E":
                break
            elif options == "e":
                break
            else:
                print("Invalid key, Press [E] again to exit: ")
                continue


#Modification tenant data
#define function FilePath for open the tenant_data.txt so that can call at other function without duplicate function
def FilePath(file):                                     #file in a parameter for call the file as tenant_data.txt that are set in function Modify_Tenant_Data
    records = []                                        #set records as a array for store data inside
    #open the tenant_data.txt to read the data inside  
    with open(file,"r") as data:                        
        for line in data:
            item = line.rstrip("\n").rstrip(",").split(",")     
            records.append(item)   
        return records


def ColumnInput(file):                                  #define this function for input the specific data for modify
    flag = False                                        #when the program is return to flag, it will end the loop and exit this function
    list = []                                           #its an empty list, after the data append into the list, it will be store inside to []
    with open (file,"r") as data:
        for line in data:  
            line = line.strip().strip(',').split(',')
            list.append(line[0])

    while True:
        Column = input("Please enter the tenant ID that you want to MODIFY: ")
        if Column not in list:
            options = input("The Tenant ID you entered does not exist! Press[E] to exit, any other key to continue: ")
            if options == "E":
                return flag                             #if its E/e button, set it as false and end the loop
            elif options == "e":
                return flag
            else:
                return ColumnInput(file)                #if its other than E/e button, it will call back to the ColumnInput function for read back the file

        return Column                                   #go back to the Column for input again the tenant ID


def TenantChoices(data, Column):
    flag = False                                        #when the program is return to flag, it will define as false and end the loop and exit this function
    for records in data:
        #since the enemurate is begin from 0, so set the input of tenant ID as records[0] and when it equals to Column then show the records of [1-8] 
        while records[0] == Column:                     
            print("1.Tenant_apartment ID:" ,records[0])
            print("2.Tenant_name:" ,records[1])
            print("3.Tenant_identitynumber:" ,records[2])
            print("4.Tenant_contactnumber:" ,records[3])
            print("5.Tenant_placeofbirth:" ,records[4])
            print("6.Tenant_cityofbirth:" ,records[5])
            print("7.Tenant_workhistory:" ,records[6])
            print("8.Tenant_currentwork:" ,records[7], "\n")
            choices = int(input("Select a data that you want to MODIFY(1-8): "))
            if not 1<=choices<=8:
                options = input("Invalid choices....Press[E] to exit, any other key to continue: ")
                if options == "E":
                    return flag
                elif options == "e":
                    return flag
                else:
                    return TenantChoices(data, Column)
            #set the choices to Subtract AND for help to auto deduct of the integer that user enter in choices since the enemurate begin from 0
            choices -=1                                                                            
            return choices


def replacement(Column, choices, DataReplace, data):
    for records in data:
        if Column == records[0]:                                    
            records[choices] = DataReplace                    #when admin entered the new data in choices, it will append to records and name it as DataReplace
    
    #open the tenant_data.txt file and write the new data that admin entered and update to the file
    with open("tenant_data.txt","w") as fhand:
        for records in data:
            for item in records:
                fhand.write(item)
                fhand.write(",")
            fhand.write("\n")


def Modify_Tenant_Data():
    while True:
        file = "tenant_data.txt"      
        data = FilePath(file)
        Column = ColumnInput(file)
        if Column == False:
            return
        choices = TenantChoices(data, Column)
        if choices == False:
            return
        DataReplace = input("Please enter the new data: ")
        replacement(Column, choices, DataReplace, data)
        print ("Your data has been succesfully stored!")
        options = input("Continue modify tenant data?(Y/N): ")
        if options == "Y":
            continue
        elif options == "y":
            continue
        else:
            break


#Entering new apartment details
def insert_new_apartment_details():                     #define this function for admin to insert all the apartment details
    Apartment_details=[]                                #set apartment detail as a array for store data inside
    while True:                                         #executes the loop body while the input evaluates to True
        Tenant_aptID = inputforValidation("Please enter occupant's ID: ", validate_tenantaptID)
        if Tenant_aptID == False:
            return

        Apartment_ExpectedRent = inputforValidation("Please enter expected rent(without RM): ", validate_Rental)
        if Apartment_ExpectedRent == False:
            return

        Apartment_RentalHistory = inputforValidation("Please enter the number of rental history: ", validate_Rental)
        if Apartment_RentalHistory == False:
            return

        Apartment_DateofAcquisition = inputforValidation("Please enter date of acquisition (YYYY-MM-DD): ", validate_date)
        if Apartment_DateofAcquisition == False:
            return 

        Apartment_PastRentalDate = inputforValidation("Please enter past rental date (YYYY-MM-DD): ", validate_date)
        if Apartment_PastRentalDate == False:
            return

        Apartment_Footage = inputforValidation("Please enter square ft of the apartment: ", validate_footage)
        if Apartment_Footage == False:
            return 

        #after input above each of the data, then set apartment details as a data storage for letting all the data to store inside
        details = [Tenant_aptID, str("RM "+Apartment_ExpectedRent), Apartment_RentalHistory, Apartment_DateofAcquisition, Apartment_PastRentalDate, str(Apartment_Footage+" square ft")]
        Apartment_details.append(details)           #append the data in apartment details storage to tenant detail list 


        options = input("Continue enter apartment details?(Y/N): ") 
        if options == "Y":
            continue
        elif options == "y":
            continue
        else:            
            with open("Apartment_details.txt","a") as fhand:                          
                for record in Apartment_details:
                    for item in record:
                        fhand.write(item + ",")
                    fhand.write("\n")

            print (Apartment_details)              #after all the details has append to the text file, it will display the details again
            print("Apartment details stored")
            break

insert_new_tenant_data()


#check if input is validations
def validate_tenantaptID(Tenant_aptID):             # check if the tenantID is equal to 3 and alphanumeric character or not
    if len(str(Tenant_aptID)) != 3:
        return False
    if not Tenant_aptID.isalnum():
        return False
    if Tenant_aptID.isalpha():
        return False

    return True


def validate_CharacterName(name):
    name = name.strip()                             # check if the character has content and not digit or not
    if len(name) < 1:
        return False
    for character in name:
        if character.isdigit():
            return False

    return True


def validate_number(num):                           # check if the input is digit and more than 13 or not
    if len(num) < 10:
        return False
    for character in num:
        if not character.isdigit():
            return False

    return True


def validate_Rental(rent):            #check if the expected rent is more than 1 and alphanumeric or not
    if len(rent) < 1:
        return False
    for character in rent:
        if not character.isalnum():
            return False

    return True


import datetime
def validate_date(date):                       #check if the date of acquisition is a date format or not
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False

    return True


def validate_footage(footage):
    footage=footage.strip()                          #check if the footage has content and alphanumeric or not
    if len(footage)<1:
        return False
    for characters in footage:
        if not characters.isalnum():
            return False

    return True 


def inputforValidation(text, validations):          #validate for input data if the input is invalid
    flag = False                                    #when the validation is return to flag, it will define as false and end the loop and exit this function
    while True:
        TenantData = input(text)
        if not validations(TenantData):
            options = input("Invalid data format.... Press[E] to exit, any other key to continue: ")
            if options == 'E':
                return flag                         #if its E/e button, set it as false and end the loop
            elif options == 'e':
                return flag
            else:
                return inputforValidation(text, validations)    #if its other than E/e button, it will call back to the inputforValidation function for read the file

        return TenantData                           #go back to the TenantData for input again the data

#Delete apartment data
def delete_apartment_data():

    #Get Apartment ID from User
    Tenant_aptID = inputforValidation("Please enter the apartment ID that you want to delete: ", validate_tenantaptID)
    if Tenant_aptID == False:
        return

    #Opening and reading apartment data.txt file
    with open("Apartment_details.txt","r") as fhand:
        apartment_details = fhand.readlines()

    #Ensuring apartment details exist
    if len(apartment_details) == 0:
        print("No Apartment Data Found")
        return

    new_apartment_details = []
    for record in apartment_details:

        apartment_split = record.split(",")

        if apartment_split[0] != Tenant_aptID:
            new_apartment_details.append(','.join(apartment_split))
            continue

        if apartment_split[0] == Tenant_aptID:

            with open("past_apartment_data.txt","a") as fhand:
                fhand.write(",".join(apartment_split))
                print("'" + Tenant_aptID + "' has been removed.")
                continue

    with open("Apartment_details.txt","w") as fhand:
        fhand.writelines(new_apartment_details)



#View all apartment details
def View_Apt_Data():                                    #define this function for view all the apartment details
    with open("Apartment_details.txt","r") as fhandler:     
        for records in fhandler:
            #display the apartment details and return a copy of the string with trailing characters removed
            print (records.rstrip().rstrip(","))        #separate one string into a records of multiple ones, based on the comma

    while True:                                         #executes the loop body while the input is not 'E' or 'e'
            options = input("Press [E] to exit: ")
            if options == "E":
                break                                   
            elif options == "e":
                break
            else:
                print("Invalid key, Press [E] again to exit: ")
                continue


#Search apartment details
def Search_Apt_Details():                               #define this function for search specific apartment details
    Apartment_ID = input("Please enter Tenant apartment ID that you want to search: ")          

    found = False                                       #the line will be printed out as found is always false, so when the input is invalid data it will set to default at the beginning of each search
    with open("Apartment_details.txt","r") as Data:
        DataLine = Data.readlines()                      #after open the text files in read mode, read all the lines at a single go and then return them as each line a string element in a list
        for line in DataLine:
            list = line.strip("\n").split(",")
            Tenant_aptID = list[0]                       #set tenant apartment ID as 0 in list, so that when admin entered the ID, it wont display the ID again
            Apartment_ExpectedRent = list[1]
            Apartment_RentalHistory = list[2]
            Apartment_DateofAcquisition = list[3]
            Apartment_PastRentalDate = list[4]
            Apartment_Footage = list[5]

            if Apartment_ID == Tenant_aptID:
                #display all list 1-7 that are already set data as list from above
                print("1.Expected Rent:" ,Apartment_ExpectedRent)
                print("2.Number of rental history:" ,Apartment_RentalHistory)
                print("3.Date of acquisition:" ,Apartment_DateofAcquisition)
                print("4.Past Rental Date:" ,Apartment_PastRentalDate)
                print("5.Footage:" ,Apartment_Footage)
                found = True                            #if the input is exist in the data storage, it will set at true and will break the false loop
                break

        if found:                                           #if its true, it will print the data of the tenant ID that has been entered
            print 
        else:
            print("There is no data")
        
        while True:
            options = input("Press [E] to exit: ")
            if options == "E":
                break
            elif options == "e":
                break
            else:
                print("Invalid key, Press [E] again to exit: ")
                continue


#Modification apartment details
#define function FilePath for open the tenant_data.txt so that can call at other function without duplicate function
def FilePath(file):                                         #file in a parameter for call the file as tenant_data.txt that are set in function Modify_Apartment_Details
    records = []                                            #set records as a array for store details inside
    with open(file,"r") as data:
        for line in data:
            item = line.rstrip("\n").rstrip(",").split(",")
            records.append(item)   
        return records


def ColumnInput(file):                                      #define this function for input the specific details for modify
    flag = False                                            #when the program is return to flag, it will end the loop and exit this function
    list = []                                               #its an empty list, after the details append into the list, it will be store inside to []
    with open (file,"r") as data:
        for line in data:  
            line = line.strip().strip(',').split(',')
            list.append(line[0])

    while True:
        Column = input("Please enter the occupant ID that you want to MODIFY: ")
        if Column not in list:
            options = input("The occupant ID you entered does not exist! Press[E] to exit, any other key to continue: ")
            if options == "E":
                return flag
            elif options == "e":
                return flag
            else:
                return ColumnInput(file)

        return Column


def ApartmentChoices(data, Column):
    flag = False                                                #when the program is return to flag, it will define as false and end the loop and exit this function
    for records in data:
        while records[0] == Column: 
            print("1.Apartment ID:" ,records[0])
            print("2.Expected Rent:" ,records[1])
            print("3.Number of rental history:" ,records[2])
            print("4.Date of acquisition:" ,records[3])
            print("5.Past Rental Date:" ,records[4])
            print("6.Footage:" ,records[5]) 
            choices = int(input("Select a detail that you want to MODIFY(1-6): "))
            if not 1<=choices<=6:
                options = input("Invalid choices....Press[E] to exit, any other key to continue: ")
                if options == "E":
                    return flag
                elif options == "e":
                    return flag
                else:
                    return ApartmentChoices(data, Column)
            choices -=1
            return choices


def replacement(Column, choices, DataReplace, data):
    for records in data:
        if Column == records[0]:
            records[choices] = DataReplace                          #when admin entered the new data in choices, it will append to records and name it as DataReplace

     #open the tenant_data.txt file and write the new data that admin entered and update to the file
    with open("Apartment_details.txt","w") as fhand:
        for records in data:
            for item in records:
                fhand.write(item)
                fhand.write(",")
            fhand.write("\n")


def Modify_Apartment_Details():
    while True:
        file = "Apartment_details.txt"      
        data = FilePath(file)
        Column = ColumnInput(file)
        if Column == False:
            return
        choices = ApartmentChoices(data, Column)
        if choices == False:
            return
        DataReplace = input("Please enter the new data: ")
        replacement(Column, choices, DataReplace, data)
        print ("Your details has been succesfully stored!")
        options = input("Continue modify apartment details?(Y/N): ")
        if options == "Y":
            continue
        elif options == "y":
            continue
        else:
            break

if __name__ == '__main__':

    home()

