# Password Generator

> A secure and modern Windows password generator built with Python and CustomTkinter.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-UI-2B2D42?style=for-the-badge)](https://github.com/TomSchimansky/CustomTkinter)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Latest Release](https://img.shields.io/github/v/release/DevYash-001/Password-Generator?style=for-the-badge)](https://github.com/DevYash-001/Password-Generator/releases/latest)

Password Generator is a desktop app for creating strong random passwords with configurable length and character options. It is designed for Windows, uses Python's `secrets` module for secure randomness, and can be packaged as a standalone `.exe` with PyInstaller.

![Password Generator Screenshot](assets/password-generator.png)

> If the screenshot does not appear, make sure `assets/password-generator.png` exists in the repository.

## Download

### Windows executable

Download the latest Windows build from the GitHub Releases page:

[Download latest release](https://github.com/DevYash-001/Password-Generator/releases/latest)

If the release includes an `.exe` file, download it from the **Assets** section and run it directly on Windows.

### Source code

You can also run the app from source:

```bash
git clone https://github.com/DevYash-001/Password-Generator.git
cd Password-Generator
pip install -r requirements.txt
python src/main.py
```

## Features

- Cryptographically secure password generation
- Adjustable password length from 12 to 64 characters
- Lowercase letter support
- Uppercase letter support
- Number support
- Symbol support
- Guarantees selected character categories when generating passwords
- Password strength indicator
- Show and hide generated password
- Copy password to clipboard
- Modern dark interface
- Windows executable support through PyInstaller

## Security

This project uses Python's `secrets` module instead of the standard `random` module. The `secrets` module is designed for generating cryptographically strong random values suitable for passwords, tokens, and similar security-sensitive data.

Generated passwords are not intentionally stored or transmitted by the application. As with any password tool, use the app on a trusted device and avoid sharing generated passwords through insecure channels.

## Usage

1. Open the application.
2. Choose the password length.
3. Select the character types you want to include.
4. Generate a password.
5. Review the strength indicator.
6. Copy the password when ready.

## Tech Stack

- Python
- CustomTkinter
- `secrets`
- PyInstaller

## Project Structure

```text
Password-Generator/
+-- assets/
|   +-- icon.ico
|   +-- password-generator.png
+-- src/
|   +-- main.py
+-- .gitignore
+-- LICENSE
+-- PasswordGenerator.spec
+-- README.md
+-- requirements.txt
```

## Installation From Source

### Requirements

- Python 3.x
- `pip`

### Steps

```bash
git clone https://github.com/DevYash-001/Password-Generator.git
cd Password-Generator
pip install -r requirements.txt
python src/main.py
```

## Build the Windows Executable

The repository includes a PyInstaller spec file, so the simplest build command is:

```bash
pyinstaller PasswordGenerator.spec
```

After the build completes, check the `dist/` folder for the generated executable.

If you need to build manually instead of using the spec file, a typical command may look like this:

```bash
pyinstaller --onefile --windowed --icon=assets/icon.ico src/main.py
```

The exact output name may depend on the PyInstaller configuration.

## Roadmap

Planned or possible improvements:

- Attach the packaged `.exe` to the latest GitHub Release
- Add or update the screenshot at `assets/password-generator.png`
- Add automated checks or basic tests for password generation logic
- Add more release notes for future versions
- Improve documentation with troubleshooting notes

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the app locally.
5. Open a pull request with a clear description.

Useful links:

- [Repository](https://github.com/DevYash-001/Password-Generator)
- [Issues](https://github.com/DevYash-001/Password-Generator/issues)
- [Pull Requests](https://github.com/DevYash-001/Password-Generator/pulls)
- [Releases](https://github.com/DevYash-001/Password-Generator/releases)

## Reporting Security Issues

If you find a security issue, avoid posting sensitive details publicly. Open an issue with general information, or contact the repository owner through GitHub if a private contact method is available.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
