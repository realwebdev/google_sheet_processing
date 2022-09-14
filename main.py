# from oauth2client.service_account import ServiceAccountCredentials
import gspread

sa = gspread.service_account()
sh = sa.open('data_processing')
wks = sh.worksheet("data")
print('Rows: ', wks.row_count)
print('Rows: ', wks.col_count)

# gc = gspread.oauth(
#     credentials_filename='/home/webdev/Documents/google_sheet_processing/avian-bird-257818-31a232b9fbaf.json',
#     authorized_user_filename='/home/webdev/Documents/google_sheet_processing/avian-bird-257818-31a232b9fbaf.json'
# )

# credentials = {"installed": {"client_id": "46831077427-fidv0u87hgukeqc6afve3d6o5c2m2cna.apps.googleusercontent.com",
#                              "project_id": "avian-bird-257818", "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#                              "token_uri": "https://oauth2.googleapis.com/token",
#                              "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#                              "client_secret": "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",
#                              "redirect_uris": ["http://localhost"]}}
#
# gc, authorized_user = gspread.oauth_from_dict(credentials)
#
# sh = gc.open("data_processing")
#
# print(sh.sheet1.get('A1'))
