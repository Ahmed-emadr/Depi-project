pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build --no-cache -t simple-flask-app .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh 'docker run --rm simple-flask-app pytest'
                }
            }
        }
        // stage('Push to Docker Hub') {
        //     steps {
        //         script {
        //             // Log in to Docker Hub
        //             //docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials-id') {
        //                 // Push the Docker image to Docker Hub
        //                 //sh 'docker tag simple-flask-app your-dockerhub-username/simple-flask-app:${env.BUILD_ID}'
        //                 //sh 'docker push your-dockerhub-username/simple-flask-app:${env.BUILD_ID}'
        //             }
        //         }
        //     }
        // }
        stage('Deploy') {
            steps {
                script {
                    // Deploy the Docker container
                    sh 'docker run -d -p 5000:5000 simple-flask-app'
                }
            }
        }
    }
    post {
        success {
            emailext(
                subject: "Pipeline Success: ${env.JOB_NAME}",
                body: "The pipeline has completed successfully.",
                to: "emadrar15@gmail.com"
            )
        }
        failure {
            emailext(
                subject: "Pipeline Failure: ${env.JOB_NAME}",
                body: "The pipeline has failed.",
                to: "emadrar15@gmail.com"
            )
        }
    }
}
