"""To create instances of various classes
such as Flask, API, Swagger et al

Returns:
    _type_: _description_
"""

from flask import Flask
# from flask_restful import Api
from flask_restx import Api
from flasgger import Swagger


def create_app() -> Flask:
    """To create a Flask instance

    Returns:
        Flask: Flask app instance
    """
    return Flask(__name__)


def create_api(app_flask: Flask) -> Api:
    """Create an API instance

    Args:
        app (Flask): _description_

    Returns:
        Api: _description_
    """
    # return Api(app_flask)
    return Api(app_flask, version='1.0',
               title='Report Generation API', doc='/swagger')


def create_swg(app_flask: Flask) -> Swagger:
    """Create a swagger instance

    Args:
        app (Flask): _description_

    Returns:
        Swagger: _description_
    """
    return Swagger(app_flask)
