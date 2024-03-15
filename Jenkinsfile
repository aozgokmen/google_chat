pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/aozgokmen/google_chat.git', credentialsId: 'github_info' , branch: 'main'
            }
        }
        stage('Load Environment Variables') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OPSGENIE_API_KEY', variable: 'OPSGENIE_API_KEY'),
                        string(credentialsId: 'SCHEDULE_IDENTIFIER', variable: 'SCHEDULE_IDENTIFIER'),
                        string(credentialsId: 'GOOGLE_CHAT_WEBHOOK_URL', variable: 'GOOGLE_CHAT_WEBHOOK_URL')
                    ]) {
                        sh 'echo "OPSGENIE_API_KEY=$OPSGENIE_API_KEY" > .env'
                        sh 'echo "SCHEDULE_IDENTIFIER=$SCHEDULE_IDENTIFIER" >> .env'
                        sh 'echo "GOOGLE_CHAT_WEBHOOK_URL=$GOOGLE_CHAT_WEBHOOK_URL" >> .env'
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
                sh 'docker run --name my-app-container --env-file .env -d my-app:latest'
                sh 'docker ps' // Çalışan container'ları göster
                sh 'docker logs my-app-container' // Logları yazdır
            }
        }
    }
    post {
        always {
            sh 'docker stop my-app-container || true'
            sh 'docker rm my-app-container || true'
            sh 'docker rmi my-app:latest || true'
            sh 'rm -f .env || true'
        }
    }
}
