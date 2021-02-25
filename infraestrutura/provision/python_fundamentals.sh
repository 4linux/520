#!/bin/bash

# atualiza lista de pacotes
apt-get update 

# instala dependências do curso 
apt-get install -y passwd wget vim fluxbox git xinit x11-xserver-utils firefox-esr thunar geany geany-plugin-treebrowser unzip vagrant sakura idesk 

#criação dos usuários developer e suporte e configuração do gerenciador de janelas

for U in developer suporte; do
	useradd -d /home/$U -m -s /bin/bash $U
	echo -e "$U\n$U" | passwd $U
	rm -rf /home/$U/.fluxbox
	rm -rf /home/$U/.idesk*
	cp -a /home/vagrant/files/user/.fluxbox /home/$U
	cp -a /home/vagrant/files/user/.idesk* /home/$U
	cp -a /home/vagrant/files/user/.mozilla /home/$U
	cp -a /home/vagrant/files/user/.config /home/$U
	mkdir -p /home/$U/{Documentos,Downloads}
	chown $U:$U /home/$U/{Documentos,Downloads}
	echo "exec fluxbox" > /home/$U/.xinitrc
	echo 'if [ -z "$DISPLAY" ] && [ $(tty) == /dev/tty1 ]; then
			     startx
	    fi' >> /home/$U/.bash_profile
	chown -R $U:$U /home/$U/{.config,.mozilla,.fluxbox,.idesk*,.bash*}
done


# atualiza parâmetro de login do systemd
echo "NAutoVTs=1" >> /etc/systemd/logind.conf 

# adiciona serviço de auto-login no systemd
mkdir -p /etc/systemd/system/getty@tty1.service.d
cat > /etc/systemd/system/getty@tty1.service.d/override.conf <<'EOF'
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin developer --noclear %I 38400 linux
EOF

# atualiza e habilita o novo serviço para inicialização
systemctl daemon-reload
systemctl enable getty@tty1.service

# modifica permissões para os scripts de instalação de editores de texto
cp /home/vagrant/files/bin/install-* /usr/local/bin/
chmod +x /usr/local/bin/install-*
cp /home/vagrant/files/bin/find-resolution.sh /usr/local/bin/
chmod +x /usr/local/bin/find-resolution.sh

# adiciona usuário developer no sudoers
sed -i 's,%sudo.*,%sudo ALL=(ALL:ALL) NOPASSWD:ALL,' /etc/sudoers
gpasswd -a developer sudo

# desliga a máquina
poweroff
