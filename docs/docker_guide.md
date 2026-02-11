# 🐳 Docker Guide — GenAI Foundry

A step-by-step guide to running the GenAI Foundry demos using Docker. No prior Docker experience needed.

---

## Part 1: What is Docker?

Think of Docker as a **shipping container for software**. Just like a shipping container holds everything needed for delivery, a Docker container holds everything your app needs to run — Python, libraries, code — all in one neat package.

**Why use it?**

| Benefit | What it means |
|---------|---------------|
| **Consistent** | Works the same on every computer |
| **No conflicts** | Won't interfere with your other Python projects |
| **Easy cleanup** | Remove everything with one command |
| **One command** | Build once, run anywhere |

---

## Part 2: Install Docker Desktop

Download Docker Desktop for your operating system:

| Operating System | Download Link |
|-----------------|---------------|
| **Windows** | [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/) |
| **Mac (Intel)** | [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/) |
| **Mac (Apple Silicon)** | [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/) |
| **Linux** | [Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux/) |

After installation:
1. **Open Docker Desktop**
2. **Wait** for the whale icon to stop animating (this means it's ready)
3. **Verify** by opening a terminal and typing: `docker --version`

---

## Part 3: Running GenAI Foundry

### Step 1: Get the Code

**Option A: Clone with Git** (recommended)
```bash
git clone https://github.com/dlwhyte/GenAI_foundry.git
cd GenAI_foundry
```

**Option B: Download ZIP**
1. Go to https://github.com/dlwhyte/GenAI_foundry
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Extract the ZIP file
5. Open a terminal and navigate to the folder

### Step 2: Build the Docker Image

```bash
docker build -t genai-foundry .
```

- `-t genai-foundry` gives the image a name
- `.` tells Docker to look in the current folder for the Dockerfile

**This will take 3-5 minutes** the first time (downloading Python, ML libraries, etc.).

Wait until you see:
```
Successfully built xxxxxxxxxx
Successfully tagged genai-foundry:latest
```

### Step 3: Run the Container

**Without an API key** (RAG Explorer works without one):
```bash
docker run -p 8501:8501 genai-foundry
```

**With an OpenAI API key** (needed for Ontology demo + RAG Chat):
```bash
docker run -p 8501:8501 -e OPENAI_API_KEY=sk-your-key-here genai-foundry
```

You'll see:
```
You can now view your Streamlit app in your browser.
URL: http://0.0.0.0:8501
```

### Step 4: Open the App

Open your browser and go to: **http://localhost:8501**

🎉 **You should see the GenAI Foundry home page with all three demos!**

### Step 5: Stop the App

Press `Ctrl+C` in the terminal to stop the container.

---

## Part 4: Common Issues & Solutions

### "Docker command not found"
- **Cause:** Docker isn't installed or terminal was opened before installation
- **Solution:**
  1. Make sure Docker Desktop is installed
  2. Close and reopen your terminal
  3. On Windows, try restarting your computer

### "Cannot connect to Docker daemon"
- **Cause:** Docker Desktop isn't running
- **Solution:**
  1. Open Docker Desktop application
  2. Wait for the whale icon to stop animating
  3. Try the command again

### "Port 8501 is already in use"
- **Cause:** Another app (or another container) is using that port
- **Solution:** Use a different port:
  ```bash
  docker run -p 8502:8501 genai-foundry
  ```
  Then open `http://localhost:8502` instead

### "COPY failed: file not found"
- **Cause:** You're not in the right directory
- **Solution:** Make sure you `cd` into the folder containing the `Dockerfile`:
  ```bash
  cd path/to/GenAI_foundry
  ls  # Should show Dockerfile, Home.py, etc.
  ```

### Build is very slow
- **Cause:** First-time download of Python, ML libraries, and models (~1GB+)
- **Solution:** This is normal for the first build. Subsequent builds are much faster due to caching.

### App works but looks different than expected
- **Cause:** Browser cache
- **Solution:** Hard refresh with `Ctrl + Shift + R` (Windows/Linux) or `Cmd + Shift + R` (Mac)

---

## Part 5: Useful Docker Commands Reference

```bash
# See running containers
docker ps

# See all containers (including stopped)
docker ps -a

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>

# See all images
docker images

# Remove an image
docker rmi genai-foundry

# Rebuild without cache (if you need a fresh build)
docker build --no-cache -t genai-foundry .

# Run in background (detached mode)
docker run -d -p 8501:8501 genai-foundry

# View logs of a background container
docker logs <container_id>

# Stop all running containers
docker stop $(docker ps -q)
```

---

## Part 6: Cleanup

If you want to free up disk space later:

```bash
# Remove the container (after stopping it)
docker rm $(docker ps -a -q --filter ancestor=genai-foundry)

# Remove the image
docker rmi genai-foundry

# Remove all unused Docker data (careful!)
docker system prune
```

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────┐
│                    DOCKER QUICK START                    │
├─────────────────────────────────────────────────────────┤
│  1. Open terminal                                       │
│  2. cd GenAI_foundry                                    │
│  3. docker build -t genai-foundry .                     │
│  4. docker run -p 8501:8501 genai-foundry               │
│  5. Open http://localhost:8501                           │
│  6. Ctrl+C to stop                                      │
│                                                         │
│  With API key:                                          │
│  docker run -p 8501:8501 -e OPENAI_API_KEY=sk-... \     │
│    genai-foundry                                        │
└─────────────────────────────────────────────────────────┘
```

---

## Need More Help?

- **Docker Documentation:** https://docs.docker.com/get-started/
- **Streamlit Documentation:** https://docs.streamlit.io/
- **Course Discussion Forum:** Post your question with any error messages

---

*MIT Professional Education: Applied Generative AI for Digital Transformation*
