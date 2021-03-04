!# /bin/bash

echo Detecting OS...

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  local DISTRIB=$(awk -F= '/^NAME/{print $2}' /etc/os-release)
  if [[ ${DISTRIB} = "Ubuntu"* ]]; then
    if uname -a | grep -q '^Linux.*Microsoft'; then
      # ubuntu via WSL Windows Subsystem for Linux
    else
      echo Refresh Repos...
      $(sudo apt update)
      echo Installing Python...
      $(sudo apt install python3)
      echo Installing pip...
      $(sudo apt install python3-pip)

      echo Installing necessary packages...
      $(sudo pip install opencv-python pygame SpeechRecognition numpy)
    fi
  elif [[ ${DISTRIB} = "Debian"* ]]; then
    echo Refresh Repos...
    $(sudo apt update)
    echo Installing Python...
    $(sudo apt install python3)
    echo Installing pip...
    $(sudo apt install python3-pip)

    echo Installing necessary packages...
    $(sudo pip install opencv-python pygame SpeechRecognition numpy)
  fi

  elif [[ ${DISTRIB} = "Manjaro"*]]; then
     echo Refresh Repos...
     $(sudo pacman -Syuu)
     echo Installing Python...
     $(sudo pacman -S python3)

     echo Installing pip...
     $(sudo pacman -S python3-pip)

     echo Installing necessary packages... 
     $(sudo pip install opencv-python pygame SpeechRecognition numpy)
   fi

elif [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS OSX
fi
