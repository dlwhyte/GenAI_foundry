# 🐳 Getting Started with Docker

A beginner's guide to using Docker for running course demos.

---

## What is Docker?

Docker is a tool that packages applications into **containers** — self-contained units that include everything needed to run the app. 

Think of it like a shipping container: everything is pre-packed, and it works the same way on any ship (computer).

### Why use Docker for this course?

| Without Docker | With Docker |
|----------------|-------------|
| Install Python | Just install Docker |
| Install 10+ packages | Run one command |
| Fix version conflicts | Everything pre-configured |
| "It works on my machine" problems | Works the same everywhere |

---

## Step 1: Install Docker Desktop

Download and install Docker Desktop for your operating system:

| Operating System | Download Link | Notes |
|-----------------|---------------|-------|
| **Windows 10/11** | [Download](https://docs.docker.com/desktop/install/windows-install/) | Requires WSL 2 (installer will guide you) |
| **Mac (Intel)** | [Download](https://docs.docker.com/desktop/install/mac-install/) | Choose "Mac with Intel chip" |
| **Mac (Apple Silicon)** | [Download](https://docs.docker.com/desktop/install/mac-install/) | Choose "Mac with Apple chip" |
| **Linux** | [Download](https://docs.docker.com/desktop/install/linux-install/) | Ubuntu, Debian, Fedora supported |

### Installation Steps

1. Download the installer for your OS
2. Run the installer
3. Follow the prompts (accept defaults)
4. **Restart your computer** when asked
5. Open Docker Desktop
6. Wait for it to start (you'll see "Docker Desktop is running")

### How to Know It's Working

Open Terminal (Mac/Linux) or Command Prompt (Windows) and type:

```bash
docker --version
```

You should see something like:
```
Docker version 24.0.7, build afdd53b
```

---

## Step 2: Understand the Basic Commands

You only need **three commands** for this course:

### Build an Image
```bash
docker build -t my-app-name .
```
- Creates a container image from a Dockerfile
- `-t my-app-name` gives it a name
- `.` means "look in the current folder"
- **Run once** (unless files change)

### Run a Container
```bash
docker run -p 8501:8501 my-app-name
```
- Starts the application
- `-p 8501:8501` connects port 8501 on your computer to the container
- Run this **every time** you want to use the app

### Stop a Container
Press `Ctrl+C` in the terminal, or:
```bash
docker stop $(docker ps -q)
```

---

## Step 3: Run the Course Demos

### Navigate to the Demo Folder
```bash
cd GenAI_foundry/docker-demo
```

### Build the Container (First Time Only)
```bash
docker build -t mit-genai-demos .
```

This takes 2-3 minutes. You'll see lots of output — that's normal.

**What's happening:**
1. Docker downloads a base Python image
2. Installs all required packages
3. Copies the application files
4. Creates a ready-to-run image

### Run the Demos
```bash
docker run -p 8501:8501 mit-genai-demos
```

You'll see:
```
You can now view your Streamlit app in your browser.
URL: http://0.0.0.0:8501
```

### Open in Browser
Go to: **http://localhost:8501**

### Stop When Done
Press `Ctrl+C` in the terminal.

---

## Running Again Later

You only build once. After that:

```bash
cd GenAI_foundry/docker-demo
docker run -p 8501:8501 mit-genai-demos
```

---

## Visual Guide: What Happens When You Run Docker

```
┌─────────────────────────────────────────────────────────────┐
│  YOUR COMPUTER                                              │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐  │
│   │  DOCKER CONTAINER                                    │  │
│   │                                                      │  │
│   │   Python 3.11                                        │  │
│   │   + Streamlit                                        │  │
│   │   + OpenAI library                                   │  │
│   │   + All other packages                               │  │
│   │   + Demo application code                            │  │
│   │                                                      │  │
│   │   Running on port 8501 ─────────────────────────┐   │  │
│   │                                                  │   │  │
│   └──────────────────────────────────────────────────│───┘  │
│                                                      │      │
│   Your browser ◄─────────────────────────────────────┘      │
│   http://localhost:8501                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Common Issues & Solutions

### "Docker command not found"

**Problem:** Docker isn't installed or Terminal can't find it.

**Solution:**
- Make sure Docker Desktop is installed
- Restart your terminal/command prompt
- On Windows, restart your computer

---

### "Cannot connect to Docker daemon"

**Problem:** Docker Desktop isn't running.

**Solution:**
1. Look for the whale icon in your system tray (Windows) or menu bar (Mac)
2. If not there, open Docker Desktop from your applications
3. Wait for it to fully start (whale icon stops animating)

---

### "Port 8501 is already in use"

**Problem:** Something else is using that port.

**Solutions:**

Option A — Find and stop the other container:
```bash
docker ps
docker stop <container_id>
```

Option B — Use a different port:
```bash
docker run -p 8502:8501 mit-genai-demos
```
Then go to `http://localhost:8502`

---

### Build fails with "no space left on device"

**Problem:** Docker's storage is full.

**Solution:**
```bash
docker system prune -a
```
This removes unused images and containers. Then rebuild.

---

### Build fails with memory error

**Problem:** Docker needs more RAM.

**Solution:**
1. Open Docker Desktop
2. Go to **Settings** (gear icon)
3. Select **Resources**
4. Increase **Memory** to at least 4 GB
5. Click **Apply & Restart**

---

### "Image not found" when running

**Problem:** You haven't built the image yet, or used a different name.

**Solution:**
Make sure you're in the right folder and build first:
```bash
cd GenAI_foundry/docker-demo
docker build -t mit-genai-demos .
docker run -p 8501:8501 mit-genai-demos
```

---

### App runs but shows errors in browser

**Solutions:**
- Refresh the page
- Check if you entered your API key (for Ontology demo)
- Check the terminal for error messages

---

## Useful Docker Commands

| Command | What it does |
|---------|--------------|
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (including stopped) |
| `docker images` | List all images |
| `docker stop $(docker ps -q)` | Stop all running containers |
| `docker rm $(docker ps -aq)` | Remove all containers |
| `docker rmi mit-genai-demos` | Remove a specific image |
| `docker system prune -a` | Clean up unused data |
| `docker build --no-cache -t name .` | Rebuild from scratch |

---

## Glossary

| Term | Meaning |
|------|---------|
| **Image** | A template/blueprint for containers (like a recipe) |
| **Container** | A running instance of an image (like the cooked meal) |
| **Dockerfile** | Instructions for building an image |
| **Port** | A network endpoint (like a door number) |
| **Volume** | Shared storage between container and your computer |
| **Docker Desktop** | The application that runs Docker on your computer |

---

## Want to Learn More?

- [Docker's Official Getting Started Guide](https://docs.docker.com/get-started/)
- [Docker in 100 Seconds (Video)](https://www.youtube.com/watch?v=Gjnup-PuquQ)
- [Docker Tutorial for Beginners](https://www.youtube.com/watch?v=fqMOX6JJhGo)

---

*MIT Professional Education — Applied Generative AI for Digital Transformation*
