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
                    sh 'docker build -t harbor.sdpaas.com/devops/chat:v1.0 .'
                    withCredentials([usernamePassword(credentialsId: 'harbor_credentials', usernameVariable: 'HARBOR_USERNAME', passwordVariable: 'HARBOR_PASSWORD')]) {
                        sh 'docker login harbor.sdpaas.com -u $HARBOR_USERNAME -p $HARBOR_PASSWORD'
                    }
                    sh 'docker push harbor.sdpaas.com/devops/chat:v1.0'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'helm upgrade --install chatbot-exporter-scraper helm -f helm/values.yaml -n'

                }
            }
        }
    }
    post {
        always {
            // İşlemler bittikten sonra konteyner ve image'ları temizle
            sh 'docker stop chat-container || true'
            sh 'docker rm chat-container || true'
            sh 'docker rmi harbor.sdpaas.com/devops/chat:v1.0 || true'
        }
    }
}
