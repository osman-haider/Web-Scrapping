import gspread
from google.oauth2.service_account import Credentials

def inert_in_sheet(df,current_date, sheet_id):
    formatted_date = current_date.strftime("%Y-%m-%d")
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id)
    sheet.sheet1.clear()
    print("Sheet is Deleted")
    sheet.update_title(formatted_date)
    print("Sheet Title Updated")
    sheet.sheet1.clear()
    sheet.sheet1.update([df.columns.values.tolist()] + df.values.tolist())
    print("Data is Inserted in Google Sheet")