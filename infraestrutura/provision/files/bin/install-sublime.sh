#!/bin/bash

read -p 'Instalar Sublime? [s/n]: ' RESPOSTA
RESPOSTA="$(echo "$RESPOSTA" | tr [:upper:] [:lower:])"
if [ "$RESPOSTA" != "s" ]; then
	echo 'Abortando...'
	sleep 1
	exit 0
fi

sudo apt-get update
sudo apt-get install -y wget curl apt-transport-https

wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install -y sublime-text

sed -i 's,Instalar Sublime,Sublime,' /home/developer/.fluxbox/menu
sed -i 's,sakura .*-sublime.*,subl},' /home/developer/.fluxbox/menu

cat > /home/developer/.idesktop/sublime.lnk <<EOF
table Icon
  Caption: Sublime
  ToolTip.Caption: Sublime Editor
  Icon: /usr/share/icons/hicolor/128x128/apps/sublime-text.png
  Width: 48
  Height: 48
  X: 15
  Y: 508
  Command[0]: subl
end
EOF

sudo pkill idesk
setsid idesk > /dev/null 2>&1 &
echo 'Reiniando ícones...'
sleep 2
exit 0
