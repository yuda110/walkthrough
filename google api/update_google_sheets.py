from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = '1T1o7XxzrIznXCsF5ZYsM6IN74-cVn2_eYrebY-aBf0s'


def main():
    values = [
        ['이건', '첫 번째', '힝입니다.'],
        ['첫 번째'],
        ['열입니다.'],
    ]
    body = {
        'values': values
    }

    credentials = ServiceAccountCredentials.from_json_keyfile_name('My Python Project-13f8199aebe1.json', SCOPES)
    http_auth = credentials.authorize(Http())
    service = build('sheets', 'v4', http=http_auth)
    request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                     range='시트1!A1:D3',
                                                     valueInputOption='RAW',
                                                     body=body)
    request.execute()


if __name__ == '__main__':
    main()
