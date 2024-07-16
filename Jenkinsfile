pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Debug') {
            steps {
                sh 'pwd'  // Print working directory
                sh 'ls -la'  // List all files in the directory
            }
        }
        stage('Build') {
            steps {
                sh '''
                source venv/bin/activate
                python setup.py build
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                // Activate the virtual environment and run tests
                sh '''
                   source $VIRTUAL_ENV/bin/activate
                   pytest tests/
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Activate the virtual environment and deploy the application
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
