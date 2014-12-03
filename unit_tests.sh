curl -i -X POST -u $user:$password -H "Content-Type: application/json" -d '{"title": "'"$message"'"}' https://api.github.com/repos/arbor-test/parameter-injection/issues
