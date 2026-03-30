# 🛡️ SafeGuard AI

<br>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Stato](https://img.shields.io/badge/Stato-Prototipo-brightgreen?style=for-the-badge)
![Licenza](https://img.shields.io/badge/Licenza-MIT-lightgrey?style=for-the-badge)

---

🌍 This README is available in:&nbsp;&nbsp;[<img src="https://github.com/flaviolanzafame/flaviolanzafame/raw/main/flags/gb-flag.svg" width="20" alt="EN"/> English](README.md)&nbsp;&nbsp;·&nbsp;&nbsp;[**<img src="https://github.com/flaviolanzafame/flaviolanzafame/raw/main/flags/it-flag.svg" width="20" alt="IT"/> Italian**](README.it.md)

---

**SafeGuard AI** è un prototipo di sistema di sicurezza domestica intelligente che analizza i dati di tre sensori in tempo reale e distingue le minacce reali dagli eventi innocui, così l'allarme scatta solo quando serve davvero.

---
 
## 📑 Indice
 
- [⚠️ Il problema](#%EF%B8%8F-il-problema)
- [💡 La soluzione](#-la-soluzione)
- [🎯 A chi serve](#-a-chi-serve)
- [🧰 Tecnologie utilizzate](#-tecnologie-utilizzate)
- [📦 Codice](#-codice)
- [🚀 Installazione](#-installazione)
- [⚙️ Come funziona](#%EF%B8%8F-come-funziona)
- [📊 Risultati](#-risultati)
- [👥 Team](#-team)
- [📄 Licenza](#-licenza)
 
---

## ⚠️ Il problema

I sistemi di allarme tradizionali non distinguono un intruso da un gatto che salta sul divano. Ogni movimento, ogni rumore — stesso allarme. Il risultato? Si finisce per ignorarli tutti.

- 🔔 Falsi allarmi continui → le notifiche vengono disattivate
- 😤 Stress inutile → interruzioni a ogni ora del giorno
- 🚨 Interventi dei soccorsi per niente → spreco di risorse
- 📉 Fiducia nel sistema a zero → l'allarme diventa inutile

---

## 💡 La soluzione

SafeGuard AI non si limita a rilevare un segnale — cerca di capire cosa sta succedendo. Combina i dati di tre sensori e li analizza con un modello di machine learning addestrato a riconoscere quattro tipi di evento:

```
Sensore movimento + Sensore sonoro + Sensore temperatura/fumi
                          ↓
             Random Forest Classifier
                          ↓
     NORMALE · ANIMALE · PERSONA · EMERGENZA
                          ↓
          Risposta automatica — solo quando serve
```

| Evento | Cosa significa | Cosa fa il sistema |
|---|---|---|
| 🟢 `NORMALE` | Vento, vibrazioni, rumore ambientale | Nessuna azione |
| 🟡 `ANIMALE` | Animale domestico in giro | Registrato, nessun allarme |
| 🟠 `PERSONA` | Presenza umana rilevata | Notifica al proprietario |
| 🔴 `EMERGENZA` | Incendio, intrusione, evento critico | Allerta immediata ai soccorsi |

---

## 🎯 A chi serve

SafeGuard AI è pensato per chi ha già un sistema d'allarme ma non ne può più dei falsi allarmi — famiglie con animali domestici, case con molto via vai, professionisti che vogliono notifiche solo quando c'è un motivo vero.

![SafeGuard AI Product Concept](assets/safeguardai-product.png)

---

## 🧰 Tecnologie utilizzate

| Componente | Tecnologia |
|---|---|
| **Sensori** | Movimento (PIR), Suono (dB), Temperatura / Fumi |
| **Modello ML** | Random Forest Classifier (`scikit-learn`) |
| **Elaborazione** | Locale — nessun dato inviato al cloud |
| **Linguaggio** | Python 3.8+ |
| **Librerie** | `numpy`, `pandas`, `matplotlib`, `scikit-learn` |

---

## 📦 Codice

Tutto il progetto vive in un unico script Python:

```
safeguard-ai/
│
├── safeguard_ai.py                # Pipeline completa
├── assets/
│   ├── safeguardai-logo.png
│   ├── safeguardai-product.png
│   └── safeguardai-use.png
├── safeguard_eda_plot.png         # Generato automaticamente
├── safeguard_confusion_matrix.png # Generato automaticamente
├── README.md                      # English
├── README.it.md                   # Italiano
└── LICENSE                        # Licenza
```

👉 [`safeguard_ai.py`](./safeguard_ai.py)

---

## 🚀 Installazione

### 1. Clona il repository

```bash
git clone https://github.com/your-org/safeguard-ai.git
cd safeguard-ai
```

### 2. Installa le dipendenze

```bash
pip install numpy pandas matplotlib scikit-learn
```

### 3. Avvia

```bash
python safeguard_ai.py
```

---

## ⚙️ Come funziona

Lo script esegue cinque fasi in sequenza:

**① Dataset**
Vengono simulati 400 eventi domestici con valori realistici per ogni classe:

| Classe | Campioni | Movimento | Suono (dB) | Temp Δ (°C) |
|---|---|---|---|---|
| NORMALE | 160 | 5–30 | 15–45 | −0.3 – 0.3 |
| ANIMALE | 110 | 35–70 | 30–65 | −0.2 – 0.4 |
| PERSONA | 90 | 60–100 | 45–90 | 0.3 – 1.5 |
| EMERGENZA | 40 | 70–100 | 80–130 | 2.0 – 8.0 |

**② Analisi esplorativa (EDA)**
Un grafico mostra i valori medi di ogni sensore per classe — utile per capire quanto le classi siano separabili.

**③ Addestramento**
Un `RandomForestClassifier` con 50 alberi viene addestrato sull'80% dei dati, con seed fisso per garantire risultati riproducibili.

**④ Valutazione**
Accuratezza e matrice di confusione vengono calcolate sul 20% restante e salvate come immagini PNG.

**⑤ Simulatore**
Tre scenari reali vengono classificati dal modello:

```text
'Foglia che cade'    → NORMALE:    Nessuna azione necessaria.
'Gatto sul divano'   → ANIMALE:    Registrato. Nessun allarme.
'Possibile incendio' → EMERGENZA:  ALLERTA — Chiama i soccorsi!
```

![SafeGuard AI in uso](assets/safeguardai-use.png)

---

## 📊 Risultati

Grazie alla buona separazione dei valori tra le classi, il modello raggiunge un'accuratezza elevata. All'avvio vengono generati automaticamente due file:

- **`safeguard_eda_plot.png`** — grafico a barre dei valori medi per tipo di evento
- **`safeguard_confusion_matrix.png`** — heatmap delle previsioni del modello

| Parametro | Valore |
|---|---|
| Algoritmo | Random Forest Classifier |
| Numero di alberi | 50 |
| Split Train / Test | 80% / 20% |
| Seed | 42 |
| Feature | `motion`, `sound`, `temp_delta` |

---

## 👥 Team

Progetto sviluppato nell'ambito del corso di **Intelligenza artificiale** del **[progetto RiseVET](https://risevet.eu)** — un'iniziativa che porta studenti a sperimentare con IA e tecnologie emergenti attraverso prototipi reali.

- **Flavio Lanzafame** — [@flaviolanzafame](https://github.com/flaviolanzafame)
- **Luigi Larecchiuta** — [@Luigi879](https://github.com/Luigi879)
- **Carmelo Vicari** — [@carmelo19vicari](https://github.com/carmelo19vicari)
- **Carmelo Vicari** — [@VicariCarmelo8](https://github.com/VicariCarmelo8)
  
**Docente:** Luisa Gangi Chiodo — [@lujsa](https://github.com/lujsa)

---

## 📄 Licenza

Rilasciato sotto [Licenza MIT](LICENSE).

---

<div align="center">

Realizzato con Python · scikit-learn · pandas · matplotlib

</div>
