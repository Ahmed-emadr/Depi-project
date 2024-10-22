Project Overview
This project demonstrates a CI/CD pipeline for automating the deployment of a containerized application using tools such as Jenkins, Docker, Docker Hub, GitHub, Ansible, and Terraform. The pipeline is designed to build, test, and deploy a Docker container, push it to Docker Hub, and deploy the application on an Amazon EC2 instance. Monitoring is handled using Prometheus, and notifications are sent to Slack.

Pipeline Diagram

![image](https://github.com/user-attachments/assets/b13d0513-3eab-4cad-8cec-450675e9273e)

Key Components:
Jenkins: Continuous integration and pipeline orchestration.
Docker: Containerization of the application.
Docker Hub: Storing Docker images.
GitHub: Version control for source code.
Ansible: Configuration management and automation.
Terraform: Infrastructure as code to manage cloud resources (Amazon EC2, S3).
Prometheus: Monitoring the health of EC2 instances.
CloudWatch: Monitoring and alerting.
Slack: Notifications on build and deployment status.
Pipeline Stages

    docker build --no-cache -t ${DOCKER_IMAGE}:${DOCKER_TAG} .

Jenkins pulls the source code from GitHub.
Docker builds the application image from the Dockerfile.
The image is tagged with the current Git commit hash.

    Test

The Docker container runs tests (e.g., pytest).
If tests fail, Jenkins marks the pipeline as failed and sends an alert.

    Push to Docker Hub
    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"

After successful testing, the Docker image is pushed to Docker Hub using your credentials.

    Deployment

Ansible deploys the Docker image to the target Amazon EC2 instance.
Terraform provisions the EC2 instance and manages infrastructure resources (S3 for state storage).
Kubernetes (if applicable) is used to manage application instances on EC2.

    Monitoring

Prometheus monitors the health of the EC2 instance.
CloudWatch tracks performance metrics, sending alerts to Slack.
Prerequisites
Ensure you have the following installed and configured:

Jenkins (with necessary plugins like Docker and GitHub)
Docker and Docker Hub account
GitHub repository for source code
AWS EC2 instance and AWS CLI installed (for Terraform/Ansible)
Ansible for automating EC2 setup
Terraform for infrastructure provisioning
Prometheus for monitoring
Slack webhook for Jenkins notifications
Setup Instructions

    Clone the Repository

bash
Copy code
git clone (https://github.com/Ahmed-emadr/Depi-project.git)
cd your-repo

    Jenkins Configuration

Create a new Jenkins pipeline job.
Add your pipeline script (Jenkinsfile) to the job.
Configure credentials for Docker Hub and AWS.

    Docker

Ensure your Dockerfile is ready for building the application image.
Verify that Docker is running on your system.

    Ansible Playbook
    ansible-playbook -i inventory.ini deploy.yml

Use the provided Ansible playbook to configure and deploy to your EC2 instance.

    Terraform

Set up Terraform to provision your infrastructure on AWS.
Store Terraform state files on an S3 bucket.

    Monitoring and Alerts

Set up Prometheus to monitor the EC2 instance.
Connect CloudWatch and Slack for monitoring and alerting.
How to Run the Pipeline
Commit changes to GitHub – Trigger the pipeline by pushing code to your GitHub repository.
Jenkins triggers the build – Jenkins starts the pipeline automatically using GitHub webhooks.
Docker image build – The pipeline builds a Docker image of your application.
Push to Docker Hub – The Docker image is pushed to your Docker Hub repository.
Deploy to EC2 – Ansible deploys the application on an EC2 instance provisioned by Terraform.
Monitor – The EC2 instance is monitored by Prometheus, and CloudWatch sends alerts to Slack if any issues arise.
Technologies Used
Jenkins: Orchestrating the pipeline
Docker: Containerizing the application
Docker Hub: Hosting Docker images
GitHub: Source code management
Ansible: Configuration management and deployment automation
Terraform: Infrastructure as Code (IaC)
Prometheus: Monitoring the health of the infrastructure
AWS EC2 & S3: Cloud infrastructure for hosting the app
Slack: Team notifications for build and deployment statuses

Future Improvements
Integrate Kubernetes for container orchestration.
Expand monitoring with Grafana dashboards.
Improve security by integrating Vault for secrets management.

    Tips & Tricks:

1. SSH Key and Permissions Management:

    Problem: You encountered an error with the SSH key permissions being too open.
    Solution: Set the proper permissions for SSH keys using chmod 600 your_private_key to avoid this issue.
    Tip: Always ensure that SSH keys are not world-readable for security.

2. Pipeline Failures:

    Problem: The Jenkins pipeline failed with the error CredentialId could not be found.
    Solution: Verify that credentials are stored in Jenkins, and properly reference the credentials ID in the pipeline.
    Tip: Use Jenkins credentials management securely to avoid pipeline disruptions.

3. Docker Warning:

    Problem: "DEPRECATED: The legacy builder is deprecated."
    Solution: Install buildx for Docker to leverage BuildKit, which offers improved features for building images.
    Tip: Regularly check for deprecated features and update tools accordingly to avoid future issues.

4. Root Warning in Docker Builds:

    Problem: Warning about running pip as the root user.
    Solution: Use a virtual environment or add --root-user-action=ignore if running in a controlled environment.
    Tip: For production-grade builds, avoid using the root user in Docker containers.

5. Python Deprecation Warnings (Pytest):

    Problem: Deprecation warnings about ast.Str in Python 3.14.
    Solution: Keep an eye on the Python version you are using, and update your code to adapt to the latest changes.
    Tip: Regularly review library and language updates to ensure compatibility.

6. Docker Cleanup in Jenkins Pipeline:

    Problem: The pipeline uses a container from a previous run, which might cause conflicts.
    Solution: Use docker ps -q -f name=container_name to check if a container exists, and remove it if necessary before starting a new one.
    Tip: Always clean up containers to ensure fresh deployments.

7. Automating Docker Push to Docker Hub:

    Problem: The push to Docker Hub was skipped due to a previous failure.
    Solution: Ensure all steps before pushing the image succeed, especially commits and credentials.
    Tip: Add conditional stages to handle errors gracefully, ensuring that the pipeline can continue or retry certain steps.

8. Jenkins Git Integration:

    Problem: Commit failed because there were no changes to commit.
    Solution: Use git status to check for changes before committing.
    Tip: Automate Git commands only when changes exist to avoid unnecessary failures.
