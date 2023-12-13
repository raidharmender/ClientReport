"""Flask application with REST endpoint for generating report

Returns:
    _type_: _description_
"""

from flask import Flask
from flask_restful import Api, Resource
from flasgger import Swagger
from constant_vars import ConstantVar
from process_data import read_config, parse_fixed_width_file
from process_data import generate_daily_summary, write_csv

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

@app.route("/")
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    cfg_dict = read_config(ConstantVar.CFG_FILE)
    parsed_data = parse_fixed_width_file(ConstantVar.INPUT_FILE, cfg_dict)
    daily_summary = generate_daily_summary(parsed_data)
    write_csv(daily_summary)
    return "Daily summary report generated: Output.csv"


if __name__ == "__main__":
    app.run(debug=True)
