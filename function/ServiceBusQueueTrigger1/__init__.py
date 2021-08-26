## This folder will contains the Azure function code.

## Note:

# - Before deploying, be sure to update your requirements.txt file by running `pip freeze > requirements.txt`
# - Known issue, the python package `psycopg2` does not work directly in Azure; install `psycopg2-binary` instead to use the `psycopg2` library in Azure

# The skelton of the `__init__.py` file will consist of the following logic:

# ```
import ServiceBusQueueTrigger1 
import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

##################################################
## TODO: __DONE__ Refactor This logic into an Azure Function
## Code below will be replaced by a message queue
#################################################

def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    POSTGRES_URL='hlopgserver.postgres.database.azure.com'  #TODO: __DONE__ Update value
    POSTGRES_USER='hloadmin@hlopgserver' #TODO: __DONE__ Update value
    POSTGRES_PW = os.getenv('POSTGRES_PW')  #TODO: __DONE__ Update value
    POSTGRES_DB='techconfdb'   #TODO: __DONE__ Update value

    # Connect to the PostgreSQL database server
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
            host=POSTGRES_URL,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PW,
            port=5432)
            
        # create a cursor
        cur = conn.cursor()

        # TODO: Get notification message and subject from database using the notification_id
        cur.execute("SELECT message, subject FROM public.notification where id={}".format(notification_id))
        notification = cur.fetchone()
        notification_subject = notification[1]
        notification_message = notification[0]
        print("Info on notification {}: Subject={} and Message={}".format(notification_id, notification_subject, notification_message))

        # TODO: Get attendees email and name
        cur.execute("SELECT email, first_name FROM public.attendee")
        email = 0
        first_name = 1
        print("{} attendees".format(cur.rowcount))


        # TODO: Loop through each attendee and send an email with a personalized subject
        email_sent = 0
        for attendee in cur:
            subject = '{}: {}'.format(attendee[first_name], notification_subject)
            print("Send email to {}\nSubject: {}\nMessage = {}\n************".format(attendee[email], subject, notification_message))
            send_email(attendee[email], subject, notification_message)
            email_sent += 1


        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        notification_completed_date = datetime.utcnow()
        notification_status = 'Notified {} attendees'.format(email_sent)

        cur.execute("UPDATE notification SET completed_date=%s, status=%s where id=%s", (notification_completed_date, notification_status, notification_id))

    	# close the communication with the PostgreSQL
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        logging.error(error)
    finally:
        # TODO: Close connection
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def send_email(email, subject, body):
    message = Mail(
        from_email='howardop@outlook.com',
        #from_email='info@techconf.com',
        to_emails=email,
        subject=subject,
        plain_text_content=body)
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API'))
        
        #sg = SendGridAPIClient('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')
        response = sg.send(message)
        print("SendGrid Response Code = {}".format(response.status_code))
        print("SendGrid Response Body = {}".format(response.body))
        print("SendGrid Response Headers = {}".format(response.headers))
    except Exception as e:
        print(e.message)


