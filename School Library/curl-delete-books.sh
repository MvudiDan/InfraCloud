APIKEY="cisco|inAvuJqxLo2YzEYexkvr5QsVP7e_7Frtb53MPu4VzMg"
BOOK=11111111
DELETE_URL = "http://library.demo.local/api/v1/books/"$BOOK
echo $DELETE_url
curl -X DELETE DELETE_URL -H "accept: application/json" \
-H "X-API-KEY: $APIKEY" -H "Content-Type: application/json"
