# Welland Canal Web Scraper

The project is a web scraper for the Welland Canal application.

This application scrapes the Great Lakes system for current bridge status and closures on the Welland Canal and then generates a JSON payload that is then sent to the [Welland Canal Api](https://github.com/joshuakaluba/WellandCanalApi). The payload from the Welland Canal Api is then used to power the Welland Canal Bridge Status Mobile application.

The Welland Canal Bridge Status Mobile application can be found [on the google play store](https://play.google.com/store/apps/details?id=com.nextappointments.wellandcanal&hl=en). Additionally, source code for the Welland Canal Mobile application is available [here](https://github.com/joshuakaluba/WellandCanal)

## Prerequisites

Install docker as per this [tutorial](https://docs.docker.com/docker-for-windows/install/)

## Execution

To run the application, first build the docker container using the following commands:

`docker build -t joshuakaluba\welland-canal-scraper .`

Once the container is built, run the container using the following commands:

`docker run -ti joshuakaluba\welland-canal-scraper`
