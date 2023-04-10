# WifiQRTool

This app generates a wifi logon qr code for mobile devices, can be used to share wifi passwords easily

## Installation

- requires `python` (3.0 >)
- requires `pip`

```bash
python -m pip install -r requirements.txt
```

## Usage

```bash
python gen.py
```

## Output

### In TERMINAL:

```bash
User name : <SSID>
Password : <Password>
    █▀▀▀▀▀█  █▄▀ ███▄ ▀▀█ █▀▀▀▀▀█    
    █ ███ █ ██ █ ▀▄█ ▄▀   █ ███ █    
    █ ▀▀▀ █ ██▄ █  ▀▀▄▄▀█ █ ▀▀▀ █    
    ▀▀▀▀▀▀▀ █ █▄█ █ █ ▀▄█ ▀▀▀▀▀▀▀    
    █ █▀██▀ ▄█▄▀ ▄▄▄ █▀ ▄ █▀█▀█▄     
    █  ▀▄█▀▄ ▀  ██▀▀▀▀▀▄ ██▀▄▀ ▄▄    
     ▀█▀ █▀ ▄ ▀██ ▀ ▀▄▄█▀▄ ██▀█▄     
    ▄▄▄▀ █▀▄█ ▄█▄ ▄▀▀ █  ██▀ ▄▀      
    █▄█▄█▄▀▄▄▄▀▀█▄▄ ▀█▀ █▄▄▀▄█ █▀    
    █  ▄▄▄▀▀▄▄▄█▀█▀██▀█▄▀▀ ▀█   ▄    
    ▀ ▀▀ ▀▀▀█ ▄▀█ ▀▀▄▀▄██▀▀▀█▀█      
    █▀▀▀▀▀█ ▄█▄██ ▄▀▀▀▄▀█ ▀ █▄▀▄▄    
    █ ███ █ ██▀▀▀ ▄▀█▀▄▄▀▀▀▀██ █▄    
    █ ▀▀▀ █ ▀ ▄▀▀█▄█▄ ▀▀▄██▀██▀█     
    ▀▀▀▀▀▀▀ ▀ ▀▀▀ ▀  ▀ ▀  ▀ ▀▀    
```

### In File System

- a png named after the SSID containing only the QR Code