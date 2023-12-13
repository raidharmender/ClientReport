"""Flask application with REST endpoint for generating report

Returns:
    _type_: _description_
"""

import json
import csv
from flask import Flask
from ConstantVar import ConstantVar
from processdata import read_config, parse_fixed_width_file
from processdata import generate_daily_summary, write_csv

app = Flask(__name__)


@app.route('/')
def index():
    cfg_dict = read_config(ConstantVar.CFG_FILE)
    parsed_data = parse_fixed_width_file(ConstantVar.INPUT_FILE, cfg_dict)
    daily_summary = generate_daily_summary(parsed_data)
    write_csv(daily_summary)
    return 'Daily summary report generated: Output.csv'


if __name__ == '__main__':
    app.run(debug=True)
