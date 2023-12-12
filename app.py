"""Flask application with REST endpoint for generating report

Returns:
    _type_: _description_
"""
from collections import defaultdict
import json
from flask import Flask
from ConstantVar import ConstantVar

app = Flask(__name__)


def parse_fixed_width_file(file_path: str, cfg: dict) -> list:
    """Function for parsing a fixed width file with provided field definitions

    Args:
        file_path (str): Input data file
        cfg (dict): Dictionary with field definitions

    Returns:
        list: _description_
    """
    data = []
    with open(file_path, 'r', encoding=ConstantVar.INPUT_FILE_ENC) as fd:
        for line in fd:
            record = {}
            for field, specs in cfg.items():
                start = specs['START'] - 1
                end = specs['END']
                record[field] = line[start:end].strip()
            data.append(record)
    return data


def read_config(file: str) -> dict:
    """Reads JSON file and return Python dict

    Args:
        file (str): File with field details in JSON format

    Returns:
        dict: Dictionary data
    """
    with open(file, 'r', encoding=ConstantVar.CFG_FILE_ENC) as f:
        return json.load(f)


def verify_config(conf_data: dict) -> bool:
    """Verifies if the provided configuration data is correct

    Args:
        conf_data (dict): Dictionary data
    """
    all_good = True
    for key, value in conf_data.items():
        if value['LENGTH'] != value['END'] - value['START']:
            print(f"{key}:length, start and end data are not matching")
            all_good = False
    return all_good


def generate_daily_summary(parsed_data: list) -> defaultdict:
    """This function processes the parsed data to generate the daily summary
    report as a dictionary with client and product information as keys and
    total transaction amount as values.

    Args:
        parsed_data (list): List of rows read from the file

    Returns:
        defaultdict: Client and product information as keys
        and total transaction amount as values.
    """
    summary = defaultdict(lambda: defaultdict(int))

    for record in parsed_data:
        client_info = tuple(
            record[field] for field in ['CLIENT_TYPE', 'CLIENT_NUMBER',
                                        'ACCOUNT_NUMBER', 'SUBACCOUNT_NUMBER']
        )
        product_info = tuple(
            record[field] for field in ['EXCHANGE_CODE', 'PRODUCT_GROUP_CODE',
                                        'SYMBOL', 'EXPIRATION_DATE']
        )
        quantity_long = int(record['QUANTITY_LONG'])
        quantity_short = int(record['QUANTITY_SHORT'])
        total_amount = quantity_long - quantity_short

        summary[client_info][product_info] += total_amount

    return summary
    

@app.route('/')
def index():
    cfg_dict = read_config(ConstantVar.CFG_FILE)
    parsed_data = parse_fixed_width_file(ConstantVar.INPUT_FILE, cfg_dict)
    return 'Hello, Flask!'


if __name__ == '__main__':
    app.run(debug=True)
