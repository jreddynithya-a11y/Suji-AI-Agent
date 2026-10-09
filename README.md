# 🤖 Suji AI Agent

## 1. Project Name
**Suji – Personal AI Agent**

## 2. Project Overview
Suji is a personal AI agent developed using Python, Ollama, and the Llama language model. This project explores how locally running AI models can be integrated into Python applications to create an interactive AI assistant.

By using Ollama to run Llama locally, Suji aims to provide an AI experience without requiring a cloud-based AI API.

## 3. Features
- 🤖 AI-powered conversational assistance.
- 🧠 Uses the Llama large language model.
- 🐍 Built using Python.
- 🖥️ Runs AI models locally through Ollama.
- 🔒 Supports local model execution, reducing dependence on external AI services.

## 4. Technologies Used
- **Python:** Core programming language.
- **Ollama:** Runs and manages local large language models.
- **Llama:** Language model used to generate AI responses.

## 5. Installation Instructions

### Prerequisites
- Python installed on your computer.
- Ollama installed.
- Git installed (optional, for cloning the repository).

### Step 1: Install Ollama
Download and install Ollama from its official website:

https://ollama.com/

### Step 2: Download the Llama Model
Open your terminal and run:

```bash
ollama pull llama3.2
```

This downloads the Llama 3.2 model. If your code uses a different model, download that model instead.

### Step 3: Clone the Repository

```bash
git clone https://github.com/jreddynithya-a11y/Suji-AI-Agent.git
```

### Step 4: Navigate to the Project Directory

```bash
cd Suji-AI-Agent
```

### Step 5: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 6: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

### Step 7: Install Dependencies

If the project contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

Otherwise, install the Python packages required by your code.

## 6. How to Run the Project

### Step 1: Start Ollama
Ensure Ollama is installed and running on your computer.

### Step 2: Verify the Model


ollama list


Confirm that the Llama model configured in your code is available.

### Step 3: Run Suji

Run the Python entry-point file for your project.

## 7. Future Improvements
- 💬 Add a more interactive conversational interface.
- 🧠 Implement conversation memory to maintain context across interactions.
- 🎙️ Explore voice input and voice responses.
- 🛠️ Integrate tools to perform useful tasks.
- 🌐 Develop a user-friendly web interface.
- ⚙️ Improve error handling and response performance.

---

**Developed as a hands-on project to explore Python, local language models, and AI agent development.**
