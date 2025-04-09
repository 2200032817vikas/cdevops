pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        
        stage('Deploy Weather App') {
            steps {
                sh 'ansible-playbook -i ansible/inventory ansible/playbook.yml'
            }
        }
    }
}
