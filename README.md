# Sequenciador de LEDs com ESP32

Este é um projeto inicial em MicroPython para aprender a controlar LEDs e ler botões usando a placa ESP32 no simulador Wokwi.

![Interface do Projeto](https://github.com/joaotorresdev/Piano-ESP32/blob/main/PRINTPIANO.png)

## 🚀 Sobre o Projeto

O circuito usa 3 botões para ativar diferentes efeitos de pisca-pisca em 3 LEDs (Vermelho, Amarelo e Verde). Ele funciona como o sistema de um semáforo automático ou luzes de sinalização.

## 🛠️ Tecnologias

* MicroPython
* Placa ESP32
* Simulador Wokwi

## 💻 Como Funciona

O programa fica monitorando os botões dentro de um laço infinito (`while True`):

* **Botão 1:** Ativa o modo semáforo (acende o LED Vermelho por 3s, o Amarelo por 5s e o Verde por 1s).
* **Botão 2:** Ativa um modo de alerta rápido, alternando os LEDs a cada 0.5 segundos.
* **Botão 3:** Ativa uma sequência personalizada de testes.
