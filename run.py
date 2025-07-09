import os
import sys
from flask import Flask

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.routes import home as bp

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(
        __name__,
        static_folder=os.path.join(base_dir, '../frontend/static'),
        template_folder=os.path.join(base_dir, 'frontend/templates')
    )
    app.register_blueprint(bp)
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
