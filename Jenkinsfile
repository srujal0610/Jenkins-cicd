pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "stdocker2901/docker-training"
        DOCKER_CREDENTIALS = "dockerhub-credentials"
        REMOTE_SSH = "remote-server-credentials"
        CONTAINER_NAME = "node-app"
    }

    stages {
        stage('Cleanup Workspace') {
            steps {
                deleteDir() // Cleans the workspace before the build
            }
        }
        stage('Checkout Code') {
            steps {
                sh "pwd"
                sh "whoami"
                git branch: 'main', url: 'https://github.com/srujal0610/Jenkins-cicd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def pipelineId = env.BUILD_ID
                    sh "chmod +x gradlew"
                    sh "./gradlew clean"
                    sh "./gradlew buildDockerImage -Pliferay.workspace.environment=prod"
                    sh "docker build -t ${DOCKER_IMAGE}:lr_${pipelineId} ."
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

        // stage('Push Docker Image') {
        //     steps {
        //         script {
        //             def pipelineId = env.BUILD_ID
        //             sh "docker push ${DOCKER_IMAGE}:php_${pipelineId}"
        //             sh "docker tag ${DOCKER_IMAGE}:php_${pipelineId} ${DOCKER_IMAGE}:latest"
        //             sh "docker push ${DOCKER_IMAGE}:latest"
        //             echo "Pushed current version image and latest version image to docker hub"
        //         }
        //     }
        // }

        // stage('Deploy on Remote Server') {
        //     steps {
        //         script {
        //             def pipelineId = env.BUILD_ID
        //             sh "docker pull ${DOCKER_IMAGE}:latest"
        //             sh "docker-compose ps | grep 'Up' >/dev/null 2>&1 && docker-compose down -v || true"
        //             sh "docker-compose up -d"
        //             sh "pwd"
        //             echo "Deployment stage completed"
        //         }
        //     }
        // }
    }

    // post {
    //     always {
    //         echo "Pipeline completed."
    //         sh "cd .."
    //         sh "pwd"
    //         // sh "rm -r *"
    //     }
    // }
}
