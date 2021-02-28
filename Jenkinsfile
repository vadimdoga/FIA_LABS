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
                sh 'docker build -t lab_4:${BUILD_NUMBER} .'
                sh 'docker tag lab_4:${BUILD_NUMBER} lab_4:latest'
            }
        }
        stage('test') {
            steps {
                sh 'docker run -i --rm lab_4'
            }
        }
    }
}
