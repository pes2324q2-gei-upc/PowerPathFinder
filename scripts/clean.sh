sudo "Started project cleanup"
echo "Composing down containers, this might take a while"
docker compose -f 'docker-compose.development.yml' down > /dev/null 2>&1

if [ "$1" = "ultra" ]; then
    echo "Prunning all docker system, this may take a while"
    sudo docker system prune -af > /dev/null 2>&1 &
fi


echo "Removing all python cache files, migrations, database, build files"
sudo find . -type d -name '__pycache__' -exec rm -fr {} + > /dev/null 2>&1 &
sudo find . -path 'ppf/common/migrations/*.py' -not -name '__init__.py' -delete > /dev/null 2>&1 &

echo "Removing all python installation files and database"
sudo rm -f db/db.sqlite3 > /dev/null 2>&1 &
sudo rm -rf ppf/build/ ppf/ppf.egg-info/ > /dev/null 2>&1 &

echo "Removing installed editable python packages"
sudo .venv/bin/pip uninstall -y ppf > /dev/null 2>&1 &

wait
echo "🧼 Clean complete 🧼"
echo ""