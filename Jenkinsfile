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
                        string(credentialsId: 'GOOGLE_CHAT_WEBHOOK_URL', variable: 'CHAT_WEBHOOK'),
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
                script {
                    // Docker Image'ı build et
                    sh 'docker build -t ahmetcan114/chat .'
                    // Docker Hub'a login ol
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // GitHub'dan çekilen kod içerisindeki Kubernetes deployment dosyasını uygula
                    sh 'kubectl apply -f deployment.yaml'
                }
            }
        }
    }
    post {
        always {
            // İşlemler bittikten sonra konteyner ve image'ları temizle
            sh 'docker stop chat-container || true'
            sh 'docker rm chat-container || true'
            sh 'docker rmi ahmetcan114/chat || true'
        }
    }
}
