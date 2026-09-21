from socket import *
from constCS import *  # -
 
 
def calc_overhang(target_overhang_str, max_blocks=2_000_000):
    """Problema do empilhamento de blocos (block-stacking / overhang problem).
    Com blocos de comprimento 1, o deslocamento (overhang) máximo alcançável
    com n blocos é (1/2) * H_n, onde H_n = 1 + 1/2 + 1/3 + ... + 1/n
    (soma harmônica). Essa soma diverge, mas muito devagar, então calculamos
    iterativamente até batr o alvo ou um teto de segurança."""
    target = float(target_overhang_str)
    harmonic_sum = 0.0
    n = 0
    while harmonic_sum / 2 < target:
        n += 1
        harmonic_sum += 1.0 / n
        if n >= max_blocks:
            return (f"Não convergiu até {max_blocks} blocos "
                     f"(overhang alcançado: {harmonic_sum / 2:.4f} comprimentos de bloco)")
    return f"{n} blocos necessários (overhang alcançado: {harmonic_sum / 2:.4f} comprimentos de bloco)"
 
 
def check_prime(n_str):
    """Verifica primalidade por tentativa de divisão até a raiz quadrada."""
    n = int(n_str)
    if n < 2:
        return f"{n} não é primo"
    if n % 2 == 0:
        return f"{n} não é primo" if n != 2 else f"{n} é primo"
    i = 3
    while i * i <= n:
        if n % i == 0:
            return f"{n} não é primo (divisível por {i})"
        i += 2
    return f"{n} é primo"
 
 
def word_freq(text):
    """Conta a frequência de cada palavra em um texto e retorna a mais comum."""
    words = text.lower().split()
    if not words:
        return "texto vazio"
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    mais_comum = max(freq, key=freq.get)
    return (f"palavra mais frequente: '{mais_comum}' ({freq[mais_comum]}x) | "
            f"total de palavras distintas: {len(freq)}")
 
 
OPERATIONS = {
    "overhang": calc_overhang,
    "prime": check_prime,
    "wordfreq": word_freq,
}
 
 
def process_request(request):
    """Protocolo simples: 'operacao;argumento'. Roteia para a função certa."""
    try:
        op, _, arg = request.partition(";")
        op = op.strip().lower()
        arg = arg.strip()
        if op not in OPERATIONS:
            return f"Operação desconhecida: '{op}'. Use: {', '.join(OPERATIONS)}"
        return OPERATIONS[op](arg)
    except Exception as e:
        return f"Erro ao processar requisição: {e}"
 
 
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))                    # -
s.listen(1)                             # -
print(f"Servidor escutando em {HOST}:{PORT}...")
 
(conn, addr) = s.accept()               # returns new socket and addr. client
print(f"Conectado por {addr}")
while True:                             # forever
    data = conn.recv(1024)              # receive data from client
    if not data:
        break                           # stop if client stopped
    request = bytes.decode(data)
    print(f"Recebido: {request}")
    response = process_request(request)  # processamento real da requisição
    conn.send(str.encode(response))     # devolve o resultado processado
conn.close()       
