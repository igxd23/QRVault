# QRVault

A lightweight web-based QR code scanner built with **Flask**. Scan QR codes directly from your browser and automatically save the scanned data with a timestamp to a CSV file.

## Features

- 📷 Browser-based QR code scanning
- ⚡ Flask backend
- 💾 Automatically saves scanned QR data
- 🕒 Records the date and time of every scan
- 📄 Stores scan history in `scans.csv`
- 🎨 Custom frontend styling

## Tech Stack

- **Python**
- **Flask**
- **HTML / CSS / JavaScript**
- **CSV** for scan storage

## Project Structure

```text
QRVault/
│
├── app.py
├── requirements.txt
├── scans.csv
├── cert.pem
├── key.pem
├── style.css
│
└── templates/
    └── index.html
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/igxd23/test.git
cd test
```

### 2. Create a virtual environment

It is recommended to use a virtual environment so Python packages don't turn your system into a dependency crime scene.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

The Flask server will start locally.

Open the address shown in the terminal in your browser, for example:

```text
http://127.0.0.1:5000
```

## How It Works

1. Open the web application.
2. Allow the browser to access your camera.
3. Point the camera at a QR code.
4. The QR code is decoded in the browser.
5. The decoded data is sent to the Flask backend.
6. Flask stores the data and timestamp in `scans.csv`.

## API

### `POST /save-scan`

Saves a scanned QR code.

#### Request

```json
{
  "qr_data": "https://example.com"
}
```

#### Response

```json
{
  "status": "saved",
  "data": "https://example.com"
}
```

## Scan Storage

Scans are stored in:

```text
scans.csv
```

The CSV contains:

| Column | Description |
|---|---|
| `timestamp` | Date and time of the scan |
| `qr_data` | Data contained in the QR code |

Example:

```csv
timestamp,qr_data
2026-09-10T17:30:12,https://example.com
```

## Requirements

The project uses Flask and its related dependencies listed in `requirements.txt`.

## Security Note

Do **not** expose private keys or certificates in a public repository.

If `key.pem` contains a real private key, revoke or replace it and remove the sensitive key from the repository history before using this project publicly.

For production deployment, also use proper authentication, secure storage, HTTPS configuration, and input validation.

## Future Improvements

- Add a scan history dashboard
- Add search and filtering
- Export scans to CSV
- Add SQLite/PostgreSQL database support
- Add user authentication
- Add duplicate-scan detection
- Improve mobile responsiveness
- Deploy using Gunicorn or another production WSGI server

## License

This project is currently provided for educational and personal use.
