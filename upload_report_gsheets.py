import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone
from gspread_dataframe import set_with_dataframe

# Define the scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# Authenticate
credential_file = "YOUR_GCP_CRED.json"
creds = Credentials.from_service_account_file(credential_file, scopes=SCOPES)
client = gspread.authorize(creds)

def upload_predictions_to_gsheet(spreadsheet_id, data):
    """
    Upload model predictions to Google Sheets
    Create a new sheet with current date and time up to seconds

    Args:
        spreadsheet_id: Your Google Sheets id, e.g., {xxxxxx-xxxxxxxxx} in docs.google.com/spreadsheets/d/xxxxxx-xxxxxxxxx
        data: predictions DataFrame
    """
    # Get the current datetime
    now_utc_plus_8 = datetime.now().astimezone(timezone(timedelta(hours=8)))
    # Format the datetime in the desired format
    formatted_datetime = now_utc_plus_8.strftime("%Y-%m-%d-%H-%M-%S")
    # Open the spreadsheet
    sheet = client.open_by_key(spreadsheet_id).add_worksheet(
        title=formatted_datetime + "-predictions", rows=len(data), cols=len(data.iloc[0])
    )
    set_with_dataframe(sheet, data)

def upload_report_to_gsheet(spreadsheet_id, data, labels):
    """
    Upload scikit-learn formatted classification_report dict to Google Sheets
    Create a new sheet with current date and time up to seconds

    Args:
        spreadsheet_id: Your Google Sheets id, e.g., {xxxxxx-xxxxxxxxx} in docs.google.com/spreadsheets/d/xxxxxx-xxxxxxxxx
        data: scikit-learn classification_report output as dict
        labels: class names you want to save, e.g., ["positive", "negative", "neutral"]
    """

    metrics = ["precision", "recall", "f1-score", "support"]
    results = []
    results.append(["type"] + metrics)
    for label in labels:
        label_perf = []
        if perf := data.get(label):
            label_perf.append(label)
            for m in metrics:
                factor = 100 if m in ["precision", "recall", "f1-score"] else 1
                label_perf.append(float(f"{perf.get(m, 0) * factor:.1f}"))
        results.append(label_perf)

    # Get the current datetime
    now_utc_plus_8 = datetime.now().astimezone(timezone(timedelta(hours=8)))
    # Format the datetime in the desired format
    formatted_datetime = now_utc_plus_8.strftime("%Y-%m-%d-%H-%M-%S")
    # Open the spreadsheet
    sheet = client.open_by_key(spreadsheet_id).add_worksheet(
        title=formatted_datetime + "-report", rows=len(results), cols=len(results[0])
    )
    sheet.batch_update(
        data=[
            {"range": "A1", "values": results},
        ]
    )
