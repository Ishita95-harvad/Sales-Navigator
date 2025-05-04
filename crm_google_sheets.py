import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def add_lead_to_sheet(lead):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("LeadGeneration").sheet1
    sheet.append_row([lead['name'], lead['email'], lead['phone'], lead['company'], lead['interest']])