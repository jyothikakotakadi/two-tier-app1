
pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Code is already available in Jenkins workspace'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Start Containers') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Verify Application') {
            steps {
                sh 'curl http://localhost:5000'
            }
        }
    }
}
