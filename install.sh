

command -v xbps-install
if [! $? -eq 0]; then
	echo "ERR: xbps-install not found, are you on void linux?"		
	exit
fi


ping -c 3 8.8.8.8
if [! $? -eq 0]; then
	echo "CONNECT TO THE INTERWEB";
	exit


echo "adding .bashrc"
rm $HOME/.config && mv $HOME/conf .config;
rm ~/.bashrc && mv $HOME/.config/.bashrc $HOME
. $HOME/.bashrc

sysup

echo repository=https://raw.githubusercontent.com/Makrennel/hyprland-void/repository-x86_64-glibc | sudo echo /etc/xbps.d/hyprland-void.conf

sysad

echo "adding packages:"

sysad hyprland \
	xdg-desktop-portal-hyprland \
	neovim \
	kitty \
	Thunar \
	Waybar \
	sddm \
	dbus \
	elogind \
	seatd \
	hyprpaper \
	hyprlock \
	curl \
	wget \
	clang \
	clang-analyzer \
	clang-tools-extra \
	fastfetch \
	networkmanager \
	iwd

echo "setting up services"

sudo ln -s /etc/sv/sddm /var/service
sudo ln -s /etc/sv/elogind /var/service
sudo ln -s /etc/sv/seatd /var/service
sudo ln -s /etc/sv/NetworkManager /var/service
sudo ln -s /etc/sv/iwd /var/service
sudo ln -s /etc/sv/dbus /var/service

echo "donezo time to reboot"
reboot


