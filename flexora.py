import os
import time
import ctypes
from datetime import datetime
from collections import defaultdict

# Constants for Windows volume control
VOLUME_MIN = 0
VOLUME_MAX = 100

# Time slots for different activities (24-hour format)
activity_time_slots = {
    'work': {'start': 9, 'end': 18},
    'leisure': {'start': 18, 'end': 22},
    'sleep': {'start': 22, 'end': 9}
}

# Volume settings for each activity
activity_volume_settings = {
    'work': 30,
    'leisure': 70,
    'sleep': 10
}

def set_system_volume(volume_level):
    """
    Set the system volume level on Windows
    :param volume_level: Desired volume level (0 to 100)
    """
    if VOLUME_MIN <= volume_level <= VOLUME_MAX:
        # Convert volume level to a scale of 0 to 65535
        new_volume = int((volume_level / 100) * 65535)
        ctypes.windll.winmm.waveOutSetVolume(0, new_volume)
    else:
        print(f"Volume level must be between {VOLUME_MIN} and {VOLUME_MAX}.")

def get_current_activity():
    """
    Determine current user activity based on the time of day.
    :return: Activity name (work, leisure, or sleep)
    """
    current_hour = datetime.now().hour
    for activity, times in activity_time_slots.items():
        if ((times['start'] <= current_hour < times['end']) or
            (times['start'] > times['end'] and (current_hour >= times['start'] or current_hour < times['end']))):
            return activity
    return 'leisure'  # Default activity

def main():
    """
    Main function to monitor and adjust volume based on activity.
    """
    last_activity = None

    while True:
        current_activity = get_current_activity()
        
        if current_activity != last_activity:
            volume_level = activity_volume_settings[current_activity]
            set_system_volume(volume_level)
            print(f"Activity: {current_activity}, Volume set to: {volume_level}%")
            last_activity = current_activity
        
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()