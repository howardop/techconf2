import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="hlopgserver.postgres.database.azure.com"  #TODO: __DONE__ Update value
    POSTGRES_USER="hloadmin@hlopgserver" #TODO: __DONE__ Update value
    POSTGRES_PW="P@ssw0rd"   #TODO: __DONE__ Update value
    POSTGRES_DB="techconfdb"   #TODO: __DONE__ Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://howiesb2.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=7swZ0NCBYsVTg0+ap8jmHWrj03zuk5DOhDZBV3f+UpU=' #TODO: __DONE__ Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: "hlo4@cornell.edu"
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False