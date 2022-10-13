
# Cyderes Assessment

Flask API that gets domain/IP address data from WHOIS API. Returns data in JSON format.

Deployed a Dockerized Flask API to GCP, while provisioning the infrastructure using Terraform.

Severless function deployed here: https://cyderes-assessment-tigecyl3va-wl.a.run.app/


## API Reference

#### Get all items

```http
  GET https://cyderes-assessment-tigecyl3va-wl.a.run.app/${domain}
```

| Parameter || Description                |
| :-------- | :------- | :------------------------- |
| `domain` || **Required**. domain or IPv4 IPv6 address |

