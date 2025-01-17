# Flexora

Flexora is a Python program designed to enhance your audio experience on Windows by automatically adjusting the system volume based on your daily activity patterns. It modifies system volume settings according to predefined time slots for work, leisure, and sleep activities.

## Features

- **Automatic Volume Adjustment**: Adjusts system volume based on time of day and user activity.
- **Customizable Time Slots**: Define your own time slots for different activities.
- **Customizable Volume Levels**: Set preferred volume levels for each activity.

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/flexora.git
   ```
2. Ensure you have Python installed on your system.

## Usage

Run `flexora.py` to start the program:

```bash
python flexora.py
```

The script will run in the background, adjusting the volume as per the schedule.

## Configuration

- Edit the `activity_time_slots` dictionary to change time slots for different activities.
- Edit the `activity_volume_settings` dictionary to set desired volume levels for each activity.

## Requirements

- Windows operating system
- Python 3.x

## Notes

- The program uses the Windows API to control system volume. Ensure you have the necessary permissions to adjust system settings.
- The default time slots and volume levels are set for typical work, leisure, and sleep hours but can be customized as per your needs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.