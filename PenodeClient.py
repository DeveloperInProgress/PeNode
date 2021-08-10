import docker 
import json 

class PenodeClient:
    def __init__(self):
        self.dockerClient = docker.from_env()
        self.dockerLowClient = docker.APIClient(base_url='unix://var/run/docker.sock')
            
    def pullImage(self,imageName):
        #params format: dict with keys [image]
        return self.dockerClient.images.pull(imageName)

    def runContainer(self,imageName,name,containerPort):
        #params format: dict with keys [image,containerPort,,protocol,name]
        container = self.dockerClient.containers.run(
            imageName,
            name=name,
            ports={
                str(containerPort)+'/tcp':None 
            },
            detach = True
        )
        return container 

    def portBindings(self,containerName):
        #params format: dict with keys [name]
        container = self.dockerClient.containers.get(containerName)
        #return self.dockerLowClient.inspect_container(container.get('id'))['NetworkSettings']['Ports']
        return container.ports

    def forceStop(self,containerName):
        #params format: dict with keys [name]
        container = self.dockerClient.containers.get(containerName)
        return self.dockerLowClient.stop(container=container.id) 

    def startContainer(self,containerName):
        #params format: dict with keys [name]
        container = self.dockerClient.containers.get(containerName)
        return self.dockerLowClient.start(container=container.id) 

    def streamStats(self):
        for c in self.dockerClient.containers.list():
            yield self.dockerLowClient.stats(c.id)