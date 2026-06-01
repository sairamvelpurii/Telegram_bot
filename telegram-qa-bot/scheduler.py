import schedule
import time
import json
import subprocess
from datetime import datetime, timedelta

def load_config():
    """Load configuration from config.json"""
    with open('config.json', 'r') as f:
        return json.load(f)

def run_extraction_and_send():
    """Extract from PDFs and send to Telegram"""
    config = load_config()
    
    print(f"\n{'='*60}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running scheduled task...")
    print(f"{'='*60}")
    
    try:
        # Step 1: Extract from PDFs with RANDOM selection
        print("\n1. Extracting RANDOM Q&A from PDFs...")
        result = subprocess.run(['python', 'extract_and_generate.py'], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error during extraction: {result.stderr}")
            return
        
        # Step 2: Send to Telegram
        print("\n2. Sending to Telegram...")
        result = subprocess.run(['python', 'bot.py'], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error sending to Telegram: {result.stderr}")
            return
        
        print(f"✓ Task completed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    except Exception as e:
        print(f"Error: {e}")

def start_scheduler():
    """Start the scheduler with 18-hour intervals"""
    config = load_config()
    interval_hours = config.get('interval_hours', 18)
    
    print(f"Scheduler started!")
    print(f"📅 Will run every {interval_hours} hours automatically")
    print(f"📁 PDF folder: {config.get('pdf_folder', 'pdfs')}")
    print(f"📊 Questions per send: {config.get('num_questions', 5)}")
    print(f"🔄 Each time: NEW random questions will be selected from the PDF")
    print(f"\nPress Ctrl+C to stop the scheduler\n")
    
    # Schedule the task to run every N hours
    schedule.every(interval_hours).hours.do(run_extraction_and_send)
    
    # Run immediately on startup
    print(f"Running immediately on startup...")
    run_extraction_and_send()
    
    # Keep the scheduler running
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("\n\nScheduler stopped.")

if __name__ == "__main__":
    # Install schedule library if not installed
    try:
        import schedule
    except ImportError:
        print("Installing schedule library...")
        subprocess.run(['pip', 'install', 'schedule'], check=True)
        import schedule
    
    start_scheduler()

