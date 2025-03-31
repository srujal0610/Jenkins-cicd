pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "stdocker2901/docker-training"
        DOCKER_CREDENTIALS = "dockerhub-credentials"
        REMOTE_SSH = "remote-server-credentials"
        CONTAINER_NAME = "node-app"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/srujal0610/Jenkins-cicd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def pipelineId = env.BUILD_ID
                    sh "whoami"
                    sh "id"
                    sh "ip addr show | grep inet | head -n 3 | tail -n 1"
                    sh "docker build -t ${DOCKER_IMAGE}:${pipelineId} ."
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
                    sh "docker push ${DOCKER_IMAGE}:${pipelineId}"
                    echo "Push to docker hub stage successful"
                }
            }
        }

        stage('Deploy on Remote Server') {
            steps {
                script {
                    def pipelineId = env.BUILD_ID
                    sshagent(['remote-server-credentials']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no st07061901@192.168.1.218 \
                        "docker pull ${DOCKER_IMAGE}:${pipelineId} && \
                        docker stop ${CONTAINER_NAME} || true && \
                        docker rm ${CONTAINER_NAME} || true && \
                        docker run -d --name ${CONTAINER_NAME} -p 3001:3001 ${DOCKER_IMAGE}:${pipelineId} && \
                        echo 'Deployment completed and successful'"
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
    }
}
