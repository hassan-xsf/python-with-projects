import os
from pathlib import Path

def load_data():
    try:
        current_dir = Path(__file__).parent
        data_path = current_dir / "data" / "smiu-data.md"
        with open(data_path, "r", encoding="utf-8") as file:
            text_content = file.read()
            
        return text_content
    
    except FileNotFoundError:
        print("Error: Data file not found")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    text = load_data()
    if text:
        print(text.strip()[:100])
        print("Data loaded successfully")