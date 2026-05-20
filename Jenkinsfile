pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Sahana-N-M/PythonPlaywrightFramework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
                bat 'venv\\Scripts\\playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            echo "Execution Completed"
        }
    }
}