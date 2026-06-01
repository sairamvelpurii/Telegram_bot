# Telegram QA Bot - Setup Guide

## 📁 Where to Upload PDFs

Upload your PDF files to the **`pdfs/`** folder in the project directory. Nested folders are also supported, so you can organize by subject or date:

```
telegram-qa-bot/
  └── pdfs/
      ├── sql.pdf
      ├── folder1/
      │   ├── document1.pdf
      │   └── document2.pdf
      └── folder2/
          └── document3.pdf
```

## ⚙️ How to Configure

Edit `config.json` to customize:

```json
{
    "num_questions": 5,           // Number of Q&A pairs to send
    "schedule_time": "06:00",     // Daily send time (24-hour format)
    "timezone": "Asia/Kolkata",   // Your timezone
    "pdf_folder": "pdfs",         // Folder containing PDFs
    "auto_extract": true          // Auto-extract from PDFs
}
```

### Configuration Options:
- **`num_questions`**: Change this to send more or fewer questions (e.g., 3, 10, 20)
- **`schedule_time`**: Change the time in HH:MM format (e.g., "05:30", "07:00")
- **`timezone`**: Set your timezone for correct scheduling

## 🚀 How to Use

### Option 1: Manual Extraction & Send
Run anytime to extract and send immediately:

```bash
python extract_and_generate.py  # Extract from PDFs
python bot.py                    # Send to Telegram
```

### Option 2: Automatic Daily Sending (Recommended)
Run the scheduler to send automatically every day at the configured time:

```bash
python scheduler.py
```

Keep this running in a terminal. It will:
1. Extract Q&A from all PDFs in the `pdfs/` folder and nested folders
2. Generate `questions.json`
3. Send to Telegram at the scheduled time
4. Repeat daily

## 📄 PDF Format

Your PDFs should contain questions and answers as plain text. The parser works best when Q&A are clearly separated. Supported formats:

**Format 1: Q&A pairs**
```
Q: What are the four pillars of OOPs? A: Encapsulation, Abstraction, Inheritance, and Polymorphism.
Q: Can we override a static method? A: No. Static methods belong to the class, not the instance.
```

**Format 2: Question then Answer (separate lines)**
```
What are the four pillars of OOPs?
Encapsulation, Abstraction, Inheritance, and Polymorphism.

What is the difference between Abstraction and Encapsulation?
Abstraction hides implementation details, while Encapsulation protects object state.
```

**Format 3: Numbered format with Answer:**
```
1. What are the four pillars of OOPs?
Answer: Encapsulation, Abstraction, Inheritance, and Polymorphism.

2. What is the difference between Abstraction and Encapsulation?
Answer: Abstraction hides implementation complexities, while Encapsulation hides internal state.
```

### Best PDF creation tips
- Export from a text editor or word processor as a plain-text-based PDF.
- Avoid scanning images or using fancy page layouts.
- Keep each question and answer close together in the text.
- Use `Q:`/`Answer:` labels if possible.
- Avoid duplicate numbering like `1. 1.` or split answers across too many broken lines.

### If Gemini-generated PDF is not parsing well
1. Open the Gemini output in a text editor.
2. Convert it to one of the supported formats above.
3. Save it as a simple PDF from Word, Google Docs, or another editor.
4. Place the PDF in the `pdfs/` folder.

## ✨ Features

✅ Automatic PDF extraction  
✅ Q&A pair generation  
✅ Daily scheduled sending  
✅ Configurable number of questions  
✅ Adjustable send time  
✅ Support for multiple PDFs  

## 🔧 Advanced

To stop the scheduler: Press `Ctrl+C` in the terminal

To change number of questions: Edit `config.json` and set `num_questions`

To change send time: Edit `config.json` and update `schedule_time`

## 📝 Example Workflow

1. Place your PDFs in the `pdfs/` folder
2. Edit `config.json` with your preferences
3. Run `python scheduler.py`
4. Let it run - messages will be sent daily at the scheduled time!

---

Need help? Check that:
- PDFs are in the `pdfs/` folder
- PDF format is clear (questions and answers separated)
- `config.json` has valid settings
- Telegram bot token is still valid
