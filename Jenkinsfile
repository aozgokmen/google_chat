pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/aozgokmen/google_chat.git', credentialsId: 'github_info', branch: 'main'
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
                        // Ortam değişkenlerini dosyaya yazmak yerine doğrudan Docker'da kullan
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
                sh 'docker build --progress=plain -t my-app:latest .'
            }
        }
        stage('Deploy') {
            steps {
                // Docker container'ını ortam değişkenleri ile çalıştır
                sh 'docker run --name my-app-container -e OPSGENIE_API_KEY -e SCHEDULE_IDENTIFIER -e GOOGLE_CHAT_WEBHOOK_URL -d my-app:latest'
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
        }
    }
}
