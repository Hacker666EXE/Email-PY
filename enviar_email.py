import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Parágrafo1</p>
    <p>test python</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'SEU EMAIL FICA AQUI' 
    password = 'SUA SENHA FICA AQUI' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    # Arte ASCII para banner
    banner = """
  
+--------------------------------------------------------------+
|                                                              |
| ███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░  ██████╗░██╗░░░██╗    |
| ██╔════╝████╗░████║██╔══██╗██║██║░░░░░  ██╔══██╗╚██╗░██╔╝    |
| █████╗░░██╔████╔██║███████║██║██║░░░░░  ██████╔╝░╚████╔╝░    |
| ██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░  ██╔═══╝░░░╚██╔╝░░    |
| ███████╗██║░╚═╝░██║██║░░██║██║███████╗  ██║░░░░░░░░██║░░░    |
| ╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ╚═╝░░░░░░░░╚═╝░░░    |
|                         by: zBLACKHAT                        |
|                                                              |
+--------------------------------------------------------------+
    """

    print(banner)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)

    # Lendo os destinatários do arquivo email.txt
    with open('email.txt', 'r') as file:
        recipients = file.read().splitlines()

    try:
        num_emails = len(recipients)
        print(f"Quantidade de emails para enviar: {num_emails}")
    except ValueError:
        print("Erro ao contar os emails.")
        return

    try:
        num_envios = int(input("Quantas vezes deseja enviar o email para cada destinatário? "))
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    for to_email in recipients:
        for _ in range(num_envios):
            # Cria um novo objeto Message para cada email
            msg_individual = email.message.Message()
            msg_individual.add_header('Content-Type', 'text/html')
            msg_individual.set_payload(corpo_email)
            msg_individual['Subject'] = msg['Subject']
            msg_individual['From'] = msg['From']
            msg_individual['To'] = to_email

            s.sendmail(msg['From'], to_email, msg_individual.as_string().encode('utf-8'))
            print(f'Email enviado para {to_email}')

    s.quit()

if __name__ == "__main__":
    enviar_email()