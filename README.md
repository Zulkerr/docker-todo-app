# 📝 Docker To-Do App

Eine moderne To-Do List Anwendung mit **Flask**, **PostgreSQL** und **Docker**. Vollständig containerisiert und produktionsbereit.

## 🚀 Features

- ✅ **Aufgaben hinzufügen** mit Titel und Beschreibung
- ✅ **Aufgaben als erledigt markieren** 
- ✅ **Aufgaben löschen**
- ✅ **Responsive Design** (Desktop & Mobile)
- ✅ **PostgreSQL Datenbank** für persistente Speicherung
- ✅ **Docker Multi-Container Setup**
- ✅ **Automatische Datenbank-Initialisierung**

## 🛠️ Technologie-Stack

- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Datenbank:** PostgreSQL 15
- **Container:** Docker & Docker Compose
- **Styling:** Modern CSS mit Gradients & Animations

## 📦 Installation & Start

### Voraussetzungen
- Docker Desktop installiert
- Git installiert

### Projekt klonen
```bash
git clone https://github.com/Zulkerr/docker-todo-app.git
cd docker-todo-app
```

### Anwendung starten
```bash
# Alle Container starten
docker-compose up -d

# Status überprüfen
docker-compose ps

# Logs anschauen
docker-compose logs -f
```

### Anwendung öffnen
Öffne deinen Browser und gehe zu: **http://localhost:5000**

## 📊 Container-Architektur

```
┌─────────────────┐    ┌─────────────────┐
│   Web App       │    │  PostgreSQL     │
│   (Flask)       │◄──►│  Database       │
│   Port: 5000    │    │   Port: 5432    │
└─────────────────┘    └─────────────────┘
```

## 🗄️ Datenbank-Schema

```sql
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🎯 API Endpoints

| Method | Endpoint | Beschreibung |
|--------|----------|--------------|
| GET | `/` | Alle To-Dos anzeigen |
| POST | `/add` | Neues To-Do hinzufügen |
| GET | `/complete/<id>` | To-Do als erledigt markieren |
| GET | `/delete/<id>` | To-Do löschen |

## 🔧 Entwicklung

### Container stoppen
```bash
docker-compose down
```

### Container neu bauen
```bash
docker-compose build --no-cache
docker-compose up -d
```

### Datenbank zurücksetzen
```bash
docker-compose down -v  # Löscht auch Volumes
docker-compose up -d
```

### In Container einsteigen
```bash
# Web-App Container
docker-compose exec web bash

# PostgreSQL Container
docker-compose exec postgres psql -U postgres -d todoapp
```

## 📁 Projekt-Struktur

```
docker-todo-app/
├── app.py                 # Flask Hauptanwendung
├── requirements.txt       # Python Dependencies
├── Dockerfile            # Container Build Instructions
├── docker-compose.yml    # Multi-Container Configuration
├── init.sql              # Datenbank Initialisierung
├── templates/
│   └── index.html        # Frontend Template
├── static/               # CSS, JS, Images (leer)
└── README.md            # Diese Datei
```

## 🌟 Screenshots

![To-Do App Screenshot](Screenshot.png)

## 🚀 Production Deployment

Diese App ist bereit für Cloud-Deployment auf:
- **AWS ECS/EKS**
- **Google Cloud Run** 
- **Azure Container Instances**
- **DigitalOcean App Platform**

## 🤝 Beitragen

1. Fork das Repository
2. Erstelle einen Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne eine Pull Request

## 📝 Lizenz

Dieses Projekt steht unter der MIT License - siehe [LICENSE](LICENSE) Datei für Details.

## 👨‍💻 Autor

**Zulker Tursun**
- GitHub: (https://github.com/Zulkerr)

## 🙏 Danksagungen

- Docker Community
- Flask Documentation
- PostgreSQL Team

---

**⭐ Wenn dir dieses Projekt gefällt, gib ihm einen Stern auf GitHub!** 
