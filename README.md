# PowerPathFinder
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
### Python
(@Miki pots fer els de python? acuerdate de pep8 y pylint (mes el suite de testing si cal))

### Flutter + Dart

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

### VSCode
- ide
- extensiones
 - Docker
 - Python
 - Flutter
 - TodoTree
