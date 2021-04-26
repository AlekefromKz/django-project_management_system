# Dockerized Django web application

This web project has been made by using Python Dhango framework and Docker containerization has been utilized to run the it in the isolated environment. 

Docker takes the best of the virtualization features and removes the drawbacks of it, such as resource drain, setup time, and maintenance. The portability of Docker also enables various developers/project members to run it in an OS/system-agnostic way. 

In the project main Docker image configuration settings are located inside ``Dockerfile`` file. With the help of ``docker-compose.yml`` file it was possible to configure application's services.

Run the following to start project in detached mode: 
`docker-compose up -d --build`
