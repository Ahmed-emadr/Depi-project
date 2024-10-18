pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('206') // Replace with your Docker Hub credentials ID
        DOCKER_IMAGE = 'ahmedaemadra/depi-20depi-2066:tagname' // Replace with your Docker Hub image name
        
    }
    stages {
        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    env.DOCKER_IMAGE = "${IMAGE_NAME}:${BUILD_NUMBER}"
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
