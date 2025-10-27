# 🏏 IPL API Service

A RESTful **IPL (Indian Premier League) API Service** built using **Python** and **Flask**.  
This project allows users to access detailed IPL data through **GET methods**, including information on **matches**, **teams**, **players**, and **deliveries (ball-by-ball actions)**.

---

## 📘 Overview

This API service provides structured access to IPL data for analysis, dashboards, and visualization.  
It utilizes comprehensive datasets covering all major aspects of IPL — from match outcomes to granular delivery-level insights.

### 📂 Datasets Used

#### 🏆 Matches Dataset
Contains detailed records of every IPL match played, including:
- Season and Match ID  
- Teams, City, and Venue  
- Toss Winner and Decision  
- Match Winner and Player of the Match  
- Date and Umpires  

#### 🎯 Deliveries Dataset
Provides **ball-by-ball details** for in-depth cricket analysis, including:
- Match ID, Over, and Ball  
- Batsman, Bowler, and Non-Striker  
- Runs (Batsman, Extras, Total)  
- Wickets, Dismissal Type, and Fielder Info  

These datasets together enable rich analysis of team performance, player stats, and match outcomes.

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python |
| **Framework** | Flask |
| **API Type** | REST (GET methods) |
| **Data Handling** | Pandas, CSV |
| **Environment** | Localhost |

---

## 🚀 Features

- 📡 **RESTful API** using Flask  
- 📊 Access IPL data (matches, deliveries, players, teams, etc.)  
- ⚡ Fast and lightweight server  
- 🔍 Filter and explore detailed cricket statistics  
- 🧠 Easy to integrate with ML models or dashboards  

---

## 🧩 Example API Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/` | GET | Home route — basic API info |
| `/matches` | GET | Fetch details of all IPL matches |
| `/deliveries` | GET | Fetch all ball-by-ball details |
| `/teams` | GET | Retrieve all IPL teams and stats |
| `/players` | GET | Retrieve all players and performance summary |
| `/matches/<season>` | GET | Get all matches for a specific IPL season |
| `/team/<team_name>` | GET | Get details or performance of a specific team |

---

## 🧰 Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ipl-api-service.git
cd ipl-api-service
