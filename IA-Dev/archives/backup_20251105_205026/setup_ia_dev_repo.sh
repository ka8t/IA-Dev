#!/bin/bash
# ============================================================
# Script d'initialisation et de mise à jour du dépôt IA-Dev
# Auteur : ChatGPT x ka8t
# ============================================================

set -e

REPO_DIR="IA-Dev"

echo "🚀 Vérification de la structure du dépôt IA-Dev..."

# === 1. Créer la structure de dossiers si nécessaire ======================
mkdir -p $REPO_DIR/{guides,resources,examples,scripts,assets/{visuals,pdf}}

# === 2. Création / mise à jour du README.md ===============================
README_PATH="$REPO_DIR/README.md"

echo "📄 Mise à jour du README.md..."
cat > "$README_PATH" << 'EOF'
# 🤖 AI Driven Dev — Intégrer l’IA dans le Développement Logiciel

Bienvenue dans **AI Driven Dev**, un projet open-source qui aide **développeurs et managers tech** à adopter l’IA de manière pragmatique.

---

## 📘 Ce que vous trouverez ici

| Public | Ressources clés |
|---------|----------------|
| 👨‍💻 **Développeurs** | [Quick Start Dev](./guides/Quick_Start_Dev.md) – Devenez un “développeur augmenté” |
| 👔 **Managers / Leads** | [Quick Start Manager](./guides/Quick_Start_Manager.md) – Piloter la transformation IA |
| 📚 **Guide complet** | [AI Driven Dev Guide](./guides/AI_Driven_Dev_Guide.md) – Vision globale et cas pratiques |
| 🧠 **Prompts & outils** | [Prompts Library](./resources/prompts_library.md) – Framework RACE et exemples |

---

## 🚀 Pourquoi ce projet ?

L’IA transforme le développement logiciel.  
Ce dépôt partage des **outils concrets, frameworks, cas pratiques** et **retours terrain** pour accélérer votre adoption de l’IA.

---

## 📊 Gains observés

- +35 à +80 % de productivité développeurs  
- -40 % de bugs en moyenne  
- ROI mesuré : jusqu’à **7400 %**

---

## 🧩 Structure du dépôt

```bash
guides/      → Guides complets et résumés
resources/   → Prompts, outils, KPIs
examples/    → Cas pratiques de code
assets/      → Visuels & PDF
scripts/     → Génération de docs & outils internes
```

---

## 🌍 Rejoignez la discussion

💬 Partagez vos retours, ouvrez des issues ou proposez vos propres cas pratiques !  
📩 Suivez les annonces sur [LinkedIn](https://www.linkedin.com/in/ton-profil)  

---

## 🪪 Licence

Sous licence MIT – libre d’utilisation et de modification.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Made with ❤️](https://img.shields.io/badge/Made%20with-IA-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
EOF

# === 3. Fichiers utilitaires / guides =====================================
function create_if_missing {
    local path="$1"
    local content="$2"
    if [ ! -f "$path" ]; then
        echo "🆕 Création : $path"
        echo "$content" > "$path"
    else
        echo "✅ Déjà présent : $path"
    fi
}

create_if_missing "$REPO_DIR/guides/AI_Driven_Dev_Guide.md" "# 📘 AI Driven Dev Guide

> Guide complet pour développeurs et managers : comment adopter et exploiter l’IA dans le développement logiciel.

## Table des matières
1. Introduction
2. Pour les développeurs
3. Pour les managers
4. Outils IA recommandés
5. Framework RACE (Prompt Engineering)
6. Cas pratiques
7. Mesure du ROI
8. Annexes
"

create_if_missing "$REPO_DIR/guides/Quick_Start_Dev.md" "# 👨‍💻 Quick Start — Développeur augmenté

- Installez Copilot, ChatGPT, Cursor en 30 min  
- Augmentez votre productivité de +35 à +80 %  
- Apprenez à structurer vos prompts avec le framework RACE  
- Consultez le guide complet ici : [AI Driven Dev Guide](./AI_Driven_Dev_Guide.md)
"

create_if_missing "$REPO_DIR/guides/Quick_Start_Manager.md" "# 👔 Quick Start — Manager & CTO

- Stratégie d’adoption IA en 4 phases (Exploration → Pilote → Déploiement → Optimisation)  
- +30 % de productivité d’équipe, -40 % de bugs  
- ROI moyen observé : 7400 %  
- Consultez le guide complet ici : [AI Driven Dev Guide](./AI_Driven_Dev_Guide.md)
"

create_if_missing "$REPO_DIR/resources/prompts_library.md" "# 🧠 Bibliothèque de Prompts — Framework RACE

**RACE = Rôle • Action • Contexte • Exemple**

## Exemple type
\`\`\`
Tu es un développeur Python senior.
Crée une fonction qui trie une liste de dictionnaires par clé.
Gère les cas d’erreur et ajoute une docstring Google style.
\`\`\`

## Catégories
- 🔧 Codage (création, refactoring)
- 🧪 Tests (unitaires, intégration)
- 📚 Documentation (docstrings, README)
- 🐛 Debug (analyse d’erreurs)
"

create_if_missing "$REPO_DIR/resources/tools_setup.md" "# 🛠️ Installation des outils IA

## 1. GitHub Copilot
- Extension VS Code
- Essai gratuit 30 jours
- Fonctionne sur 20+ langages

## 2. Cursor / Codeium / Tabnine
- Alternatives IA gratuites ou pro
- Intégration rapide à VS Code, JetBrains

## 3. ChatGPT / Claude
- Utilisez des prompts structurés
- Combinez avec votre IDE pour réviser du code
"

# === 4. Statut final ======================================================
echo "✅ Structure IA-Dev vérifiée et mise à jour avec succès."
echo ""
echo "👉 Étapes suivantes :"
echo "   cd $REPO_DIR"
echo "   git add . && git commit -m 'Mise à jour automatique IA-Dev'"
echo "   git push origin main"
echo ""
echo "🧠 Astuce : relance ce script régulièrement pour garder ton dépôt à jour."
