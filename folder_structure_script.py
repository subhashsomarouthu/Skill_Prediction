import os

# Folder paths to create
folders = [
    "data/raw",
    "data/processed",
    "models",
    "scripts",
    "src/components",
    "src/notebook",
    "src/pipeline",
    "templates",
    "artifacts"
]

# Files to initialize
files = [
    
    "requirements.txt",
    "setup.py",
    "app.py",

    "scripts/scrape_jobs.py",
    "src/__init__.py",
    "src/utils.py",
    "src/logger.py",
    "src/exception.py",
    "templates/index.html",
    "templates/home.html",
    
]

def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"📁 Created folder: {folder}")

    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write("")  # Empty placeholder
            print(f"📄 Created file: {file}")
        else:
            print(f"⚠️ Skipped (already exists): {file}")

if __name__ == "__main__":
    create_structure()
