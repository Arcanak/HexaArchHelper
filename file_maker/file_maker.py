from string import Template
import os

def make_app_ports(name: str, path: str):
    '''Generate application ports'''
    capName = name.capitalize()
    useCase = {
        'interfaceName': 'I' + capName + 'UseCase'
    }
    outputPort = {
        'interfaceName': 'I' + capName + 'OutputPort'
    }
    eventPublisher = {
        'interfaceName': 'I' + capName + 'EventPublisher'
    }
    # Use case and output interface
    with open('file_maker/templates/InterfaceTemplate.java', 'r') as f:
        i = Template(f.read())
        useCaseF = os.open(path + '/application/ports/input/' + useCase['interfaceName'] + '.java', os.O_CREAT | os.O_WRONLY)
        outputPortF = os.open(path + '/application/ports/output/' + outputPort['interfaceName'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(useCaseF, bytes(i.substitute(useCase), 'utf-8'))
        os.write(outputPortF, bytes(i.substitute(outputPort), 'utf-8'))
        os.close(useCaseF)
        os.close(outputPortF)
    
    # Event publisher interface
    with open('file_maker/templates/InterfaceTemplate.java', 'r') as f:
        i = Template(f.read())
        eventPublisherF = os.open(path + '/application/ports/output/' + eventPublisher['interfaceName'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(eventPublisherF, bytes(i.substitute(eventPublisher), 'utf-8'))
        os.close(eventPublisherF)
    

def make_infrastructure(name: str, path: str):
    '''Generate infrastructure files'''
    capName = name.capitalize()
    # INPUT
    eventListener = {
        'eventListenerName': capName + 'EventListenerAdapter',
        'event': capName + 'Event'
    }
    request =  {
        'className': capName + 'Request'
    }

    response = {
        'className': capName + 'Response'
    }

    mapper = {
        'modelMapper': 'I' + capName + 'RestMapper'
    }

    rest = {
        'modelRestAdapter': capName + 'RestAdapter'
    }
    
    # Bean configuration
    with open('file_maker/templates/BeanConfigTemplate.java') as f:
        i = Template(f.read())
        beanConfig = os.open(path + '/infrastructure/adapters/config/BeanConfig.java', os.O_CREAT | os.O_WRONLY)
        os.write(beanConfig, bytes(i.substitute(), 'utf-8'))
        os.close(beanConfig)
    
    # Event listener adapter 
    with open('file_maker/templates/EventListenerTemplate.java') as f:
        i = Template(f.read())
        eventListenerF = os.open(path + '/infrastructure/adapters/input/eventListener/' + eventListener['eventListenerName'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(eventListenerF, bytes(i.substitute(eventListener), 'utf-8'))
        os.close(eventListenerF)
    
    # Requests
    with open('file_maker/templates/ClassTemplate.java') as f:
        i = Template(f.read())
        requestF = os.open(path + '/infrastructure/adapters/input/rest/data/request/' + request['className'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(requestF, bytes(i.substitute(request), 'utf-8'))
        os.close(requestF)
    
    # Responses
    with open('file_maker/templates/ClassTemplate.java') as f:
        i = Template(f.read())
        responseF = os.open(path + '/infrastructure/adapters/input/rest/data/response/' + response['className'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(responseF, bytes(i.substitute(response), 'utf-8'))
        os.close(responseF)

    # Rest mapper
    with open('file_maker/templates/MapperTemplate.java') as f:
        i = Template(f.read())
        mapperF = os.open(path + '/infrastructure/adapters/input/rest/mapper/' + mapper['modelMapper'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(mapperF, bytes(i.substitute(mapper), 'utf-8'))
        os.close(mapperF)

    # Rest adapter
    with open('file_maker/templates/RestAdapterTemplate.java') as f:
        i = Template(f.read())
        restF = os.open(path + '/infrastructure/adapters/input/rest/' + rest['modelRestAdapter'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(restF, bytes(i.substitute(rest), 'utf-8'))
        os.close(restF)
    
    # OUTPUT
    eventPublisher = {
        'eventPublisherName': capName + 'EventPublisherAdapter'
    }

    dto = {
        'className': capName + 'Dto'
    }

    mapperO = {
        'modelMapper': 'I' + capName + 'PersistenceMapper'
    }

    # Event publisher adapter
    with open('file_maker/templates/EventPublisherAdapterTemplate.java') as f:
        i = Template(f.read())
        eventPublisherF = os.open(path + '/infrastructure/adapters/output/eventPublisher/' + eventPublisher['eventPublisherName'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(eventPublisherF, bytes(i.substitute(eventPublisher), 'utf-8'))
        os.close(eventPublisherF)

    # DTO
    with open('file_maker/templates/ClassTemplate.java') as f:
        i = Template(f.read())
        dtoF = os.open(path + '/infrastructure/adapters/output/persistence/dto/' + dto['className'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(dtoF, bytes(i.substitute(dto), 'utf-8'))
        os.close(dtoF)

    # Persistence mapper
    with open('file_maker/templates/MapperTemplate.java') as f:
        i = Template(f.read())
        mapperOF = os.open(path + '/infrastructure/adapters/output/persistence/mapper/' + mapperO['modelMapper'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(mapperOF, bytes(i.substitute(mapperO), 'utf-8'))
        os.close(mapperOF)

def make_domain(name: str, path: str):
    '''Generate domain files'''
    capName = name.capitalize()
    
    event = {
        'className': capName + 'Event'
    }
    
    model = {
        'className': capName + 'Dto'
    }

    service = {
        'serviceName': capName + 'Service'
    }

    exception = {
        'exceptionName': capName + 'Exception'
    }
    
    # Domain events
    with open('file_maker/templates/ClassTemplate.java') as f:
        i = Template(f.read())
        eventF = os.open(path + '/domain/event/' + event['className'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(eventF, bytes(i.substitute(event), 'utf-8'))
        os.close(eventF)
    
    # Model
    with open('file_maker/templates/ClassTemplate.java') as f:
        i = Template(f.read())
        dtoF = os.open(path + '/domain/model/' + model['className'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(dtoF, bytes(i.substitute(model), 'utf-8'))
        os.close(dtoF)
    
    # Service
    with open('file_maker/templates/ServiceTemplate.java') as f:
        i = Template(f.read())
        serviceF = os.open(path + '/domain/service/' + service['serviceName'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(serviceF, bytes(i.substitute(service), 'utf-8'))
        os.close(serviceF)
    
    # Exception
    with open('file_maker/templates/ExceptionTemplate.java') as f:
        i = Template(f.read())
        exceptionF = os.open(path + '/domain/exception/' + exception['exceptionName'] + '.java', os.O_CREAT | os.O_WRONLY)
        os.write(exceptionF, bytes(i.substitute(exception), 'utf-8'))
        os.close(exceptionF)



        
        