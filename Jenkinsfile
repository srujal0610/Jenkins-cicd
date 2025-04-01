pipeline {
    agent any
    
    stages {
        stage('Copy custom addons to remote') {
            steps {
                script {
                    def remoteUser = 'odoo'  // Replace with actual remote user
                    def remoteHost = '192.168.1.218'  // Replace with actual remote server IP/hostname
                    def sourcePath = '/opt/odoo/extra-addons/custom-addons/'  // Source directory
                    def destinationPath = '/opt/odoo/extra-addons/custom-addons/'  // Destination directory on remote server
                    
                    sh """
                        rsync -avz ${sourcePath} ${remoteUser}@${remoteHost}:${destinationPath}
                    """
                }
            }
        }
        
        stage('Restart Docker Containers') {
            steps {
                script {
                    def remoteUser = 'odoo'  // Replace with actual remote user
                    def remoteHost = '192.168.1.218'  // Replace with actual remote server IP/hostname
                    def composePath = '/opt/odoo/extra-addons/custom-addons/'  // Path where docker-compose.yml is located
                        
                    sh """
                        ssh ${remoteUser}@${remoteHost} 'cd ${composePath} && docker-compose restart'
                    """
                }
            }
        }
    }
}
