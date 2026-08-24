# AQI_Tracker_by_Zipcode
Python AQI Tracker using AirNow API with secure API key structure. 

# AQI Tracker — Real-Time Air Quality by ZIP Code

Thank you for checking out this project. This is my first upload to GitHub, created as part of my personal learning journey, scholarship applications, and future career development in software engineering and cybersecurity.

AQI Tracker is a Python application that fetches real-time air quality data (PM2.5) from the AirNow API using a user-provided ZIP code. The project is designed to help communities in Wisconsin and other regions affected by wildfire smoke quickly access accurate AQI information.

---

## 📌 Features

- Fetches real-time AQI (PM2.5) data by ZIP code  
- Uses the official AirNow API  
- Secure API key handling via `.env` file  
- Color-coded hazard levels (green → maroon)  
- Tkinter graphical interface  
- JSON view mode for raw API responses  
- Modular backend design (UI separated from logic)

---

## 🧩 Project Structure

AQI_Tracker_Ver1/
│
├── main.py                 # Tkinter UI and application entry point
├── aqi_fetcher.py          # API calls, AQI processing, data handling
├── hazards.py              # Hazard color logic
├── config_properties.env   # API key (not included in repo)
├── config_example.env      # Template for user setup
└── README.md               # Project documentation



---

## 🔧 Installation

1. Clone the repository:

git clone https://github.com/somejoeguy/AQI_Tracker_by_Zipcode.git


2. Install required packages:

pip install requests python-dotenv


3. Modify your `config_properties.env` file:

You need to go to AirNow's developer portal and create your own account. They will give you an API key that you will put here
in the apiKey = "YOUR_KEY_HERE" replace "YOUR_KEY_HERE" with your personal AirNow API key. 


4. Run the application:

python main.py


---

## 🔐 Configuration

This project uses environment variables to protect your API key.

- `config_example.env` shows the required format  
- `config_properties.env` should **not** be committed to GitHub  
- The application loads the key using `python-dotenv`

---

## 🎨 Hazard Color Guide

| AQI Range | Meaning                          | Color   |
|-----------|----------------------------------|---------|
| 0–50      | Good                             | Green   |
| 51–100    | Moderate                         | Yellow  |
| 101–150   | Unhealthy for Sensitive Groups   | Orange  |
| 151–200   | Unhealthy                        | Red     |
| 201–300   | Very Unhealthy                   | Purple  |
| 301+      | Hazardous                        | Maroon  |

---

## 🎯 Purpose

This project was created to:

- Help Wisconsin residents quickly check AQI during wildfire smoke events  
- Demonstrate secure API usage and modular programming  
- Support my scholarship and grant applications  
- Build a portfolio piece for future employers  
- Strengthen my Python, UI, and backend development skills  

---

## 🚀 Future Plans

- Add ZIP code comparison mode  
- Add multi-city AQI dashboard  
- Add historical AQI tracking  
- Add C-language version for Linux coursework  
- Add packaging and installer options  

---

## 👤 Author

**Joseph**  
Night-shift Amazon employee • Cybersecurity student • Python developer  
Kenosha, Wisconsin  

