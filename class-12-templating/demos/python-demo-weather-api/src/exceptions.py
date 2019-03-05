from . import app
from flask import render_template


@app.errorhandler(404)
def not_found(error):
    """Custom 404 Not Found handler.
    """
    return render_template('exceptions/404_notfound.html', error=error), 404


@app.errorhandler(400)
def bad_request(error):
    """Custom 400 Bad Request handler.
    """
    return render_template('exceptions/400_badrequest.html', error=error), 400
