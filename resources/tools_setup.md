# 🔧 Configuration des Outils IA — Guide d'installation

## 🎯 Objectif

Ce guide vous permet d'**installer et configurer les principaux outils IA** pour le développement en moins de 30 minutes. De GitHub Copilot à ChatGPT, en passant par Cursor et les alternatives.

---

## 📋 Table des matières

1. [Vue d'ensemble des outils](#vue-densemble-des-outils)
2. [GitHub Copilot](#github-copilot)
3. [ChatGPT](#chatgpt)
4. [Claude](#claude)
5. [Cursor](#cursor)
6. [Alternatives](#alternatives)
7. [APIs et automatisation](#apis-et-automatisation)
8. [Configuration avancée](#configuration-avancée)
9. [Troubleshooting](#troubleshooting)

---

## Vue d'ensemble des outils

### Comparatif rapide

| Outil | Type | Prix | Idéal pour | Installation |
|-------|------|------|-----------|--------------|
| **GitHub Copilot** | Extension IDE | 10$/mois | Complétion temps réel | 5 min |
| **ChatGPT** | Web + API | 0-20$/mois | Questions complexes | Immédiat |
| **Claude** | Web + API | 0-20$/mois | Analyse de code | Immédiat |
| **Cursor** | IDE complet | 20$/mois | Développement IA-first | 10 min |
| **Tabnine** | Extension IDE | 0-39$/mois | Alternative Copilot | 5 min |

### Recommandation pour débuter

**Combo optimal** :
1. **GitHub Copilot** (10€/mois) → IDE
2. **ChatGPT Free** ou **Claude Free** → navigateur

**Budget total : 10€/mois** (ou 0€ avec versions gratuites)

---

## GitHub Copilot

### Présentation

- **Type** : Assistant de code intégré à l'IDE
- **Prix** : 10$/mois (individuel), 19$/mois (Business)
- **Points forts** : Complétion en temps réel, contexte du fichier
- **Prérequis** : Compte GitHub

---

### Installation (VS Code)

#### Étape 1 : Installer l'extension

**Via l'interface VS Code** :
1. Ouvrir VS Code
2. Aller dans Extensions (`Cmd/Ctrl + Shift + X`)
3. Rechercher "GitHub Copilot"
4. Cliquer sur "Install"

**Via la ligne de commande** :
```bash
code --install-extension GitHub.copilot
```

#### Étape 2 : Se connecter à GitHub

1. Cliquer sur l'icône Copilot (barre latérale)
2. Cliquer sur "Sign in to GitHub"
3. Autoriser l'accès dans le navigateur
4. Revenir à VS Code

#### Étape 3 : Activer l'abonnement

1. Aller sur [github.com/settings/copilot](https://github.com/settings/copilot)
2. Cliquer sur "Start free trial" (60 jours gratuits)
3. Entrer les informations de paiement
4. Activer Copilot

**Vérification** :
- Ouvrir un fichier `.js` ou `.py`
- Taper un commentaire : `// fonction qui calcule la moyenne`
- Appuyer sur `Enter`
- Copilot devrait suggérer du code (en gris)
- Appuyer sur `Tab` pour accepter

---

### Configuration recommandée

**Fichier `settings.json`** (VS Code) :

```json
{
  // Activer Copilot pour les langages souhaités
  "github.copilot.enable": {
    "*": true,
    "yaml": false,
    "plaintext": false,
    "markdown": false
  },

  // Nombre de suggestions inline
  "github.copilot.advanced": {
    "inlineSuggestCount": 3
  },

  // Auto-trigger des suggestions
  "editor.inlineSuggest.enabled": true,

  // Raccourcis clavier
  "github.copilot.editor.enableAutoCompletions": true
}
```

**Accès au fichier `settings.json`** :
- `Cmd/Ctrl + Shift + P`
- Taper "Preferences: Open Settings (JSON)"
- Ajouter la configuration ci-dessus

---

### Raccourcis clavier essentiels

| Action | Raccourci (Mac) | Raccourci (Windows/Linux) |
|--------|----------------|--------------------------|
| Accepter suggestion | `Tab` | `Tab` |
| Refuser suggestion | `Esc` | `Esc` |
| Suggestion suivante | `Option + ]` | `Alt + ]` |
| Suggestion précédente | `Option + [` | `Alt + [` |
| Ouvrir panel Copilot | `Cmd + I` | `Ctrl + I` |
| Générer code à partir de commentaire | Écrire commentaire + `Enter` | Écrire commentaire + `Enter` |

---

### Installation (autres IDEs)

#### JetBrains (IntelliJ, PyCharm, WebStorm, etc.)

1. Aller dans `Preferences/Settings` → `Plugins`
2. Chercher "GitHub Copilot"
3. Installer et redémarrer
4. Se connecter à GitHub

#### Neovim

```bash
# Installer le plugin via vim-plug
Plug 'github/copilot.vim'

# Redémarrer Neovim et exécuter
:Copilot setup
```

#### Visual Studio

1. Extensions → Manage Extensions
2. Chercher "GitHub Copilot"
3. Installer et redémarrer

---

## ChatGPT

### Présentation

- **Type** : Assistant conversationnel (web + mobile + API)
- **Prix** : Gratuit (GPT-3.5) / 20$/mois (GPT-4, Plus)
- **Points forts** : Raisonnement complexe, plugins, DALL-E
- **Prérequis** : Compte OpenAI

---

### Inscription

1. Aller sur [chat.openai.com](https://chat.openai.com)
2. Cliquer sur "Sign up"
3. Créer un compte (email ou Google/Microsoft)
4. Vérifier l'email

**Version gratuite** :
- Accès à GPT-3.5
- Limité en requêtes (pas de limite stricte)
- Pas de plugins

**Version Plus (20$/mois)** :
- Accès à GPT-4 (plus puissant)
- Plugins (recherche web, Python, DALL-E)
- Priorité en cas de forte demande

---

### Configuration recommandée

#### Créer des conversations dédiées

**Bonne pratique** :
- 1 conversation = 1 projet ou 1 fonctionnalité
- Titres explicites : "Projet XYZ - Refactoring Auth"

**Exemples** :
```
📁 Mes conversations ChatGPT
  ├── Projet E-commerce - API REST
  ├── Projet E-commerce - Frontend React
  ├── Projet E-commerce - Tests
  ├── Bug #1234 - Race condition
  ├── Formation TypeScript
  └── Veille techno
```

#### Activer le mode "Code Interpreter"

1. Ouvrir ChatGPT
2. Cliquer sur votre profil (en bas à gauche)
3. Settings → Beta features
4. Activer "Code interpreter"

**Usage** : Permet d'exécuter du code Python directement dans ChatGPT.

---

### Extensions navigateur

#### ChatGPT for Google (Chrome/Firefox)

**Installation** :
1. Chrome : [Chrome Web Store](https://chrome.google.com/webstore)
2. Chercher "ChatGPT for Google"
3. Installer

**Usage** : Affiche les réponses ChatGPT à côté des résultats Google.

#### Prompt Genius (sauvegarde de prompts)

**Installation** :
1. [Chrome Web Store](https://chrome.google.com/webstore)
2. Chercher "Prompt Genius"
3. Installer

**Usage** : Sauvegarde et réutilise vos meilleurs prompts.

---

## Claude

### Présentation

- **Type** : Assistant conversationnel (web + API)
- **Prix** : Gratuit / 20$/mois (Pro)
- **Points forts** : Contexte énorme (200k tokens), excellente analyse de code
- **Prérequis** : Compte Anthropic

---

### Inscription

1. Aller sur [claude.ai](https://claude.ai)
2. Cliquer sur "Sign up"
3. Créer un compte (email ou Google)
4. Vérifier l'email

**Version gratuite** :
- Accès à Claude 3 Sonnet
- Limité en requêtes (~30-50/jour)

**Version Pro (20$/mois)** :
- Accès à Claude 3 Opus (le plus puissant)
- 5x plus de requêtes
- Priorité

---

### Fonctionnalités clés

#### Artifacts (génération de code interactive)

**Activation** :
1. Ouvrir Claude
2. Cliquer sur votre profil
3. Feature Preview → Activer "Artifacts"

**Usage** :
```
Prompt : Crée un composant React pour un formulaire de login

→ Claude génère le code dans un panneau séparé (Artifact)
→ Vous pouvez copier, modifier, télécharger
```

#### Projects (contexte persistant)

**Création** :
1. Cliquer sur "New Project"
2. Nommer le projet : "Projet E-commerce"
3. Ajouter des fichiers de contexte (README, schéma DB, etc.)

**Avantage** : Claude garde le contexte du projet entre les sessions.

---

### Configuration recommandée

**Organisation** :
```
📁 Mes projets Claude
  ├── Projet E-commerce (contexte : README.md, schema.sql)
  ├── Migration Python 2→3 (contexte : requirements.txt, code samples)
  ├── Formation IA (contexte : notes, ressources)
  └── Veille techno
```

---

## Cursor

### Présentation

- **Type** : IDE complet avec IA native
- **Prix** : Gratuit (limité) / 20$/mois (Pro)
- **Points forts** : Chat contextuel, génération de code multi-fichiers
- **Prérequis** : Aucun

---

### Installation

#### macOS

1. Télécharger : [cursor.sh](https://cursor.sh)
2. Ouvrir le fichier `.dmg`
3. Glisser Cursor dans Applications
4. Ouvrir Cursor

#### Windows

1. Télécharger : [cursor.sh](https://cursor.sh)
2. Exécuter l'installateur `.exe`
3. Suivre les instructions

#### Linux

```bash
# Télécharger
wget https://cursor.sh/download/linux

# Installer
sudo dpkg -i cursor_*.deb
```

---

### Configuration initiale

#### Étape 1 : Créer un compte

1. Ouvrir Cursor
2. Cliquer sur "Sign up"
3. Créer un compte (email ou Google)

#### Étape 2 : Importer vos paramètres VS Code (optionnel)

1. `Cmd/Ctrl + Shift + P`
2. Taper "Import VS Code settings"
3. Sélectionner votre profil VS Code

#### Étape 3 : Configurer le modèle IA

1. Cliquer sur l'icône ⚙️ (Settings)
2. Onglet "AI"
3. Choisir le modèle :
   - **GPT-4** (recommandé pour Pro)
   - **GPT-3.5** (plus rapide, gratuit)
   - **Claude 3 Opus** (meilleure analyse de code)

---

### Fonctionnalités clés

#### 1. Chat contextuel (`Cmd/Ctrl + L`)

**Usage** :
```
1. Sélectionner du code
2. Cmd/Ctrl + L
3. Poser une question : "Explique ce code"
4. L'IA analyse le code sélectionné
```

#### 2. Génération multi-fichiers (`Cmd/Ctrl + K`)

**Usage** :
```
1. Cmd/Ctrl + K
2. Décrire la feature : "Créer un endpoint POST /users avec validation"
3. L'IA génère le code dans plusieurs fichiers (route, controller, test)
```

#### 3. Terminal intégré avec IA

**Usage** :
```
1. Ouvrir le terminal
2. Cmd/Ctrl + K dans le terminal
3. Demander : "Commande pour installer React Router"
4. L'IA suggère : npm install react-router-dom
```

---

### Configuration recommandée

**Fichier `settings.json`** :

```json
{
  "cursor.ai.model": "gpt-4",
  "cursor.ai.temperature": 0.2,
  "cursor.ai.maxTokens": 2000,
  "cursor.ai.enableInlineChat": true,
  "cursor.ai.enableTerminalSuggestions": true
}
```

---

## Alternatives

### Tabnine

**Installation (VS Code)** :
```bash
code --install-extension TabNine.tabnine-vscode
```

**Prix** :
- Gratuit : complétion basique
- Pro (12$/mois) : complétion avancée
- Enterprise (39$/mois) : modèle on-premise

**Avantages** :
- ✅ Version on-premise possible (sécurité)
- ✅ Support multi-langages
- ❌ Moins performant que Copilot

---

### Amazon CodeWhisperer

**Installation (VS Code)** :
```bash
code --install-extension AmazonWebServices.aws-toolkit-vscode
```

**Prix** : Gratuit pour usage individuel

**Avantages** :
- ✅ Gratuit
- ✅ Excellente intégration AWS SDK
- ❌ Moins bon sur code non-AWS

---

### Codeium

**Installation (VS Code)** :
```bash
code --install-extension Codeium.codeium
```

**Prix** : Gratuit

**Avantages** :
- ✅ Gratuit
- ✅ Rapide
- ❌ Moins précis que Copilot

---

### Sourcegraph Cody

**Installation (VS Code)** :
```bash
code --install-extension sourcegraph.cody-ai
```

**Prix** :
- Gratuit (limité)
- Pro (9$/mois)
- Enterprise (sur devis)

**Avantages** :
- ✅ Compréhension de codebase complète
- ✅ Recherche sémantique
- ❌ Nécessite indexation

---

## APIs et automatisation

### OpenAI API

#### Installation

```bash
# Python
pip install openai

# Node.js
npm install openai
```

#### Configuration

**Python** :
```python
import openai

openai.api_key = "sk-..."  # Votre clé API

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Explique le pattern Repository"}
    ]
)

print(response.choices[0].message.content)
```

**Node.js** :
```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

const response = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [
    { role: "user", content: "Explique le pattern Repository" }
  ]
});

console.log(response.choices[0].message.content);
```

#### Obtenir une clé API

1. Aller sur [platform.openai.com](https://platform.openai.com)
2. Se connecter
3. API Keys → Create new secret key
4. Copier la clé (commence par `sk-...`)

**Prix** :
- GPT-3.5-turbo : $0.001 / 1k tokens (~500 mots)
- GPT-4 : $0.03 / 1k tokens
- GPT-4-turbo : $0.01 / 1k tokens

---

### Anthropic API (Claude)

#### Installation

```bash
# Python
pip install anthropic

# Node.js
npm install @anthropic-ai/sdk
```

#### Configuration

**Python** :
```python
import anthropic

client = anthropic.Anthropic(api_key="sk-ant-...")

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explique le pattern Repository"}
    ]
)

print(message.content[0].text)
```

**Node.js** :
```javascript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY
});

const message = await client.messages.create({
  model: "claude-3-opus-20240229",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "Explique le pattern Repository" }
  ]
});

console.log(message.content[0].text);
```

**Prix** :
- Claude 3 Haiku : $0.00025 / 1k tokens (le moins cher)
- Claude 3 Sonnet : $0.003 / 1k tokens
- Claude 3 Opus : $0.015 / 1k tokens

---

## Configuration avancée

### Variables d'environnement

**Créer un fichier `.env`** :
```bash
# .env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GITHUB_TOKEN=ghp_...
```

**Charger avec Python** :
```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
```

**Charger avec Node.js** :
```javascript
import dotenv from 'dotenv';
dotenv.config();

const apiKey = process.env.OPENAI_API_KEY;
```

---

### Intégration CI/CD

**GitHub Actions (génération automatique de docs)** :

```yaml
# .github/workflows/auto-docs.yml
name: Auto Documentation

on:
  push:
    branches: [main]

jobs:
  generate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Generate documentation
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python scripts/generate_docs_ai.py

      - name: Commit changes
        run: |
          git config user.name "AI Bot"
          git add docs/
          git commit -m "docs: Auto-generate documentation"
          git push
```

---

## Troubleshooting

### GitHub Copilot

#### Problème : Suggestions ne s'affichent pas

**Solutions** :
1. Vérifier que Copilot est activé :
   - `Cmd/Ctrl + Shift + P` → "GitHub Copilot: Enable"

2. Vérifier la connexion :
   - Icône Copilot (barre latérale) → Status

3. Redémarrer VS Code

4. Vérifier les settings :
   ```json
   "github.copilot.enable": {
     "*": true
   }
   ```

#### Problème : Abonnement non reconnu

**Solutions** :
1. Se déconnecter et se reconnecter :
   - `Cmd/Ctrl + Shift + P` → "GitHub Copilot: Sign out"
   - Puis "GitHub Copilot: Sign in"

2. Vérifier l'abonnement :
   - [github.com/settings/copilot](https://github.com/settings/copilot)

---

### ChatGPT

#### Problème : Erreur "Too many requests"

**Solutions** :
1. Attendre 1 heure
2. Passer à ChatGPT Plus (20$/mois) pour éviter les limites

#### Problème : Réponses coupées

**Solutions** :
1. Demander "Continue"
2. Utiliser Claude (contexte plus large)

---

### Claude

#### Problème : Limite de requêtes atteinte

**Solutions** :
1. Attendre le reset (toutes les 8h en version gratuite)
2. Passer à Claude Pro (20$/mois)

---

### API OpenAI

#### Problème : Rate limit exceeded

**Solutions** :
1. Ralentir les requêtes (ajouter `time.sleep(1)`)
2. Passer à un tier supérieur (plus de requêtes/min)

#### Problème : Insufficient quota

**Solutions** :
1. Vérifier le billing : [platform.openai.com/account/billing](https://platform.openai.com/account/billing)
2. Ajouter des crédits

---

## 🚀 Checklist de démarrage

### Pour développeurs

```
☐ Installer GitHub Copilot dans VS Code
☐ Configurer settings.json
☐ Tester la complétion de code
☐ Créer un compte ChatGPT
☐ Créer un compte Claude
☐ Tester 3-5 prompts de base
☐ Lire la bibliothèque de prompts
```

### Pour équipes

```
☐ Acheter licences GitHub Copilot (10$/dev)
☐ Décider : ChatGPT Plus ou Claude Pro ?
☐ Créer comptes d'équipe
☐ Former les développeurs (2h)
☐ Distribuer le Quick Start Dev
☐ Créer un canal Slack/Teams #ia-dev
☐ Mettre en place le suivi (métriques)
```

---

## 📚 Ressources

- [Quick Start Dev](../guides/Quick_Start_Dev.md) → Premiers pas
- [Bibliothèque de prompts](./prompts_library.md) → Prompts prêts à l'emploi
- [Métriques](./metrics_templates.md) → Mesurer l'impact

**Liens officiels** :
- [GitHub Copilot Docs](https://docs.github.com/en/copilot)
- [ChatGPT Help](https://help.openai.com)
- [Claude Documentation](https://docs.anthropic.com)
- [Cursor Docs](https://cursor.sh/docs)

---

**Temps d'installation total : 30 minutes**

🚀 **Vous êtes prêt ! Commencez à coder avec l'IA dès maintenant.**
