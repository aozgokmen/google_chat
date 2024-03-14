pipeline {
    agent any
    environment {
        // Jenkins'deki Credentials'dan alınan kimlik bilgileri
        OPSGENIE_API_KEY = credentials('OPSGENIE_API_KEY')
        SCHEDULE_IDENTIFIER = credentials('SCHEDULE_IDENTIFIER')
        GOOGLE_CHAT_WEBHOOK_URL = credentials('GOOGLE_CHAT_WEBHOOK_URL')
        // Diğer değişkenleri ekleyin, örnek:
        GITHUB_INFO = credentials('github_info')
        DOCKER_INFO = credentials('docker_info')
    }
    stages {
        stage('Checkout') {
            steps {
                // GitHub'dan kod çekme
                git url: 'https://github.com/aozgokmen/google_chat.git', credentialsId: 'github_info'
            }
        }
        stage('Load Environment Variables') {
            steps {
                script {
                    // .env dosyasını dinamik olarak yaratma veya mevcut birini kullanma
                    sh 'echo OPSGENIE_API_KEY=$OPSGENIE_API_KEY > .env'
                    sh 'echo SCHEDULE_IDENTIFIER=$SCHEDULE_IDENTIFIER >> .env'
                    sh 'echo GOOGLE_CHAT_WEBHOOK_URL=$GOOGLE_CHAT_WEBHOOK_URL >> .env'
                    // Diğer ortam değişkenlerini ekleyin
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                // Docker image'ını build etme ve çalıştırma
                sh 'docker build -t your-app-name .'
            }
        }
        stage('Deploy') {
            steps {
                // Docker container'ını çalıştırma
                sh 'docker run --env-file .env -d your-app-name'
            }
        }
    }
}
