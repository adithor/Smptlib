# Daily Motivation Email Script

This Python script sends a motivational quote every Tuesday to a specified email address. It connects to your Gmail account to send the email securely.

## How it Works

1. **Read a Quote**: Every Tuesday, the script reads a random quote from a `quotes.txt` file.
2. **Send Email**: It sends this quote as an email to a specified recipient using Gmail's SMTP server.

## Prerequisites

- Python 3.x installed on your system.
- A Gmail account.
- `quotes.txt` file containing motivational quotes, with each quote on a new line.

## Setup Guide

### 1. Create an App Password in Google Security

For enhanced security, use an App Password instead of your regular Gmail password. Follow these steps:

1. Go to your Google Account's [Security page](https://myaccount.google.com/security).
2. Under "Signing in to Google," select **App passwords**. You might need to sign in again.
3. At the bottom, choose **Select app** and **Other (Custom name)**. Name it something like "Python Script".
4. Click **Generate**. You'll get a 16-character code.
5. Use this code as your password in the script.

> **Note:** App Passwords are specific to your Google account and provide limited access for specific applications. They are a secure way to use your Gmail account in third-party applications.

### 2. Hide Sensitive Information

Instead of hardcoding your email and password in the script, use environment variables for security:

#### On Windows:

1. Open the **Command Prompt**.
2. Set the environment variables using the following commands:
    ```bash
    setx MY_EMAIL "your-email@gmail.com"
    setx EMAIL_PASSWORD "your-generated-app-password"
    ```

#### On macOS and Linux:

1. Open the **Terminal**.
2. Set the environment variables using the following commands:
    ```bash
    export MY_EMAIL="your-email@gmail.com"
    export EMAIL_PASSWORD="your-generated-app-password"
    ```

You can then access these variables in your script using Python's `os` module.

### 3. Modify the Script

Update your script to read the email and password from environment variables.

