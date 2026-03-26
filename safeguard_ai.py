# =========================================================
#  SAFEGUARD AI — Mini IA per Sicurezza Intelligente
#  Modello: Random Forest Classifier
#  Librerie: numpy, pandas, matplotlib, scikit-learn
# =========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder

np.random.seed(13)

# ---------------------------------------------------------
#  1. DATASET — 400 eventi dai sensori di casa
# ---------------------------------------------------------

classi = {
    'NORMALE':   {'movimento': (5,  30),  'suono': (15, 45),  'temp': (-0.3, 0.3),  'n': 160},
    'ANIMALE':   {'movimento': (35, 70),  'suono': (30, 65),  'temp': (-0.2, 0.4),  'n': 110},
    'PERSONA':   {'movimento': (60, 100), 'suono': (45, 90),  'temp': (0.3,  1.5),  'n':  90},
    'EMERGENZA': {'movimento': (70, 100), 'suono': (80, 130), 'temp': (2.0,  8.0),  'n':  40},
}

frames = []
for etich, p in classi.items():
    nn = p['n']
    frames.append(pd.DataFrame({
        'movimento': np.random.uniform(*p['movimento'], nn),
        'suono':     np.random.uniform(*p['suono'], nn),
        'temp':      np.random.uniform(*p['temp'], nn),
        'evento':    etich
    }))

df = pd.concat(frames, ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)

print("SAFEGUARD AI — Dataset:", len(df), "eventi")
for c, n_ in df['evento'].value_counts().items():
    print(f"  {c}: {n_}")
print(df.head(4).to_string(index=False))

# ---------------------------------------------------------
#  2. GRAFICO EDA — Medie sensori per tipo evento
# ---------------------------------------------------------

ordine = ['NORMALE', 'ANIMALE', 'PERSONA', 'EMERGENZA']
colori = ['#95a5a6', '#f39c12', '#e67e22', '#e74c3c']

medie = df.groupby('evento')[['movimento', 'suono', 'temp']].mean().loc[ordine]
variabili = ['Movimento', 'Suono (dB)', 'Delta Temp (C)']

fig, ax = plt.subplots(figsize=(9, 4))
x = np.arange(len(variabili))
larghezza = 0.2

for i, (classe, colore) in enumerate(zip(ordine, colori)):
    valori = medie.loc[classe].values
    barre  = ax.bar(x + i * larghezza, valori, larghezza,
                    label=classe, color=colore, edgecolor='black', linewidth=0.7)
    for b, v in zip(barre, valori):
        ax.text(b.get_x() + b.get_width()/2, v + 0.3,
                f'{v:.0f}', ha='center', fontsize=7, fontweight='bold')

ax.set_title('SAFEGUARD AI — Medie Sensori per Tipo Evento', fontweight='bold')
ax.set_xticks(x + larghezza * 1.5)
ax.set_xticklabels(variabili)
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig('safeguard_grafico.png', dpi=120, bbox_inches='tight')
plt.show()
print("Grafico salvato: safeguard_grafico.png")

# ---------------------------------------------------------
#  3. MODELLO ML
# ---------------------------------------------------------

le = LabelEncoder()
le.fit(ordine)
y = le.transform(df['evento'])
X = df[['movimento', 'suono', 'temp']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modello = RandomForestClassifier(n_estimators=50, random_state=42)
modello.fit(X_train, y_train)
y_pred = modello.predict(X_test)

print(f"\nAccuratezza del modello: {accuracy_score(y_test, y_pred)*100:.1f}%")

# ---------------------------------------------------------
#  4. GRAFICO RISULTATI — Matrice di confusione
# ---------------------------------------------------------

cm  = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(5, 4))
ax.imshow(cm, cmap='Blues')
ax.set_xticks(range(4)); ax.set_yticks(range(4))
ax.set_xticklabels(ordine, rotation=20, fontsize=8)
ax.set_yticklabels(ordine, fontsize=8)
ax.set_xlabel('Predizione'); ax.set_ylabel('Reale')
ax.set_title('SAFEGUARD AI — Matrice di Confusione', fontweight='bold')
for i in range(4):
    for j in range(4):
        ax.text(j, i, str(cm[i, j]), ha='center', va='center',
                fontsize=14, fontweight='bold',
                color='white' if cm[i, j] > cm.max() * 0.6 else 'black')
plt.tight_layout()
plt.savefig('safeguard_risultati.png', dpi=120, bbox_inches='tight')
plt.show()
print("Risultati salvati: safeguard_risultati.png")

# ---------------------------------------------------------
#  5. SIMULATORE — Classificazione nuovi eventi
# ---------------------------------------------------------

azioni = {
    'NORMALE':   'Nessuna azione.',
    'ANIMALE':   'Annotato. Nessun allarme.',
    'PERSONA':   'Notifica proprietario!',
    'EMERGENZA': 'ALLERTA — Chiamata emergenza!'
}

print("\nSIMULATORE:")
nuovi = pd.DataFrame({'movimento': [10,  55,  90],
                       'suono':    [20,  50, 110],
                       'temp':     [0.1, 0.2, 5.5]})
descrizioni = ['Foglia caduta', 'Gatto sul divano', 'Possibile incendio']
pred = le.inverse_transform(modello.predict(nuovi))
for desc, etich in zip(descrizioni, pred):
    print(f"  '{desc}'  →  {etich}: {azioni[etich]}")
