# backend/app/core/config.py
import os
from dotenv import load_dotenv
from google.oauth2 import service_account

load_dotenv()


class Settings:
    PROJECT_NAME: str = "JourniQ Backend"
    FIREBASE_PRIVATE_KEY: str = os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n')
    FIREBASE_CLIENT_EMAIL: str = os.getenv("FIREBASE_CLIENT_EMAIL")
    FIREBASE_PROJECT_ID: str = os.getenv("FIREBASE_PROJECT_ID")


settings = Settings()

credentials = service_account.Credentials.from_service_account_info({
    "type": "service_account",
    "project_id": settings.FIREBASE_PROJECT_ID,
    "private_key_id": "46b17f5734706e6f3963ea076b90e217a46e22e0",
    "private_key": settings.FIREBASE_PRIVATE_KEY,
    "client_email": settings.FIREBASE_CLIENT_EMAIL,
    "client_id": "112204666777568295223",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firestore-service-account%40journiq.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})

