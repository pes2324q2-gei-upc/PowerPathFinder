@echo off
echo Ultra clean
echo Removing all docker containers, images, volumes, networks
docker compose -f "docker-compose.development.yml" down
docker system prune -af

echo Removing all python cache files, migrations, database, build files
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
for /r . %%f in (ppf\common\migrations\*.py) do @if not "%%~nxf"=="__init__.py" del "%%f"

echo Removing all python installation files and database
del /f /q db\db.sqlite3
rmdir /s /q ppf\build
rmdir /s /q ppf\ppf.egg-info

echo Removing installed editable python packages
.venv\Scripts\pip.exe uninstall -y ppf

echo Clean complete
