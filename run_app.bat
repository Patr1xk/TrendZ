@echo off
echo ========================================
echo    TrendSpotter - Beauty Trend Analysis
echo ========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting TrendSpotter...
echo.
echo The dashboard will open in your browser at:
echo http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.
python -m streamlit run app.py
pause 