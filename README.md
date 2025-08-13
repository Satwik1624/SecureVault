# 🔐 SecureVault

A modern, secure digital vault system built with Python Flask that allows users to store and retrieve files with military-grade encryption.
<img width="1362" height="640" alt="image" src="https://github.com/user-attachments/assets/255b60fc-4e7b-4af7-b711-112daf931f5d" />


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

<img width="1073" height="645" alt="image" src="https://github.com/user-attachments/assets/4f8f6ad7-09a6-4553-879a-97fa67787577" />
<img width="1047" height="641" alt="image" src="https://github.com/user-attachments/assets/e43eb86a-6da5-456a-b251-b80170a97562" />



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
<img width="1365" height="642" alt="image" src="https://github.com/user-attachments/assets/435b73fe-666a-427a-bd9f-af04b93607a9" />


### Dark Mode
- Eye-friendly dark theme with smooth transitions
- Consistent design language across all pages
<img width="1362" height="640" alt="image" src="https://github.com/user-attachments/assets/d3daf404-e09e-4f2f-be3a-109e630b162c" />


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
