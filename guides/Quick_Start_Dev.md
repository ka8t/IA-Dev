# 👨‍💻 Quick Start Dev — Devenez un Développeur Augmenté

## 🎯 Objectif

Ce guide vous permet de **devenir opérationnel avec l'IA en moins de 30 minutes** et d'intégrer des assistants IA dans votre workflow quotidien de développement.

---

## 📋 Table des matières

- [Prérequis](#prérequis)
- [Étape 1 : Choisir vos outils IA](#étape-1--choisir-vos-outils-ia)
- [Étape 2 : Configuration initiale](#étape-2--configuration-initiale)
- [Étape 3 : Premiers prompts efficaces](#étape-3--premiers-prompts-efficaces)
- [Étape 4 : Intégrer l'IA dans votre workflow](#étape-4--intégrer-lia-dans-votre-workflow)
- [Bonnes pratiques](#bonnes-pratiques)
- [Erreurs courantes à éviter](#erreurs-courantes-à-éviter)
- [Prochaines étapes](#prochaines-étapes)

---

## Prérequis

- Un IDE moderne (VS Code, JetBrains, etc.)
- Connexion internet stable
- Compte GitHub (pour Copilot) ou compte OpenAI/Anthropic
- Budget : 0€ (versions gratuites) à 50€/mois (versions pro)

---

## Étape 1 : Choisir vos outils IA

### 🔧 Outils recommandés par cas d'usage

| Outil | Idéal pour | Prix | Intégration IDE |
|-------|-----------|------|-----------------|
| **GitHub Copilot** | Complétion de code en temps réel | 10$/mois | ⭐⭐⭐⭐⭐ |
| **ChatGPT Plus** | Questions complexes, architecture | 20$/mois | ⭐⭐ |
| **Claude Pro** | Analyse de code, refactoring | 20$/mois | ⭐⭐ |
| **Cursor** | IDE avec IA intégrée | 20$/mois | ⭐⭐⭐⭐⭐ |
| **Tabnine** | Alternative à Copilot, on-premise | Gratuit-39$/mois | ⭐⭐⭐⭐ |

### 💡 Recommandation pour débuter

**Combo gagnant** :
1. **GitHub Copilot** (IDE) → complétion en temps réel
2. **ChatGPT Free ou Claude Free** (navigateur) → questions complexes

**Coût total : 10€/mois** (Copilot uniquement) ou **0€** (versions gratuites)

---

## Étape 2 : Configuration initiale

### A. Installer GitHub Copilot (VS Code)

```bash
# 1. Installer VS Code si nécessaire
# 2. Installer l'extension Copilot
code --install-extension GitHub.copilot

# 3. Redémarrer VS Code et se connecter avec GitHub
```

**Configuration recommandée** (`settings.json`) :

```json
{
  "github.copilot.enable": {
    "*": true,
    "yaml": false,
    "plaintext": false,
    "markdown": false
  },
  "github.copilot.advanced": {
    "inlineSuggestCount": 3
  }
}
```

### B. Configurer ChatGPT / Claude

1. Créer un compte sur [chat.openai.com](https://chat.openai.com) ou [claude.ai](https://claude.ai)
2. Activer le mode "Code Interpreter" (ChatGPT) ou "Artifacts" (Claude)
3. Créer des conversations dédiées par projet

**Organisation recommandée** :
- 1 conversation = 1 projet ou 1 fonctionnalité
- Titres explicites : "Projet XYZ - Refactoring Auth"

---

## Étape 3 : Premiers prompts efficaces

### 🧠 Framework RACE pour des prompts de qualité

**R**ole — **A**ction — **C**ontext — **E**xpectations

#### Exemple 1 : Génération de code

❌ **Mauvais prompt** :
```
Crée une fonction pour calculer la moyenne
```

✅ **Bon prompt** :
```
Role : Tu es un développeur Python senior.

Action : Crée une fonction calculate_average() qui :
- Prend une liste de nombres en entrée
- Gère les cas limites (liste vide, valeurs nulles)
- Retourne la moyenne ou None si impossible

Context : Pour un projet d'analyse de données, Python 3.11, typage strict.

Expectations :
- Code avec type hints
- Docstring Google style
- Tests unitaires pytest
- Gestion d'erreurs explicite
```

#### Exemple 2 : Revue de code

```
Role : Tu es un code reviewer senior spécialisé en sécurité.

Action : Analyse cette fonction d'authentification et identifie :
- Les vulnérabilités de sécurité
- Les problèmes de performance
- Les violations de bonnes pratiques

Context : API REST Node.js, Express, production avec 10k users/jour.

[COLLER LE CODE ICI]

Expectations :
- Liste priorisée des issues (Critical, High, Medium, Low)
- Suggestion de correction pour chaque issue
- Explication pédagogique
```

#### Exemple 3 : Debugging

```
Role : Tu es un expert en debugging Python.

Action : Aide-moi à comprendre pourquoi ce code génère une erreur.

Context :
- Erreur : KeyError: 'user_id'
- Environnement : Django 4.2, PostgreSQL
- Se produit sur la route /api/users/profile

[COLLER LE CODE + TRACEBACK]

Expectations :
- Explication de la cause racine
- Solution pas à pas
- Comment éviter ce type d'erreur à l'avenir
```

---

## Étape 4 : Intégrer l'IA dans votre workflow

### 🔄 Workflow quotidien recommandé

#### **1. Début de journée (5 min)**
```
Prompt à l'IA :
"Voici mes tâches du jour : [liste des issues/tickets]
Propose-moi un ordre optimal et identifie les risques potentiels."
```

#### **2. Avant de coder (10 min)**
```
Prompt :
"Je vais implémenter [fonctionnalité].
Voici le contexte : [specs, contraintes, architecture existante]
Propose-moi 3 approches différentes avec leurs avantages/inconvénients."
```

#### **3. Pendant le développement**
- Utiliser Copilot pour la complétion automatique
- Demander à l'IA de générer les tests unitaires
- Valider les choix d'architecture complexes

#### **4. Avant le commit (5 min)**
```
Prompt :
"Voici mon diff Git :
[COLLER LE DIFF]

Vérifie :
- La qualité du code
- Les tests manquants
- Les commentaires nécessaires
- Le message de commit approprié"
```

#### **5. Revue de code (10 min)**
```
Prompt :
"Analyse cette PR et vérifie :
- Sécurité
- Performance
- Maintenabilité
- Tests
- Documentation

[LIEN OU CONTENU DE LA PR]"
```

---

## Bonnes pratiques

### ✅ DO

1. **Itérer sur les prompts** : si la réponse n'est pas satisfaisante, reformulez
2. **Donner du contexte** : partagez votre stack, contraintes, objectifs
3. **Vérifier le code généré** : l'IA peut se tromper ou halluciner
4. **Apprendre des réponses** : comprendre le "pourquoi", pas juste copier
5. **Sécuriser les données** : ne partagez jamais de secrets, tokens, données clients

### ❌ DON'T

1. **Copier-coller aveuglément** : toujours lire et comprendre le code
2. **Partager du code propriétaire sensible** : politique de confidentialité
3. **Remplacer les tests** : l'IA génère des tests, mais vous validez
4. **Ignorer les warnings** : l'IA peut suggérer du code obsolète/vulnérable
5. **Se reposer uniquement sur l'IA** : elle augmente, ne remplace pas

---

## Erreurs courantes à éviter

### 1. Le syndrome du "copier-coller"
**Problème** : Copier du code sans le comprendre
**Solution** : Demander à l'IA d'expliquer ligne par ligne

### 2. Prompts trop vagues
**Problème** : "Fais un serveur web"
**Solution** : Utiliser le framework RACE (Role, Action, Context, Expectations)

### 3. Ne pas itérer
**Problème** : Accepter la première réponse même si insatisfaisante
**Solution** : Dire "Améliore cette réponse en ajoutant..." ou "Refais en simplifiant..."

### 4. Ignorer les tests
**Problème** : Générer du code sans tests
**Solution** : Toujours demander tests unitaires + tests d'intégration

### 5. Exposer des données sensibles
**Problème** : Partager des tokens, mots de passe, données clients
**Solution** : Anonymiser ou remplacer par des placeholders

---

## Prochaines étapes

### 🎓 Approfondir vos compétences

1. Lire le [Guide complet AI Driven Dev](./AI_Driven_Dev_Guide.md)
2. Explorer la [Bibliothèque de prompts](../resources/prompts_library.md)
3. Consulter les [exemples pratiques](../examples/README.md)

### 📊 Mesurer votre progression

Suivez ces métriques pendant 2 semaines :
- **Temps gagné** par tâche (avant/après IA)
- **Qualité** : nombre de bugs trouvés en revue
- **Apprentissage** : nouvelles techniques découvertes via IA

Template : [metrics_templates.md](../resources/metrics_templates.md)

### 🚀 Niveau suivant

- Automatiser avec des scripts (voir [scripts/](../scripts/README.md))
- Intégrer l'IA dans votre CI/CD
- Former votre équipe

---

## 🆘 Besoin d'aide ?

- 📚 Consulter la [FAQ](./FAQ.md)
- 💬 Ouvrir une [issue GitHub](https://github.com/ka8t/IA-Dev/issues)
- 🤝 Partager vos retours d'expérience

---

**Temps de lecture : 10 min**
**Temps de mise en pratique : 20-30 min**
**ROI attendu : +30% productivité dès la première semaine**

🚀 **Vous êtes prêt ! Commencez dès maintenant votre première session de code assisté par IA.**
