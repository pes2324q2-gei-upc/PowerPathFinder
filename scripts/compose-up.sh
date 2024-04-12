# Get the first argument into a variable
ARG1="$1"

touch ./db/db.sqlite3
echo "Installing requirements"
.venv/bin/pip install -r ppf-route-api/requirements.txt &
.venv/bin/pip install -r ppf-user-api/requirements.txt &
echo "Installing editable ppf package"
.venv/bin/pip install -e ppf &
wait

echo "Creating migrations and loading sample data"
.venv/bin/python ppf-route-api/manage.py makemigrations
.venv/bin/python ppf-route-api/manage.py migrate
.venv/bin/python ppf-route-api/manage.py loaddata sample_users.json sample_routes.json
echo "Spinning up development environment"

if [ "$1" = "macos" ]; then
    docker compose -f 'docker-compose.development.yml' 'docker-compose.macos.yml' up -d
    exit 0
fi

docker compose -f 'docker-compose.development.yml' up -d