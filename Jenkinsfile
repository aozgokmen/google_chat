pipeline {
    agent any
    environment {
        // Jenkins'deki Credentials'dan alınan kimlik bilgileri
        OPSGENIE_API_KEY = credentials('OPSGENIE_API_KEY')
        SCHEDULE_IDENTIFIER = credentials('SCHEDULE_IDENTIFIER')
        GOOGLE_CHAT_WEBHOOK_URL = credentials('GOOGLE_CHAT_WEBHOOK_URL')
        GITHUB_INFO = credentials('github_info')
        DOCKER_INFO = credentials('docker_info')
    }
    stages {
        stage('Checkout') {
            steps {
                // GitHub'dan main branch kod çekme
                git url: 'https://github.com/aozgokmen/google_chat.git', branch: 'main', credentialsId: 'github_info'
            }
        }
        stage('Load Environment Variables') {
            steps {
                script {
            // Ortam değişkenlerini gizli bir şekilde .env dosyasına yaz
                withCredentials([
                string(credentialsId: 'OPSGENIE_API_KEY', variable: 'OPSGENIE_API_KEY'),
                string(credentialsId: 'SCHEDULE_IDENTIFIER', variable: 'SCHEDULE_IDENTIFIER'),
                string(credentialsId: 'GOOGLE_CHAT_WEBHOOK_URL', variable: 'GOOGLE_CHAT_WEBHOOK_URL')
                ]) {
                // OPSGENIE_API_KEY ve diğer değişkenler burada kullanılabilir ve maskelenmez
                sh 'echo OPSGENIE_API_KEY=$OPSGENIE_API_KEY > .env'
                sh 'echo SCHEDULE_IDENTIFIER=$SCHEDULE_IDENTIFIER >> .env'
                sh 'echo GOOGLE_CHAT_WEBHOOK_URL=$GOOGLE_CHAT_WEBHOOK_URL >> .env'
            }
        }
    }
}

        }
        stage('Build Docker Image') {
            steps {
                // Docker image'ını build etme
                // Dockerfile'ın konumunu kontrol edin; varsayılan olarak projenizin kök dizininde olmalıdır.
                sh 'docker build -t your-app-name .'
            }
        }
        stage('Deploy') {
            steps {
                // Docker container'ını çalıştırma
                // -d: detached modunda çalıştırır
                // --env-file: Environment variables'ları kullanır
                sh 'docker run --env-file .env -d your-app-name'
            }
        }
    }
    post {
        always {
            // Script sonunda temizlik işlemleri yapılır
            // Örneğin: build edilen Docker image'ını silme, geçici dosyaları temizleme vs.
            sh 'echo "Clean up actions"'
        }
    }
}
