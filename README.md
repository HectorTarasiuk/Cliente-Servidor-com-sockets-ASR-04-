Cliente-Servidor com Sockets — Multiplas Operacoes (veja no modo codigo)

Extensão do exemplo do Cap. 2 (slide 5) do livro-texto, com um servidor que realiza processamento real sobre as requisições e permite que o cliente escolha, a cada requisição, qual funcionalidade quer invocar.

Protocolo

Cada requisição enviada pelo cliente segue o formato:

<operacao>;<argumento>

O servidor identifica a operação, executa a função correspondente e devolve o resultado como texto.

Operações disponíveis
- overhang, de argumento um número (overhang alvo, em comprimentos de bloco), calcula quantos blocos são necessários para alcançar um deslocamento (overhang) alvo no problema clássico do empilhamento de blocos, usando a soma harmônica (overhang(n) = H_n / 2). A soma harmônica diverge muito lentamente, então o cálculo tem um teto de segurança de iterações.
-prime, de argumento um	número inteiro, o qual e verificaado se é primo, por tentativa de divisão até a raiz quadrada.
-wordfreq, cujo argumento 'e um	texto livre,	do qual e contada a frequência de cada palavra do texto e retornada a mais frequente.

Exemplos de requisição:

overhang;10
prime;67
wordfreq; o Titanic afundou em 1912. tenho hiperfoco nele, em jaca e coelhos. Uma jaqueira adulta e saudável produz de 100 a 200 frutos por ano, o que equivale a mais ou menos 1,5 a 3 toneladas de fruta por árvore ao ano

Arquivos
constCS.py — define HOST e PORT usados por cliente e servidor.
server.py — abre o socket, aceita uma conexão e, em loop, recebe requisições, roteia para a operação pedida e devolve o resultado.
client.py — conecta ao servidor e permite ao usuário digitar várias requisições (potencialmente com operações diferentes) na mesma conexão.
Como executar
ajustar HOST em constCS.py para o IP da máquina que vai rodar o server.py 
Na instância que será o servidor:
   python3 server.py
Na máquina/instância que será o cliente:
   python3 client.py
Digite requisições no formato operacao;argumento. Digite sair para encerrar a conexão.

Execução na AWS

Testado com servidor rodando em uma instância EC2 (Ubuntu), com a porta definida em constCS.py liberada no Security Group da instância para permitir conexões de entrada TCP.
