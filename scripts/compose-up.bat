@echo off
echo Installing requirements
.venv\Scripts\pip.exe install -r ppf-route-api\requirements.txt
.venv\Scripts\pip.exe install -r ppf-user-api\requirements.txt

echo Installing editable ppf package
.venv\Scripts\pip.exe install -e ppf

echo Creating migrations and loading sample data
type nul > db\db.sqlite3
.venv\Scripts\python.exe ppf-route-api\manage.py makemigrations
.venv\Scripts\python.exe ppf-route-api\manage.py migrate
.venv\Scripts\python.exe ppf-route-api\manage.py loaddata sample_common_driver.json sample_common_user.json sample_user_auth.json sample_common_routes.json

echo Spinning up development environment
docker compose -f "docker-compose.development.yml" up -d
