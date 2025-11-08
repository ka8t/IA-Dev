# 🌍 Traductions / Translations

Ce dossier contient les traductions de la documentation **AI Driven Dev** dans différentes langues.

---

## 📋 Langues disponibles

| Langue | Code | Statut | Contributeurs |
|--------|------|--------|---------------|
| 🇫🇷 Français | `fr` | ✅ Complet | Équipe principale |
| 🇬🇧 English | `en` | 🚧 En cours | À venir |
| 🇪🇸 Español | `es` | ⏳ Planifié | Besoin de contributeurs |
| 🇩🇪 Deutsch | `de` | ⏳ Planifié | Besoin de contributeurs |

---

## 🎯 Comment contribuer une traduction

### Étape 1 : Vérifier qu'elle n'existe pas déjà

Consultez la liste ci-dessus et les [issues de traduction](https://github.com/your-repo/issues?q=label%3Atranslation).

### Étape 2 : Créer une issue

Ouvrez une issue avec le titre : `[Translation] Add [Language] translation`

Exemple : `[Translation] Add Spanish translation`

### Étape 3 : Structure à suivre

Créez un dossier avec le code de langue (ISO 639-1) :

```
translations/
└── en/                           # Code langue
    ├── README.md                 # README traduit
    ├── guides/
    │   ├── Quick_Start_Dev.md
    │   ├── Quick_Start_Manager.md
    │   └── AI_Driven_Dev_Guide.md
    ├── resources/
    │   ├── prompts_library.md
    │   ├── metrics_templates.md
    │   └── tools_setup.md
    └── FAQ.md
```

### Étape 4 : Fichiers prioritaires à traduire

**Priorité HAUTE** (minimum pour une langue) :
1. `README.md` - Page d'accueil
2. `guides/Quick_Start_Dev.md` - Guide développeur
3. `FAQ.md` - Questions fréquentes

**Priorité MOYENNE** :
4. `guides/Quick_Start_Manager.md` - Guide manager
5. `resources/prompts_library.md` - Bibliothèque de prompts
6. `CONTRIBUTING.md` - Guide de contribution

**Priorité BASSE** :
7. `guides/AI_Driven_Dev_Guide.md` - Guide complet
8. `resources/metrics_templates.md` - Templates de métriques
9. Tous les autres fichiers

### Étape 5 : Standards de traduction

#### ✅ À faire :
- Traduire le contenu tout en gardant le sens original
- Adapter les exemples au contexte culturel si nécessaire
- Conserver les termes techniques en anglais entre parenthèses la première fois
- Maintenir la même structure de fichiers
- Traduire les commentaires de code
- Mettre à jour les liens internes vers les fichiers traduits

#### ❌ À éviter :
- Traduction mot-à-mot sans contexte
- Changer la structure ou l'organisation
- Traduire les noms de variables/fonctions dans le code
- Oublier de mettre à jour les liens

#### Exemple :

**Français (original) :**
```markdown
## 🎯 Framework RACE

RACE est un framework pour structurer vos prompts :
- **R**ole : Qui est l'IA
- **A**ction : Ce qu'elle doit faire
- **C**ontext : Le contexte métier
- **E**xpectations : Le résultat attendu
```

**Anglais (traduction) :**
```markdown
## 🎯 RACE Framework

RACE is a framework for structuring your prompts:
- **R**ole: Who the AI is
- **A**ction: What it should do
- **C**ontext: Business context
- **E**xpectations: Expected output
```

### Étape 6 : Glossaire de termes

Utilisez le glossaire pour maintenir la cohérence :

| Français | English | Español | Deutsch |
|----------|---------|---------|---------|
| Développeur | Developer | Desarrollador | Entwickler |
| Manager | Manager | Gerente | Manager |
| Prompt | Prompt | Prompt | Prompt |
| IA / Intelligence Artificielle | AI / Artificial Intelligence | IA / Inteligencia Artificial | KI / Künstliche Intelligenz |
| Code review | Code review | Revisión de código | Code-Review |
| Productivité | Productivity | Productividad | Produktivität |
| ROI | ROI | ROI | ROI |
| Tests unitaires | Unit tests | Pruebas unitarias | Unit-Tests |

### Étape 7 : Tester la traduction

Avant de soumettre :

- [ ] Tous les liens fonctionnent
- [ ] Le formatage Markdown est correct
- [ ] Les exemples de code sont inchangés
- [ ] Les termes sont cohérents dans toute la traduction
- [ ] Relecture par un natif (si possible)

### Étape 8 : Soumettre la Pull Request

Titre : `[Translation] Add [Language] translation - [Files]`

Exemple : `[Translation] Add Spanish translation - README and Quick Start`

---

## 🤖 Utiliser l'IA pour traduire

Vous pouvez utiliser l'IA pour accélérer la traduction, mais **relisez toujours** !

### Prompt RACE pour traduction

```
Role : Tu es un traducteur technique expert en documentation logicielle.

Action : Traduis ce document Markdown du français vers l'anglais.

Context :
- Document : AI Driven Dev - Guide technique
- Public : Développeurs et managers tech internationaux
- Ton : Professionnel mais accessible
- Fichier source : [nom du fichier]

Expectations :
- Traduction fidèle au sens original
- Maintenir tout le formatage Markdown
- Ne pas traduire le code ni les noms de variables
- Conserver les émojis
- Adapter les exemples au contexte anglophone si nécessaire
- Traduire les commentaires de code
- Format de sortie : Markdown prêt à copier/coller
```

---

## 📊 État d'avancement des traductions

### 🇬🇧 English (en)

**Progression : 0%**

- [ ] README.md
- [ ] guides/Quick_Start_Dev.md
- [ ] guides/Quick_Start_Manager.md
- [ ] FAQ.md
- [ ] CONTRIBUTING.md
- [ ] resources/prompts_library.md

**Besoin d'aide ?** [Ouvrir une issue](https://github.com/your-repo/issues/new)

---

### 🇪🇸 Español (es)

**Progression : 0%**

Aucune traduction démarrée. Contributeurs recherchés !

---

### 🇩🇪 Deutsch (de)

**Progression : 0%**

Aucune traduction démarrée. Contributeurs recherchés !

---

## 🙏 Reconnaissance

Tous les traducteurs seront crédités dans :
- Le README principal
- Le fichier de traduction correspondant
- La section Contributors

**Merci de rendre AI Driven Dev accessible au monde entier ! 🌍**

---

## 💬 Questions ?

- Ouvrez une [Discussion](https://github.com/your-repo/discussions)
- Rejoignez notre [Discord](#) (à venir)
- Contactez l'équipe via [Issue](https://github.com/your-repo/issues)

---

*Dernière mise à jour : 2025-11-08*
