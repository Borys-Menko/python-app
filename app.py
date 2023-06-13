from project import create_app
import os
import logging

app = create_app()
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    print(os.getenv("DEBUG_MODE"))
    print("Welcome Home _______------____")
    app.run(debug=os.getenv("DEBUG_MODE"))
