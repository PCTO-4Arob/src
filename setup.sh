#!/bin/bash

OS=`uname -s`
REV=`uname -r`
MACH=`uname -m`

GetVersionFromFile() {
	VERSION="$(tr "\n" ' ' < cat "$1" | sed s/.*VERSION.*=\ // )"
}


if [ "${OS}" = "SunOS" ] ; then
	OS=Solaris
	ARCH=$(uname -p)
	OSSTR="${OS} ${REV}(${ARCH} $(uname -v)"
  echo ${OSSTR}
  echo Unsupported
  return

elif [ "${OS}" = "AIX" ] ; then
	OSSTR="${OS} $(oslevel) ($(oslevel -r)"
  echo ${OSSTR}
  echo Unsupported
  return

elif [ "${OS}" = "Linux" ] ; then
	KERNEL=$(uname -r)
	if [ -f /etc/redhat-release ] ; then
		DIST='RedHat'
		PSUEDONAME=$(sed s/.*\(// < /etc/redhat-release | sed s/\)//)
		REV=$(sed s/.*release\ // < /etc/redhat-release | sed s/\ .*//)
        echo Unsupported
	elif [ -f /etc/SuSE-release ] ; then
		DIST=$(tr "\n" ' ' < /etc/SuSE-release | sed s/VERSION.*//)
		REV=$(tr "\n" ' ' < /etc/SuSE-release| sed s/.*=\ //)
        echo Unsupported
	elif [ -f /etc/mandrake-release ] ; then
		DIST='Mandrake'
		PSUEDONAME=$(sed s/.*\(// < /etc/mandrake-release | sed s/\)//)
		REV=$(sed s/.*release\ // < /etc/mandrake-release | sed s/\ .*//)
        echo Unsupported
	elif [ -f /etc/debian_version ] ; then	
		if [ "$(awk -F= '/DISTRIB_ID/ {print $2}' /etc/lsb-release)" = "Ubuntu" ]; then
			DIST="Ubuntu"
            echo Debian-based script:
            echo Refresh repos...
            $(sudo apt update -y > log.txt 2>&1)
            $(sudo apt autoremove -y >> log.txt 2>&1)
            echo Installing Python...
            $(sudo apt install -y python3 >> log.txt 2>&1)
            echo Installing pip...
            $(sudo apt install -y python3-pip >> log.txt 2>&1)
            echo Installing necessary packages:
            $(sudo pip install -r requirements.txt >> log.txt 2>&1)
		else
			DIST="Debian $(cat /etc/debian_version)"
			REV=""
            echo Debian-based script:
            echo Refresh repos...
            $(sudo apt update -y > log.txt 2>&1)
            $(sudo apt autoremove -y >> log.txt 2>&1)
            echo Installing Python...
            $(sudo apt install -y python3 >> log.txt 2>&1)
            echo Installing pip...
            $(sudo apt install -y python3-pip >> log.txt 2>&1)
            echo Installing necessary packages:
            $(sudo pip install -r requirements.txt >> log.txt 2>&1)
		fi
	elif [ -f /etc/arch-release ] ; then
		DIST="Arch"
        echo Arch-based script:
        echo Refresh repos...
        $(sudo pacmam -Syyuu --noconfirm > log.txt 2>&1)
        echo Installing Python...
        $(sudo pacman -S python3 --noconfirm>> log.txt 2>&1)
        echo Installing pip...
        $(sudo pacman -S python-pip --noconfirm>> log.txt 2>&1)
        echo Installing necessary packages:
        $(sudo pip install -r requirements.txt >> log.txt 2>&1)
	fi
	if [ -f /etc/UnitedLinux-release ] ; then
		DIST="${DIST}[$(tr "\n" ' ' < /etc/UnitedLinux-release | sed s/VERSION.*//)]"
	fi
	OSSTR="${OS} ${DIST} ${REV}(${PSUEDONAME} ${KERNEL} ${MACH})"
  #echo Your distro: ${OSSTR}

elif [ "${OS}" == "Darwin" ]; then
  type -p sw_vers &>/dev/null
  [ $? -eq 0 ] && {
    which -s brew
    if [[$? != 0]]; then
      echo "Installing Homebrew"
      $(/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)")
      $(export PATH="/usr/local/opt/python/libexec/bin:$PATH")
      $(export PATH=/usr/local/bin:/usr/local/sbin:$PATH)
    else
      echo "Updating Homebrew"
      $(brew update)

    echo "Install python"
    $(brew install python)

    echo "Install Library"
    $(pip install -r requirements.txt)

    
    #OS=`sw_vers | grep 'ProductName' | cut -f 2`
    #VER=`sw_vers | grep 'ProductVersion' | cut -f 2`
    #BUILD=`sw_vers | grep 'BuildVersion' | cut -f 2`
    #OSSTR="Darwin ${OS} ${VER} ${BUILD}"
  } || {
    OSSTR="MacOSX"
  }
  echo ${OSSTR}
  return

fi

exit 1
