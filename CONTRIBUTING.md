# 🤝 Guide de Contribution

Merci de votre intérêt pour contribuer à **AI Driven Dev** ! Ce guide vous aidera à contribuer efficacement au projet.

---

## 📋 Table des matières

- [Code de conduite](#code-de-conduite)
- [Comment contribuer](#comment-contribuer)
- [Types de contributions](#types-de-contributions)
- [Processus de contribution](#processus-de-contribution)
- [Standards de qualité](#standards-de-qualité)
- [Structure du projet](#structure-du-projet)
- [Ressources utiles](#ressources-utiles)

---

## 📜 Code de conduite

En participant à ce projet, vous vous engagez à :

- ✅ Respecter tous les contributeurs
- ✅ Accepter les critiques constructives
- ✅ Collaborer de manière positive
- ✅ Maintenir un environnement accueillant

Nous ne tolèrerons aucun comportement irrespectueux, discriminatoire ou harcelant.

---

## 🎯 Comment contribuer

### Vous pouvez contribuer de plusieurs façons :

1. **📝 Documentation** : Améliorer les guides, corriger des typos
2. **💡 Exemples** : Ajouter de nouveaux cas d'usage pratiques
3. **🐛 Bugs** : Signaler ou corriger des erreurs
4. **✨ Fonctionnalités** : Proposer de nouvelles idées
5. **🌍 Traductions** : Traduire le contenu en d'autres langues
6. **📊 Retours d'expérience** : Partager vos résultats avec l'IA

---

## 📝 Types de contributions

### 1. Documentation

**Ce qu'on recherche :**
- Corrections de typos et fautes de grammaire
- Clarifications sur des points complexes
- Nouveaux guides ou tutoriels
- Amélioration des diagrammes

**Comment contribuer :**
1. Modifiez le fichier Markdown concerné
2. Vérifiez que les liens fonctionnent
3. Assurez-vous que le formatage est correct
4. Soumettez une Pull Request

**Exemple de contribution documentation :**
```markdown
### Avant
L'IA peut générer du code.

### Après
L'IA peut générer du code de qualité production en utilisant des prompts structurés
avec le framework RACE (Role, Action, Context, Expectations).
```

---

### 2. Nouveaux exemples pratiques

**Ce qu'on recherche :**
- Exemples réels et testés
- Code fonctionnel et commenté
- Métriques de résultats (temps gagné, qualité)
- Prompts RACE utilisés

**Structure d'un exemple :**
```
examples/XX_nom_exemple/
├── README.md              # Description complète
├── before/                # Code avant IA (si applicable)
│   └── code.js
├── after/                 # Code généré par IA
│   └── code.js
├── prompts/               # Prompts RACE utilisés
│   └── prompt.txt
├── results/               # Résultats et métriques
│   └── metrics.md
└── package.json           # Dépendances
```

**Template README pour un exemple :**
```markdown
# 🎯 Exemple XX : [Titre]

## Objectif
[Ce que cet exemple démontre]

## Contexte
- Situation initiale
- Problème à résoudre
- Stack technique

## Processus
### Prompt RACE utilisé
[Le prompt complet]

### Résultats
| Métrique | Avant IA | Avec IA | Gain |
|----------|----------|---------|------|
| Temps | Xh | Ymin | Z% |

## Code généré
[Le code ou lien vers fichiers]

## Leçons apprises
[Ce que vous avez appris]
```

---

### 3. Rapports de bugs

**Avant de signaler un bug :**
- ✅ Vérifiez que le bug n'a pas déjà été signalé
- ✅ Assurez-vous que c'est bien un bug (pas une question)
- ✅ Testez avec la dernière version

**Utilisez le template de bug report :**
- Allez dans `Issues → New Issue → Bug Report`
- Remplissez toutes les sections
- Ajoutez des captures d'écran si pertinent

---

### 4. Nouvelles fonctionnalités

**Avant de proposer une feature :**
1. Vérifiez qu'elle n'existe pas déjà
2. Ouvrez une issue pour discussion
3. Attendez validation avant de coder

**Processus :**
1. `Issues → New Issue → Feature Request`
2. Décrivez le problème que ça résout
3. Proposez une solution
4. Discutez avec les mainteneurs
5. Une fois validé, créez une Pull Request

---

## 🔄 Processus de contribution

### Étape 1 : Fork et Clone

```bash
# Fork le projet via GitHub UI, puis :
git clone https://github.com/VOTRE-USERNAME/IA-Dev.git
cd IA-Dev
```

### Étape 2 : Créer une branche

```bash
# Convention de nommage :
# - docs/description       (pour documentation)
# - feature/description    (pour nouvelles fonctionnalités)
# - fix/description        (pour corrections de bugs)
# - example/description    (pour nouveaux exemples)

git checkout -b docs/ameliorer-quickstart
```

### Étape 3 : Faire vos modifications

- ✅ Suivez les standards de qualité (voir section suivante)
- ✅ Testez vos modifications
- ✅ Vérifiez les liens et le formatage

### Étape 4 : Commit vos changements

```bash
# Convention de commit :
# - docs: pour documentation
# - feat: pour nouvelles fonctionnalités
# - fix: pour corrections
# - example: pour exemples
# - chore: pour maintenance

git add .
git commit -m "docs: améliorer le guide quick start avec exemples concrets"
```

**Bonnes pratiques de commit :**
- ✅ Message en français ou anglais (cohérent avec le projet)
- ✅ Descriptif et concis
- ✅ Utilise les préfixes conventionnels
- ✅ Un commit = une modification logique

### Étape 5 : Push et Pull Request

```bash
git push origin docs/ameliorer-quickstart
```

Puis sur GitHub :
1. Allez sur votre fork
2. Cliquez "Compare & pull request"
3. Remplissez le template de PR
4. Attendez la review

---

## ✅ Standards de qualité

### Documentation

**Markdown :**
- ✅ Titres avec émojis pour clarté
- ✅ Code blocks avec syntaxe highlighting
- ✅ Liens relatifs pour navigation interne
- ✅ Table des matières pour docs longues

**Exemple :**
```markdown
## 🎯 Section avec émoji

Texte avec `code inline` et [lien](./autre-doc.md).

\`\`\`python
# Code avec highlighting
def example():
    pass
\`\`\`
```

### Code

**Python :**
- ✅ PEP 8 compliant
- ✅ Type hints quand possible
- ✅ Docstrings pour fonctions/classes
- ✅ Tests unitaires

**JavaScript/Node.js :**
- ✅ ESLint + Prettier
- ✅ JSDoc pour documentation
- ✅ Tests avec Jest/Mocha

**Exemple Python :**
```python
def validate_email(email: str) -> bool:
    """
    Validate email format.

    Args:
        email: Email address to validate

    Returns:
        True if valid, False otherwise

    Example:
        >>> validate_email("user@example.com")
        True
    """
    # Implementation
```

### Prompts RACE

**Structure obligatoire :**
```
Role : [Qui est l'IA]

Action : [Ce qu'elle doit faire]

Context :
- [Élément de contexte 1]
- [Élément de contexte 2]

Expectations :
- [Attente 1]
- [Attente 2]
```

---

## 📁 Structure du projet

```
IA-Dev/
├── README.md                    # Page d'accueil
├── CONTRIBUTING.md              # Ce fichier
├── FAQ.md                       # Questions fréquentes
├── guides/                      # Guides détaillés
│   ├── Quick_Start_Dev.md
│   ├── Quick_Start_Manager.md
│   └── AI_Driven_Dev_Guide.md
├── resources/                   # Ressources pratiques
│   ├── prompts_library.md       # 28+ prompts RACE
│   ├── metrics_templates.md     # Templates de métriques
│   └── tools_setup.md           # Installation des outils
├── examples/                    # 5 exemples pratiques
│   ├── 01_code_generation/
│   ├── 02_test_automation/
│   ├── 03_documentation/
│   ├── 04_ci_cd_integration/
│   └── 05_security_review/
├── assets/                      # Diagrammes et visuels
│   └── diagrams/
├── scripts/                     # Scripts d'automatisation
└── .github/                     # Templates GitHub
    ├── ISSUE_TEMPLATE/
    └── workflows/
```

---

## 🔍 Checklist avant de soumettre une PR

### Pour Documentation

- [ ] Pas de fautes d'orthographe ou grammaire
- [ ] Tous les liens fonctionnent
- [ ] Le formatage Markdown est correct
- [ ] Les exemples de code sont testés
- [ ] Les diagrammes sont à jour (si modifiés)

### Pour Exemples de code

- [ ] Le code fonctionne (testé localement)
- [ ] Les dépendances sont listées (requirements.txt ou package.json)
- [ ] Le README de l'exemple est complet
- [ ] Les prompts RACE sont fournis
- [ ] Les métriques de résultats sont incluses
- [ ] Le code est commenté

### Pour Scripts

- [ ] Le script a un help message (-h)
- [ ] Les dépendances sont documentées
- [ ] Le code gère les erreurs correctement
- [ ] Des exemples d'utilisation sont fournis

---

## 🎓 Ressources utiles

### Markdown
- [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/)
- [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)

### Diagrammes Mermaid
- [Mermaid Documentation](https://mermaid.js.org/)
- [Mermaid Live Editor](https://mermaid.live/)

### Git & GitHub
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

### Prompts IA
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

---

## 💬 Questions ?

- 💬 Ouvrez une [Discussion](https://github.com/your-repo/discussions)
- 🐛 Signalez un [Bug](https://github.com/your-repo/issues/new?template=bug_report.md)
- 💡 Proposez une [Feature](https://github.com/your-repo/issues/new?template=feature_request.md)

---

## 🙏 Reconnaissance

Tous les contributeurs seront ajoutés à la section "Contributors" du README.

**Merci de contribuer à AI Driven Dev !** 🚀

---

*Dernière mise à jour : 2025-11-08*