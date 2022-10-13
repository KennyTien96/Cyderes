from flask import Flask, render_template
from whois_token import WHOIS_API_KEY
import requests, json

app = Flask(__name__)

# Route for home page
@app.route("/")
def home_page():
    return render_template("index.html")

# Route for domain query
@app.route("/<domain>", methods=['GET'])
def get_details(domain):
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={WHOIS_API_KEY}&outputFormat=JSON&domainName={domain}"
    response = requests.get(url)
    return (response.json())

if __name__ == '__main__':
    app.run(debug=False)
