import socket

def escanear_puertos_abiertos(ip, timeout=5):
    """
    Este escaner solo te va a mostrar los puertos abiertos de la ip.
    """
    print(f"Escaneando puertos abiertos en {ip}...")
    for puerto in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        try:
            result = sock.connect_ex((ip, puerto))
            if result == 0:
                print(f"Puerto abierto: {puerto}")
        except socket.error as e:
            print(f"Error al escanear el puerto {puerto}: {e}")
        finally:
            sock.close()

if __name__ == "__main__":
    ip = input("Ingresa la dirección IP a escanear: ")
    escanear_puertos_abiertos(ip)
