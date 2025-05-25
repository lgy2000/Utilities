import sys
from pyicloud import PyiCloudService
from pyicloud.exceptions import PyiCloudFailedLoginException
from datetime import datetime


def verify_icloud_connection(email, password):
    try:
        api = PyiCloudService(apple_id=email, password=password)

        if api.requires_2fa:
            print("Two-factor authentication required.")
            code = input("Enter the code you received on one of your approved devices: ")
            result = api.validate_2fa_code(code)
            if not result:
                print("Failed to verify security code")
                sys.exit(1)
            if not api.is_trusted_session:
                print("Session is not trusted. Requesting trust...")
                result = api.trust_session()
                if not result:
                    print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
        elif api.requires_2sa:
            import click
            print("Two-step authentication required. Your trusted devices are:")
            devices = api.trusted_devices
            for i, device in enumerate(devices):
                print(f"  {i}: {device.get('deviceName', 'SMS to %s' % device.get('phoneNumber'))}")
            device = click.prompt('Which device would you like to use?', default=0)
            device = devices[device]
            if not api.send_verification_code(device):
                print("Failed to send verification code")
                sys.exit(1)
            code = click.prompt('Please enter validation code')
            if not api.validate_verification_code(device, code):
                print("Failed to verify verification code")
                sys.exit(1)
        print("Successfully connected to iCloud")

        return api
    except PyiCloudFailedLoginException as e:
        print(f"Failed to log in to iCloud: {e}")


def create_event(api, calendar_name, event_title, event_start, event_end):
    # Find the calendar by name
    calendars = api.calendar.calendars()  # Call the method to get the list of calendars
    calendar = next((cal for cal in calendars if cal['title'] == calendar_name), None)
    if not calendar:
        print(f"Calendar '{calendar_name}' not found.")
        return

    # Create the event
    event = {
        'title': event_title,
        'location': '',
        'starts': event_start,
        'ends': event_end,
        'alarms': [],
        'notes': '',
        'url': '',
    }
    api.calendar.create(event, calendar['guid'])
    print(f"Event '{event_title}' created successfully in calendar '{calendar_name}'.")

def main(_email_address_ios_calendar, _email_password_ios_calendar, calendar_name, event_title, event_start, event_end):
    api=verify_icloud_connection(_email_address_ios_calendar, _email_password_ios_calendar)
    create_event(api, calendar_name, event_title, event_start, event_end)


if __name__ == "__main__":
    from config import email_address_ios_calendar, email_password_ios_calendar

    calendar_name = '📅 Sleep Log'  # Replace with your calendar name
    event_title = 'Meeting with Team'
    event_start = datetime(2025, 3, 27, 10, 0)  # Replace with your event start time
    event_end = datetime(2025, 3, 27, 11, 0)  # Replace with your event end time

    main(email_address_ios_calendar, email_password_ios_calendar, calendar_name, event_title, event_start, event_end)