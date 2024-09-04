from os import getenv
from os.path import join, dirname, abspath
from dotenv import load_dotenv


config_path = abspath(dirname(__file__))
root_dir = dirname(config_path)
env_path = join(root_dir, ".env")
load_dotenv(dotenv_path=env_path)


DB_HOST = getenv("DB_HOST", default="localhost")
DB_USER = getenv("DB_USER", default="root")
DB_PASSWORD = getenv("DB_PASSWORD", default="123456")
DB_PORT = getenv("DB_PORT", default=3313)  # outer port
DB_NAME = getenv("DB_NAME", default="gain_miles")
DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
