import os
from app import app

if __name__ == "__main__":
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_RUN_PORT", "3001"))
    debug = os.getenv("FLASK_ENV", "").lower() == "development"
    app.run(host=host, port=port, debug=debug)
