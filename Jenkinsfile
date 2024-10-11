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
      //  stage('Test') {
        //    steps {
          //      script {
                    // Run tests
         //           sh 'docker run --rm simple-flask-app pytest'
           //     }
           // }
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
}

