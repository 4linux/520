#!/bin/bash

read -p 'Instalar Atom? [s/n]: ' RESPOSTA
RESPOSTA="$(echo "$RESPOSTA" | tr [:upper:] [:lower:])"
if [ "$RESPOSTA" != "s" ]; then
	echo 'Abortando...'
	sleep 1
	exit 0
fi

sudo apt-get update
sudo apt-get install -y wget curl

wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
sudo apt-get update
sudo apt-get install -y atom

sed -i 's,Instalar Atom,Atom,' /home/developer/.fluxbox/menu
sed -i 's,sakura .*-atom.*,atom},' /home/developer/.fluxbox/menu

cat > /home/developer/.idesktop/atom.lnk <<EOF
table Icon
  Caption: Atom
  ToolTip.Caption: Atom Editor
  Icon: /usr/share/atom/atom.png
  Width: 48
  Height: 48
  X: 15
  Y: 342
  Command[0]: atom
end
EOF

sudo pkill idesk
setsid idesk > /dev/null 2>&1 &
echo 'Reiniciando ícones...'
sleep 2
exit 0
