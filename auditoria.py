#!/usr/bin/env python3
"""
Network Auditor
Ferramenta de mapeamento de rede, detecção de ARP Spoofing (MitM)
e varredura rápida de portas com Nmap.
"""

import subprocess
import sys
from scapy.all import srp, Ether, ARP


def scan_network(ip_range: str) -> list:
    """
    Realiza varredura ARP na sub-rede informada.
    Retorna lista de dispositivos encontrados (IP + MAC).
    Também detecta possível ARP Spoofing (mesmo MAC respondendo por múltiplos IPs).
    """
    print(f"\n[*] Mapeando a rede {ip_range}")

    # Cria requisição ARP para todos os IPs da sub-rede
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Envia a requisição e recebe as respostas
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    clients = []
    mac_addresses = {}
    mitm_detected = False

    for element in answered_list:
        ip = element[1].psrc
        mac = element[1].hwsrc
        clients.append({"ip": ip, "mac": mac})

        # Assinatura clássica de MitM: múltiplos IPs apontando para o mesmo MAC
        if mac in mac_addresses:
            print(f"[!] ALERTA CRÍTICO: Possível ARP Spoofing (MitM) detectado!")
            print(f"    O MAC {mac} está sendo usado pelos IPs {mac_addresses[mac]} e {ip}")
            mitm_detected = True
        else:
            mac_addresses[mac] = ip

    if not mitm_detected:
        print("[+] Nenhum indício de ARP Spoofing detectado.")

    return clients


def scan_vulnerabilities(ip: str) -> None:
    """Executa Nmap em modo rápido (-F) no host informado."""
    print(f"\n[*] Executando Nmap rápido em {ip} (Top 100 portas)...")
    try:
        result = subprocess.run(
            ["nmap", "-F", ip],
            capture_output=True,
            text=True,
            timeout=30
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except subprocess.TimeoutExpired:
        print(f"[-] Timeout ao escanear {ip}")
    except FileNotFoundError:
        print("[-] Nmap não encontrado. Instale com: sudo apt install nmap")
    except Exception as e:
        print(f"[-] Erro ao escanear {ip}: {e}")


def main():
    # Altere aqui para o range da sua rede
    ALVO = "192.168.100.0/24"

    if len(sys.argv) > 1:
        ALVO = sys.argv[1]

    print("=" * 55)
    print("       NETWORK AUDITOR - Auditoria de Rede Local")
    print("=" * 55)

    dispositivos = scan_network(ALVO)

    print("\n[*] Dispositivos encontrados na rede:")
    if not dispositivos:
        print("    Nenhum dispositivo respondeu ao ARP.")
    else:
        for node in dispositivos:
            print(f"    IP: {node['ip']:<16}  MAC: {node['mac']}")

    print("\n[*] Iniciando varredura de portas (Pressione Ctrl+C para pular)...")
    try:
        for node in dispositivos:
            scan_vulnerabilities(node["ip"])
    except KeyboardInterrupt:
        print("\n[!] Varredura de vulnerabilidades interrompida pelo usuário.")

    print("\n[+] Auditoria finalizada.")


if __name__ == "__main__":
    main()
