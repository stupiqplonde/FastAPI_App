import os

dir_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.dirname(dir_path)

DB_NAME = "app.db"
DATABASE_URL = f"sqlite:///{root_path}/{DB_NAME}"