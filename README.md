[README.md](https://github.com/user-attachments/files/25289207/README.md)
# Password Security Checker

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.51.0-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Requests](https://img.shields.io/badge/Requests-2.32.3-2A6DB0)](https://pypi.org/project/requests/)

Streamlit app for password strength scoring and breach lookup using Have I Been Pwned (Pwned Passwords API).

## Live Demo
- Streamlit Cloud: `ADD_YOUR_DEPLOY_URL_HERE`

## Features
- Strength checks for:
  - uppercase letters
  - lowercase letters
  - digits
  - special characters
  - length
- Score from 0 to 100
- Visual feedback (messages + progress bar)
- Breach check with HIBP Pwned Passwords API (k-anonymity flow)

## Screenshot
Add a screenshot after deployment:

```md
![App Screenshot](docs/screenshot.png)
```

## Project Structure
- App entrypoint: `slike/pass_checker.py`
- Dependencies: `requirements.txt`

## Run Locally
Requirements: Python 3.10+

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the app:
```bash
streamlit run slike/pass_checker.py
```

3. Open the local URL shown by Streamlit (usually `http://localhost:8501`).

## Deploy to Streamlit Community Cloud
1. Push this repo to GitHub.
2. Open `https://share.streamlit.io`.
3. Click `New app`.
4. Select repo and branch.
5. Set **Main file path** to:
   - `slike/pass_checker.py`
6. Click `Deploy`.

## Tech Stack
- Python
- Streamlit
- requests
- hashlib

## Security Note
The app sends only the first 5 characters of the SHA-1 hash prefix to HIBP (k-anonymity model), not the raw password.

## Roadmap
- Improve UI text and encoding cleanup
- Add unit tests for scoring logic
- Add copy-safe password tips
- Add CI check for lint and basic run

## Author
- Filip (20% Digital)
- 
