import pandas as pd
from ics import Calendar, Event
from datetime import datetime
import pytz
import uuid

def create_ics_from_excel(excel_file, ics_file):
    # Read the Excel file
    df = pd.read_excel(excel_file)

    # Define the timezones
    tz_utc_plus_8 = pytz.timezone('Asia/Singapore')  # UTC+8
    tz_utc = pytz.utc  # UTC+0

    # Create a new calendar
    calendar = Calendar()

    # Iterate over the DataFrame and create events
    for index, row in df.iterrows():
        event = Event()
        event.name = row.get('Event Name', '')

        # Convert start time from UTC+8 to UTC+0
        start_time = row['Start Time'].replace(tzinfo=tz_utc_plus_8).astimezone(tz_utc)
        event.begin = start_time.strftime('%Y-%m-%d %H:%M:%S')

        # Convert end time from UTC+8 to UTC+0
        end_time = row['End Time'].replace(tzinfo=tz_utc_plus_8).astimezone(tz_utc)
        event.end = end_time.strftime('%Y-%m-%d %H:%M:%S')

        # Additional fields
        event.location = row.get('Location', '')
        event.description = row.get('Description', '')
        event.status = row.get('Status', 'CONFIRMED')
        event.organizer = row.get('Organizer', '')
        event.uid = row.get('UID', str(uuid.uuid4()))  # Generate a unique UID if empty
        event.created = datetime.now() if pd.isna(row.get('Created')) else pd.to_datetime(row['Created'])
        event.last_modified = datetime.now() if pd.isna(row.get('Last Modified')) else pd.to_datetime(row['Last Modified'])
        event.sequence = row.get('Sequence', 0)
        event.transp = row.get('Transparency', 'OPAQUE')

        calendar.events.add(event)

    # Write the calendar to an .ics file
    with open(ics_file, 'w', encoding='utf-8') as f:
        f.write(calendar.serialize())

if __name__ == "__main__":
    excel_file = r"D:\YK\Downloads\Sleep Data - hard coded.xlsx"  # Replace with your Excel file path
    ics_file = r'D:\YK\Downloads\Sleep Data.ics'  # Replace with your desired .ics file path
    create_ics_from_excel(excel_file, ics_file)