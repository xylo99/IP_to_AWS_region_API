# Description

Simple API implementation which converts your IP address into an AWS region. A POST request must be made before the region is caculated.
Regions are added to the database and retrieved in a FIFO manner. 

## API Doc

| Endpoint                        | GET                  | POST          |
| -------                         | ---                  | ---           |
| IP_to_AWS_region_API/api/       | Get the AWS region   | Add a new IP  |
|                                 | for the most recent  |               |
|                                 | IP (IPs are          |               |
|                                 | selected in a FIFO   |               |
|                                 | manner)              |               |
|                                 |                      |               |
| IP_to_AWS_region_API/api/ips    | List all IPs used    |   N/A         | (coming soon)
|                                 |                      |               |
| IP_to_AWS_region_API/api/regions| List all regions used|   N/A         | (coming soon)

## How to run

* First create an admin user:
  * `python3 manage.py createsuperuser`
* Then run the server:
  * `python3 manage.py runserver`
* Make your initial curl requests:
  * `curl --user name:password --data "ip=public_address" http://127.0.0.1:8000/IP_to_AWS_region_API/api/`
    * (replace localhost address and port with whatever you've configured django to use)
  * `curl --user name:password http://127.0.0.1:8000/IP_to_AWS_region_API/api/ `