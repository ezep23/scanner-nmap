import nmap

def escanear_puertos(ip):
    # Creamos un objeto de escáner de nmap
    escaner = nmap.PortScanner()
    # Ejecutamos un escaneo de puertos en la IP especificada, en los puertos comúnmente utilizados
    escaner.scan(ip, '1-1024')
    
    # Iteramos sobre los resultados del escaneo
    for host in escaner.all_hosts():
        print(f"Host : {host} ({escaner[host].hostname()})")
        print("Estado del host: %s" % escaner[host].state())
        # Iteramos sobre los puertos escaneados
        for puerto in escaner[host]['tcp'].keys():
            print(f"Puerto {puerto}: {escaner[host]['tcp'][puerto]['state']}")

# Solicitamos al usuario que ingrese la dirección IP a escanear
ip = input("Ingrese la dirección IP a escanear: ")

# Llamamos a la función para escanear los puertos
escanear_puertos(ip)
