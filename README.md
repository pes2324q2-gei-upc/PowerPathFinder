# PowerPathFinder
The main repo of power path finder, contains docker files and other pipeline configs

## Project Setup
### Repository Setup

**Instalar Github CLI (Saltate esto si ya tienes el tema de credenciales con git solucionado)**
- linux Debian (Ubuntu, etc): `sudo apt install gh`
- macOS: https://github.com/cli/cli/releases/download/v2.44.1/gh_2.44.1_macOS_arm64.zip
- win64: https://github.com/cli/cli/releases/download/v2.44.1/gh_2.44.1_windows_amd64.msi

**Login a Github**
> Copiad solo la primera linea! ;)  
```bash
gh auth login
> Github.com
> HTTPS
> Login with a web browser
# Y seguid las instrucciones
```

**Clonad los repos**
```bash
# Si utilizas gh
gh repo clone pes2324q2-gei-upc/PowerPathFinder
cd PowerPathFinder
gh repo clone pes2324q2-gei-upc/ppf-user-api &
gh repo clone pes2324q2-gei-upc/ppf-route-api &
gh repo clone pes2324q2-gei-upc/ppf_mobile_client &
```
o
```bash
# Si eres un real i tiras de git
git clone https://github.com/pes2324q2-gei-upc/PowerPathFinder.git
cd PowerPathFinder
git clone https://github.com/pes2324q2-gei-upc/ppf-user-api.git &
git clone https://github.com/pes2324q2-gei-upc/ppf-route-api.git &
git clone https://github.com/pes2324q2-gei-upc/ppf_mobile_client.git &
```

## Instalar requisitos
### VSCode
- IDE: https://code.visualstudio.com/#alt-downloads
- Extensiones:
1. Abrid el repo/carpeta PowerPathFinder con VSCode
2. Abrid la seccion de extensiones
3. Copiad y pegad los siguientes nombres de extension en la barra de busqueda:
```
ms-azuretools.vscode-docker Dart-Code.flutter Dart-Code.dart-code GitHub.copilot GitHub.copilot-chat GitHub.vscode-pull-request-github Gruntfuggly.todo-tree ms-python.python ms-python.pylint ms-python.debugpy ms-python.black-formatter ms-python.vscode-pylance ms-python.mypy-type-checker  
```
![image](https://github.com/pes2324q2-gei-upc/PowerPathFinder/assets/75203757/7e479d8b-4d1c-47fb-9e85-fb2b351a2628)

4. Instalad todas las que aparezcan

_OPCIONAL PERO RECOMENDADO_
> Cuando tienes 30 extensiones como yo, si todas tus extensiones estan activadas de forma global estas se cargaran cada vez que abras VScode, sea el workspace(=carpeta) que sea. Para evitar eso... 

5. Desactivad la extension de forma global  
![image](https://github.com/pes2324q2-gei-upc/PowerPathFinder/assets/75203757/da128750-3024-4fd7-98fc-df587e904b3a)

7. Activadla solo en el workspace  
![image](https://github.com/pes2324q2-gei-upc/PowerPathFinder/assets/75203757/e3bb372f-bdc1-475d-bce9-0f8040fc6494)

---

### Docker
**Los de macOS y Windows os toca apechugar con Docker Desktop**
- **macOS** https://docs.docker.com/desktop/install/mac-install/
- **Windows** https://docs.docker.com/desktop/install/windows-install/
 - Fijaos bien en los System requirements

**A mis niños de Linux os mal crio, copiad i pegad esto**
```bash
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt remove $pkg; done
sleep 1
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
- Verificad si todo a ido bien con  
```bash
sudo docker run hello-world
```

---

### Python
##seguid las instru :)
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt install python3 -y && sudo apt install python3-pip -y 
pip3 install django djangorestframework pytest drf-yasg pep8 

# Y seguid las instrucciones
```

---

### Flutter + Dart (+Android Studio)  
**Solo Linux Debian**   
```bash
wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.19.2-stable.tar.xz -O flutter.tar.xz &
wget https://redirector.gvt1.com/edgedl/android/studio/ide-zips/2023.2.1.23/android-studio-2023.2.1.23-linux.tar.gz -O android-studio.tar.gz &
wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O cmd-tools.zip &
sleep 1
tail -q -F -s 5 -n 1 wget-log wget-log.1 wget-log.2
wait
```

- Cuando acaben las descargas seguid con:
```bash
rm wget-log
rm wget-log.1
rm wget-log.2

cd /usr/local
sudo tar vxf ~/Downloads/flutter.tar.xz
echo 'export PATH="$PATH:/usr/local/flutter/bin"' >> $HOME/.bashrc

sudo tar vxf ~/Downloads/android-studio.tar.gz
sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386 openjdk-19-jre-headless
/usr/local/android-studio/bin/studio.sh

cd ~/Android/Sdk
unzip ~/Downloads/cmd-tools.zip
cd cmdline-tools
mkdir latest
mv bin  lib  NOTICE.txt  source.properties ./latest
./latest/bin/sdkmanager --install "cmdline-tools;latest"
rm -r latest && mv latest-2/ latest
```
![image](https://github.com/pes2324q2-gei-upc/PowerPathFinder/assets/75203757/1f16b73c-900b-42b5-a3be-1f8f1518be93)

**Los demas mortales**  
_Flutter_  
- MAC: https://docs.flutter.dev/get-started/install/macos
- WIN: https://docs.flutter.dev/get-started/install/windows

_Android Studio_  
- Download: https://developer.android.com/studio
- Install: https://developer.android.com/studio/intro

