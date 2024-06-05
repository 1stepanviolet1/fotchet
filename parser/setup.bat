@echo off

python setup.py build_ext --inplace

if %ERRORLEVEL% == 0 (
    mv *.pyd bin/
)
