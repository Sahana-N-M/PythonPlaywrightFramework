pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Sahana-N-M/PythonPlaywrightFramework.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '"C:\\Users\\sahana.nm\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
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