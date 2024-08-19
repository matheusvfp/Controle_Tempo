import ctypes
import tkinter as tk
from tkinter import ttk

def bloquear_computador():
    """
    Bloqueia a estação de trabalho usando a API do Windows.
    """
    ctypes.windll.user32.LockWorkStation()

def verificar_tela_bloqueada():
    """
    Verifica se a tela está bloqueada.
    :return: True se a tela estiver bloqueada, False caso contrário.
    """
    return ctypes.windll.user32.GetForegroundWindow() == 0

def mostrar_aviso(tempo_espera):
    """
    Exibe uma janela com uma contagem regressiva que, ao expirar, bloqueia o computador.
    
    :param tempo_espera: Tempo total em segundos para a contagem regressiva.
    """
    def formatar_tempo(segundos):
        """
        Converte o tempo em segundos para o formato de horas, minutos e segundos.
        
        :param segundos: Tempo total em segundos.
        :return: Tempo formatado como uma string "HH:MM:SS".
        """
        horas, segundos = divmod(segundos, 3600)
        minutos, segundos = divmod(segundos, 60)
        return f"{horas:02}:{minutos:02}:{segundos:02}"

    def adicionar_tempo_extra():
        """
        Adiciona 2 minutos (120 segundos) ao tempo restante e atualiza a interface.
        Somente é possível adicionar tempo extra uma vez, e somente no minuto final.
        """
        nonlocal tempo_restante, tempo_extra_adicionado
        if tempo_restante <= 60 and not tempo_extra_adicionado:
            tempo_restante += 120
            tempo_extra_adicionado = True
            atualizar_tempo_restante()  # Atualiza a contagem regressiva
        elif tempo_restante > 60:
            label.config(text="Você só pode adicionar tempo extra no minuto final.")
        else:
            label.config(text="Tempo extra já foi adicionado.")

    root = tk.Tk()
    root.title("Aviso de Bloqueio")
    root.geometry("320x200")
    root.configure(bg="#f5f5f5")
    
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    
    frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10, relief=tk.FLAT, borderwidth=2)
    frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    
    label = tk.Label(frame, text="", font=("Arial", 14, "bold"), bg="#ffffff", fg="#333333", wraplength=280)
    label.pack(expand=True, fill=tk.BOTH, pady=20)
    
    progress = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
    progress.pack(pady=10)
    
    tempo_inicial = tempo_espera
    tempo_restante = tempo_espera  # Tempo restante atual
    tempo_extra_adicionado = False  # Flag para verificar se o tempo extra já foi adicionado

    def atualizar_tempo_restante():
        """
        Atualiza o tempo restante na interface e a barra de progresso.
        Bloqueia o computador e fecha a janela quando o tempo expira.
        """
        nonlocal tempo_restante
        if verificar_tela_bloqueada():
            root.destroy()  # Fecha a janela se a tela estiver bloqueada
            return
        
        if tempo_restante > 0:
            label.config(text=f"Tempo restante: {formatar_tempo(tempo_restante)}")
            progress['value'] = 100 * (1 - (tempo_restante / tempo_inicial))
            tempo_restante -= 1
            root.after(1000, atualizar_tempo_restante)
        else:
            label.config(text="Tempo esgotado! Bloqueando o computador...")
            label.update_idletasks()  # Atualiza o layout da label
            root.after(1000, lambda: [root.destroy(), bloquear_computador()])

    atualizar_tempo_restante()
    
    # Botão para adicionar 2 minutos ao tempo restante
    tempo_extra_button = ttk.Button(frame, text="Adicionar Tempo Extra", command=adicionar_tempo_extra, style="TButton")
    tempo_extra_button.pack(pady=10)

    # Adiciona estilo ao botão
    style = ttk.Style()
    style.configure("TButton",
                    padding=(6, 0),
                    relief="flat",
                    background="#111111",   
                    foreground="#111111",  
                    font=("Arial", 10, "bold"))

    root.mainloop()

if __name__ == "__main__":
    tempo_espera = 20 
    mostrar_aviso(tempo_espera)
