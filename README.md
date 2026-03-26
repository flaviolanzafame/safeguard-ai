# RiseVET — SAFEGUARD AI

**Mini IA per Sicurezza Intelligente**

SAFEGUARD AI è un prototipo di sistema di sicurezza domestica basato su machine learning che classifica eventi rilevati dai sensori di una casa (movimento, suono, temperatura). Usa un **Random Forest Classifier** per identificare la natura di ogni evento e suggerire azioni appropriate.

---

## Caratteristiche principali

- **Classificazione eventi**:
  - **NORMALE**: attività di routine senza anomalie
  - **ANIMALE**: presenza di animali domestici
  - **PERSONA**: possibile intrusione umana
  - **EMERGENZA**: situazioni critiche (es. incendi)
- **Visualizzazione dati**: grafici delle medie dei sensori per tipo di evento
- **Valutazione modello ML**: accuratezza e matrice di confusione
- **Simulatore di eventi**: test rapido di nuovi eventi con azioni consigliate

---

## Tecnologie e librerie

- Python 3
- Librerie: `numpy`, `pandas`, `matplotlib`, `scikit-learn`
- Modello ML: **Random Forest Classifier** con 50 alberi

---

## Dataset

Dataset generato artificialmente, 400 eventi suddivisi in 4 classi:

- **NORMALE**: 160 eventi  
- **ANIMALE**: 110 eventi  
- **PERSONA**: 90 eventi  
- **EMERGENZA**: 40 eventi  

Ogni evento contiene:  
`movimento`, `suono`, `temp`, `evento`

---

## Come usare il progetto

1. **Installazione librerie**:

```bash
pip install numpy pandas matplotlib scikit-learn