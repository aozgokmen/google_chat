# OpsGenie On-Call Notification as a Cron Job

This project sends notifications to a Google Chat room about the current on-call user based on OpsGenie's schedule using a cron job.

## Overview

The script integrates with OpsGenie to fetch on-call user information and posts notifications to Google Chat. By setting this up as a cron job, the process is automated, running at specified times without manual intervention.

## Prerequisites

- Python 3.6 or higher.
- `requests` and `python-dotenv` libraries.
- Access to OpsGenie and Google Chat APIs.
- A Unix-like operating system for setting up the cron job.

## Setup

1. Environment Configuration:**
   Create a `.env` file in the project directory with the necessary API keys and webhook URLs:

   ```
   OPSGENIE_API_KEY=your_opsgenie_api_key
   SCHEDULE_IDENTIFIER=your_schedule_identifier
   GOOGLE_CHAT_WEBHOOK_URL=your_google_chat_webhook_url
   ```

2. Install Dependencies:**
   Ensure that Python and the required packages are installed. You can install the necessary Python packages using:

   ```bash
   pip install -r requirements.txt
   ```

3. Cron Job Configuration:**
   - Edit the crontab file by running `crontab -e` in your terminal.
   - Add a line to specify the frequency of the job, for example, to run at 9 AM every day:

   ```
   0 9 * * * /usr/bin/python /path/to/nobet_bot.py
   ```

   Replace `/usr/bin/python` with the path to your Python interpreter and `/path/to/nobet_bot.py` with the full path to the script.

## Usage

Once the cron job is configured, it will run automatically at the specified times. The script will fetch the on-call user from OpsGenie and send a notification to the configured Google Chat room.

## Monitoring and Logs

- Monitor the cron job execution through the system's cron logs, typically found in `/var/log/cron` or by checking the system mail inbox for cron job execution reports.
- Check the script logs or output redirection in the cron job setup for debugging.

![chat](https://github.com/aozgokmen/google_chat/assets/74674469/a97ee074-71a1-4e38-a716-b9a721612ae1)

