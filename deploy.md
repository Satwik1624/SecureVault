# SecureVault Deployment Guide

## Local Development
```bash
pip install -r requirements.txt
python web_locker.py
```
Visit: http://localhost:5000

## Deploy to Heroku

1. **Install Heroku CLI**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-securevault-app
   ```

4. **Deploy**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

5. **Open App**
   ```bash
   heroku open
   ```

## Deploy to Railway

1. **Connect GitHub**
   - Go to https://railway.app
   - Connect your GitHub repository

2. **Deploy**
   - Railway will automatically detect and deploy your Flask app
   - Set environment variables if needed

## Deploy to Render

1. **Connect Repository**
   - Go to https://render.com
   - Connect your GitHub repository

2. **Configure**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`

## Environment Variables (Optional)
- `SECRET_KEY`: Flask secret key for sessions
- `PORT`: Port number (default: 5000)

## Features
- ✅ Modern, minimalistic UI with Inter font
- ✅ File upload support (all file types)
- ✅ Text content creation
- ✅ Encrypted storage with Fernet
- ✅ User authentication with PIN
- ✅ Responsive design
- ✅ Production-ready deployment files