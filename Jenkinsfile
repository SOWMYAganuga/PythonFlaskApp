pipeline {
    agent any
    environment {
        VIRTUAL_ENV = 'venv'
    }
    stages {
        stage('Setup') {
            steps {
                echo 'Setting up the environment...'
                sh 'ls -la' // List the files in the workspace
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
            // Optional: Add further actions on success
        }
        failure {
            echo 'Build failed!'
            // Optional: Add further actions on failure
        }
    }
}
