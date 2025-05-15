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
		sh "python3 skrypt.sh"
            }
        }
    }
}
