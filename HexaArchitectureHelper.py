import os
import file_maker.file_maker as fm

curPath = os.curdir
def create_hexa_arch(name: str, path: str):
    folder = path + "/" + name
    os.mkdir(folder)
    os.mkdir(folder + "/application/")
    os.mkdir(folder + "/infrastructure/")
    os.mkdir(folder + "/domain/")

    os.mkdir(folder + "/application/ports/")
    os.mkdir(folder + "/application/ports/input")
    os.mkdir(folder + "/application/ports/output")

    os.mkdir(folder + "/infrastructure/adapters/")

    os.mkdir(folder + "/infrastructure/adapters/input/")
    os.mkdir(folder + "/infrastructure/adapters/config")
    os.mkdir(folder + "/infrastructure/adapters/output/")   

    os.mkdir(folder + "/infrastructure/adapters/input/rest/")
    os.mkdir(folder + "/infrastructure/adapters/input/eventListener")

    os.mkdir(folder + "/infrastructure/adapters/input/rest/data")
    os.mkdir(folder + "/infrastructure/adapters/input/rest/mapper")

    os.mkdir(folder + "/infrastructure/adapters/input/rest/data/request")
    os.mkdir(folder + "/infrastructure/adapters/input/rest/data/response")
     
    os.mkdir(folder + "/infrastructure/adapters/output/customizedException/")    
    os.mkdir(folder + "/infrastructure/adapters/output/persistence/")   
    os.mkdir(folder + "/infrastructure/adapters/output/eventPublisher/")

    os.mkdir(folder + "/infrastructure/adapters/output/customizedException/data/")

    os.mkdir(folder + "/infrastructure/adapters/output/persistence/dto")
    os.mkdir(folder + "/infrastructure/adapters/output/persistence/mapper")
    os.mkdir(folder + "/infrastructure/adapters/output/persistence/repository")    
    
    os.mkdir(folder + "/infrastructure/adapters/output/customizedException/data/response")    
    
    os.mkdir(folder + "/domain/event")
    os.mkdir(folder + "/domain/exception")
    os.mkdir(folder + "/domain/model")
    os.mkdir(folder + "/domain/service")


def main():
    path = "/home/bryan/Escritorio/Proyectos/Ecovinal/erp-back/src/main/java/com/ecovinal/erp/bundles/silicie/bundles"
    print("Insert the name of the folder:")
    name = input()
    create_hexa_arch(name, path)
    # Make files
    new_path = path + "/" + name
    fm.make_app_ports(name, new_path)
    fm.make_domain(name, new_path)
    fm.make_infrastructure(name, new_path)

if __name__ == '__main__':
    main()
