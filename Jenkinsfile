pipeline {
    agent any
    // environment bloğu şu anda boş, bu yüzden kaldırıldı
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
                    withCredentials([
                        string(credentialsId: 'OPSGENIE_API_KEY', variable: 'OPSGENIE_API_KEY'),
                        string(credentialsId: 'SCHEDULE_IDENTIFIER', variable: 'SCHEDULE_IDENTIFIER'),
                        string(credentialsId: 'GOOGLE_CHAT_WEBHOOK_URL', variable: 'GOOGLE_CHAT_WEBHOOK_URL')
                    ]) {
                        sh 'echo OPSGENIE_API_KEY=$OPSGENIE_API_KEY > .env'
                        sh 'echo SCHEDULE_IDENTIFIER=$SCHEDULE_IDENTIFIER >> .env'
                        sh 'echo GOOGLE_CHAT_WEBHOOK_URL=$GOOGLE_CHAT_WEBHOOK_URL >> .env'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t your-app-name .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run --env-file .env -d your-app-name'
            }
        }
    }
    post {
        always {
            sh 'docker rmi your-app-name || true'
            sh 'rm -f .env || true'
        }
    }
}
