import unittest
from Preprocessing import *


class UnitTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    # So this test method is effectively cleaning for any 0 or missing values NaN
    def test_Remove_bad_rows(self):
        dirty_one = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/BadOne.csv')
        clean_one = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/CleanOneFile.csv')
        #removeNonNumericRows will be used on sample csv
        dirtyCleaned = removeNonNumericRows(dirty_one)
        #Coverting series for column Lat to list
        listA = list(dirtyCleaned['Lat'])
        listB = list(clean_one['Lat'])
        #assertEquals check both arguments are equals
        self.assertEquals(listA, listB)

    # So this test method is to demonstrate that method will not be cleaning string among numbers
    def test_Remove_bad_rows_StringTypeAmongNumbers(self):
        dirty_one = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/BadOneNew.csv')
        clean_one = pd.read_csv(
            'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/CleanOneFile.csv')
        #removeNonNumericRows will be used on sample csv
        dirtyCleaned = removeNonNumericRows(dirty_one)
        #Coverting series for column Lat to list
        listA = list(dirtyCleaned['Lat'])
        listB = list(clean_one['Lat'])
        # It is expected that it will not match as the removeBadDataMethod is not written in such a way
        #assertNotEquals check both arguments are not equals
        self.assertNotEquals(listA, listB)


if __name__ == "__main__":
    main()
