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
}pipeline {
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
<<<<<<< HEAD
=======
}pipeline {
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
>>>>>>> 6dc08d3 (Add Jenkinsfile for Jenkins CI pipeline)
}
