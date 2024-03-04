![image](https://github.com/pes2324q2-gei-upc/PowerPathFinder/assets/75203757/3dd3785e-9c3d-4241-b682-c72127bcab46)# PowerPathFinder
The main repo of power path finder, contains docker files and other pipeline configs

## Project Setup
### Repository Setup

**Instalar Github CLI**
- linux Debian (Ubuntu, etc): `sudo apt install gh`
- macOS: https://github.com/cli/cli/releases/download/v2.44.1/gh_2.44.1_macOS_arm64.zip
- win64: https://github.com/cli/cli/releases/download/v2.44.1/gh_2.44.1_windows_amd64.msi

**Login a Github**
```bash
gh auth login
> Github.com
> HTTPS
> Login with a web browser
# Y seguid las instrucciones
```

**Clonad los repos (seguid los mimos cmds)**
```bash
gh repo clone pes2324q2-gei-upc/PowerPathFinder
cd PowerPathFinder
gh repo clone pes2324q2-gei-upc/ppf-user-api
gh repo clone pes2324q2-gei-upc/ppf-route-api
```

## Instalar requisitos

### VSCode
- IDE: https://code.visualstudio.com/#alt-downloads
- Extensiones:
1. Abrid el repo/carpeta PowerPathFinder con VSCode
2. Abrid la seccion de extensiones
3. Copiad y pegad los siguientes nombres de extension en la barra de busqueda:
```
ms-azuretools.vscode-docker Dart-Code.flutter Dart-Code.dart-code GitHub.copilot GitHub.copilot-chat Gruntfuggly.todo-tree ms-python.python ms-python.pylint ms-python.debugpy ms-python.black-formatter ms-python.vscode-pylance ms-python.mypy-type-checker
```
![image](https://github.com/pes2324q2-gei-upc/PowerPathFinder/assets/75203757/7e479d8b-4d1c-47fb-9e85-fb2b351a2628)

4. Instalad todas las que aparezcan

_OPCIONAL PERO RECOMENDADO_
> Cuando tienes 30 extensiones como yo, si todas tus extensiones estan activadas de forma global estas se cargaran cada vez que abras VScode, sea el workspace(=carpeta) que sea. Para evitar eso... 

5. Desactivad la extension de forma global  
![image](https://github.com/pes2324q2-gei-upc/PowerPathFinder/assets/75203757/da128750-3024-4fd7-98fc-df587e904b3a)

7. Activadla solo en el workspace  
![image](https://github.com/pes2324q2-gei-upc/PowerPathFinder/assets/75203757/e3bb372f-bdc1-475d-bce9-0f8040fc6494)

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

### Python
(@Miki pots fer els de python? acuerdate de pep8 y pylint (mes el suite de testing si cal))

### Flutter + Dart

**Linux Debian**
- Descargar https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.19.2-stable.tar.xz
```
cd ~
tar xf ~/Downloads/flutter_linux_v3.19.2-stable.tar.xz
echo 'export PATH="$PATH:~/flutter/bin"' >> $HOME/.bashrc
```
- Opcional `flutter precache`
