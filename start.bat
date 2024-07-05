@echo off

REM Activate the virtual environment
call .\venv\Scripts\activate

REM Install Python dependencies
python -m pip install -r requirements.txt

REM Start the Flask backend in a new command prompt window
start cmd /k "python backend/run.py"

REM Navigate to the frontend directory and start the React development server
cd frontend
start cmd /k "npm install & npm run dev"

REM Navigate back to the root directory
cd ..

REM Keep the original command prompt window open
pause
