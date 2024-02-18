import unittest

from user import User
from main import Log_In_Window
from check_in import Summary, Check_in

class User_Input_Check(unittest.TestCase):

    def test_equal(self):
        # checking if "LOG IN" works when loging in to the system
        log_in = Log_In_Window()
        self.assertEqual(log_in.check_user_info("inkar", "12345"), True)
        self.assertEqual(log_in.check_user_info("inkar", "1234"), False)
        self.assertEqual(log_in.check_user_info("inkar", "123"), False)
        self.assertEqual(log_in.check_user_info("eero", "23456"), True)
        self.assertEqual(log_in.check_user_info("Inkar ", "12345"), False)
        self.assertEqual(log_in.check_user_info("", ""), False)
        
        # checking if "ADD" works when adding the new user
        dialog = User("ADD USER")
        self.assertEqual(dialog.check_new_user("", "1234", "2345"), 0)
        self.assertEqual(dialog.check_new_user("Inkar", "1234", "2345"), 1)
        self.assertEqual(dialog.check_new_user("inkar", "12345", "12345"), 2)
        self.assertEqual(dialog.check_new_user("miranda", "09876", "09876"), 3)
        
        summary = Summary()
        self.assertEqual(summary.calculate_nights("2020-12-10", "2020-12-15"), "5")
        self.assertEqual(summary.calculate_nights("2020-12-10", "2021-12-15"), "370")
        self.assertEqual(summary.calculate_nights("2020-12-10", "2020-12-11"), "1")
        
        
        self.assertEqual(summary.calculate_price("VIP", "family", 10), 500)
        self.assertEqual(summary.calculate_price("normal", "family", 1), 35)
        self.assertEqual(summary.calculate_price("VIP", "double", 2), 90)
        self.assertEqual(summary.calculate_price("economy", "single", 10), 100)
        
        check_in = Check_in()
        self.assertEqual(check_in.check_date("2022-06-07", "2022-06-12", "2022-06-07", "2022-06-09"), "OVERLAP")
        self.assertEqual(check_in.check_date("2022-06-07", "2022-06-09", "2022-06-08", "2022-06-09"), "OVERLAP")
        self.assertEqual(check_in.check_date("2022-06-07", "2022-06-08", "2022-06-07", "2022-06-09"), "OVERLAP")
        self.assertEqual(check_in.check_date("2022-06-07", "2022-06-09", "2022-06-09", "2022-06-10"), "OK")
        self.assertEqual(check_in.check_date("2022-06-07", "2022-06-15", "2022-06-16", "2022-06-18"), "OK")
        self.assertEqual(check_in.check_date("2022-06-07", "2022-06-09", "2022-06-06", "2022-06-10"), "OVERLAP")
        self.assertEqual(check_in.check_date("2022-06-07", "2022-06-09", "2022-06-20", "2022-06-21"), "OK")
        
        
if __name__ == '__main__':
    unittest.main()