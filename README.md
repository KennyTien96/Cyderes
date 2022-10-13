
# Cyderes Assessment

Flask API that gets domain/IP address data from [WHOIS API](https://whois.whoisxmlapi.com/ "Named link title"). Returns data in JSON format.

Deployed a Dockerized Flask API to GCP, while provisioning the infrastructure using Terraform.

Severless function deployed here: https://cyderes-assessment-tigecyl3va-wl.a.run.app/


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

To run tests, export the Cyderes.Tests.json file in the tests directory and import it into Postman to run. The test cases cover the following : 

* Home page status code is 200
* Text on home page is displayed
* Valid domain request
* Valid IPv4 request
* Valid IPv6 request
* Invalid request

