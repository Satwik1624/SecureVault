# 🔐 SecureVault

A modern, secure digital vault system built with Python Flask that allows users to store and retrieve files with military-grade encryption.

## ✨ Features

- **🎨 Modern UI**: Beautiful, minimalistic interface with Inter font
- **🌙 Dark Mode**: Toggle between light and dark themes with persistent settings
- **📁 File Upload**: Support for all file types (documents, images, videos, etc.)
- **📝 Text Storage**: Create and store text content directly
- **🔒 Military-Grade Security**: 
  - PIN-based authentication with SHA-256 hashing
  - Fernet symmetric encryption for all files
  - Individual user directories for complete data isolation
- **📱 Responsive Design**: Works perfectly on desktop and mobile
- **☁️ Easy Deployment**: Ready-to-deploy with multiple hosting options

## 🚀 Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python web_locker.py
```
Visit: http://localhost:5000

### 🌐 Deploy to Cloud

#### Heroku
```bash
heroku create your-securevault-app
git push heroku main
heroku open
```

#### Railway
1. Connect your GitHub repo at https://railway.app
2. Deploy automatically

#### Render
1. Connect repo at https://render.com
2. Build: `pip install -r requirements.txt`
3. Start: `python app.py`

## 🎯 Usage

1. **Register**: Create your secure account with username and PIN
2. **Login**: Access your encrypted vault
3. **Upload Files**: Drag & drop any file type or create text content
4. **Manage Files**: View, download, or delete your encrypted files
5. **Dark Mode**: Toggle theme with the 🌙/☀️ button

## 🔧 Tech Stack

- **Backend**: Python Flask
- **Encryption**: Cryptography (Fernet)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Inter (Google Fonts)
- **Deployment**: Gunicorn, Heroku/Railway/Render ready

## 🛡️ Security Features

- **PIN Hashing**: SHA-256 with salt
- **File Encryption**: AES 128-bit via Fernet
- **Session Management**: Secure Flask sessions
- **Data Isolation**: User-specific encrypted directories
- **No Plain Text**: All sensitive data encrypted at rest

## 📱 Screenshots

### Light Mode
- Clean, modern interface with gradient backgrounds
- Intuitive file management with card-based layout

### Dark Mode
- Eye-friendly dark theme with smooth transitions
- Consistent design language across all pages

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

---

**SecureVault** - Your files, encrypted and secure. 🔐