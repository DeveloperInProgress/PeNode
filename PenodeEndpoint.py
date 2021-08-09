from Penode import Penode
import argparse

def downloadImage(args):
    output = client.pullImage(args.imageName)
    return responseGenerator('download', output)

def runImage(args):
    output = client.runContainer(
        args.i,
        args.n,
        args.p
    )
    return responseGenerator('run',output)

def getPort(args):
    output = client.portBindings(args.n)
    return responseGenerator('port',output)

def startContainer(args):
    output = client.startContainer(args.n)
    return responseGenerator('start',output)

def stopContainer(args):
    output = client.forceStop(args.n)
    return responseGenerator('stop',output)

def streamStats():
    #todo: stream resource usage stats for all containers
    return "coming soon"
    
def responseGenerator(task, output):
    response = {}
    if task=='download':
        #output is the Image pulled
        response['data'] = output.id 
        response['message'] = 'Download complete!'
        response['error'] = None
    elif task=='run':
        #output is the Container running
        response['data'] = output.id
        response['message'] = 'Container running succesfully!'
        response['error'] = None 
    elif task=='port':
        #output is the port attached to the container
        response['data'] = output
        response['message'] = 'Port retrieved succesfully!'
        response['error'] = None 
    elif task=='start':
        response['data'] = None
        response['message'] = 'Container started succesfully!'
        response['error'] = None 
    elif task=='stop':
        response['data'] = None
        response['message'] = 'Container stopped succesfully!'
        response['error'] = None
    elif task=='stats':
        pass
    print(response)


client = Penode()
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

parser_download = subparser.add_parser('download')
parser_download.add_argument('imageName', required=True, help='Name of the image to be downloaded')
parser_download.set_defaults(func=downloadImage)

parser_run = subparser.add_parser('run')
parser_run.add_argument('-i',required=True,help='Name of the image to run')
parser_run.add_argument('-n',required=True,help='Name to be given to container')
parser_run.add_argument('-p',required=True,type=int,help='Container port to be exposed')
parser_run.set_defaults(func=runImage)

parser_port = subparser.add_parser('port')
parser_port.add_argument('-n',required=True,help='Name of the container')
parser_port.set_defaults(func=getPort)

parser_start = subparser.add_parser('start')
parser_start.add_argument('-n',required=True,help='Name of the container')
parser_start.set_defaults(func=startContainer)

parser_stop = subparser.add_parser('stop')
parser_stop.add_argument('-n',required=True,help='Name of the container')
parser_stop.set_defaults(func=stopContainer)

