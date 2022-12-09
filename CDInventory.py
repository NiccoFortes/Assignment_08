#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# NFortes, 2022-Dec-8, Added functionality to code to alow usere to create, delete, store, and load data on CD's. Script stores data in a list of CD objects. CD objects being a custom class defined below..
#------------------------------------------#

import pickle 

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object


class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    
    #constructor
    def __init__(self,ID,title,artist):
        #attributes
        self.__cd_id = ID
        self.__cd_title = title
        self.__cd_artist = artist
    
    # Defining properties for class
    @property    
    def cd_id(self):
        return self.__cd_id 
    @cd_id.setter
    def cd_id(self,I):
        self.__cd_id = I 
        
    @property
    def cd_title(self):
        return self.__cd_title
    @cd_title.setter
    def cd_title(self,Title):
        self.__cd_title = Title
       
    @property
    def cd_artist(self):
        return self.__cd_artist
    @cd_artist.setter
    def cd_artist(self,Artist):
        self.__cd_artist = Artist          
    
    #methods
    

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """ 
    """Procxessing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of objects) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            Loaded data from storage.
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            #unpickleing data from storage
            with open(file_name, 'rb') as objFile:
                table = pickle.load(objFile)
        except FileNotFoundError as e:
            print('File does not found. Please check file name.')
            print(e)
        except Exception as e:
            print('File load error.')
            print(e)
        return table 
        

    @staticmethod
    def write_file(file_name, table):
        """Function to manage data export from list of dictionaries to file.
           Function writes data into text file.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            with open(file_name, 'wb') as objFile:        
            #pickling data and exporting
                pickle.dump(table, objFile)
        except FileNotFoundError as e:
            print('File does not found. Please check file name.')
            print(e)
        except Exception as e:
            print('File save error.')
            print(e)
    

# Data Procssing
class DataProcessor:
    """Handles processing of data within the list of CD objects"""
    
    @staticmethod
    def cd_delete(tbl, IDDel):
        """Function deletes row specified by user input
    
        Args :
            IDDel : ID of n 
            tbl : main storage list
        Returns:
            none, global variable deletes row within function.
        """
        global lstTbl
        
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row.cd_id == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

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
        table1 = []
        rowtable1 = ()
        for row in table:
            rowtable1 = (row.cd_id, row.cd_title, row.cd_artist)
            table1.append(rowtable1)
        
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table1:
            print('{}\t{} (by:{})'.format(*row))
        print('======================================')

    @staticmethod
    def cd_input():
        """Gets user input for menu selection
    
        Args:
            None.
    
        Returns:
            CD information fron user inputs (string): 
    
        """
        try:     
            intID = int(len(lstTbl))+1
            strTitle = input('What is the CD\'s title? ').strip()
            stArtist = input('What is the Artist\'s name? ').strip()
        except ValueError as e:
            print('ID input needs to be an interger')
            print(e)
        except Exception as e:
            print('Input error.')
            print(e)
        return intID, strTitle, stArtist

# -- Main Body of Script -- #    
lstTbl = FileIO.read_file(strFileName, lstTbl)

# Main Loop
while True:

    IO.print_menu()
    strChoice = IO.menu_choice()

    if strChoice == 'x':
        # Breaks out of loop.
        break

    if strChoice == 'l':
        # Loads data into given file.
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstTbl = FileIO.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    
    elif strChoice == 'a':
        # Creates CD object and adds to list of CD ofjects.
        intID, strTitle, stArtist = IO.cd_input()
        CDrow = CD(intID, strTitle, stArtist)
        lstTbl.append(CDrow)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.


    elif strChoice == 'i':
        # Displays inventory
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
   
    elif strChoice == 'd':
        # Deletes CD object in list.
        IO.show_inventory(lstTbl)
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
            CDIDDel = CD(intIDDel, "PLACE HOLDER", "PLACE HOLDER")
            DataProcessor.cd_delete(lstTbl, CDIDDel)    
            IO.show_inventory(lstTbl)
        except ValueError as e:
                print('ID input needs to be an interger')
                print(e)
        except Exception as e:
                print('Input error.')
                print(e)

      
        continue  # start loop back at top.
    
    elif strChoice == 's':
        # Saves current table data into given file
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        
        if strYesNo == 'y':
            FileIO.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
       
        continue  # start loop back at top.
    
    else:
        print('General Error')




