import pandas as pd
from src.functions.file_readers import read_csv_to_dataframe
def test_read_csv():
    #arrange
    filename = "data/test_stock.csv"

    #act

    result = read_csv_to_dataframe(filename)

    #assert
    filetype = pd.DataFrame
    assert filetype == type(result)   
#testing