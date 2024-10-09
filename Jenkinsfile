pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t simple-flask-app .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest test_app.py'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 simple-flask-app'
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

