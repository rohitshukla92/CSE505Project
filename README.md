# IDP3: Docker version

This document details how to acquire and run the dockerized version of IDP3. Please note that you have to install docker yourself: https://www.docker.com/ .

### Running the idp-ide

To run the idp-ide, simply:
1. Make sure the docker service is running.
2. Create a folder for idp files.
By default, we will assume this is the folder called `idp` in your home directory.
If you choose to change this folder, you should change the occurrence of `~/idp` in the following steps to the correct path.
3. run

    ```
    docker pull krrkul/idp3:latest; \
    docker run -it --rm --name idp3 -p 4004:4004 -v ~/idp:/root/idp krrkul/idp3:latest
    ```

    The first part will make sure that you are running the newest image, and requires an active internet connection.
4. Visit the idp-ide on http://localhost:4004.

### Running idp

Take care when running idp directly: because it runs in an image, accessing your own files can become a bit tricky.
The following step-by-step lists a few possible ways of handling this.

1. Start again by making sure that the docker service is running.
2. Update to the latest krrkul/idp3 image `docker pull krrkul/idp3:latest;`.
This will require an active internet connection.
3. Depending on what you want, choose a variation on the command `docker run -i --rm --name idp krrkul/idp3:latest idp`.
We will refer to this command as `idp3-docker`.
 
