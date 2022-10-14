pipeline {
  agent any
  stages {
    stage('Ongoing') {
      parallel {
        stage('msg1') {
          steps {
            sh 'echo "Launchin the script....."'
          }
        }

        stage('msg2') {
          steps {
            sh 'echo "A script is ongoing"'
          }
        }

      }
    }

    stage('virtualenv') {
      steps {
        sh 'python3 -m venv .venv'
        sh '''#!/bin/bash
              source .venv/bin/activate 
         '''
      }
    } 
    
    stage('Dependencies') {
      steps {
         sh '''#!/bin/bash
              source .venv/bin/activate 
              pip install -r requirements.txt 
         '''
      }
    }

    stage('Plan Testing') {
      parallel {
        stage('Setup Plan') {
          steps {
            sh '''#!/bin/bash
                  source .venv/bin/activate 
                  pytest --setup-plan --disable-warnings
            '''
          }
        }

        stage('Collect Tests') {
          steps {
            sh '''#!/bin/bash
                  source .venv/bin/activate 
                  pytest --disable-warnings --collect-only
            '''
          }
        }

      }
    }

    stage('Test') {
      steps {
         sh '''#!/bin/bash
              source .venv/bin/activate 
              pytest --disable-warnings -v
         '''
      }
    }    
    
    stage('Deploy') {
        steps {
            script {
                def USER_INPUT = input(
                        message: 'Please choose environment',
                        parameters: [
                                [$class: 'ChoiceParameterDefinition',
                                choices: ['QA','Prod'].join('\n'),
                                name: 'env',
                                description: 'Menu - select box option']
                        ])

                echo "The Choice is: ${USER_INPUT}"

                if( "${USER_INPUT}" == "QA"){
                    echo 'Deploying on the QA server'
                    // sshagent(credentials:['ssh_key']){
                    //               sh '''ssh  -o StrictHostKeyChecking=no  ubuntu@192.168.64.103 << EOF
                    //                     date
                    //                     hostname
                    //                     touch qa.txt
                    //                     EOF
                    //                  '''
                    //           }
                } else {
                    echo 'Deploying on the Prod server'
                //     sshagent(credentials:['ssh_key']){
                //                   sh '''ssh  -o StrictHostKeyChecking=no  ubuntu@192.168.64.102 << EOF
                //                         date
                //                         hostname
                //                         touch prod.txt
                //                         EOF
                //                      '''
                // }
            }
        }
    }

    stage('Closing') {
      steps {
        sh 'echo "ending the script"'
      }
    }

  }
}