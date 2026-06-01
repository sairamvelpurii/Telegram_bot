# 🤖 Telegram QA Bot: Automated Learning Delivered Daily

## 📱 What I Built

I created an **intelligent Telegram bot** that automatically extracts questions and answers from PDFs and sends random curated sets directly to Telegram **every 18 hours** — completely automated.

---

## 🎯 The Problem

📚 Study materials scattered across PDFs  
⏰ Manual distribution of learning content  
🔄 Repetitive content gets boring  
😴 No consistent learning schedule  

**Solution:** Automate it with a smart bot!

---

## ⚙️ How It Works

### 🔧 Tech Stack
- **Python** - Core logic
- **PyMuPDF** - PDF text extraction
- **Schedule** - Automated task scheduling
- **Telegram Bot API** - Message delivery
- **JSON** - Data management

### 🏗️ Architecture

1. **PDF Processing Module**
   - Scans `pdfs/` folder (supports nested folders)
   - Extracts text from multiple PDFs
   - Parses Q&A in multiple formats:
     - `Q: Question? A: Answer`
     - `Question?` then `Answer:` on next line
     - Numbered format with labels

2. **Smart Selection Engine**
   - Parses all questions from PDFs (150+ questions in my demo)
   - **Randomly selects 10 questions** each cycle
   - No repeats in same cycle
   - Ensures fresh content every 18 hours

3. **Automated Scheduler**
   - Runs **every 18 hours automatically**
   - Extracts new random questions
   - Sends via Telegram Bot API
   - Completely hands-free operation

4. **Manual Override**
   - Run `python bot.py` anytime for instant send
   - Run `python extract_and_generate.py` for new questions
   - Full control when needed

---

## 📂 Project Structure

```
telegram-qa-bot/
├── bot.py                      # Sends questions to Telegram
├── extract_and_generate.py     # Extracts PDFs & selects random Q&A
├── scheduler.py                # Runs extraction & sending every 18hrs
├── config.json                 # Settings (10 questions, 18hr interval)
├── questions.json              # Current set of questions
├── chat_id.py                  # Auto-detects Telegram chat ID
├── requirements.txt            # Dependencies
├── pdfs/                        # Place PDF files here
│   ├── sql_questions.pdf      # PDF 1
│   └── programming_qa.pdf     # PDF 2
└── SETUP_GUIDE.md             # Setup instructions
```

---

## 🚀 Key Features

✅ **Multi-PDF Support** - Combine questions from 2+ PDFs  
✅ **Random Selection** - Different questions each cycle (no boredom)  
✅ **Auto-Scheduling** - 18-hour intervals, completely hands-free  
✅ **Smart Parsing** - Multiple Q&A formats supported  
✅ **Nested Folders** - Organize PDFs by topic/date  
✅ **Configurable** - Change question count & interval anytime  
✅ **Error Handling** - Robust PDF reading & parsing  
✅ **Manual Control** - Send instantly when you want  

---

## 💡 How to Use

### Setup (One-time)
```bash
# Install dependencies
pip install requests PyMuPDF schedule

# Get your Telegram chat ID
python chat_id.py

# Update config.json if needed
```

### Run It

**Manual Mode** (send whenever you want):
```bash
python extract_and_generate.py  # Get 10 random questions from PDFs
python bot.py                    # Send to Telegram
```

**Automatic Mode** (18-hour intervals):
```bash
python scheduler.py  # Runs forever, sending every 18 hours
```

---

## 📊 Real Example Output

**First Cycle:**
1. Unique Constraint vs. Primary Key
2. WHERE vs. HAVING
3. CAP Theorem
4. Types of Anomalies
5. View vs. Materialized View
6. Denormalization
7. SQL Injection
8. Indexing Strategies
9. ACID Properties
10. Normalization Forms

**Next Cycle (18 hours later):**
✨ Different 10 random questions ✨

---

## 🔑 Technical Highlights

- **Recursive PDF Discovery** - `os.walk()` finds PDFs in nested folders
- **Smart Parsing** - Regex patterns handle multiple Q&A formats
- **Random Sampling** - `random.sample()` ensures no duplicates in same batch
- **Process Automation** - `subprocess` runs extraction & sending seamlessly
- **Configuration-Driven** - Single JSON file controls all parameters

---

## 💼 Use Cases

📖 **Daily Learning** - Automated quiz delivery for exam prep  
🎓 **Corporate Training** - Distribute training content to employees  
📚 **Language Learning** - Send vocabulary & grammar questions  
💻 **Technical Certification** - Daily practice questions  
🏥 **Medical Education** - Flashcard distribution  

---

## 🎯 Future Enhancements

🔄 Support for images & diagrams in PDFs  
📊 Analytics dashboard (tracking engagement)  
🌍 Multi-language support  
🔔 WhatsApp, Discord, Slack integration  
💾 Database to track sent questions  
🧠 AI-powered difficulty levels  

---

## 🔗 Get Started

1. Clone/download the project
2. Add your PDFs to `pdfs/` folder
3. Run `python scheduler.py`
4. Let it run 24/7 for automated learning!

---

## 📌 Key Takeaway

**Automation isn't just about saving time — it's about creating consistent, scalable systems that work while you sleep.**

This project demonstrates how simple Python scripts, APIs, and automation can transform manual workflows into intelligent systems.

---

*Built with Python 🐍 | Powered by Telegram 🤖*

#Python #Automation #Telegram #Bot #Learning #ProductivityHack #CodingProject #DevTools
