"""Functions for data handling
Returns:
    _type_: _description_
"""
from collections import defaultdict
import json
import csv
from ReportGen.constant_vars import ConstantVar


def parse_fixed_width_file(file_path: str, cfg: dict) -> list:
    """Function for parsing a fixed width file with provided field definitions

    Args:
        file_path (str): Input data file
        cfg (dict): Dictionary with field definitions

    Returns:
        list: _description_
    """
    data = []
    with open(file_path, "r", encoding=ConstantVar.INPUT_FILE_ENC) as fd:
        for line in fd:
            record = {}
            for field, specs in cfg.items():
                start = specs["START"] - 1
                end = specs["END"]
                record[field] = line[start:end].strip()
            data.append(record)
    return data


def read_config(file: str) -> dict:
    """
    Reads JSON file and returns Python dict

    Args:
        file (str): File with field details in JSON format

    Returns:
        dict: Dictionary data
    >>> cfg = read_config('config/parse.json')
    >>> isinstance(cfg, dict)
    True
    >>> 'Name' in cfg
    True
    >>> cfg['RECORD_CODE']['LENGTH']
    3
    >>> cfg['CLIENT_TYPE']['LENGTH']
    4
    >>> cfg['CLIENT_NUMBER']['LENGTH']
    4
    """
    with open(file, "r", encoding=ConstantVar.CFG_FILE_ENC) as f:
        return json.load(f)


def verify_config(conf_data: dict) -> bool:
    """Verifies if the provided configuration data is correct

    Args:
        conf_data (dict): Dictionary data
    """
    all_good = True
    for key, value in conf_data.items():
        if value["LENGTH"] != value["END"] - value["START"]:
            print(f"{key}:length, start and end data are not matching")
            all_good = False
    return all_good


def generate_daily_summary(parsed_data: list) -> defaultdict:
    """
    This function processes the parsed data to generate the daily summary
    report as a dictionary with client and product information as keys and
    total transaction amount as values.

    Args:
        parsed_data (list): List of rows read from the file

    Returns:
        defaultdict: Client and product information as keys and total
        transaction amount as values
    >>> data = [{'RECORD_CODE': '315', 'CLIENT_TYPE': 'CL',
    'CLIENT_NUMBER': '4321', 'ACCOUNT_NUMBER': '0002',
    'SUBACCOUNT_NUMBER': '0001', 'OPPOSITE_PARTY_CODE': 'SGXDC',
    'PRODUCT_GROUP_CODE': 'FU', 'EXCHANGE_CODE': 'SGX', 'SYMBOL': 'NK',
    'EXPIRATION_DATE': '20100910', 'CURRENCY_CODE': 'JPY',
    'MOVEMENT_CODE': '01', 'BUY_SELL_CODE': 'B', 'QUANTTTY_LONG_SIGN': '',
    'QUANTITY_LONG': '0000000001', 'QUANTITY_SHORT_SIGN': '',
    'QUANTITY_SHORT': '0000000000', 'EXCH_BROKER_FEE_DEC': '000000000060',
    'EXCH_BROKER_FEE_D_C': 'D', 'ExCH_BROKER_FEE_CUR_CODE': 'USD',
    'CLEARING_FEE_DEC': '000000000030', 'CLEARING_FEE_D_C': 'D',
    'CLEARING_FEE_CUR_CODE': 'USD', 'COMMISSION': '000000000000',
    'COMMISSION_D_C': 'D', 'COMMISSION_CUR_CODE': 'JPY',
    'TRANSACTION_DATE': '20100820', 'FUTURE_REFERENCE': '001238',
    'TICKET_NUMBER': '0', 'EXTERNAL_NUMBER': '688032',
    'TRANSACTION_PRICE_DEC': '000092500000000', 'TRADER_INITIALS': '',
    'OPPOSITE_TRADER_ID': '', 'OPEN_CLOSE_CODE': 'O', 'FILLER': ''},
    {'RECORD_CODE': '315', 'CLIENT_TYPE': 'CL', 'CLIENT_NUMBER': '4321',
    'ACCOUNT_NUMBER': '0002', 'SUBACCOUNT_NUMBER': '0001',
    'OPPOSITE_PARTY_CODE': 'SGXDC', 'PRODUCT_GROUP_CODE': 'FU',
    'EXCHANGE_CODE': 'SGX', 'SYMBOL': 'NK', 'EXPIRATION_DATE': '20100910',
    'CURRENCY_CODE': 'JPY', 'MOVEMENT_CODE': '01', 'BUY_SELL_CODE': 'B',
    'QUANTTTY_LONG_SIGN': '', 'QUANTITY_LONG': '0000000001',
    'QUANTITY_SHORT_SIGN': '', 'QUANTITY_SHORT': '0000000000',
    'EXCH_BROKER_FEE_DEC': '000000000060', 'EXCH_BROKER_FEE_D_C': 'D',
    'ExCH_BROKER_FEE_CUR_CODE': 'USD', 'CLEARING_FEE_DEC': '000000000030',
    'CLEARING_FEE_D_C': 'D', 'CLEARING_FEE_CUR_CODE': 'USD',
    'COMMISSION': '000000000000', 'COMMISSION_D_C': 'D',
    'COMMISSION_CUR_CODE': 'JPY', 'TRANSACTION_DATE': '20100820',
    'FUTURE_REFERENCE': '001240', 'TICKET_NUMBER': '0',
    'EXTERNAL_NUMBER': '688058', 'TRANSACTION_PRICE_DEC': '000092500000000',
    'TRADER_INITIALS': '', 'OPPOSITE_TRADER_ID': '', 'OPEN_CLOSE_CODE': 'O',
    'FILLER': ''}]
    >>> summary = generate_daily_summary(data)
    >>> len(summary)
    1
    """
    summary = defaultdict(lambda: defaultdict(int))

    for record in parsed_data:
        client_info = tuple(record[field] for field in ConstantVar.CLIENT_INFO)
        product_info = tuple(record[field]
                             for field in ConstantVar.PRODUCT_INFO)
        quantity_long = int(record["QUANTITY_LONG"])
        quantity_short = int(record["QUANTITY_SHORT"])
        total_amount = quantity_long - quantity_short

        summary[client_info][product_info] += total_amount

    return summary


def write_csv(report_data: dict):
    """Generate CSV report file from the input report data dict

    Args:
        report_data (dict): _description_
    """
    with open(
        ConstantVar.OUTPUT_FILE, "w",
        encoding=ConstantVar.OUTPUT_FILE_ENC, newline=""
    ) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=ConstantVar.FIELD_NAMES)
        writer.writeheader()

        for client_info, products in report_data.items():
            for product_info, total_amount in products.items():
                client_info_str = ",".join(client_info)
                product_info_str = ",".join(product_info)
                writer.writerow(
                    {
                        "Client_Information": client_info_str,
                        "Product_Information": product_info_str,
                        "Total_Transaction_Amount": total_amount,
                    }
                )
