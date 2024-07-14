pipeline {
    agent any
    environment {
        VIRTUAL_ENV = 'venv'
    }
    stages {
        stage('Setup') {
            steps {
                echo 'Setting up the environment...'
                sh '''
                   python3 -m venv $VIRTUAL_ENV
                   source $VIRTUAL_ENV/bin/activate
                   pip install -r requirements.txt
                '''
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                   source $VIRTUAL_ENV/bin/activate
                   python setup.py build
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh '''
                   source $VIRTUAL_ENV/bin/activate
                   pytest tests/
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh '''
                   source $VIRTUAL_ENV/bin/activate
                   # Add your deployment script here
                   # Example: scp -r * user@server:/path/to/deploy
                '''
            }
        }
    }
    post {
        success {
            echo 'Build successful!'
            mail to: 'team@example.com',
                 subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                 body: "Good news! The job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' has succeeded."
        }
        failure {
            echo 'Build failed!'
            mail to: 'team@example.com',
                 subject: "FAILURE: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                 body: "Bad news! The job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' has failed."
        }
    }
}
