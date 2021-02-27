pipeline {
    agent any

    stages {
        stage('prepare') {
            steps {
                sh 'apt-get install curl -y'
                sh 'chmod +x fetch_from_mega.sh'
                sh './fetch_from_mega.sh ${FILE_URL}'
            }
        }
        stage('build') {
            steps {
                sh 'docker build -t lab_3:${BUILD_NUMBER} .'
                sh 'docker tag lab_3:${BUILD_NUMBER} lab_3:latest'
                sh 'docker run -d -i --name lab --rm lab_3'
            }
        }
        stage('test') {
            steps {
                sh 'docker exec -i lab_3 sh -c "pytest test.py"'
            }
        }
    }

    post {
        always {
            sh 'docker rm -f lab'
        }
    }
}
