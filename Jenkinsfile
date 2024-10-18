pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('206') // Replace with your Docker Hub credentials ID
        DOCKER_IMAGE = 'ahmedaemadra/depi-206' // Replace with your Docker Hub image name
        DOCKER_TAG = "${GIT_COMMIT}"
        
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
    stage('Kubernetes Deployment') {
    steps {
        script {
            withCredentials([file(credentialsId: 'kubeconfig-id', variable: 'KUBECONFIG')]) {
                sh '''
                    kubectl --kubeconfig=$KUBECONFIG set image deployment/${DEPLOYMENT_NAME} \
                    ${DEPLOYMENT_NAME}=${DOCKER_IMAGE}:${DOCKER_TAG} --namespace=${NAMESPACE}
                    kubectl --kubeconfig=$KUBECONFIG rollout status deployment/${DEPLOYMENT_NAME} --namespace=${NAMESPACE}
                '''
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
