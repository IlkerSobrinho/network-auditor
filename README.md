# 🔍 Network Auditor

Ferramenta em Python para **mapeamento de redes locais**, detecção de possíveis ataques de **ARP Spoofing (Man-in-the-Middle)** e varredura rápida de portas com Nmap.

Desenvolvida com foco em laboratórios de redes, análise de telemetria e identificação de vulnerabilidades em ambientes controlados.

---

## ✨ Funcionalidades

- **Mapeamento de rede via ARP**  
  Descobre todos os dispositivos ativos na sub-rede (IP + MAC Address).

- **Detecção de ARP Spoofing / MitM**  
  Identifica quando um mesmo MAC address responde por múltiplos IPs (assinatura clássica de ataque Man-in-the-Middle).

- **Varredura de portas com Nmap**  
  Executa scan rápido (`nmap -F`) nas top 100 portas de cada host encontrado.

- **Interrupção segura**  
  Suporte a `Ctrl+C` durante a fase de varredura de vulnerabilidades.

- **Argumento via linha de comando**  
  Permite informar o range da rede diretamente na execução.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Uso |
|------------|-----|
| **Python 3** | Linguagem principal |
| **Scapy** | Envio e captura de pacotes ARP |
| **Nmap** | Varredura de portas |
| **subprocess** | Integração com ferramentas do sistema |

---

## 📋 Pré-requisitos

```bash
# Instalar o Nmap (Ubuntu/Debian)
sudo apt update && sudo apt install nmap

# Instalar o Scapy
pip install scapy
```

> ⚠️ O script precisa ser executado com privilégios de **root/administrador** para conseguir enviar pacotes ARP.

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/IlkerSobrinho/network-auditor.git
cd network-auditor
```

### 2. Execute o script

```bash
# Usando o range padrão (edite dentro do código se preferir)
sudo python3 auditoria.py

# Ou passando o range da sua rede como argumento
sudo python3 auditoria.py 192.168.1.0/24
```

---

## 📸 Exemplo de saída

```
=======================================================
       NETWORK AUDITOR - Auditoria de Rede Local
=======================================================

[*] Mapeando a rede 192.168.100.0/24
[+] Nenhum indício de ARP Spoofing detectado.

[*] Dispositivos encontrados na rede:
    IP: 192.168.100.1      MAC: aa:bb:cc:dd:ee:ff
    IP: 192.168.100.15     MAC: 11:22:33:44:55:66

[*] Iniciando varredura de portas (Pressione Ctrl+C para pular)...

[*] Executando Nmap rápido em 192.168.100.1 (Top 100 portas)...
Starting Nmap ...
...
```

---

## ⚠️ Aviso Legal

Esta ferramenta foi desenvolvida **exclusivamente para fins educacionais e de laboratório**.  
Utilize apenas em redes que você possui ou tem autorização explícita para auditar.

O uso indevido desta ferramenta pode ser ilegal.

---

## 📁 Estrutura do projeto

```
network-auditor/
├── auditoria.py      # Script principal
└── README.md
```

---

## 🧠 Aprendizados aplicados

- Manipulação de pacotes de rede com Scapy
- Detecção de anomalias de ARP (técnica clássica de MitM)
- Automação de varreduras com Nmap via Python
- Boas práticas de scripts de diagnóstico de rede

---

## 👤 Autor

**Ilker Berg da Silva Sobrinho**  

[LinkedIn](https://www.linkedin.com/) · [GitHub](https://github.com/IlkerSobrinho)
```
