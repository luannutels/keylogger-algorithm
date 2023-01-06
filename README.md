# keylogger-algorithm

Um keylogger é um tipo de software que registra as teclas digitadas em um computador e as envia para o atacante. 
Ele é geralmente usado para capturar senhas e outras informações confidenciais.

Esse código cria uma classe chamada "Keylogger" com um método "process_key_press()" que é chamado sempre que uma tecla é pressionada. O método registra a tecla pressionada no log do keylogger. Depois, um monitor de teclado é criado usando a biblioteca pynput e é iniciado. 
O monitor de teclado chamará o método "process_key_press()" sempre que uma tecla for pressionada. Por fim, o log de teclas digitadas é impresso.
