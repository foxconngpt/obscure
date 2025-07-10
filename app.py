from flask import Flask
from config import Config
from routes.dashboard import dashboard_bp
from routes.errdisable import errdisable_bp
from routes.diagnostico import diagnostico_bp
from routes.historico import historico_bp
from routes.analise import analise_bp
from routes.common import common_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY
    app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(errdisable_bp)
    app.register_blueprint(diagnostico_bp)
    app.register_blueprint(historico_bp)
    app.register_blueprint(analise_bp)
    app.register_blueprint(common_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
