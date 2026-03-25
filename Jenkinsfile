pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SatishYedida-hub/node-ai-review-project.git'
            }
        }

        stage('Install') {
            steps {
                sh 'npm install'
            }
        }

        stage('Run App') {
            steps {
                sh 'node app.js'
            }
        }

        stage('Get Changes') {
            steps {
                sh 'git diff HEAD~1 > changes.diff || echo "No diff"'
            }
        }
        stage('Install Python Dependencies') {
            steps {
                sh 'pip3 install boto3'
            }
        }

        stage('AI Review') {
            steps {
                sh 'python3 ai_review.py'
            }
        }
    }
}
