from PyPDF2 import PdfFileReader, PdfFileWriter
from getpass import getpass
def displayMenu():
    print("""          
            Welcome to PDF Player, Merge PDFs and Password Protect them easily !
            Please choose an option
            1. Merge PDFs
            2. Encrypt a PDF               
        """) 
def merge():
    # Getting the number of pdfs from the user
    nof = int(input("Enter the number of PDFs you have: "))
    # Creating a list of all the pdfs
    pdfs = []
    for i in range(nof):
        pdfs.append(input("Enter the URL of PDF No. " + str(i) + ": "))
    splitList = pdfs[0].split("\\")
    folderURL = ""
    for i in range(len(splitList)-1):
        folderURL += splitList[i]+"\\"  
    # Creating the pdfWriter() Object, need to encrypt it as well
    pdfWriter = PdfFileWriter()
    # Going through the list, adding each page of each pdf to PDFWriter Class
    for pdf in pdfs:
        pdfReader = PdfFileReader(pdf)
        numOfPages = pdfReader.getNumPages()
        for j in range(numOfPages):
            pageToBeAdded = pdfReader.getPage(j)
            pdfWriter.addPage(pageToBeAdded)    
    # Creating the newly merged file
    filename = input("Give a name to your new file: ")
    mergedFile = open(folderURL+filename+".pdf", "wb")
    encryptOrNot = input("Do you want to encrypt your file ? [Y/N]: ")
    while encryptOrNot.upper() != "Y" and encryptOrNot.upper() != "N":
        print("Please give answer in Y or N !")
        encryptOrNot = input("Do you want to encrypt your file ? [Y/N]: ")
    if encryptOrNot.upper() == "Y":
        # Getting a password
        password = str(getpass("Set Password for your file: "))
        password_confirmation = str(getpass("Confirm Password: "))
        while password != password_confirmation:
            print("Passwords don't match ! Try again :( ")
            password = str(getpass("Set Password for your file: "))
            password_confirmation = str(getpass("Confirm Password: "))
        pdfWriter.encrypt(password, password, True)
        print("File Encrypted Successfully!")    
    pdfWriter.write(mergedFile)
    mergedFile.close()
    print("HooRay !!! Your files have been merged !")
    return None

def encrypt(file):
    # Creating writer object
    pdfWriter = PdfFileWriter()
    # Creating Reader Object
    pdfReader = PdfFileReader(file)
    # Getting the number of pages in the Reader file
    numOfPages = pdfReader.getNumPages()
    # Getting each individual drive/folder name
    splitList = file.split("\\")
    folderURL = ""
    # Creating the URL of the Folder
    for i in range(len(splitList)-1):
        folderURL += splitList[i]+"\\"
    # Getting a new name for the file
    newName = input("We will create a new file in the same folder, \n Give a new name to your new encrypted file: ")
    # Opening the file
    new_file = open(folderURL+newName+".pdf", "wb")
    # Adding pages
    for i in range(numOfPages):
        pdfWriter.addPage(pdfReader.getPage(i))
    # Getting a password
    password = str(getpass("Set Password for your file: "))
    password_confirmation = str(getpass("Confirm Password: "))
    while password != password_confirmation:
        print("Passwords don't match ! Try again :( ")
        password = str(getpass("Set Password for your file: "))
        password_confirmation = str(getpass("Confirm Password: "))
    # Encrypting the pdfWriter Object
    pdfWriter.encrypt(password, password, True)
    # Writing the object to the file
    pdfWriter.write(new_file)  
    print("File Successfully Encrypted !!")
    new_file.close()
    return None
    
    
    
def main():
     main_choice = "Y"
     while main_choice == "Y":
        displayMenu()
        choice = int(input("Enter Choice: "))
        while choice != 1 and choice != 2:
            print("Invalid choice !")
            choice = int(input("Enter Choice: "))
        if choice == 1:
            merge()
        elif choice == 2:
            fileURL = input("Give URL of file you want to encrypt: ")
            encrypt(fileURL)
            
        print("\n")
        main_choice = input("Do you want to continue ? [Y/N]: ").upper()
        while main_choice.upper() != "Y" and main_choice.upper() != "N":
            print("Invalid choice !")
            main_choice = input("Do you want to continue ? [Y/N]: ").upper()
main()
input("Press the ENTER key to exit..")
    