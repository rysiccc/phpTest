pipeline{
    agent any

    stages{
        stage("Start"){
            steps{
                sh 'echo Start!'
            }
        }
        stage("CloneRepo"){
            steps{
                sh "git pull"
            }
        }
        stage("RunScript"){
            steps{
                sh "chmod +x skrypt.sh"
            }
            steps{
                sh "python3 skrypt.sh"
            }
        }
    }
}
