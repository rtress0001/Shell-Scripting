#!usr/bin/env bash

read -p "Would you like to play rock paper scissors type yes/no: " answer

if [ "$answer" == "yes" ]; then
    python "C:\Users\ryan\Coding Temple\Shell Scripting\Game.py"
    ./run_python_script.bat
else
    echo "That's too bad, maybe next time"
fi
