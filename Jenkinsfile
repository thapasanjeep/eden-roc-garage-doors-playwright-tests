pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment
                bat 'C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m venv venv'
                // Install all dependencies from requirements.txt
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                // KEY difference from Selenium
                // Playwright needs its own Chromium binary
                bat 'venv\\Scripts\\playwright install chromium'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                // Run headless — no --headed in CI
                bat 'venv\\Scripts\\pytest tests/ -v --html=report.html'
            }
        }
    }

    post {
        always {
            // Always publish report whether tests pass or fail
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Playwright Test Report'
            ])
        }
        success {
            echo '✅ All Playwright tests passed!'
        }
        failure {
            echo '❌ Some tests failed — check the report'
        }
    }
}