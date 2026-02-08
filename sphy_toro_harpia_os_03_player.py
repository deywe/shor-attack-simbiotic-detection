# ==================================================================================
# 🕵️ HARPIA OS v12.1 - STANDALONE ATTACK ANALYZER
# ----------------------------------------------------------------------------------
# Objetivo: Abrir o Dataset e visualizar a resistência aos 15 ataques de Shor.
# Autor: Deywe Okabe & Gemini Flash
# ==================================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys

def run_shor_analyzer(csv_path="telemetry_supremacia.csv"):
    try:
        print(f"📡 Abrindo Telemetria de Combate: {csv_path}...")
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"❌ Erro ao abrir arquivo: {e}")
        return

    # Configuração Visual Dark
    plt.rcParams['toolbar'] = 'None'
    fig = plt.figure(figsize=(10, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d', facecolor='black')
    ax.set_axis_off()

    # Geometria do Toro (Biscoito)
    R, r, flatten = 21.0, 8.0, 0.4
    u, v = np.linspace(0, 2*np.pi, 30), np.linspace(0, 2*np.pi, 30)
    U, V = np.meshgrid(u, v)
    X, Y, Z = (R + r*np.cos(V)) * np.cos(U), (R + r*np.cos(V)) * np.sin(U), (r * flatten) * np.sin(V)
    ax.plot_wireframe(X, Y, Z, color='white', alpha=0.07, linewidth=0.5)

    # Identificar qubits no dataset (limitando a 15 para performance do player)
    all_cols = df.columns
    q_indices = np.linspace(0, 119, 15, dtype=int)
    plots = [ax.plot([], [], [], 'o', markersize=7, markeredgecolor='white')[0] for _ in q_indices]
    
    # HUD de Auditoria
    hud = ax.text2D(0.05, 0.90, "", transform=ax.transAxes, family='monospace', fontsize=11)

    def update(f):
        data = df.iloc[f]
        # O segredo está aqui: o player lê o status gravado pelo Kernel
        is_attack = data.get('Attack_Status', 0) == 1
        
        # Estética de Alerta
        color = "#FF3333" if is_attack else "#00FF00"
        status = "!!! SHOR ATTACK DETECTED !!!" if is_attack else "STATUS: SUPREMACY STABLE"
        
        hud.set_text(f"HARPIA SHOR ANALYZER v12.1\n"
                     f"DATASET: {csv_path}\n"
                     f"FRAME: {f:04d} | FIDELITY: {data['Avg_VR_Gain']*100:.4f}%\n"
                     f"{status}")
        hud.set_color(color)

        for i, q_idx in enumerate(q_indices):
            x, y, z = data[f'q{q_idx}_x'], data[f'q{q_idx}_y'], data[f'q{q_idx}_z']
            plots[i].set_data([x], [y])
            plots[i].set_3d_properties([z])
            plots[i].set_color(color)

        return plots + [hud]

    ani = FuncAnimation(fig, update, frames=len(df), interval=25, blit=True)
    
    print("🌌 Analisador de Campo Ativo. Procure pelos frames em vermelho.")
    plt.show()

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "telemetry_supremacia.csv"
    run_shor_analyzer(target)