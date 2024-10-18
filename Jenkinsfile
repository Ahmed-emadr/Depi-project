pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('206') // Replace with your Docker Hub credentials ID
        DOCKER_IMAGE = 'ahmedaemadra/depi-206' // Replace with your Docker Hub image name
        DOCKER_TAG = "${GIT_COMMIT}"
        KUBECONFIG_CREDENTIALS = credentials('kubeconfig-id') // Replace with your kubeconfig credentials ID
    }
    stages {
        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build --no-cache -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh 'docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} pytest'
                }
            }
        }
        stage('Kubernetes Deployment') {
    steps {
        script {
            // Securely write kubeconfig to a file
            withCredentials([file(credentialsId: 'kubeconfig-id', variable: 'KUBECONFIG_FILE')]) {
                sh 'cp $KUBECONFIG_FILE /tmp/kubeconfig'
                env.KUBECONFIG = '/tmp/kubeconfig'

                // Verify kubeconfig
                sh 'kubectl config view'

                // Apply Kubernetes deployment
                sh 'kubectl apply -f k8s/deployment.yaml' // Update with your deployment file path
            }
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
                    sh "docker run -d --name simple-flask-app -p 5000:5000 ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                    // Push the Docker image
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
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
