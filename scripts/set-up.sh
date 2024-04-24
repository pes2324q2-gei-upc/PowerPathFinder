# Get the first argument into a variable
ARG1="$1"

echo this will remove the following folders:
echo ppf-route-api
echo ppf-user-api
echo ppf-admin-page
echo ppf-payments-api
echo ppf-chat-engine
echo db

read -p "Are you sure you want to continue? (y/n): " answer

if [ "$answer" = "y" ]; then
    echo Removing all cloned repositories
    rm -rf ppf-route-api
    rm -rf ppf-user-api
    rm -rf ppf-admin-page
    rm -rf ppf-payments-api
    rm -rf ppf-chat-engine
    echo Removing database
    rm -rf db
    echo "Removal completed"
else
    exit 1
fi

# If a service is not present, clone it
repos=("ppf-route-api" "ppf-user-api" "ppf-admin-page" "ppf-payments-api" "ppf-chat-engine")

reload=false
for repo in "${repos[@]}"; do
    if [ ! -d "$repo" ]; then
        reload=true
        echo "Cloning $repo"
        git clone https://github.com/pes2324q2-gei-upc/$repo.git &
    fi
done

if [ $reload = true ]; then
    wait
    echo "-----------------------------------------------------"
    echo "| repos have been cloned! reload your vscode window |"
    echo "-----------------------------------------------------"

    echo creating database file...

    cd $(dirname "$0")/..

    mkdir -p db
    rm -f db/db.sqlite3
    touch db/db.sqlite3

    echo "Set-up complete"
    exit 1
fi
