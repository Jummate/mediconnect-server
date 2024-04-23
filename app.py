from flask import Flask, request, make_response, jsonify
# from utils.error_custom import CustomException
# from flask_migrate import Migrate
from flask_cors import CORS

# from model.Todo import db

from routes.doctor_route import doctor_bp

# instantiate the database
app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":["http://127.0.0.1:5173", "http://localhost:5173"]}})

# load the configuration from the config file
# app.config.from_object("config")

# db.init_app(app)
# migrate = Migrate(app, db)

# db.create_all()

# register the route in the blueprint
app.register_blueprint(doctor_bp)


@app.errorhandler(404)
def not_found(error):
    # return f"Can't find {request.url} with {request.method} method on the server", 404
    return make_response(jsonify(message=f"Can't find {request.url} with {request.method} method on the server"), 404)

    # raise CustomException("This page does not exist at all", 404)

if __name__ == '__main__':
    app.run('127.0.0.1', port=3000, debug=True)