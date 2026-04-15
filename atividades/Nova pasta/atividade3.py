from datetime import datetime

def gerar_log():
    input("Pressione Enter para gerar o log...")
    data = datetime.now()
    print(f"[{datetime.now():%d/%m/%Y %H:%M}] Atendimento registrado com sucesso")
    
gerar_log()
