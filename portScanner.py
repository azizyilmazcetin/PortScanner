import socket
from concurrent.futures import ThreadPoolExecutor

#Kullanıcıdan IP adresi,port aralığı ve protokol tipi al
target_ip=input("Enter target IP address:")
start_port=int(input("Enter start port:"))
end_port=int(input("Enter end port:"))
protocol=input("Enter protocol (TCP/UDP):  ").upper()

#Sonuçları dosyaya yazdır
output_file="scan_results.txt"
with open(output_file,"w") as file:
    file.write(f"Scan results for {target_ip} from port {start_port} to {end_port} using {protocol}: \n\n")

#TCP protokolü ile tarama fonksiyonu
def scan_tcp_port(port):
    try:

        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result=sock.connect_ex((target_ip,port))
        if result==0:
            result_str=f"TCP Port {port} is open\n"
            print(result_str,end="")
            with open(output_file, "a")as file:
                file.write(result_str)
        sock.close()
    except Exception as e:
        print(f"Error scanning TCP port {port}: {e}")

#UDP Protokolü ile tarama fonksiyonu
def scan_udp_port(port):
    try:

        sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.sendto(b'',(target_ip,port))
        try:
            data,_=sock.recvfrom(1024)
            result_str=f"UDP Port {port} is open\n"
            print(result_str,end="")
            with open(output_file, "a") as file:
                file.write(result_str)
        except socket.timeout:
            pass
        except socket.error as err:
            if err.errno==10054:
                pass
        sock.close()
    except Exception as e:
        print(f"Error scanning UDP port {port}: {e}")

#Tüm portları tarama
with ThreadPoolExecutor(max_workers=100) as executor:
    if protocol=="TCP":
        for port in range(start_port,end_port+1):
            executor.submit(scan_tcp_port,port)
    elif protocol=="UDP":
        for port in range(start_port,end_port+1):
            executor.submit(scan_udp_port,port)
    else:
        print("Invalid protocol specified. Please enter TCP or UDP.")