pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('206') // Replace with your Docker Hub credentials ID
        DOCKER_IMAGE = 'ahmedaemadra/depi-20depi-2066:tagname' // Replace with your Docker Hub image name
        GIT_CREDENTIALS_ID = 'github-ssh'  // Set your Jenkins SSH credentials ID here
        GIT_BRANCH = 'master'                             // Replace with your target branch
    }
    stages {
        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build --no-cache -t ${DOCKER_IMAGE} .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh 'docker run --rm ${DOCKER_IMAGE} pytest'
                }
            }
        }
        stage('Stop & Remove Existing Container') {
            steps {
                script {
                    // Stop and remove the existing container if it's running
                    sh '''
                        if [ "$(docker ps -q -f name=simple-flask-app)" ]; then
                            docker stop simple-flask-app
                            docker rm simple-flask-app
                        fi
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy the Docker container
                    sh "docker run -d --name simple-flask-app -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }

        // Git add, commit, and push stage
        stage('Git Add, Commit, and Push') {
            steps {
                sshagent(['github-ssh']) {   // Use SSH agent for GitHub authentication
                    sh 'git config --global user.email "emadrar15@gmail.com"'  // Set your git user email
                    sh 'git config --global user.name "Ahmed-emadr"'         // Set your git user name

                    sh '''
			    if [ -n "$(git status --porcelain)" ]; then
        			git add .
       				 git commit -m "Automated commit by Jenkins"
    			   else
        			echo "No changes to commit."
    			    fi
					'''
      
                    sh 'git push origin ${GIT_BRANCH}'                     // Push to the target branch
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                    // Push the Docker image
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
    }
    post {
        success {
            emailext(
                subject: "Pipeline Success: ${env.JOB_NAME}",
                body: "The pipeline has completed successfully.",
                to: "mostafakhaledmostafa00@gmail.com"
            )
        }
        failure {
            emailext(
                subject: "Pipeline Failure: ${env.JOB_NAME}",
                body: "The pipeline has failed.",
                to: "mostafakhaledmostafa00@gmail.com"
            )
        }
    }
}
