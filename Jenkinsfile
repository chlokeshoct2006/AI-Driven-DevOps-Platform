pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/your-username/ai-devops-platform.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ai-devops-app .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker stop app || true'
                    sh 'docker rm app || true'
                    sh 'docker run -d -p 3000:3000 --name app ai-devops-app'
                }
            }
        }

        stage('Health Check') {
            steps {
                script {
                    sh 'curl -f http://localhost:3000 || exit 1'
                }
            }
        }
    }
}