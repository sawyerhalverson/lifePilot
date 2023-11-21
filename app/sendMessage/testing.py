import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

personalEmail = os.getenv("personal_email")
appPassword = os.getenv("googleAppKey")
phoneNumber = os.getenv("phoneNumber")

