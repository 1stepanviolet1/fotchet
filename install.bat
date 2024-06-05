@echo off

pip3 install -r requirements.txt

cd "./parser" && "./setup" && cd ".."
