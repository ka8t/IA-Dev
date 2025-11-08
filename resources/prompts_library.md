# 🧠 Bibliothèque de Prompts — Framework RACE

## 🎯 Objectif

Cette bibliothèque contient **des prompts prêts à l'emploi** pour les cas d'usage les plus fréquents en développement logiciel. Tous les prompts suivent le **framework RACE** pour maximiser la qualité des réponses.

---

## 📋 Table des matières

1. [Framework RACE](#framework-race)
2. [Génération de code](#génération-de-code)
3. [Tests et qualité](#tests-et-qualité)
4. [Refactoring](#refactoring)
5. [Debugging](#debugging)
6. [Documentation](#documentation)
7. [Revue de code](#revue-de-code)
8. [Architecture](#architecture)
9. [Sécurité](#sécurité)
10. [Performance](#performance)
11. [Base de données](#base-de-données)
12. [DevOps et CI/CD](#devops-et-cicd)

---

## Framework RACE

### Structure

```
Role : [Qui est l'IA ? Expert en quoi ?]
Tu es un [rôle] expert en [domaine].

Action : [Que doit faire l'IA ?]
[Verbe d'action] + [objet] + [détails].

Context : [Informations contextuelles]
- Langage/framework : [stack technique]
- Contraintes : [limites, exigences]
- Environnement : [dev, prod, versions]

Expectations : [Format de sortie attendu]
- [Type de livrable]
- [Niveau de détail]
- [Format spécifique]
```

### Conseils d'utilisation

- ✅ **Personnalisez** chaque prompt selon votre contexte
- ✅ **Itérez** : si la réponse ne convient pas, affinez le prompt
- ✅ **Combinez** plusieurs prompts pour des tâches complexes
- ❌ **Ne copiez pas aveuglément** : relisez et adaptez le code généré

---

## Génération de code

### 1. Créer une fonction

```
Role : Tu es un développeur [LANGAGE] senior expert en [DOMAINE].

Action : Crée une fonction [NOM_FONCTION] qui :
- [Fonctionnalité principale]
- [Cas limites à gérer]
- [Contraintes spécifiques]

Context :
- Langage : [LANGAGE + VERSION]
- Framework : [FRAMEWORK si applicable]
- Environnement : [dev/prod]
- Performance : [critique/normale]

Expectations :
- Code avec type hints/types complets
- Docstring [STYLE : Google/JSDoc/etc.]
- Gestion d'erreurs explicite
- Tests unitaires [FRAMEWORK DE TEST]
- Complexité algorithmique en commentaire
```

**Exemple concret (Python)** :

```
Role : Tu es un développeur Python senior expert en data science.

Action : Crée une fonction calculate_percentile() qui :
- Prend une liste de nombres et un percentile (0-100)
- Calcule le percentile demandé
- Gère les cas limites (liste vide, percentile invalide)
- Supporte différentes méthodes d'interpolation

Context :
- Python 3.11
- Utiliser NumPy si nécessaire
- Code pour un pipeline de data analysis en production
- Performance critique (millions de valeurs)

Expectations :
- Type hints complets
- Docstring Google style
- Tests unitaires pytest (au moins 5 cas de test)
- Gestion d'erreurs avec exceptions custom
- Complexité O(n log n) maximum
```

---

### 2. Créer une classe

```
Role : Tu es un développeur [LANGAGE] expert en programmation orientée objet.

Action : Crée une classe [NOM_CLASSE] qui :
- [Responsabilité principale]
- [Méthodes publiques requises]
- [État interne à gérer]

Context :
- Langage : [LANGAGE + VERSION]
- Principes : SOLID, Clean Code
- Patterns : [PATTERN si applicable]

Expectations :
- Encapsulation correcte (public/private)
- Docstrings pour classe et méthodes
- Type hints complets
- Tests unitaires
- Exemple d'utilisation
```

**Exemple concret (TypeScript)** :

```
Role : Tu es un développeur TypeScript expert en architecture logicielle.

Action : Crée une classe UserRepository qui :
- Implémente le pattern Repository
- Gère les opérations CRUD sur les utilisateurs
- Abstrait la couche de persistence (peut être SQL ou NoSQL)
- Gère les erreurs de base de données

Context :
- TypeScript 5.0
- Utilisation avec Prisma ORM
- Architecture hexagonale
- Tests avec Jest

Expectations :
- Interface IUserRepository
- Classe UserRepository implémentant l'interface
- Type User bien défini
- Gestion d'erreurs avec exceptions custom
- Tests unitaires avec mocks
- JSDoc complet
```

---

### 3. Créer une API REST endpoint

```
Role : Tu es un développeur backend expert en API REST.

Action : Crée un endpoint [MÉTHODE HTTP] [ROUTE] qui :
- [Fonctionnalité]
- [Validation des entrées]
- [Gestion des erreurs]

Context :
- Framework : [EXPRESS/FASTAPI/SPRING/etc.]
- Base de données : [POSTGRESQL/MONGODB/etc.]
- Authentification : [JWT/OAuth/etc.]
- Documentation : OpenAPI/Swagger

Expectations :
- Code de l'endpoint complet
- Validation des paramètres (Joi/Pydantic/etc.)
- Réponses HTTP appropriées (200, 400, 401, 500)
- Tests d'intégration
- Documentation OpenAPI
```

**Exemple concret (Node.js/Express)** :

```
Role : Tu es un développeur backend expert en API REST avec Node.js.

Action : Crée un endpoint POST /api/users qui :
- Crée un nouvel utilisateur
- Valide email unique et format valide
- Hash le mot de passe
- Retourne un token JWT
- Gère les erreurs (email déjà existant, validation échouée)

Context :
- Node.js 20, Express 4.18
- PostgreSQL avec Prisma
- Authentification JWT
- Validation avec Joi
- Tests avec Jest + Supertest

Expectations :
- Code de la route complète
- Middleware de validation
- Gestion d'erreurs avec try/catch
- Tests d'intégration (succès + cas d'erreur)
- Documentation OpenAPI en commentaire
- Code sécurisé (injection SQL, XSS)
```

---

## Tests et qualité

### 4. Générer des tests unitaires

```
Role : Tu es un expert en testing [LANGAGE] avec [FRAMEWORK DE TEST].

Action : Génère une suite de tests unitaires complète pour cette fonction/classe.

Context :
- Code à tester :
[COLLER LE CODE]

- Framework : [JEST/PYTEST/JUNIT/etc.]
- Couverture cible : [80%/100%]
- Mocking : [LIBRARY si nécessaire]

Expectations :
- Au moins [N] cas de test
- Tests pour les cas normaux (happy path)
- Tests pour les cas limites (edge cases)
- Tests pour les erreurs
- Fixtures/setup si nécessaire
- Couverture estimée > [X]%
```

**Exemple concret (Jest)** :

```
Role : Tu es un expert en testing JavaScript avec Jest.

Action : Génère une suite de tests unitaires complète pour cette classe UserService.

Context :
- Code à tester :
```typescript
class UserService {
  constructor(private userRepo: UserRepository) {}

  async createUser(email: string, password: string): Promise<User> {
    if (!this.isValidEmail(email)) {
      throw new Error('Invalid email');
    }
    const existing = await this.userRepo.findByEmail(email);
    if (existing) {
      throw new Error('Email already exists');
    }
    const hashedPassword = await bcrypt.hash(password, 10);
    return this.userRepo.create({ email, password: hashedPassword });
  }

  private isValidEmail(email: string): boolean {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }
}
```

- Framework : Jest 29 + TypeScript
- Mocking : jest.mock
- Couverture cible : 100%

Expectations :
- Tests pour createUser (succès)
- Tests pour email invalide
- Tests pour email déjà existant
- Tests pour erreur du repository
- Mocks du UserRepository
- Au moins 8 cas de test
- Couverture 100%
```

---

### 5. Générer des tests d'intégration

```
Role : Tu es un expert en testing d'intégration [STACK].

Action : Génère des tests d'intégration pour ce endpoint/module.

Context :
- Code à tester :
[COLLER LE CODE]

- Stack : [FRAMEWORK + DB + etc.]
- Environnement de test : [DOCKER/IN-MEMORY/etc.]
- Framework de test : [SUPERTEST/TESTCONTAINERS/etc.]

Expectations :
- Setup de l'environnement de test
- Tests pour les cas nominaux
- Tests pour les erreurs
- Nettoyage après les tests (teardown)
- Tests isolés (pas d'interdépendance)
```

---

### 6. Générer des tests end-to-end

```
Role : Tu es un expert en testing E2E avec [PLAYWRIGHT/CYPRESS/SELENIUM].

Action : Génère des tests E2E pour ce parcours utilisateur :
[DÉCRIRE LE PARCOURS]

Context :
- Application : [REACT/VUE/ANGULAR/etc.]
- Framework E2E : [PLAYWRIGHT/CYPRESS/etc.]
- Environnement : [URL de test]

Expectations :
- Tests du parcours complet
- Assertions visuelles (si pertinent)
- Gestion des timeouts et attentes
- Screenshots en cas d'échec
- Tests résilients (pas de sélecteurs fragiles)
```

---

## Refactoring

### 7. Refactorer du code legacy

```
Role : Tu es un expert en refactoring et clean code [LANGAGE].

Action : Refactore ce code en respectant :
- Principes SOLID
- Clean Code (Robert C. Martin)
- Patterns appropriés
- Lisibilité et maintenabilité

Context :
- Code actuel :
[COLLER LE CODE]

- Langage : [LANGAGE + VERSION]
- Contraintes : [ne pas changer l'API publique/etc.]

Expectations :
- Code refactoré complet
- Explication des changements (avant/après)
- Tests de non-régression
- Amélioration de la complexité cyclomatique
- Élimination des code smells
```

**Exemple concret** :

```
Role : Tu es un expert en refactoring Python et clean code.

Action : Refactore cette fonction en respectant :
- Single Responsibility Principle
- DRY (Don't Repeat Yourself)
- Lisibilité maximale
- Type hints

Context :
- Code actuel :
```python
def process_data(data):
    result = []
    for item in data:
        if item['type'] == 'A':
            result.append(item['value'] * 2)
        elif item['type'] == 'B':
            result.append(item['value'] * 3)
        else:
            result.append(item['value'])
    total = 0
    for r in result:
        total += r
    avg = total / len(result)
    return avg
```

- Python 3.11
- Ne pas changer la signature de la fonction

Expectations :
- Code refactoré avec fonctions extraites
- Type hints complets
- Docstring
- Explication des changements
- Tests de non-régression
```

---

### 8. Simplifier du code complexe

```
Role : Tu es un expert en simplification de code [LANGAGE].

Action : Simplifie ce code en :
- Réduisant la complexité cyclomatique
- Éliminant les nested loops
- Utilisant des structures de données appropriées
- Améliorant la lisibilité

Context :
- Code actuel :
[COLLER LE CODE]

- Complexité actuelle : [CYCLOMATIC COMPLEXITY]
- Objectif : < [TARGET]

Expectations :
- Code simplifié
- Complexité réduite
- Performance maintenue ou améliorée
- Explication des optimisations
```

---

## Debugging

### 9. Analyser une erreur

```
Role : Tu es un expert en debugging [LANGAGE].

Action : Aide-moi à résoudre cette erreur :
[DÉCRIRE L'ERREUR]

Context :
- Erreur : [MESSAGE D'ERREUR]
- Stacktrace :
[COLLER LE STACKTRACE]

- Code concerné :
[COLLER LE CODE]

- Environnement : [OS, VERSION, etc.]
- Se produit : [toujours/intermittent]

Expectations :
- Explication de la cause racine
- Pourquoi cette erreur se produit ?
- Solution détaillée avec code corrigé
- Comment éviter ce pattern à l'avenir ?
- Tests pour prévenir la régression
```

---

### 10. Analyser un bug intermittent

```
Role : Tu es un expert en debugging de problèmes de concurrence/race conditions.

Action : Aide-moi à identifier et corriger ce bug intermittent :
[DÉCRIRE LE COMPORTEMENT]

Context :
- Se produit : [FRÉQUENCE]
- Environnement : [dev/prod]
- Code concerné :
[COLLER LE CODE]

- Logs/traces :
[COLLER LES LOGS]

Expectations :
- Hypothèses sur la cause (race condition, timing, etc.)
- Expériences pour reproduire le bug
- Solution proposée avec code
- Tests pour détecter le problème
```

---

## Documentation

### 11. Générer une documentation d'API

```
Role : Tu es un technical writer expert en documentation d'API.

Action : Génère une documentation complète pour cette API.

Context :
- Code de l'API :
[COLLER LE CODE]

- Format : [OPENAPI/SWAGGER/MARKDOWN]
- Audience : développeurs externes

Expectations :
- Description de chaque endpoint
- Paramètres (query, body, path)
- Réponses possibles (200, 400, 401, 404, 500)
- Exemples de requêtes (curl, JavaScript, Python)
- Schémas de données (JSON Schema)
- Authentication expliquée
```

---

### 12. Générer un README

```
Role : Tu es un technical writer expert en documentation de projets open-source.

Action : Génère un README.md complet pour ce projet.

Context :
- Projet : [DÉCRIRE LE PROJET]
- Stack : [TECHNOLOGIES]
- Public cible : [développeurs/utilisateurs finaux]

Expectations :
- Titre et description
- Badges (build status, license, etc.)
- Installation rapide
- Usage/exemples
- Configuration
- Documentation complète
- Contribution guidelines
- Licence
- Table des matières
```

---

### 13. Générer des docstrings/JSDoc

```
Role : Tu es un expert en documentation de code [LANGAGE].

Action : Génère des docstrings complètes pour ces fonctions/classes.

Context :
- Code :
[COLLER LE CODE]

- Style : [GOOGLE/NUMPY/JSDOC/etc.]
- Niveau de détail : [concis/détaillé]

Expectations :
- Description de la fonction/classe
- Paramètres avec types
- Valeur de retour
- Exceptions possibles
- Exemples d'utilisation
- Notes/warnings si pertinent
```

---

## Revue de code

### 14. Revue de code générale

```
Role : Tu es un code reviewer senior expert en [LANGAGE].

Action : Analyse ce code et identifie :
1. Bugs potentiels
2. Problèmes de performance
3. Violations de bonnes pratiques
4. Code smells
5. Améliorations possibles

Context :
- Code :
[COLLER LE CODE]

- Stack : [FRAMEWORK, VERSION]
- Environnement : [dev/prod]
- Criticité : [haute/moyenne/basse]

Expectations :
- Tableau : Priorité | Issue | Impact | Solution
- Ordre : Critical > High > Medium > Low
- Code corrigé pour les issues critiques
- Explications pédagogiques
```

---

### 15. Revue de sécurité

```
Role : Tu es un security engineer expert en [STACK].

Action : Audite ce code pour détecter les vulnérabilités de sécurité.

Context :
- Code :
[COLLER LE CODE]

- OWASP Top 10 : à vérifier
- Contexte : [API publique/interne]
- Données sensibles : [oui/non]

Expectations :
- Liste des vulnérabilités selon OWASP
- Criticité (Critical, High, Medium, Low)
- Preuve de concept (PoC) pour chaque vulnérabilité
- Code corrigé sécurisé
- Checklist de sécurité pour le futur
```

---

### 16. Revue de performance

```
Role : Tu es un expert en optimisation de performance [LANGAGE].

Action : Analyse ce code et identifie les problèmes de performance.

Context :
- Code :
[COLLER LE CODE]

- Charge attendue : [NOMBRE DE REQUÊTES/SEC]
- Complexité actuelle : [BIG O]
- Objectif : [TEMPS DE RÉPONSE TARGET]

Expectations :
- Analyse de la complexité (Big O)
- Goulots d'étranglement identifiés
- Optimisations proposées avec code
- Impact estimé (avant/après)
- Trade-offs (lisibilité vs performance)
```

---

## Architecture

### 17. Proposer une architecture

```
Role : Tu es un architecte logiciel senior expert en [DOMAINE].

Action : Propose une architecture pour ce système :
[DÉCRIRE LE SYSTÈME]

Context :
- Besoins fonctionnels : [LISTE]
- Contraintes techniques : [SCALABILITÉ/SÉCURITÉ/etc.]
- Stack envisagée : [TECHNOLOGIES]
- Charge attendue : [USERS/TRAFFIC]

Expectations :
- Schéma d'architecture (texte ou Mermaid)
- Justification des choix techniques
- Patterns utilisés (microservices, event-driven, etc.)
- Scalabilité et résilience
- Points d'attention et risques
```

---

### 18. Comparer des architectures

```
Role : Tu es un architecte logiciel expert en comparaison de solutions.

Action : Compare ces 3 approches architecturales pour [BESOIN] :
1. [APPROCHE 1]
2. [APPROCHE 2]
3. [APPROCHE 3]

Context :
- Projet : [DESCRIPTION]
- Contraintes : [TEMPS/BUDGET/ÉQUIPE]
- Critères : performance, maintenabilité, coût

Expectations :
- Tableau comparatif (critères × approches)
- Avantages / Inconvénients de chaque approche
- Recommandation justifiée
- Plan de migration si applicable
```

---

## Sécurité

### 19. Détecter les vulnérabilités

```
Role : Tu es un expert en sécurité applicative (OWASP Top 10).

Action : Analyse ce code et détecte toutes les vulnérabilités.

Context :
- Code :
[COLLER LE CODE]

- Type : [API/WEBAPP/SERVICE]
- Données manipulées : [SENSIBLES/PUBLIQUES]

Expectations :
- Vulnérabilités selon OWASP Top 10
- Criticité : Critical, High, Medium, Low
- Preuve de concept (PoC)
- Code corrigé
- Recommandations préventives
```

---

### 20. Sécuriser du code

```
Role : Tu es un expert en sécurisation de code [LANGAGE].

Action : Sécurise ce code en corrigeant toutes les failles.

Context :
- Code actuel (non sécurisé) :
[COLLER LE CODE]

- Menaces identifiées : [SQL INJECTION/XSS/CSRF/etc.]
- Environnement : [PROD/PUBLIC]

Expectations :
- Code sécurisé complet
- Explication de chaque correction
- Tests de sécurité
- Checklist de validation
```

---

## Performance

### 21. Optimiser une requête

```
Role : Tu es un expert en optimisation de [BASE DE DONNÉES].

Action : Optimise cette requête SQL/NoSQL.

Context :
- Requête actuelle :
[COLLER LA REQUÊTE]

- Schéma de base de données :
[DÉCRIRE LE SCHÉMA]

- Volume de données : [NOMBRE DE LIGNES]
- Performance actuelle : [TEMPS D'EXÉCUTION]
- Objectif : < [TEMPS TARGET]

Expectations :
- Requête optimisée
- Indexes recommandés
- Explain plan (avant/après)
- Gain de performance estimé
```

---

### 22. Optimiser un algorithme

```
Role : Tu es un expert en algorithmique et optimisation.

Action : Optimise cet algorithme pour améliorer sa complexité.

Context :
- Algorithme actuel :
[COLLER LE CODE]

- Complexité actuelle : [BIG O]
- Volume de données : [TAILLE INPUT]
- Contraintes : [MÉMOIRE/TEMPS]

Expectations :
- Algorithme optimisé
- Complexité améliorée (Big O)
- Explication de l'optimisation
- Benchmarks (avant/après)
- Trade-offs si applicable
```

---

## Base de données

### 23. Concevoir un schéma de base de données

```
Role : Tu es un expert en conception de bases de données [SQL/NOSQL].

Action : Conçois un schéma de base de données pour ce système :
[DÉCRIRE LE SYSTÈME]

Context :
- Entités principales : [LISTE]
- Relations : [DÉCRIRE]
- Type de DB : [POSTGRESQL/MONGODB/etc.]
- Volume attendu : [NOMBRE D'ENTRÉES]

Expectations :
- Schéma complet (tables/collections)
- Relations (1-N, N-N)
- Indexes recommandés
- Contraintes (clés étrangères, unique, etc.)
- Migrations SQL/ORM
```

---

### 24. Optimiser un schéma existant

```
Role : Tu es un expert en optimisation de bases de données.

Action : Analyse et optimise ce schéma de base de données.

Context :
- Schéma actuel :
[COLLER LE SCHÉMA]

- Problèmes identifiés : [LENTEUR/DÉNORMALISATION/etc.]
- Volume : [NOMBRE DE LIGNES]

Expectations :
- Analyse des problèmes
- Schéma optimisé
- Migrations nécessaires
- Impact sur l'application
- Plan de migration
```

---

## DevOps et CI/CD

### 25. Créer un pipeline CI/CD

```
Role : Tu es un expert DevOps en CI/CD.

Action : Crée un pipeline CI/CD pour ce projet.

Context :
- Projet : [TYPE : API/WEBAPP/etc.]
- Stack : [TECHNOLOGIES]
- Plateforme : [GITHUB ACTIONS/GITLAB CI/JENKINS]
- Environnements : dev, staging, prod

Expectations :
- Fichier de configuration complet (.github/workflows, .gitlab-ci.yml, etc.)
- Étapes : lint, test, build, deploy
- Gestion des secrets
- Notifications en cas d'échec
- Rollback automatique si erreur
```

---

### 26. Créer un Dockerfile optimisé

```
Role : Tu es un expert Docker et optimisation d'images.

Action : Crée un Dockerfile optimisé pour cette application.

Context :
- Application : [TYPE]
- Stack : [NODE/PYTHON/GO/etc.]
- Objectif : image < [TAILLE TARGET]

Expectations :
- Dockerfile multi-stage
- Image minimale (Alpine si possible)
- Cache layers optimisé
- Sécurité (non-root user)
- .dockerignore
- Instructions de build et run
```

---

## Prompts avancés

### 27. Analyser une codebase complète

```
Role : Tu es un architecte logiciel expert en analyse de code.

Action : Analyse cette codebase et fournis :
1. Architecture actuelle (schéma)
2. Dette technique identifiée
3. Refactorings prioritaires
4. Recommandations d'amélioration

Context :
- Codebase : [LIEN GITHUB ou FICHIERS]
- Stack : [TECHNOLOGIES]
- Taille : [NOMBRE DE LIGNES]
- Problèmes connus : [LISTE]

Expectations :
- Rapport d'analyse structuré
- Schéma d'architecture actuelle
- Top 10 des refactorings prioritaires
- Roadmap d'amélioration (3-6 mois)
```

---

### 28. Migrer une technologie

```
Role : Tu es un expert en migration de stack technique.

Action : Aide-moi à migrer ce projet de [TECH A] vers [TECH B].

Context :
- Codebase actuelle :
[COLLER LE CODE ou LIEN]

- Stack actuelle : [TECH A + VERSION]
- Stack cible : [TECH B + VERSION]
- Contraintes : [TEMPS/DOWNTIME/etc.]

Expectations :
- Plan de migration étape par étape
- Code migré (exemples clés)
- Tests de non-régression
- Risques et mitigations
- Estimation de charge (jours-homme)
```

---

## 🎯 Conseils pour créer vos propres prompts

### 1. Soyez spécifique
❌ "Crée une API"
✅ "Crée une API REST avec Node.js/Express pour gérer des utilisateurs (CRUD)"

### 2. Donnez du contexte
❌ "Optimise ce code"
✅ "Optimise ce code Python pour traiter 1M de lignes en < 5 secondes"

### 3. Définissez les attentes
❌ "Génère des tests"
✅ "Génère 10 tests unitaires avec Jest, couverture > 80%, incluant cas limites"

### 4. Itérez si nécessaire
Si la réponse ne convient pas :
- "Refais en simplifiant la logique"
- "Ajoute plus de commentaires explicatifs"
- "Génère une version alternative"

### 5. Validez toujours
- ✅ Relisez le code généré
- ✅ Testez le code
- ✅ Adaptez à votre contexte
- ❌ Ne copiez jamais aveuglément

---

## 📚 Ressources complémentaires

- [Quick Start Dev](../guides/Quick_Start_Dev.md) → Pour commencer
- [Guide complet AI Driven Dev](../guides/AI_Driven_Dev_Guide.md) → Vision d'ensemble
- [Exemples pratiques](../examples/README.md) → Cas concrets

---

**Vous avez un prompt utile à partager ?** Contribuez en ouvrant une PR !

🚀 **Utilisez ces prompts et gagnez jusqu'à 80% de temps sur vos tâches quotidiennes.**
