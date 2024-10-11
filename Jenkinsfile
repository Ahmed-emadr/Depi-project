pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Ahmed-emadr/Depi-project.git' // Adjust this to your repo URL
            }
        }
        stage('Check Python and Pip') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }
        stage('Test') {
            steps {
                script {
                    sh '. pytest test_app.py'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t simple-flask-app .'
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
}

