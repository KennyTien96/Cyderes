
# Cyderes Assessment

Flask API that gets domain/IP address data from [WHOIS API](https://whois.whoisxmlapi.com/ "Named link title"). Returns data in JSON format.

Deployed a Dockerized Flask API to GCP, while provisioning the infrastructure using Terraform.

Severless function deployed here: https://cyderes-assessment-tigecyl3va-wl.a.run.app/

This was my first time utilizing Terraform to deploy infrastructure, so most of my time was spent reading documentation and troubleshooting Terraform. I decided to go with a lightweight framework such as Flask to get my simple API up and running quickly. 

However there are many improvements I could add such as: 
* More functionality to the API itself, instead of just returning the entire JSON file
* UI changes, creating styles.css for Flask app
* Implementing Terraform Backend to store the .tfstate files
* Utilzing Github Actions to build Docker image, tag image, and push to Google Container Registry 


## Local Installation

Get API key to [WHOIS API](https://whois.whoisxmlapi.com/ "Named link title") by signing up for an account

For local installation and deployment, clone the repo and do the following:

```bash
  cd Cyderes
```
Install the dependencies
```bash
  pip install -r requirements.txt
```
Create whois_token.py in root directory and place the API key there
```bash
  WHOIS_API_KEY = "at_IaNR9kBp8zu3IVkjZQzSubZ7DeZ8q"
```
Launch the Flask server with 
```bash
  flask run
```
## Deployment

To deploy this project run the following: 

Navigate to infrastructure directory and initialize the directory with

```bash
  terraform init
```

then validate the files with 
```bash
  terraform validate
```
and deploy with 
```bash
  terraform apply
```
## API Reference

#### Get all items

```http
  GET https://cyderes-assessment-tigecyl3va-wl.a.run.app/${domain}
```

| Parameter || Description                |
| :-------- | :------- | :------------------------- |
| `domain` || **Required**. domain or IPv4 IPv6 address |


## Running Tests

To run tests, export the Cyderes.Tests.json file from the tests directory and import it into Postman to run. The test cases cover the following : 

* Home page status code is 200
* Text on home page is displayed
* Valid domain request
* Valid IPv4 request
* Valid IPv6 request
* Invalid request

