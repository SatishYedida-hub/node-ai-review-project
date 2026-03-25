pipeline {
    agent any

    environment {
        OPENAI_API_KEY = credentials('openai-api-key')
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Run App') {
            steps {
                sh 'node app.js'
            }
        }

        stage('Get Code Changes') {
            steps {
                sh 'git diff HEAD~1 > changes.diff || echo "No diff"'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                sh 'pip3 install openai'
            }
        }

        stage('AI Code Review') {
            steps {
                sh 'python3 ai_review.py'
            }
        }
    }
}
