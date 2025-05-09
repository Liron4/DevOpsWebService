# 🎵 Playlist Server with YouTube Embedding

A lightweight playlist management server that allows users to save and retrieve song entries using a simple API. Each song is stored with a title and a YouTube link, enabling easy embedding in a frontend (e.g. React).

---

## 🧩 Features

- Create users and manage per-user song lists
- Add songs using title + YouTube link
- Fetch all users or a specific user's playlist
- Delete songs or entire users
- Built-in error handling for duplicates or missing entries

---

## 📦 Tech Stack

- **Backend:** Python (FastAPI)
- **Database:** Redis (local file-based)
- **Frontend-ready:** Returns JSON for direct consumption and YouTube embedding

---

## ⚙️ Deployment (Docker + Docker Compose)

### 🐳 Requirements

- Docker
- Docker Compose

### 🚀 How to Run

```bash
git clone https://github.com/your-username/playlist-server.git
cd playlist-server
docker-compose up --build
```
# Architecture Diagram
![System Architecture](https://i.imgur.com/r5Af02k.png)