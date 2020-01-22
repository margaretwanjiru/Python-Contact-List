import pyperclip
import unittest # Importing the unittest module
from contact import Contact # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args: 
        unittest.TestCase: TestCase class that helps in creating 
    test cases
    '''    
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("James","Muriuki","0712345678","james@ms.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"james@ms.com")

    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)
# Items up here...

    # def test_save_multiple_contact(self):
    #         '''
    #         test_save_multiple_contact to check if we can save multiple contact
    #         objects to our contact_list
    #         '''
    #         self.new_contact.save_contact()
    #         test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
    #         test_contact.save_contact()
    #         self.assertEqual(len(Contact.contact_list),2)
# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Contact.contact_list = []

# other test cases here
    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
            test_contact.save_contact()
            self.assertEqual(len(Contact.contact_list),2)
# More tests above
  
    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)   
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
    @classmethod
    def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False
    def test_display_all_contacts(self):
            '''
            method that returns a list of all contacts saved
           '''

            self.assertEqual(Contact.display_contacts(),Contact.contact_list)

    
        
if __name__ == '__main__':
    unittest.main()