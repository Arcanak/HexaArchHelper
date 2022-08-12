import os

curPath = os.curdir
def create_hexa_arch(name: str, path: str):
    folder = path + "/" + name
    os.mkdir(folder)
    os.mkdir(folder + "/application/")
    os.mkdir(folder + "/domain/")
    os.mkdir(folder + "/application/ports/")
    os.mkdir(folder + "/infraestructure/")
    os.mkdir(folder + "/infraestructure/adapters/")
    os.mkdir(folder + "/infraestructure/adapters/input/")
    os.mkdir(folder + "/infraestructure/adapters/output/")
    os.mkdir(folder + "/infraestructure/adapters/input/rest/")
    os.mkdir(folder + "/infraestructure/adapters/output/customizedException/")
    os.mkdir(folder + "/infraestructure/adapters/output/customizedException/data/")
    os.mkdir(folder + "/infraestructure/adapters/output/persistence/")
    os.mkdir(folder + "/application/ports/input")
    os.mkdir(folder + "/application/ports/output")
    os.mkdir(folder + "/infraestructure/adapters/config")
    os.mkdir(folder + "/infraestructure/adapters/input/eventListener")
    os.mkdir(folder + "/infraestructure/adapters/input/rest/data")
    os.mkdir(folder + "/infraestructure/adapters/input/rest/mapper")
    os.mkdir(folder + "/infraestructure/adapters/output/customizedException/data/response")
    os.mkdir(folder + "/infraestructure/adapters/output/eventPublisher")
    os.mkdir(folder + "/infraestructure/adapters/output/persistence/entity")
    os.mkdir(folder + "/infraestructure/adapters/output/persistence/mapper")
    os.mkdir(folder + "/infraestructure/adapters/output/persistence/repository")
    os.mkdir(folder + "/domain/event")
    os.mkdir(folder + "/domain/exception")
    os.mkdir(folder + "/domain/model")
    os.mkdir(folder + "/domain/service")


def main():
    path = "C:\\Users\\Bryan\\Desktop\\Proyectos\\Ecovinal\\erp-back\\src\\main\\java\\com\\ecovinal\\erp\\bundles\\silicie\\bundles"
    print("Insert the name of the folder:")
    name = input()
    create_hexa_arch(name, path)

if __name__ == '__main__':
    main()
