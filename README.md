# Scapy Network Scripts

A collection of customized network sniffers built with Python's **Scapy** library, along with demonstrations of network attacks using **Mininet**. Ideal for learning packet manipulation, traffic analysis, and simulated attacks in a controlled environment.

## Overview
This repository includes:
- **Custom Network Sniffers**: Capture and analyze network packets using Scapy.
- **Attack Simulations**: Execute network attacks to understand vulnerabilities in a safe environment.

## Features
- **Network Sniffing**: Build customized sniffers to capture and analyze traffic.
- **Simulated Attacks**: Perform attacks like Man-in-the-Middle (MITM) and session hijacking.
- **Custom Topology**: Includes `hub_topo.py` to create a hub-and-spoke Mininet topology, ideal for centralized traffic analysis and interception.

## Prerequisites
- Python 3.x
- Scapy library
- Mininet (for network simulation)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/medTrigui/Scapy-Scripts.git
   cd Scapy-Scripts
2. Install dependencies:
   ```bash
   pip install scapy

## Folder Structure
Each attack simulation is organized into its own folder with relevant scripts and descriptions:

```plaintext
Scapy-Scripts/
├── hub_topo.py               # Mininet topology setup (hub-and-spoke model)
├── sniff_and_spoof/          # Folder for sniffing and spoofing scripts
│   └── sniff_and_spoof.py    # Script demonstrating sniffing and basic spoofing techniques
├── mitm_attack/              # Folder for MITM attack simulation
│   └── mitm_attack.py        # Script for executing a Man-in-the-Middle attack
├── session_hijacking/        # Folder for session hijacking simulation
│   └── session_hijacking.py  # Script for simulating session hijacking
└── README.md                 # Repository documentation
```


## Disclaimer
These scripts are for educational purposes only. Use them in a controlled environment to avoid legal or ethical issues.
