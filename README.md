# Telegram Account Deletion Tool

A Python-based command-line tool to securely and permanently delete a Telegram account via the official Telegram API. This script automates the process of sending a verification code, validating it, and deleting the account with a user-friendly terminal interface, featuring colorful output and a confirmation mechanism to prevent accidental deletions.

## Features
- **Secure Deletion**: Deletes your Telegram account using Telegram's official web API.
- **Double Confirmation**: Prompts for two confirmations to ensure intentional account deletion.
- **Interactive CLI**: User-friendly terminal interface with colorful output using `colorama`.
- **Unscramble Effect**: Displays contact information with a visually appealing unscramble animation.
- **Error Handling**: Robust handling of API errors, invalid codes, and rate limits.
- **No External Dependencies**: Uses standard Python libraries and minimal third-party packages.

## Requirements
- Python 3.6 or higher
- Required Python packages:
  - `requests`
  - `colorama`

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ItsReZNuM/telegram-account-deletion.git
   cd telegram-account-deletion
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Alternatively, install the required packages manually:
   ```bash
   pip install requests colorama
   ```

3. **Run the Script**:
   ```bash
   python DeleteAccount.py
   ```

## Usage
1. Launch the script:
   ```bash
   python DeleteAccount.py
   ```
2. Follow the on-screen prompts:
   - Enter your phone number with the country code (e.g., `+98XXXXXX`).
   - Confirm your intent to delete the account (first confirmation).
   - Confirm again to ensure you are absolutely sure (second confirmation).
   - Enter the verification code sent to your Telegram account.
3. Upon successful execution, the script will display a confirmation message indicating that your account has been deleted.

### Example Output
```
$$$$$$$\            $$$$$$$$\ $$\   $$\           $$\      $$\ 
$$  __$$\           \____$$  |$$$\  $$ |          $$$\    $$$ |
...

ReZNuM's Tool to Delete Telegram Account 

Telegram: @ItsReZNuM | Instagram: ReZ.NuM | GitHub: https://github.com/ItsReZNuM
[+] Enter your number with country code [Ex: +98XXXXXX]: 
[!] Are you sure you want to delete your Telegram account? This action is irreversible! (yes/no): 
[!!] Are you ABSOLUTELY sure you want to delete your account? This is your final confirmation! (yes/no): 
[+] Enter the code sent to your Telegram account: 
...

Account successfully deleted!
```

## Important Notes
- **Irreversible Action**: Deleting a Telegram account is permanent and cannot be undone. All data, including chats, contacts, and media, will be lost.
- **Rate Limits**: Telegram may impose rate limits if too many requests are made. If you encounter a "too many tries" error, wait for 8 hours before retrying.
- **Phone Number Format**: Ensure the phone number is entered with the correct country code (e.g., `+98` for Iran, `+1` for the USA).
- **Security**: This script communicates directly with Telegram's official API (`my.telegram.org`). No sensitive data is stored locally.

## Troubleshooting
- **Invalid Code**: Ensure you enter the exact code sent by Telegram. Codes are time-sensitive and may expire.
- **Server Errors**: Check your internet connection and try again later if you encounter server-related errors.
- **Banned Account**: If your account is banned due to excessive attempts, wait for the specified period (usually 8 hours) before retrying.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please ensure your code follows the existing style and includes appropriate error handling.

## Contact
For questions, suggestions, or issues, reach out via:
- **Telegram**: [@ItsReZNuM](https://t.me/ItsReZNuM)
- **Instagram**: [ReZ.NuM](https://instagram.com/ReZ.NuM)
- **GitHub**: [ItsReZNuM](https://github.com/ItsReZNuM)

## Acknowledgments
- Built with [Python](https://www.python.org/), [requests](https://requests.readthedocs.io/), and [colorama](https://pypi.org/project/colorama/).
- Inspired by the need for a simple, secure, and user-friendly Telegram account deletion tool.