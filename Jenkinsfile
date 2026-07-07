$ docker-compose build
Command 'docker-compose' not found, but can be installed with:
sudo snap install docker
jyothika@jtest:~/two-tier-app/two-tier-app
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
