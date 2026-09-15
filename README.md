# 🔐 Password Generator

<p align="center">
  <strong>A secure, modern, and lightweight password generator for Windows</strong>
</p>

<p align="center">
  Built with <strong>Python</strong> + <strong>CustomTkinter</strong> with security-focused password generation using Python's <code>secrets</code> module.
</p>

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-GUI-1F6FEB?style=for-the-badge)](https://github.com/TomSchimansky/CustomTkinter)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</p>

---

## ✨ Overview

**Password Generator** is a desktop application designed to generate strong and customizable passwords through a clean, modern Windows interface.

The application allows users to control password length and character types while providing a password-strength indicator and convenient clipboard functionality.

Security is a core focus of the project. Password generation uses Python's built-in `secrets` module, which is designed for generating cryptographically strong random values.

---

## 🎯 Why This Project?

Weak and reused passwords remain a common security problem.

This project was built to provide a simple desktop tool that makes generating strong passwords quick, convenient, and accessible without requiring an online password generator.

### Key goals

- 🔐 Generate stronger passwords
- ⚡ Make password generation fast and simple
- 🖥️ Provide a modern desktop interface
- 🛡️ Use security-focused randomness
- 📋 Make generated passwords easy to copy
- 📦 Provide a standalone Windows executable

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🔐 Secure Generation | Uses Python's `secrets` module for security-focused randomness |
| 📏 Custom Length | Generate passwords from **12–64 characters** |
| 🔤 Lowercase | Include lowercase letters |
| 🔠 Uppercase | Include uppercase letters |
| 🔢 Numbers | Include numeric characters |
| 🔣 Symbols | Include special characters |
| 🛡️ Character Guarantees | Selected character categories are represented in the generated password |
| 📊 Strength Indicator | Displays an indication of password strength |
| 👁️ Show / Hide | Toggle password visibility |
| 📋 Copy to Clipboard | Copy generated passwords quickly |
| 🌙 Modern UI | Clean dark-themed CustomTkinter interface |
| 🪟 Windows Executable | Can be packaged as a standalone `.exe` |

---

## 🖼️ Application Preview

> Add screenshots of the application here.

<p align="center">
  <img src="assets/Screenshot 2026-09-15 125616.png" alt="Password Generator application screenshot" width="750">
</p>

### 💡 Recommended screenshots

Add 2–3 screenshots showing:

1. Main password generator interface
2. Generated strong password
3. Password strength indicator / settings

---

## 🛠️ Tech Stack

### Programming Language

- 🐍 Python

### GUI

- 🎨 CustomTkinter

### Security

- 🔐 Python `secrets`

### Packaging

- 📦 PyInstaller

### Development Tools

- Git
- GitHub
- Virtual Environment

---

## 📂 Project Structure

```text
Password-Generator/
│
├── assets/
│   └── icon.ico
│
├── src/
│   └── main.py
│
├── .gitignore
├── LICENSE
├── PasswordGenerator.spec
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/DevYash-001/Password-Generator.git
```

### 2. Navigate into the project

```bash
cd Password-Generator
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python src/main.py
```

---

## 📦 Build the Windows Executable

The project includes a PyInstaller specification file.

Install PyInstaller if required:

```bash
pip install pyinstaller
```

Then build the application using:

```bash
pyinstaller PasswordGenerator.spec
```

The generated executable will be available inside the `dist/` directory.

---

## 🔐 Security

Security is one of the main design considerations of this project.

### `secrets` instead of `random`

The application uses Python's:

```python
import secrets
```

instead of the standard:

```python
import random
```

The `secrets` module is intended for security-sensitive random value generation.

### Password handling

The application does not intentionally store or transmit generated passwords.

> **Important:** No password generator should be treated as a complete security solution by itself. Users should also use unique passwords and, where possible, a trusted password manager and multi-factor authentication.

---

## 🧠 How It Works

The basic workflow is:

```text
User
  │
  ▼
Select Password Options
  │
  ├── Length
  ├── Lowercase
  ├── Uppercase
  ├── Numbers
  └── Symbols
  │
  ▼
Secure Password Generation
  │
  ▼
Password Strength Evaluation
  │
  ▼
Display Generated Password
  │
  ├── Show / Hide
  └── Copy to Clipboard
```

---

## 🎨 Interface

The application is built with **CustomTkinter**, providing a modern alternative to the traditional Tkinter appearance.

The interface focuses on:

- Clean layout
- Simple controls
- Dark theme
- Easy password generation
- Clear strength feedback
- Minimal user interaction

---

## 🧪 Example

A generated password may look similar to:

```text
G7!qP2#vL9@xK4
```

> Never use example passwords from documentation for real accounts.

---

## 📋 Requirements

- Windows 10 / Windows 11
- Python 3.x
- CustomTkinter
- PyInstaller *(only required for building the executable)*

---

## 🗺️ Roadmap

Planned improvements:

- [ ] Add password history
- [ ] Add configurable character sets
- [ ] Add passphrase generation
- [ ] Add entropy calculation
- [ ] Improve password-strength analysis
- [ ] Add application settings
- [ ] Add keyboard shortcuts
- [ ] Improve accessibility
- [ ] Add automated tests
- [ ] Add GitHub Actions CI
- [ ] Publish official Windows releases
- [ ] Add release versioning and changelog

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

### Getting started

1. Fork the repository
2. Clone your fork
3. Create a feature branch

```bash
git checkout -b feature/your-feature
```

4. Make your changes
5. Test the application
6. Commit your changes

```bash
git add .
git commit -m "feat: add your feature"
```

7. Push your branch

```bash
git push origin feature/your-feature
```

8. Open a Pull Request

---

## 🐛 Reporting Issues

If you find a bug or have a feature request, please open an issue.

When reporting a bug, include:

- Windows version
- Python version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots or error messages when relevant

---

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

### DevYash

Built as a Python desktop application with a focus on security, usability, and clean software development practices.

<p align="left">

[![GitHub](https://img.shields.io/badge/GitHub-DevYash--001-181717?style=for-the-badge&logo=github)](https://github.com/DevYash-001)

</p>

---

## ⭐ Support

If you find this project useful:

⭐ **Star the repository**

🍴 **Fork the repository**

🐛 **Report bugs**

💡 **Suggest improvements**

🤝 **Contribute**

Your support helps the project grow!

---

<p align="center">
  <strong>🔐 Generate Strong. Stay Secure.</strong>
</p>
