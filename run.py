import os
import sys
import subprocess

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Run the Streamlit app
if __name__ == "__main__":
    subprocess.run(["streamlit", "run", "src/main.py"]) 