pipeline{
        agent any
        
        stages{ 
                stage('---Update Images---'){
                        steps{
                                sh '''export build="${BUILD_NUMBER}"
				      docker system prune -af
				      docker-compose up -d --build
				      docker-compose down --volumes
				      docker-compose push
                                      '''
                        }
                }
                stage('---Update Containers---'){
                        steps{
                                sh '''ssh assassin-ansible-deploy << EOF
				      export build="${BUILD_NUMBER}"
				      docker system prune -f
				      docker stack deploy --compose-file assassin-app/docker-compose.yaml assassin
				      EOF
                                      '''
                        }
                }
	}
}
