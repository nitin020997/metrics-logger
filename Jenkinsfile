pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t metrics-logger .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm metrics-logger'
            }
        }

        stage('Done') {
            steps {
                echo '✅ Jenkins pipeline completed!'
            }
        }
    }
}
