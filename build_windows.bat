@echo off
setlocal

where renpy >nul 2>nul
if errorlevel 1 (
    echo Ren'Py command was not found in PATH.
    echo Open this folder from Ren'Py Launcher and use Build Distributions instead.
    exit /b 1
)

renpy . distribute --package pc
