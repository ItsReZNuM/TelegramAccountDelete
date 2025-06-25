# Telegram Account Deletion Tool 🚀

A Python-based command-line tool to securely and permanently delete your Telegram account via the official Telegram API. This script automates the process with a vibrant terminal interface, featuring colorful output, a cool unscramble effect, and double confirmation to prevent accidental deletions. 🛡️

## Features ✨
- **Secure Deletion**: Deletes your Telegram account using Telegram's official web API. 🔒
- **Double Confirmation**: Asks for two confirmations to ensure you mean to delete your account. ✅✅
- **Interactive CLI**: User-friendly terminal with colorful output powered by `colorama`. 🌈
- **Unscramble Effect**: Displays contact info with a stylish unscramble animation. 🎨
- **Error Handling**: Robust handling of API errors, invalid codes, and rate limits. 🛠️
- **Lightweight**: Minimal dependencies, using standard Python libraries. ⚡

## Requirements 📋
- Python 3.6 or higher 🐍
- Required Python packages:
  - `requests` 📡
  - `colorama` 🎨

## Installation 🛠️
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ItsReZNuM/telegram-account-deletion.git
   cd telegram-account-deletion
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually install:
   ```bash
   pip install requests colorama
   ```
3. **Run the Script**:
   ```bash
   python DeleteAccount.py
   ```

## Usage 📖
1. Start the script:
   ```bash
   python DeleteAccount.py
   ```
2. Follow the prompts:
   - Enter your phone number with country code (e.g., `+98XXXXXX`). 📞
   - Confirm you want to delete your account (first confirmation). ❓
   - Confirm again to be absolutely sure (second confirmation). ❗
   - Enter the verification code sent to your Telegram account. 🔑
3. Success! You'll see a confirmation message when your account is deleted. 🎉

### Example Output 📺
```
$$$$$$$\            $$$$$$$$\ $$\   $$\           $$\      $$\ 
$$  __$$\           \____$$  |$$$\  $$ |          $$$\    $$$ |
...

ReZNuM's Tool to Delete Telegram Account 🌟

Telegram: @ItsReZNuM | Instagram: ReZ.NuM | GitHub: https://github.com/ItsReZNuM
[+] Enter your number with country code [Ex: +98XXXXXX]: 
[!] Are you sure you want to delete your Telegram account? This action is irreversible! (yes/no): 
[!!] Are you ABSOLUTELY sure you want to delete your account? This is your final confirmation! (yes/no): 
[+] Enter the code sent to your Telegram account: 
...

Account successfully deleted! 🎉
```

## Important Notes ⚠️
- **Irreversible Action**: Deleting your Telegram account is permanent. All chats, contacts, and media will be gone forever. 😢
- **Rate Limits**: Telegram may block requests if you try too often. Wait 8 hours if you see a "too many tries" error. ⏳
- **Phone Number Format**: Use the correct country code (e.g., `+98` for Iran, `+1` for USA). 📱
- **Security**: This script only communicates with Telegram's official API (`my.telegram.org`). No data is stored locally. 🔐

## Troubleshooting 🧰
- **Invalid Code**: Double-check the code from Telegram. Codes expire quickly! 🔍
- **Server Errors**: Ensure your internet is stable and retry later if server issues occur. 🌐
- **Banned Account**: If your account is temporarily banned, wait 8 hours before retrying. ⏱️

## Contributing 🤝
We'd love your contributions! Here's how to get started:
1. Fork the repository. 🍴
2. Create a new branch (`git checkout -b feature-branch`). 🌿
3. Make your changes and commit (`git commit -m "Add new feature"`). ✍️
4. Push to the branch (`git push origin feature-branch`). 🚀
5. Open a Pull Request. 📬

Please follow the existing code style and include error handling in your changes.

## Contact 📩
Got questions, ideas, or issues? Reach out!
- **Telegram**: [@ItsReZNuM](https://t.me/ItsReZNuM) 💬
- **Instagram**: [ReZ.NuM](https://instagram.com/ReZ.NuM) 📸
- **GitHub**: [ItsReZNuM](https://github.com/ItsReZNuM) 🖥️

## Acknowledgments 🙌
- Built with [Python](https://www.python.org/), [requests](https://requests.readthedocs.io/), and [colorama](https://pypi.org/project/colorama/). 🛠️
- Inspired by the need for a simple, secure, and stylish Telegram account deletion tool. 💡

Happy coding! 😎