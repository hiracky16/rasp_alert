import json

from httplib2 import Http
from googleapiclient.discovery import build
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials

scopes = 'https://www.googleapis.com/auth/analytics.readonly'
# admin file
filename = "./project.json"

mail = ''

credentials = ServiceAccountCredentials.from_json_keyfile_name(filename, scopes=scopes)


http = credentials.authorize(Http())

calendar_service = build('calendar', 'v3', http=http)
calendar_list = calendar_service.calendarList().get(calendarId=mail).execute()

print(calendar_list['summary'])
