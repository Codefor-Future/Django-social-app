pipeline{
    agent any
    environment {
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        AWS_DEFAULT_REGION = "ap-southeast-1"
    }
    stages {// stage blocks
        stage('Initialize'){
            steps {
                script {
                def dockerHome = tool 'docker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }
        stage('Build and push Docker image from Django project') {
                steps {
                    dir('socialapp'){
                        sh 'docker build -t django-app:latest .'
                        withCredentials([usernamePassword(credentialsId:'DockerHub', usernameVariable:'DOCKER_USERNAME', passwordVariable:'DOCKER_PASSWORD')]) {
                            sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                        }   
                        sh 'docker tag django-app:latest abhinavparakkal/django-app:latest'
                        sh 'docker push abhinavparakkal/django-app:latest'
                    }
                }
            } 
        

        stage("Deploy to eks") {
                steps {
                    script {
                        dir('kubernetes'){
                            sh '''
                                if [ -f /usr/local/bin/aws ]; then
                                # AWS is installed
                                echo "AWS is installed"
                                else
                                # AWS is not installed
                                echo "AWS is not installed"
                                curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
                                unzip -o awscliv2.zip
                                ./aws/install
                                fi
                            '''
                            
                            sh "aws eks update-kubeconfig --name EKS"
                            sh 'curl -LO "https://storage.googleapis.com/kubernetes-release/release/v1.20.5/bin/linux/amd64/kubectl"'  
                            sh 'chmod u+x ./kubectl'  
                            sh './kubectl apply -f app-deployment.yml'
                            sh './kubectl apply -f app-service.yml'
                            // sh "aws eks update-kubeconfig --name myapp-eks-cluster"
                            // sh "kubectl apply -f nginx-deployment.yaml"
                            // sh "kubectl apply -f nginx-service.yaml"
                        }
                    }
                }
            }
}
}