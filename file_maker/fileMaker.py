from string import Template
import os

def make_app_ports(name: str, path: str):
    useCase = {
        'interfaceName': 'I' + name + 'UseCase'
    }
    outputPort = {
        'interfaceName': 'I' + name + 'OutputPort'
    }
    eventPublisher = {
        'eventPublisherName': 'I' + name + 'EventPublisher'
    }

    with open('file_maker\\templates\\InterfaceTemplate.java', 'r') as f:
        i = Template(f.read())
        useCaseF = os.open(path + '\\application\\ports\\input\\' + useCase['interfaceName'] + '.java', os.O_CREAT | os.O_WRONLY)
        useCaseF.write(i.substitute(useCase))
        outputPortF = os.open(path + '\\application\\ports\\output\\' + outputPort['interfaceName'] + '.java', os.O_CREAT | os.O_WRONLY)
        outputPortF.write(i.substitute(outputPort))
        os.close(useCaseF)
        os.close(outputPortF)
    
    with open('file_maker\\templates\\EventPublisherAdapter.java', 'r') as f:
        i = Template(f.read())
        eventPublisherF = os.open(path + '\\application\\ports\\output\\' + eventPublisher['eventPublisherName'] + '.java', os.O_CREAT | os.O_WRONLY)
        eventPublisherF.write(i.substitute(useCase))
        os.close(eventPublisherF)

