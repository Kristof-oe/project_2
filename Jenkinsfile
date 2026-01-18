pipeline {
    agent any

    environment {
        PYTHON_VERSION ="3"
        VIRTUAL_ENV ="env"
        DOCKER_USERNAME="kris200036"
        DOCKERHUB_REPO="project_2"

    }

    stages {
        stage('Clone') {
            steps {
                echo 'Checkout..'
                checkout scm
                
            }
        }


        stage('Setup_Env') {
            steps {
                sh '''
                echo 'Setup..'
                python${PYTHON_VERSION} -m venv ${VIRTUAL_ENV}
                . ${VIRTUAL_ENV}/bin/activate
                '''
            }
        }

        stage('Install_Dependencies') {
            steps {
                sh '''
                echo 'Installing..'
                env/bin/python3 -m pip install --upgrade pip
                env/bin/python3 install -r requirements.txt 
                env/bin/python3 install pytest
                '''
            }
        }

        stage('Test_Unit') {
            steps {
                sh '''
                echo 'Testing..'
                export PYTHONPATH=$PWD
                pytest -v
                '''
            }
        }


        stage('Build_Local') {
            steps {
                echo 'Building..'
                sh '''
                docker build . -t localtest:test
                '''
            }
        }

        stage('Smoke_Test_Local') {
            steps {
                sh '''
                echo 'Testing..'
                docker run -d -name localtest -p 8000:8000 localtest:test
                docker logs localtest
                curl -f http://localhost:8000/health
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh '''
                echo 'Cleanup..'
                docker stop localtest
                docker rm localtest
                '''
            }
        }

        stage('Login_Docker'){
            environment{
                DOCKER_HUB = credentials('DOCKER_HUB')
            }
            steps {
                echo 'Login....'
                sh '''
                    echo ${DOCKER_HUB_PSW} | docker login -u ${DOCKER_HUB_USR} --password-stdin
                '''
            }
        }

        stage('Push') {
            steps {
                echo 'Deploying....'
                sh '''
                docker build . -t ${DOCKER_USERNAME}/${DOCKERHUB_REPO}:latest
                docker push ${DOCKER_USERNAME}/${DOCKERHUB_REPO}:latest
                '''
            }
        }

        //  stage('Build') {
        //     steps {
        //         echo 'Build....'
        //         sh '''
        //         docker pull ${DOCKER_USERNAME}/${DOCKERHUB_REPO}:latest
        //         kind load docker-image ${DOCKER_USERNAME}/${DOCKERHUB_REPO}:latest
        //         '''
        //     }
        // }
        // stage('Deploy'){
        //     steps{
        //         echo 'Deploy...'
        //         sh'''
        //         helm upgrade --install track-processing chart/ \
        //         --set image.repository=${DOCKER_USERNAME}/${DOCKERHUB_REPO} \
        //         --set image.tag=latest
        //         '''
        //     }
        // }
        stage('Monitor'){
            steps{
                echo 'Monitor...'
                sh'''
                    chmod +x prometheus.sh
                '''
            }
        }
        // stage('Debug') {
        //     steps{
        //         echo 'Debug...'
        //         sh'''
        //         sleep 5
        //         kubectl get deployment track-processing
        //         kubectl get service track-processing
        //         '''
        //     }
        // }
        // stage('Test_Helm') {
        //     steps{
        //         echo 'Tesing...'
        //         sh'''
        //         kubectl port-forward svc/track-processing 8000:80 & PORT_FORWARD_PID=$!
        //         sleep 10
        //         curl -f http://localhost:8000/health
        //         kill $PORT_FORWARD_PID
        //         '''
        //     }
        // }
     
    }

    post {
            always {
                script{
                    try {
                        sh '''
                        docker logout
                        '''
                    } catch (err) {
                        echo 'Docker login has been skipped'
                    }
                       
                }
            
            }
        }
}