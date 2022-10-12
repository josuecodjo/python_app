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

    stage('Plan test') {
      steps {
         sh '''#!/bin/bash
              source .venv/bin/activate 
              pytest --setup-plan
         '''
      }
    }

    stage('Test') {
      steps {
         sh '''#!/bin/bash
              source .venv/bin/activate 
              pytest
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
                } else {
                    echo 'Deploying on the Prod server'
                }
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
