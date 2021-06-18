
# G-Aut :sparkles:

G-Aut is a mail automation service for Gmail built on python :heart:.
## Badges

![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg) ![GNU GPL 3.0](https://img.shields.io/github/license/kanitmann/Mail_Automation) [![Stars](https://img.shields.io/github/stars/kanitmann/Mail_Automation)](https://github.com/kanitmann/Mail_Automation/stargazers) [![Issues](https://img.shields.io/github/issues/kanitmann/Mail_Automation)](https://github.com/kanitmann/Mail_Automation/issues) ![Tweet](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fkanitmann%2FMail_Automation%2F)
## Features

- Support CSV Mailing
- Send multiple mails in one-click
- Zero latency
- Supports Personalised Mails
## Tech Stack

**Language:** Python

**Libraries Used:** 
- OS
- argparse
## Installation 

1. Clone the current repository and install the ssmpt package

```bash 
  git clone https://github.com/kanitmann/Mail_Automation.git
  sudo apt install ssmtp
  nano /etc/ssmtp/ssmtp.conf
```
2. configure the package with your credentials (enter the following credentials in the ssmtp.conf file)
```
   mailhub=smtp.gmail.com:587
 UseSTARTTLS=YES
 AuthUser=your-email@gmail.com
 AuthPass=XXXXXXXXXXXXXXX
 TLS_CA_File=/etc/pki/tls/certs/ca-bundle.crt
  ```
3. Enable insecure apps in your google account settings (you might have to set up app passwords if you have 2 factor authentication)
4. Run the script
```bash
python commandline.py -r <file containing reciever Email IDs (separated by newline)> -f <file containing the email>
```

## Usage/Examples

- Edit "file.csv" and make required modifications. Further guide to handling the CSV file will be added soon.

- Change line 11 & line 12 to your Gmail Email and password.

- Run Main.py using:

```bash 
python3 Main.py
```
## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

  
## Authors

- [@kanitmann](https://www.github.com/kanitmann)

- [@Viny1ic](https://www.github.com/viny1ic)

  