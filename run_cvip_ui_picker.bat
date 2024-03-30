@echo off

python -c "import cv2" 2> nul
IF %errorlevel% NEQ 0 (
    REM Libraries are not installed, so install them
    pip install opencv-python numpy tensorflow matplotlib scikit-image keras tkinter PIL 
) ELSE (
    REM Libraries are already installed, skip installation
    echo Libraries are already installed.
)

python dehazing.py

