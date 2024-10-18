pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('206') // Replace with your Docker Hub credentials ID
        DOCKER_IMAGE = 'ahmedaemadra/depi-206'
        DOCKER_TAG = "${GIT_COMMIT}"
        KUBECONFIG_CREDENTIALS = credentials('kubeconfig-id') // Your kubeconfig ID
    }
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker build --no-cache -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} pytest'
                }
            }
        }
        stage('Kubernetes Deployment') {
            steps {
                script {
                    // Set the KUBECONFIG from the credentials
                    writeFile(file: '/tmp/kubeconfig', text: "${KUBECONFIG_CREDENTIALS}")
                    env.KUBECONFIG = '/tmp/kubeconfig'

                    // Run your kubectl command here, e.g.:
                    sh "kubectl apply -f k8s/deployment.yaml"
                }
            }
        }
        stage('Stop & Remove Existing Container') {
            steps {
                script {
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
                    sh "docker run -d --name simple-flask-app -p 5000:5000 ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
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
