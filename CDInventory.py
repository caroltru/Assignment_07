#------------------------------------------#
# Title: Assignment06_Starter.py
# Title change: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Caroline Truong, 2021-Nov-21, Updated File for Assignment 6
# Caroline Truong, 2021-Nov-28, Updated File for Assignment 7
#------------------------------------------#

import pickle


# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object
strID = ""
strTitle = ""
stArtist = ""

# -- PROCESSING -- #
class DataProcessor:
    # TODO add functions for processing here
    pass

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            with open(file_name, 'rb') as ObjFile:
                data = pickle.load(ObjFile)
            return data
        
        except FileNotFoundError:
            print('File not found. Try a .dat file')
        ObjFile.close()
 
        
    @staticmethod
    def add_file(strID, strTitle, stArtist):
        """ Function to add new item to the table.
        
        Adds user provided information to the 2D table.
        
        Args:
            
            
        Returns:
            None.
        """
      
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        lstTbl.append(dicRow)

    @staticmethod
    def dele_file(file_name, table):
        """ Function to remove data from list of dictionaries
        
        Read the data from the 2D table and removes one dictionary row at a time.
        
        Args:
            
        Returns:
            None.
        """
        
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')      
        
    @staticmethod
    def write_file(file_name, table):
        """Function to save data from list of dictionaries to file
        
        Writes the data from 2D table (list of dictionaries) per row and saves it to file.
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        # TODOne Add code here
        with open(file_name, 'wb') as ObjFile:
            pickle.dump(table, ObjFile)
        ObjFile.close()
        

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # TODO add I/O functions as needed
    @staticmethod
    def add_inventory():
        """Asks user for new ID,CD Title and Artist
        
        Args: None.
            
        Returns: new ID, CD Title, Artist Name
        
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, stArtist
    
# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # TODO move IO code into function
        strID, strTitle, stArtist = IO.add_inventory()
        # 3.3.2 Add item to the table
        # TODOne move processing code into function
        try:
            FileProcessor.add_file(strID, strTitle, stArtist)
        except ValueError:
            print('\nID is invalid. Please add an integer.')
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        except ValueError:
            print('ID is invalid. Please enter an integer.')
        # 3.5.2 search thru table and delete CD
        # TODOne move processing code into function
        FileProcessor.dele_file(strFileName, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODOne move processing code into function
            print('saving')
            FileProcessor.write_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')