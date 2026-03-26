# =========================================================
#  SAFEGUARD AI — Mini Smart Security AI
#  Model: Random Forest Classifier
#  Libraries: numpy, pandas, matplotlib, scikit-learn
# =========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Set random seed for reproducibility
np.random.seed(13)

# ---------------------------------------------------------
# 1. DATASET — 400 simulated home sensor events
# ---------------------------------------------------------

event_classes = {
    'NORMAL':   {'motion_range': (5, 30),   'sound_range': (15, 45),   'temp_change': (-0.3, 0.3),  'count': 160},
    'ANIMAL':   {'motion_range': (35, 70),  'sound_range': (30, 65),   'temp_change': (-0.2, 0.4),  'count': 110},
    'PERSON':   {'motion_range': (60, 100), 'sound_range': (45, 90),   'temp_change': (0.3, 1.5),   'count': 90},
    'EMERGENCY':{'motion_range': (70, 100), 'sound_range': (80, 130),  'temp_change': (2.0, 8.0),   'count': 40},
}

dataframes = []
for label, params in event_classes.items():
    n_events = params['count']
    df_class = pd.DataFrame({
        'motion': np.random.uniform(*params['motion_range'], n_events),
        'sound': np.random.uniform(*params['sound_range'], n_events),
        'temp_delta': np.random.uniform(*params['temp_change'], n_events),
        'event_label': label
    })
    dataframes.append(df_class)

# Combine all classes and shuffle
df_events = pd.concat(dataframes, ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)

print("SAFEGUARD AI — Dataset size:", len(df_events))
for cls, count in df_events['event_label'].value_counts().items():
    print(f"  {cls}: {count}")
print(df_events.head(4).to_string(index=False))

# ---------------------------------------------------------
# 2. EDA PLOT — Average sensor readings per event type
# ---------------------------------------------------------

event_order = ['NORMAL', 'ANIMAL', 'PERSON', 'EMERGENCY']
colors = ['#95a5a6', '#f39c12', '#e67e22', '#e74c3c']

mean_sensors = df_events.groupby('event_label')[['motion', 'sound', 'temp_delta']].mean().loc[event_order]
sensor_names = ['Motion', 'Sound (dB)', 'Temp Change (°C)']

fig, ax = plt.subplots(figsize=(9, 4))
x = np.arange(len(sensor_names))
bar_width = 0.2

for i, (event, color) in enumerate(zip(event_order, colors)):
    values = mean_sensors.loc[event].values
    bars = ax.bar(x + i * bar_width, values, bar_width, label=event, color=color, edgecolor='black', linewidth=0.7)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.3, f'{val:.0f}', ha='center', fontsize=7, fontweight='bold')

ax.set_title('SAFEGUARD AI — Average Sensor Readings by Event Type', fontweight='bold')
ax.set_xticks(x + bar_width * 1.5)
ax.set_xticklabels(sensor_names)
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig('safeguard_eda_plot.png', dpi=120, bbox_inches='tight')
plt.show()
print("Plot saved: safeguard_eda_plot.png")

# ---------------------------------------------------------
# 3. MACHINE LEARNING MODEL
# ---------------------------------------------------------

label_encoder = LabelEncoder()
label_encoder.fit(event_order)
y = label_encoder.transform(df_events['event_label'])
X = df_events[['motion', 'sound', 'temp_delta']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=50, random_state=42)
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)

print(f"\nModel Accuracy: {accuracy_score(y_test, y_pred) * 100:.1f}%")

# ---------------------------------------------------------
# 4. RESULTS PLOT — Confusion Matrix
# ---------------------------------------------------------

cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(5, 4))
ax.imshow(cm, cmap='Blues')
ax.set_xticks(range(len(event_order)))
ax.set_yticks(range(len(event_order)))
ax.set_xticklabels(event_order, rotation=20, fontsize=8)
ax.set_yticklabels(event_order, fontsize=8)
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')
ax.set_title('SAFEGUARD AI — Confusion Matrix', fontweight='bold')

for i in range(len(event_order)):
    for j in range(len(event_order)):
        ax.text(j, i, str(cm[i, j]), ha='center', va='center',
                fontsize=14, fontweight='bold',
                color='white' if cm[i, j] > cm.max() * 0.6 else 'black')

plt.tight_layout()
plt.savefig('safeguard_confusion_matrix.png', dpi=120, bbox_inches='tight')
plt.show()
print("Results saved: safeguard_confusion_matrix.png")

# ---------------------------------------------------------
# 5. EVENT SIMULATOR — Classify new events
# ---------------------------------------------------------

actions = {
    'NORMAL': 'No action needed.',
    'ANIMAL': 'Logged. No alarm triggered.',
    'PERSON': 'Notify owner!',
    'EMERGENCY': 'ALERT — Call emergency services!'
}

print("\nEVENT SIMULATOR:")
new_events = pd.DataFrame({
    'motion': [10, 55, 90],
    'sound': [20, 50, 110],
    'temp_delta': [0.1, 0.2, 5.5]
})
descriptions = ['Falling leaf', 'Cat on the sofa', 'Possible fire']

predicted_labels = label_encoder.inverse_transform(rf_model.predict(new_events))
for desc, label in zip(descriptions, predicted_labels):
    print(f"  '{desc}' → {label}: {actions[label]}")
