@echo off
title ArrowPrint Installer v1.0
color 0A

:: ============================================
::  ArrowPrint Installer
::  Esoteric Programming Language
:: ============================================

set INSTALL_DIR=C:\ArrowPrint
set BAT_NAME=arrowprint.bat
set PY_NAME=interpreter.py

echo ========================================
echo     ARROWPRINT INSTALLER v1.0
echo     Esoteric Programming Language
echo ========================================
echo.
echo ArrowPrint is a 2D stack-based esolang
echo inspired by Befunge and Brainfuck.
echo.
echo Installation directory: %INSTALL_DIR%
echo.

:: Check admin rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Administrator privileges required!
    echo Right-click this file and select "Run as administrator"
    echo.
    pause
    exit /b 1
)

:: Step 1: Create directory
echo [1/4] Creating installation directory...
if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
    echo        - Directory created: %INSTALL_DIR%
) else (
    echo        - Directory already exists: %INSTALL_DIR%
)

:: Step 2: Copy files
echo [2/4] Copying files...
if exist "%~dp0%PY_NAME%" (
    copy "%~dp0%PY_NAME%" "%INSTALL_DIR%\" >nul
    echo        - %PY_NAME% copied
) else (
    echo        - [WARNING] %PY_NAME% not found in current folder
)

if exist "%~dp0%BAT_NAME%" (
    copy "%~dp0%BAT_NAME%" "%INSTALL_DIR%\" >nul
    echo        - %BAT_NAME% copied
) else (
    echo        - [WARNING] %BAT_NAME% not found in current folder
)

:: Step 3: Add to PATH
echo [3/4] Adding to system PATH...
setx PATH "%PATH%;%INSTALL_DIR%" /M >nul
echo        - PATH updated successfully

:: Step 4: Create desktop shortcut
echo [4/4] Creating desktop shortcut...
if exist "%USERPROFILE%\Desktop" (
    echo @echo off > "%USERPROFILE%\Desktop\ArrowPrint.bat"
    echo python "%INSTALL_DIR%\interpreter.py" %%* >> "%USERPROFILE%\Desktop\ArrowPrint.bat"
    echo        - Shortcut created on Desktop
)

echo.
echo ========================================
echo     ✅ INSTALLATION COMPLETE!
echo ========================================
echo.
echo Now you can use:
echo   arrowprint            - Interactive mode (REPL)
echo   arrowprint file.arp   - Run a program
echo.
echo [NOTE] Restart your command prompt!
echo.
pause