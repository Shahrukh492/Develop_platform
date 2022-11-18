import pandas as pd
import cx_Oracle
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

dsn_tns1 = cx_Oracle.makedsn('<host_name>', '<port_number>', service_name='<service_name>')
con = cx_Oracle.connect(user=r'<user>', password=r'<password>', dsn=dsn_tns1)
df=pd.read_sql_query('SELECT name as "NAME",email AS "USERNAME",contact "MOBILE NO",created_on AS "DATE OF REGISTRATION" FROM RK_USER_MASTER where trunc (created_on) = trunc (sysdate)',con)
df.to_excel('Raksha.xlsx', index=False)
print('file generated')

#__Sending Mail_

message = Mail(
    from_email='<example@email.com>',
    to_emails='<senderemail@email.com>',
    subject='Today Registration',
    html_content='<strong>Message Pass</strong>'
)


with open('filename.xlsx', 'rb') as f:
    data = f.read()
    f.close()
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('filename.xlsx'),
    FileType('application/pdf'),
    Disposition('attachment')
)
message.attachment = attachedFile
try:
    #text_file = open("/home/oracle/sample.txt", "w")
    sg = SendGridAPIClient('<API_name>')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    #n = text_file.write("test"+str(response.status_code))
    #text_file.close()
except Exception as e:
    print(e)
print("mail sent")