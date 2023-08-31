import requests

# Define the URL of the server you want to send a request to
server_url = "http://localhost:8080"  # Change this URL to match your server's address

# Send a GET request to the server and print the response
try:
    response = requests.get(server_url)
    response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

    print("Response from the server:")
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
