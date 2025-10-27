# 🏏 IPL API Service

A RESTful **IPL (Indian Premier League) API Service** built using **Python** and **Flask**.  
This project allows users to fetch detailed IPL data via **GET methods**, including stats on **matches, teams, players, batting, and bowling records**.  

The API uses comprehensive IPL datasets that include information on **matches**, **players**, **teams**, and **seasons** — covering everything from **ball-by-ball actions** to **overall team performance**.

---

## 📘 Overview

The **IPL API Service** provides structured and programmatic access to IPL data for analytical or visualization purposes.  
Users can retrieve match records, compare team performance, and analyze player stats through simple endpoints.

---

## 📂 Datasets Used

### 🏆 Matches Dataset
Contains detailed records of every IPL match played:
- Season  
- City, Venue, Date  
- Teams  
- Toss winner & decision  
- Match winner  
- Player of the match  

### 🎯 Deliveries Dataset
Provides ball-by-ball information for granular analysis:
- Match ID, Inning, Over, Ball  
- Batsman, Bowler, and Non-Striker  
- Runs (batsman, extras, total)  
- Wicket details  

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python |
| **Framework** | Flask |
| **API Type** | RESTful (GET Methods) |
| **Data Handling** | Pandas, CSV |
| **Environment** | Localhost |

---

## 🚀 Features

- RESTful API using **Flask**
- Access to IPL match, team, and player statistics
- Separate routes for **team vs team**, **batting**, and **bowling** performance
- Data sourced from real IPL datasets
- Lightweight, extensible, and easy to integrate

---

## 🧩 API Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/` | GET | Home route – API status and available endpoints |
| `/teams` | GET | Get a list of all IPL teams |
| `/teamvteam` | GET | Get head-to-head records between two teams |
| `/team-record` | GET | Get detailed records for a specific team |
| `/batting-record` | GET | Get batting statistics for players or teams |
| `/bowling-record` | GET | Get bowling performance data |

---

### 🏠 Example Home Route

**Function:**
```python
def home():
    return {
        "message": "Welcome to the IPL API Service!",
        "status": "running",
        "endpoints": ["/teams", "/teamvteam", "/team-record", "/batting-record", "/bowling-record"]
    }
