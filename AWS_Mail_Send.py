import boto3
from botocore.exceptions import ClientError
from openpyxl import load_workbook
from docx import Document

aws_access_key_id = 'xyz'
aws_secret_access_key = 'aws_secret_access_key '
AWS_REGION = 'region'
SENDER_EMAIL = 'info@example.net'


if __name__ == "__main__":
    excel_file = 'E:/PRACTICE/NumPy/data.xlsx'
    sheet_name = 'Sheet3'
    email_column = 'A'
    wordpad_file = 'E:/PRACTICE/NumPy/Template.docx'

    recipients = read_email_addresses_from_excel(excel_file, sheet_name, email_column)
    wordpad_content = read_docx_content(wordpad_file)

    ses_client = boto3.client('ses', region_name=AWS_REGION, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    sender_email = SENDER_EMAIL
    email_subject = 'User Attractive Web Application?'

    for recipient_email in recipients:
        send_ses_email(ses_client, sender_email, recipient_email, email_subject, wordpad_content)
