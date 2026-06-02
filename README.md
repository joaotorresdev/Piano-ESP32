# Pisca-Pisca Sequencial com ESP32

## 📝 Contexto
Este é um projeto básico de sistemas embarcados desenvolvido para praticar estruturas de repetição controladas por contadores[cite: 7]. O circuito simula o acionamento sequencial de três LEDs (Vermelho, Verde e Azul) conectados a uma placa ESP32 no simulador Wokwi[cite: 7]. Os LEDs piscam em ordem, um de cada vez, repetindo esse ciclo exatamente 10 vezes antes de encerrar o programa[cite: 7].

![Circuito do Projeto]()

## 🛠️ Linguagens Utilizadas
* MicroPython[cite: 7]

## 💻 Comandos Utilizados
* `machine.Pin()`: Usado para configurar e mapear os pinos digitais do ESP32 como saídas (`machine.Pin.OUT`)[cite: 7].
* `.on()`: Comando que envia sinal elétrico alto para ligar o LED desejado[cite: 7].
* `.off()`: Comando que corta o sinal elétrico para desligar o LED[cite: 7].
* `time.sleep()`: Função que pausa a execução do código por um tempo determinado (em segundos) para criar o efeito de piscar[cite: 7].
* `while`: Estrutura de repetição usada para controlar que o ciclo só rode enquanto o contador for menor ou igual a 10[cite: 7].
