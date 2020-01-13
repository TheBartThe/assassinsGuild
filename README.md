# Assassins' Guild
## Presentation
![Presentation](https://github.com/TheBartThe/assassinsGuild/blob/master/Documentation/assassinsGuildPresentationCopy.pptx)

## Running this application
To run this application yourself:
Create two new VMs - one for Jenkins, with port 8080 opened, the other for deployment, with HTTP access allowed. Make sure you can SSH into both of these VMs.
Fork this repo into your own
Install Ansible and Git, and clone down the repository
In resources, changes the ip in the daemon.json file to the internal ip of the Jenkins VM
In the docker-compose.yaml, change the ip in the image names to the internal ip of the Jenkins vm
Change the git repo in the playbook to your repo
In the inventory, change the ip for the Jenkins group to the external ip of the Jenkins vm, and the ip of the swarm-master group to the external ip of the deployment vm. Change user to your user. Change private key file to the path to the private key being used to SSH into the other vms.
Upload these hanges to your GitHub
Run the ansible playbook using 'ansible-playbook -i inventory playbooks/jenkins-docker-playbook.yaml
A jenkins key will be shown - copy this
SSH from the Jenkins vm into the deployment vm for the first time - confirm yes when prompted
Navigate to jenkinsip:8080
Enter the key
Create a job using the Jenkinsfile and run it - app should now be deployed

## The Scope
The aim of this project was to create an application with individually containerised microservices, utilising ansible to build the VMs, version control, containers and continuous deployment.

## My Application
To satisfy this brief, I designed an application with four different microservices. One generates a random fictional character with associated points, one generates a random weapon with associated points, one combines these two services into a mission for the users and the total points acquired for this mission, and the final frontend service delivers this information to the user.

## Planning
To plan this project, I used a Trello board to design the functionality that the app would provide:
![Trello board](https://github.com/TheBartThe/assassinsGuild/blob/master/Documentation/trello.png)

A risk assessment was also undertaken, to analyse any potential problems which would be faced in creating, deploying, and maintaining the application, and minimising these risks:

| Risk      | Impact         | Likelihood  | Mitigation measure |
| :-------------: |:-------------:| :-----:|:------: |
| Losing code     | Medium | Medium | Regular uploads to GitHub |
| Website malfunctions from bad code     | Medium | High | Regular testing of code and website, throughout creation of application |
| Problem with VMs    | Medium | Medium | Create ansible playbook to set up VMs from scratch, so if a problem occurs, new VMs can be spun up and immediately be ready for deployment  |
| Not using version control tool (Git) properly    | Medium | High | Only work on a branch separate to the master branch, and test using this branch. Only edit master branch by merging other branches once they are operational |
| External SSH into VM     | High | Low | Tolerate - Google security is most likely better than any solution I can make |
| Website goes down when updating app     | Medium | High | Create multiple replicas for each container, so some containers are still running the old version when others are being updated, and nginx proxy passes user to running container |

## Creation and Deployment
The backend code was written in Python, using Flask as the web development framework, and HTML for the front end. Jinja2 was used to link the Python code to the HTML code. Trello was used as the project tracking tool, with Git as the version control system. An Ansible playbook was written to initially set up the VMs so they were instantly ready for deployment. Jenkins was used as the CI server, with Pytest used for unit testing and Docker Swarm for the deployment of the application. A webhook was created so any pushes to GitHub from the source code would trigger the Jenkins build, and deployment via Docker Swarm would be automated through this process. A CI Pipeline was created to illustrate this process:
![CI Pipeline](https://github.com/TheBartThe/assassinsGuild/blob/master/Documentation/CIPipeline.png)
