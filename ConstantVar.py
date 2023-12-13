"""A class to cover all constants
used in this project
"""


class ConstantVar:
    """This class contains all the constants
    used in this project
    """
    CFG_FILE = 'config/parse.json'
    INPUT_FILE = "data/input.txt"
    OUTPUT_FILE = "data/Output.csv"
    CFG_FILE_ENC = "utf-8"
    INPUT_FILE_ENC = "utf-8"
    OUTPUT_FILE_ENC = "utf-8"
 
    CLIENT_INFO = ['CLIENT_TYPE', 'CLIENT_NUMBER',
                   'ACCOUNT_NUMBER', 'SUBACCOUNT_NUMBER']

    PRODUCT_INFO = ['EXCHANGE_CODE', 'PRODUCT_GROUP_CODE',
                    'SYMBOL', 'EXPIRATION_DATE']

    FIELD_NAMES = ['Client_Information', 'Product_Information',
                   'Total_Transaction_Amount']
