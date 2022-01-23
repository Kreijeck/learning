from googleapiclient.discovery import build

api_key = 'AIzaSyAoGdbPRU1mH49W68vjvZ0r6G1q9dzF0wQ'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    id="UC46eF5IgqAbpFsWhF2ckdsA",
)

response = request.execute()

print(response)