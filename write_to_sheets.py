from datetime import datetime
import os, json
import gspread
from google.oauth2.service_account import Credentials

# 讀取 Secrets
creds_json = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
sheet_id = os.getenv("SHEET_ID")

if not creds_json or not sheet_id:
    raise RuntimeError("Missing GOOGLE_SHEETS_CREDENTIALS or SHEET_ID env.")

creds_dict = json.loads(creds_json)
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)

gc = gspread.authorize(creds)
ws = gc.open_by_key(sheet_id).sheet1

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
ws.append_row([now, "GitHub Actions 自動記錄"])
print(f"Wrote timestamp to Google Sheet: {now}")
