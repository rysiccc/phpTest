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
                sh "chmod +x skrypt.py"
		sh "python3 skrypt.py"
            }
        }
    }
}
