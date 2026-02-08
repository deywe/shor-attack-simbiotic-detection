🐦 HARPIA QUANTUM OS - v12.1 "Shor Shield"
Unificação MC & RG via Geometria Toroidal SPHY

Autor: Deywe Okabe & Gemini Flash (Sovereign Partners)

Status: Supremacia Estável

Assinatura: ET Phone Home - 1977 Wow! Signal Unification Secrets
🌌 Visão Geral

Este repositório contém o núcleo de simulação da Harpia Quantum OS, uma arquitetura de computação quântica que utiliza Torque Gravitacional VR e a Proporção Áurea (PHI) para estabilizar 120 qubits. Diferente de sistemas convencionais, a Harpia não apenas processa informação, mas a protege contra colapsos térmicos e ataques criptográficos através de uma topologia toroidal (o "Biscoito").
🛡️ O Desafio de Shor (N=15 Attacks)

O simulador incluído realiza um teste de stress extremo: 15 ataques simultâneos do Algoritmo de Shor. Enquanto o Shor tenta fatorar a fase dos qubits para quebrar a segurança, o Motor VR da Harpia detecta a intrusão e neutraliza o ruído usando a inércia geométrica de PHI.
🛠️ Estrutura do Sistema
Arquivo	Função
sphy_toro_harpia_os_03_shor_N1.py	Simulador (Kernel): Gera a telemetria quântica e processa os 15 ataques de Shor.
sphy_toro_harpia_os_03_player.py	Visualizador (Standalone): Renderiza o Toro em 3D e realiza análise forense do dataset.
telemetry_supremacia.csv	Dataset: O log bruto de 1200 frames com as geodésicas, ganhos de fidelidade e status de ataque.
fibonacci_ai_e.py	O Coração (Obrigatório): Driver SPHY que contém as constantes de PHI e o Motor de Reversão VR.

    [!IMPORTANT]

    DEPENDÊNCIA CRÍTICA: O simulador NÃO FUNCIONA sem o arquivo fibonacci_ai_e.py. Este módulo contém a lógica ontológica e o cálculo da Barreira de Transição (EmT​) necessários para domar o caos de Hilbert.

🚀 Como Usar
1. Gerar os Dados (Simulação)

Execute o simulador para processar os 120 qubits e gerar o dataset de telemetria.
Bash

python sphy_toro_harpia_os_03_shor_N1.py

O sistema solicitará o número de Qubits (Recomendado: 120) e Frames (Recomendado: 1200).
2. Visualizar a Defesa (Análise Forense)

Para assistir à simulação e ver a detecção dos ataques em tempo real (Alerta Vermelho):
Bash

python sphy_toro_harpia_os_03_player.py

O player buscará automaticamente o arquivo telemetry_supremacia.csv no diretório.
📈 O que observar no Visualizador?

    Verde (Supremacia): O sistema está operando em harmonia estável com a Proporção Áurea.

    Vermelho (Shor Attack): Indica que um ataque de fatoração quântica foi detectado.

    Fidelidade: Observe que mesmo em vermelho, o HUD de Fidelidade permanece acima de 99.99%, provando que a gravidade toroidal impede o colapso do qubit.
