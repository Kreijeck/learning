@echo off
REM Current directory
set dirname=%CD%
REM set name of .ui file, py_File called same
set uiName=main
set py_path=D:\Projects\BoardGameStats\venv_py39

cd %dirname%
d:
@echo on
"%py_path%\Scripts\pyside2-uic.exe" "%dirname%\%uiName%.ui" > "%dirname%\%uiName%.py"
@echo off
cd %dirname%