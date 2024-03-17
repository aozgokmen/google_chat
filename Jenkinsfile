pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/aozgokmen/google_chat.git', credentialsId: 'github_info', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Docker imajını build edin ve bir değişkene atayın
                    def appImage = docker.build("my-app:latest", ".")
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Build edilen Docker imajını çalıştırın
                    docker.image("my-app:latest").run("--name my-app-container -e OPSGENIE_API_KEY=\${OPSGENIE_API_KEY} -e SCHEDULE_IDENTIFIER=\${SCHEDULE_IDENTIFIER} -e GOOGLE_CHAT_WEBHOOK_URL=\${GOOGLE_CHAT_WEBHOOK_URL}")
                }
            }
        }
    }
    post {
        always {
            // İşlem tamamlandığında konteyneri ve imajı temizleyin
            script {
                sh 'docker stop my-app-container || true'
                sh 'docker rm my-app-container || true'
                sh 'docker rmi my-app:latest || true'
            }
        }
    }
}
