import pandas as pd
from src.functions.core_functions import read_csv_to_dataframe, increment_id, return_four_letter_word
#import read_csv_to_dataframe
#import increment_id
#import return_four_letter_word
def test_read_csv():
    #arrange
    filename = "data/test_stock.csv"

    #act

    result = read_csv_to_dataframe(filename)

    #assert
    filetype = pd.DataFrame
    assert filetype == type(result)


def test_increment_id():
    old_id = 4
    new_id = increment_id(old_id)
    assert new_id == 5
   

def test_check_id():
    pass



def test_return_four_letter_word():
    newword = return_four_letter_word()
    assert len(newword) >= 8
    #assert newword.hasnumericvalue==true
    #has capitalletter
    #has special character
    