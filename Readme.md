# Rentify Recommendor Service  

A **Python-based recommendation engine** for the Rentify platform.  
This service provides personalized **property recommendations for tenants** and **tenant recommendations for landlords**, using data exported from the [Rentify server](https://github.com/kubsamelkamu/rentify_server)..

## ⚙️ Tech Stack  

- **Python** – Core language for the service  
- **Flask** – Lightweight web framework for serving the recommendation API  
- **Pandas & NumPy** – Data processing and analysis  
- **Scikit-learn** – Machine learning utilities for recommendation logic  
- **Joblib** – Model persistence and loading  
- **Render** – Deployment platform for hosting the service 

## ✨ Features

- **Data Ingestion via Cron Jobs**  
  Automatically receives datasets (users, properties, bookings, likes, reviews) exported from the Rentify backend via GitHub Actions.

- **Tenant Recommendations**  
  Suggests properties to tenants based on their interests, activity, and interaction history.

- **Landlord Recommendations**  
  Identifies potential tenants that are most likely to be a good fit for a landlord’s properties.

- **REST API Endpoints**  
  Exposes recommendation results through simple Flask endpoints for the backend to consume.

- **Transactional Email Integration**  
  Rentify Backend can use the recommendations to send personalized emails to tenants and landlords.

- **Modular & Extensible ML Pipeline**  
  Easily extendable using Pandas, NumPy, and scikit-learn for more advanced ML models in the future.

## 📂 Project Structure

```
Rentify_recommendor/
├── app.py                # Flask entry point
├── requirements.txt      # Python dependencies
├── recommender/          # Core recommendation logic
│   ├── tenant.py         # Tenant-property recommendation
│   ├── landlord.py       # Landlord-tenant recommendation 
|_____util                 # Shared helper functions
|     |___data_loader.py   
├── data/                 # Datasets synced from backend
│   ├── users.csv
│   ├── properties.csv
│   ├── bookings.csv
│   ├── likes.csv
│   └── reviews.csv
```

## 📦 Prerequisites

Before running the service, make sure you have:

- Python **3.10+**
- pip package manager
- (Optional) virtual environment tool (`venv` or `virtualenv`)
- Dataset exported from the Rentify backend (CSV files)

---

## 🚀 Environment Setup

1. **Clone the repository**
```bash
git clone https://github.com/kubsamelkamu/Rentify_recommendor.git
cd Rentify_recommendor

```
2. **Create & activate a virtual environment**
```bash
    python -m venv venv
    .\venv\Scripts\Activate
```
3.**Install dependencies**
pip install -r requirement.txt

## 🏃‍♂️ Running the Service Locally

### Development Mode
```bash
python app.py
```
### Production Mode 
```bash
pip install gunicorn
gunicorn app:app --bind 0.0.0.0:5000
```
