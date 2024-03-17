pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/aozgokmen/google_chat.git', credentialsId: 'github_info', branch: 'main'
            }
        }
        stage('Docker Check') {
            steps {
                script {
                    // Docker versiyonunu kontrol et
                    sh 'docker --version'
                    
                    // Çalışan Docker konteynerlarını listele
                    sh 'docker ps'
                    
                    // Mevcut Docker imajlarını listele
                    sh 'docker images'
                }
            }
        }
        stage('Prepare Environment') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OPSGENIE_API_KEY', variable: 'OPSGENIE_KEY'),
                        string(credentialsId: 'SCHEDULE_IDENTIFIER', variable: 'SCHEDULE_ID'),
                        string(credentialsId: 'GOOGLE_CHAT_WEBHOOK_URL', variable: 'CHAT_WEBHOOK')
                    ]) {
                        env.OPSGENIE_API_KEY = OPSGENIE_KEY
                        env.SCHEDULE_IDENTIFIER = SCHEDULE_ID
                        env.GOOGLE_CHAT_WEBHOOK_URL = CHAT_WEBHOOK
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-app:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run --name my-app-container -d my-app:latest'
                sh 'docker ps'
                sh 'docker logs my-app-container'
            }
        }
    }
    post {
        always {
            sh 'docker stop my-app-container || true'
            sh 'docker rm my-app-container || true'
            sh 'docker rmi my-app:latest || true'
        }
    }
}
