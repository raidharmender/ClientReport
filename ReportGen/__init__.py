"""Flask application with REST endpoint for generating report

Returns:
    _type_: _description_
"""

from ReportGen.constant_vars import ConstantVar
from ReportGen.process_data import read_config, parse_fixed_width_file
from ReportGen.process_data import generate_daily_summary, write_csv
from ReportGen.instances import create_app, create_api, create_swg


app = create_app()
api = create_api(app)
swagger = create_swg(app)


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
