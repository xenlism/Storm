#What's Xenlism?         
xenlism is Computer Graphic And Programming project to make something better.    
xenlism is about minimalism and realism.   

 
#What's is Xenlism Storm?       
Xenlism Storm is icon theme for *nix desktop environment.   
inspired by macOS icon.   
best for gnome and (Maybe) unity,mate,cinamon.   

#Why you donate to me?   
b'cuz you can run Xenlism project keep alive.   
every buck of your donation help me to create newthing.   


#Donate   
Paypal: https://paypal.me/xenatt  
Bitcoin:32hEYx2CVFQxCuimR7ExajqxJfr8jtdYY1    

  
#Arch linux       
sudo nano /etc/pacman.conf    

add this line to file.

[xenlism-arch]     
SigLevel = Optional TrustAll
Server = http://downloads.sourceforge.net/project/xenlism-wildfire/repo/arch

run command
sudo pacman -Syyu
sudo pacman -Sy xenlism-storm-icon-theme

#Arch Linux Aur    
yaourt -S xenlism-storm-icon-theme      


#Ubuntu     
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 2B80AC38
sudo add-apt-repository ppa:xenatt/xenlism
sudo apt-get update
sudo apt-get install xenlism-storm-icon-theme

#Debian     
sudo nano /etc/apt/sources.list      

add this line to file.     
deb http://ppa.launchpad.net/xenatt/xenlism/ubuntu bionic main      
deb-src http://ppa.launchpad.net/xenatt/xenlism/ubuntu bionic main       

Run command
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 2B80AC38
sudo apt-get update
sudo apt-get install xenlism-storm-icon-theme

#Fedora       
sudo dnf config-manager --add-repo https://downloads.sourceforge.net/project/xenlism-wildfire/repo/fedora/xenlism-fedora.repo     
sudo rpm --import https://downloads.sourceforge.net/project/xenlism-wildfire/repo/fedora/ixenatt%40gmail.com.pub     
sudo dnf update    
sudo dnf install xenlism-storm-icon-theme     


#CentOS       
sudo wget https://downloads.sourceforge.net/project/xenlism-wildfire/repo/fedora/xenlism-fedora.repo -O /etc/yum.repos.d/xenlism-fedora.repo    
sudo rpm --import https://downloads.sourceforge.net/project/xenlism-wildfire/repo/fedora/ixenatt%40gmail.com.pub       
sudo yum update     
sudo yum install xenlism-storm-icon-theme    

#openSuse
sudo zypper ar -f -c https://downloads.sourceforge.net/project/xenlism-wildfire/repo/fedora/ xenlism-fedora  
sudo gpg --keyserver keyserver.ubuntu.com --recv-keys AFAC0680DB0F3245A643CA37B5C583782B80AC38
sudo zypper refresh
sudo zypper update
sudo zypper install xenlism-storm-icon-theme

And Other Distro [Click Here](https://xenlism.github.io/wildfire)


#COPYRIGHT                       
[![GNU GENERAL PUBLIC LICENSE](http://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl.txt/)               
**xenlism - wildfire** by [Nattapong Pullkhow](https://plus.google.com/+NattapongPullkhow/) is licensed under a [GNU GENERAL PUBLIC LICENSE - GPL](https://www.gnu.org/licenses/gpl.txt)            


![App](https://raw.githubusercontent.com/xenlism/Storm/master/screenshot/storm_app_cover.png)  
![place](https://raw.githubusercontent.com/xenlism/Storm/master/screenshot/storm_place_cover.png)  
![mime](https://raw.githubusercontent.com/xenlism/Storm/master/screenshot/storm_mime_cover.png)   



