pipeline {
    agent { label 'master-node' }

    environment {
        DOCKER_IMAGE = "stdocker2901/docker-training"
        DOCKER_CREDENTIALS = "dockerhub-credentials"
        REMOTE_SSH = "st07061901-worker-node"
        PIPELINE_ID = "${env.BUILD_ID}"
    }

    stages {
        stage('Cleanup Workspace') {
            steps {
                deleteDir() 
            }
        }
        stage('Checkout Code') {
            steps {
                sh "pwd"
                sh "whoami"
                sh "ifconfig "
                git branch: 'main', url: 'https://github.com/srujal0610/Jenkins-cicd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "chmod +x gradlew"
                    sh "./gradlew clean"
                    sh "./gradlew buildDockerImage -Pliferay.workspace.environment=prod"
                    echo "build liferay image successfully"
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "echo dockerhub login successfull"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    def pipelineId = env.BUILD_ID
                    sh "docker tag liferay-jenkins-cicd-liferay:7.4.13-u112 ${DOCKER_IMAGE}:${pipelineId}"
                    sh "docker push ${DOCKER_IMAGE}:${pipelineId}"
                    echo "Pushed docker image with name as ${DOCKER_IMAGE}:${pipelineId}"
                }
            }
        }

        stage('Deploy on Remote Server') {
            steps {
                script {
                    def pipelineId = env.BUILD_ID
                    withCredentials([usernamePassword(credentialsId: 'st07061901-liferay-user', usernameVariable: 'SSH_USER', passwordVariable: 'SSH_PASS')]) {
                        sh """
                            sshpass -p "\$SSH_PASS" ssh -o StrictHostKeyChecking=no "\$SSH_USER@192.168.1.218" <<-'EOF'
                                echo "${pipelineId}"
                                whoami
                                pwd
                                cd /opt/liferay
                                source .env
                                docker-compose down -v
                                echo "compose down successfully"
                                rm -f .env # use -f to avoid errors if the file does not exist
                                echo "DOCKER_IMAGE=${pipelineId}" > .env # use > instead of >> to overwrite
                                chmod +x .env
                                cat .env
                                docker-compose up -d
                                echo 'Started the deployment stage'
                                echo 'Deployment completed and successful'
                                exit 0
                            EOF
                        """
                    }
                }
            }
        }
    }
}
