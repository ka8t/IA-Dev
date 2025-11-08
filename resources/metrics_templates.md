# 📊 Templates de Métriques — KPIs, Qualité et ROI

## 🎯 Objectif

Ce document fournit des **templates prêts à l'emploi** pour mesurer l'impact de l'IA dans votre équipe de développement. Incluant des KPIs de productivité, qualité, adoption et ROI financier.

---

## 📋 Table des matières

1. [Vue d'ensemble des métriques](#vue-densemble-des-métriques)
2. [KPIs de productivité](#kpis-de-productivité)
3. [KPIs de qualité](#kpis-de-qualité)
4. [KPIs d'adoption](#kpis-dadoption)
5. [Calcul du ROI](#calcul-du-roi)
6. [Tableaux de bord](#tableaux-de-bord)
7. [Rapports hebdomadaires](#rapports-hebdomadaires)
8. [Rapports mensuels](#rapports-mensuels)
9. [Outils de suivi](#outils-de-suivi)

---

## Vue d'ensemble des métriques

### Catégories de métriques

| Catégorie | Objectif | Fréquence de mesure |
|-----------|----------|---------------------|
| **Productivité** | Mesurer le gain de temps et de vélocité | Quotidienne/Hebdo |
| **Qualité** | Vérifier que la qualité est maintenue | Hebdo/Mensuelle |
| **Adoption** | Suivre l'utilisation de l'IA | Quotidienne/Hebdo |
| **ROI** | Justifier l'investissement | Mensuelle/Trimestrielle |

### Objectifs cibles

| Métrique | Objectif pilote (1 mois) | Objectif déploiement (3 mois) |
|----------|-------------------------|------------------------------|
| Gain de productivité | +30% | +50% |
| Réduction bugs | -20% | -40% |
| Adoption quotidienne | 80% | 90% |
| ROI | 200% | 500% |

---

## KPIs de productivité

### 1. Vélocité de sprint

**Définition** : Nombre de story points complétés par sprint

**Formule** :
```
Vélocité = Σ Story Points complétés / Sprint
```

**Template de suivi** :

| Sprint | Avant IA | Avec IA | Gain (%) |
|--------|----------|---------|----------|
| Sprint 1 | 30 SP | 30 SP | 0% (baseline) |
| Sprint 2 | 30 SP | 38 SP | +27% |
| Sprint 3 | 32 SP | 45 SP | +41% |
| Sprint 4 | 31 SP | 48 SP | +55% |
| **Moyenne** | **31 SP** | **40 SP** | **+29%** |

**Interprétation** :
- ✅ Gain > 30% : excellent
- ⚠️ Gain 10-30% : bon, à améliorer
- ❌ Gain < 10% : revoir l'utilisation de l'IA

---

### 2. Lead time

**Définition** : Temps entre le début du développement et le déploiement en production

**Formule** :
```
Lead Time = Date de déploiement - Date de début de dev
```

**Template de suivi** :

| Période | Lead Time moyen (jours) | Objectif | Statut |
|---------|------------------------|----------|--------|
| Avant IA | 5.2 jours | - | Baseline |
| Semaine 1 | 4.8 jours | < 4.5 | 🟡 |
| Semaine 2 | 4.1 jours | < 4.5 | ✅ |
| Semaine 3 | 3.6 jours | < 4.5 | ✅ |
| Semaine 4 | 3.2 jours | < 4.5 | ✅ |
| **Gain** | **-38%** | **-30%** | **✅** |

---

### 3. Cycle time

**Définition** : Temps entre le premier commit et le merge de la PR

**Formule** :
```
Cycle Time = Date de merge PR - Date du premier commit
```

**Template de suivi** :

| Semaine | Cycle Time moyen (heures) | Avant IA | Gain |
|---------|---------------------------|----------|------|
| Semaine 1 | 18h | 32h | -44% |
| Semaine 2 | 16h | 32h | -50% |
| Semaine 3 | 14h | 32h | -56% |
| Semaine 4 | 12h | 32h | -63% |

---

### 4. Nombre de PRs mergées

**Définition** : Nombre de Pull Requests mergées par semaine

**Template de suivi** :

| Semaine | PRs mergées | Avant IA | Gain |
|---------|-------------|----------|------|
| Semaine 1 | 15 | 12 | +25% |
| Semaine 2 | 18 | 12 | +50% |
| Semaine 3 | 20 | 12 | +67% |
| Semaine 4 | 22 | 12 | +83% |

---

### 5. Temps par tâche

**Définition** : Temps moyen pour compléter différents types de tâches

**Template de suivi** :

| Type de tâche | Temps avant IA | Temps avec IA | Gain |
|---------------|----------------|---------------|------|
| Nouvelle feature simple | 4h | 2h | -50% |
| Feature complexe | 16h | 10h | -38% |
| Bug fix | 2h | 1h | -50% |
| Refactoring | 6h | 3h | -50% |
| Tests unitaires | 2h | 30min | -75% |
| Documentation | 1h | 15min | -75% |

---

## KPIs de qualité

### 6. Taux de bugs en production

**Définition** : Nombre de bugs détectés en production par mois

**Formule** :
```
Taux de bugs = Nombre de bugs en prod / Nombre de déploiements
```

**Template de suivi** :

| Mois | Bugs en prod | Déploiements | Taux | Avant IA |
|------|--------------|--------------|------|----------|
| Mois 1 | 12 | 20 | 0.60 | 0.75 (baseline) |
| Mois 2 | 9 | 22 | 0.41 | 0.75 |
| Mois 3 | 6 | 25 | 0.24 | 0.75 |
| **Gain** | **-50%** | - | **-68%** | - |

**Interprétation** :
- ✅ Réduction > 30% : excellent
- ⚠️ Réduction 10-30% : bon
- ❌ Augmentation : revoir la qualité du code IA

---

### 7. Couverture de tests

**Définition** : Pourcentage de code couvert par des tests

**Template de suivi** :

| Période | Couverture (%) | Objectif | Statut |
|---------|----------------|----------|--------|
| Avant IA | 65% | - | Baseline |
| Mois 1 | 72% | 75% | 🟡 |
| Mois 2 | 78% | 75% | ✅ |
| Mois 3 | 83% | 80% | ✅ |

---

### 8. Dette technique

**Définition** : Score de qualité du code (SonarQube, CodeClimate, etc.)

**Template de suivi** :

| Période | Score SonarQube | Code Smells | Bugs détectés | Dette technique (jours) |
|---------|-----------------|-------------|---------------|------------------------|
| Avant IA | 72/100 (C) | 145 | 28 | 12 jours |
| Mois 1 | 76/100 (B) | 120 | 22 | 10 jours |
| Mois 2 | 81/100 (A) | 95 | 15 | 7 jours |
| Mois 3 | 85/100 (A) | 68 | 9 | 4 jours |

---

### 9. Temps de revue de code

**Définition** : Temps moyen pour reviewer une PR

**Template de suivi** :

| Période | Temps de review (heures) | Avant IA | Gain |
|---------|-------------------------|----------|------|
| Semaine 1 | 2.5h | 4h | -38% |
| Semaine 2 | 2.0h | 4h | -50% |
| Semaine 3 | 1.5h | 4h | -63% |
| Semaine 4 | 1.2h | 4h | -70% |

**Note** : L'IA peut pré-reviewer et identifier les issues automatiquement.

---

## KPIs d'adoption

### 10. Utilisation quotidienne

**Définition** : Pourcentage de développeurs utilisant l'IA chaque jour

**Formule** :
```
Utilisation quotidienne = (Devs utilisant IA / Total devs) × 100
```

**Template de suivi** :

| Semaine | Utilisateurs actifs | Total devs | Taux d'adoption |
|---------|---------------------|------------|-----------------|
| Semaine 1 | 3 | 10 | 30% (pilote) |
| Semaine 2 | 3 | 10 | 30% |
| Semaine 3 | 3 | 10 | 30% |
| Semaine 4 | 8 | 10 | 80% (déploiement) |
| Semaine 8 | 10 | 10 | 100% |

**Objectif** : ≥ 80% après 1 mois de déploiement

---

### 11. Satisfaction développeurs

**Définition** : Note moyenne de satisfaction (échelle 1-10)

**Sondage mensuel** :

```
Questions :
1. Utilisez-vous l'IA quotidiennement ? (Oui/Non)
2. L'IA vous fait-elle gagner du temps ? (1-10)
3. La qualité du code généré est-elle satisfaisante ? (1-10)
4. Recommanderiez-vous l'IA à un collègue ? (1-10)
5. Commentaires libres

Note globale = Moyenne des questions 2, 3, 4
```

**Template de suivi** :

| Mois | Gain de temps (1-10) | Qualité (1-10) | Recommandation (1-10) | **Note globale** |
|------|---------------------|----------------|----------------------|------------------|
| Mois 1 | 7.5 | 6.8 | 7.2 | **7.2/10** |
| Mois 2 | 8.2 | 7.5 | 8.0 | **7.9/10** |
| Mois 3 | 8.8 | 8.2 | 8.7 | **8.6/10** |

**Interprétation** :
- ✅ Note ≥ 7/10 : excellent
- ⚠️ Note 5-7 : à améliorer
- ❌ Note < 5 : problème à résoudre

---

### 12. Nombre de prompts / jour

**Définition** : Nombre moyen de requêtes à l'IA par développeur et par jour

**Template de suivi** :

| Semaine | Prompts/dev/jour | Évolution |
|---------|------------------|-----------|
| Semaine 1 | 5 | Baseline |
| Semaine 2 | 8 | +60% |
| Semaine 3 | 12 | +140% |
| Semaine 4 | 15 | +200% |

**Interprétation** :
- Plus le nombre est élevé, plus l'adoption est forte
- Objectif : 10-20 prompts/jour

---

## Calcul du ROI

### Formule du ROI

```
ROI = ((Gain net - Coût total) / Coût total) × 100

Gain net = Temps gagné × Coût horaire chargé
Coût total = Licences + Formation + Support
```

### Template de calcul ROI

**Hypothèses** :

| Paramètre | Valeur |
|-----------|--------|
| Nombre de développeurs | 10 |
| Coût horaire chargé (€/h) | 50€ |
| Heures gagnées/dev/semaine | 5h |
| Nombre de semaines/an | 48 |
| Coût licence/dev/mois | 30€ |
| Coût formation (one-time) | 2 000€ |
| Coût support/an | 1 000€ |

**Calculs** :

```
Gain annuel :
= Nb devs × Heures gagnées/sem × Semaines/an × Coût horaire
= 10 × 5h × 48 × 50€
= 120 000€

Coût annuel :
Licences = 10 × 30€ × 12 mois = 3 600€
Formation = 2 000€ (année 1 uniquement)
Support = 1 000€
Total = 6 600€ (année 1), 4 600€ (années suivantes)

ROI année 1 :
= ((120 000€ - 6 600€) / 6 600€) × 100
= 1 718%

ROI années suivantes :
= ((120 000€ - 4 600€) / 4 600€) × 100
= 2 509%
```

---

### Template ROI pour différents scénarios

| Scénario | Nb devs | Heures/sem | Coût licence | Gain annuel | Coût annuel | ROI |
|----------|---------|------------|--------------|-------------|-------------|-----|
| **Conservateur** | 10 | 3h | 30€ | 72 000€ | 6 600€ | **991%** |
| **Réaliste** | 10 | 5h | 30€ | 120 000€ | 6 600€ | **1 718%** |
| **Optimiste** | 10 | 8h | 30€ | 192 000€ | 6 600€ | **2 809%** |
| **Petite équipe** | 5 | 5h | 30€ | 60 000€ | 3 800€ | **1 479%** |
| **Grande équipe** | 50 | 5h | 25€ | 600 000€ | 17 000€ | **3 429%** |

---

### Calculateur ROI interactif (formule)

**Copier dans Google Sheets ou Excel** :

```
A1: Nombre de développeurs
B1: [VOTRE VALEUR]

A2: Coût horaire chargé (€/h)
B2: [VOTRE VALEUR]

A3: Heures gagnées/dev/semaine
B3: [VOTRE VALEUR]

A4: Coût licence/dev/mois (€)
B4: [VOTRE VALEUR]

A5: Coût formation (€, one-time)
B5: [VOTRE VALEUR]

A6: Coût support/an (€)
B6: [VOTRE VALEUR]

--- Calculs automatiques ---

A8: Gain annuel (€)
B8: =B1*B3*48*B2

A9: Coût licences/an (€)
B9: =B1*B4*12

A10: Coût total année 1 (€)
B10: =B9+B5+B6

A11: ROI année 1 (%)
B11: =((B8-B10)/B10)*100

A12: Coût total années suivantes (€)
B12: =B9+B6

A13: ROI années suivantes (%)
B13: =((B8-B12)/B12)*100
```

---

## Tableaux de bord

### Dashboard hebdomadaire

**À suivre chaque semaine** :

| Métrique | Objectif | Semaine N | Statut | Tendance |
|----------|----------|-----------|--------|----------|
| Vélocité (SP) | 40 | 42 | ✅ | ⬆️ |
| Lead time (jours) | < 4 | 3.5 | ✅ | ⬇️ |
| PRs mergées | 20 | 22 | ✅ | ⬆️ |
| Bugs en prod | < 3 | 2 | ✅ | ⬇️ |
| Adoption (%) | > 80% | 85% | ✅ | ➡️ |
| Satisfaction (1-10) | ≥ 7 | 8.2 | ✅ | ⬆️ |

**Légende** :
- ✅ Objectif atteint
- 🟡 Proche de l'objectif
- ❌ Objectif non atteint
- ⬆️ Amélioration
- ⬇️ Dégradation
- ➡️ Stable

---

### Dashboard mensuel

**Rapport exécutif mensuel** :

```markdown
# Rapport IA Dev — Mois de [MOIS]

## 📊 Résumé exécutif

- **ROI** : 1 800% (+200 points vs mois précédent)
- **Productivité** : +42% de vélocité moyenne
- **Qualité** : -35% de bugs en production
- **Adoption** : 90% des développeurs utilisent l'IA quotidiennement

## 🎯 Métriques clés

| Métrique | Objectif | Résultat | Statut |
|----------|----------|----------|--------|
| Gain de productivité | +35% | +42% | ✅ |
| Réduction bugs | -30% | -35% | ✅ |
| Adoption quotidienne | 80% | 90% | ✅ |
| ROI | 500% | 1 800% | ✅ |

## 📈 Évolution de la productivité

- Vélocité : 31 SP → 44 SP (+42%)
- Lead time : 5.2j → 3.1j (-40%)
- PRs/semaine : 12 → 20 (+67%)

## 🐛 Évolution de la qualité

- Bugs/mois : 15 → 10 (-33%)
- Couverture tests : 68% → 78% (+10 points)
- Dette technique : 12j → 7j (-42%)

## 💰 ROI financier

- Gain mensuel : 10 000€
- Coût mensuel : 500€
- ROI : 1 900%

## 💬 Retours de l'équipe

- Note de satisfaction : 8.2/10
- Commentaires positifs :
  - "Gain de temps énorme sur les tests"
  - "Je peux me concentrer sur l'architecture"
- Points d'amélioration :
  - "Parfois le code généré est trop verbeux"

## 🚀 Actions pour le mois prochain

1. Former 2 développeurs supplémentaires
2. Intégrer l'IA dans le CI/CD (auto-docs)
3. Créer une bibliothèque de prompts interne
```

---

## Rapports hebdomadaires

### Template de rapport hebdo

**À envoyer chaque vendredi à l'équipe** :

```markdown
# Rapport IA Dev — Semaine du [DATE]

## 🎉 Faits marquants

- 🚀 Vélocité : 45 SP cette semaine (record !)
- 🏆 Zéro bug déployé en production
- 💡 Nouveau prompt partagé : génération de tests E2E

## 📊 Métriques de la semaine

| Métrique | Cette semaine | Semaine dernière | Évolution |
|----------|---------------|------------------|-----------|
| PRs mergées | 22 | 18 | +22% |
| Lead time | 3.2j | 3.8j | -16% |
| Bugs prod | 0 | 2 | -100% |
| Adoption | 88% | 85% | +3% |

## 💬 Retour d'expérience

**[Dev 1]** : "J'ai utilisé l'IA pour refactorer un module legacy de 800 lignes. Passé de 4h à 1h30 !"

**[Dev 2]** : "L'IA m'a aidé à déboguer une race condition en 10 minutes. Sans elle, j'y serais encore..."

## 🔗 Ressources utiles cette semaine

- Nouveau prompt ajouté : [Lien vers prompts_library.md]
- Article intéressant : [Lien]

## 🎯 Focus semaine prochaine

- Intégrer l'IA dans la CI/CD pour auto-générer les docs
- Atteindre 90% d'adoption quotidienne
```

---

## Rapports mensuels

### Template de rapport mensuel (direction)

**Présentation PowerPoint / PDF** :

```
Slide 1 : Résumé exécutif
- ROI : 1 800%
- Productivité : +42%
- Qualité : -35% bugs
- 90% adoption

Slide 2 : Métriques de productivité
- Graphique : Évolution vélocité (Avant/Après)
- Graphique : Lead time (Avant/Après)
- Tableau : Temps gagné par type de tâche

Slide 3 : Métriques de qualité
- Graphique : Bugs en production (tendance)
- Graphique : Couverture de tests (évolution)
- Tableau : Dette technique

Slide 4 : ROI financier
- Calcul détaillé du ROI
- Comparaison coûts vs gains
- Projection sur 12 mois

Slide 5 : Retours de l'équipe
- Satisfaction : 8.2/10
- Verbatims (citations)
- Points d'amélioration

Slide 6 : Prochaines étapes
- Objectifs mois prochain
- Nouvelles fonctionnalités à tester
- Besoins (budget, formation, etc.)
```

---

## Outils de suivi

### Outils recommandés

| Outil | Usage | Gratuit | Lien |
|-------|-------|---------|------|
| **Google Sheets** | Tableaux de suivi manuels | ✅ | [sheets.google.com](https://sheets.google.com) |
| **Notion** | Dashboards et rapports | ✅ (limité) | [notion.so](https://notion.so) |
| **Jira** | Vélocité, lead time | ❌ | [atlassian.com](https://www.atlassian.com/software/jira) |
| **GitHub Insights** | PRs, cycle time, contributions | ✅ | GitHub repo > Insights |
| **SonarQube** | Dette technique, code smells | ✅ (community) | [sonarqube.org](https://www.sonarqube.org/) |
| **Sentry/Bugsnag** | Bugs en production | ✅ (limité) | [sentry.io](https://sentry.io) |
| **Metabase** | Dashboards personnalisés | ✅ | [metabase.com](https://www.metabase.com/) |

---

### Script d'analyse Git (exemple)

**Calculer le nombre de PRs mergées par semaine** :

```bash
#!/bin/bash
# Script: git_metrics.sh
# Usage: ./git_metrics.sh

echo "=== Métriques Git des 4 dernières semaines ==="

for i in {0..3}; do
  start_date=$(date -d "$((i+1)) weeks ago" +%Y-%m-%d)
  end_date=$(date -d "$i weeks ago" +%Y-%m-%d)

  pr_count=$(git log --oneline --merges --since="$start_date" --until="$end_date" | wc -l)

  echo "Semaine du $start_date : $pr_count PRs mergées"
done
```

---

### Template Google Sheets

**Créer un Google Sheets avec ces onglets** :

1. **Dashboard** : Vue d'ensemble (graphiques)
2. **Productivité** : Vélocité, lead time, PRs
3. **Qualité** : Bugs, couverture, dette
4. **Adoption** : Utilisation, satisfaction
5. **ROI** : Calculs financiers
6. **Changelog** : Historique des changements

**Formules utiles** :

```
Calcul de gain (%) :
=((B2-A2)/A2)*100

Moyenne mobile sur 4 semaines :
=AVERAGE(B2:B5)

Somme conditionnelle :
=SUMIF(A:A, "Semaine 1", B:B)
```

---

## 🚀 Recommandations

### Fréquence de mesure

| Métrique | Mesure | Rapport |
|----------|--------|---------|
| Vélocité, PRs, adoption | Quotidien | Hebdo |
| Lead time, bugs | Hebdo | Hebdo |
| ROI, satisfaction | Mensuel | Mensuel |

### Bonnes pratiques

1. **Commencez simple** : 5-6 métriques clés maximum
2. **Automatisez** : utilisez les APIs Git, Jira, etc.
3. **Visualisez** : graphiques > tableaux
4. **Partagez** : transparence avec l'équipe
5. **Itérez** : ajustez les métriques selon les besoins

---

**Vous avez toutes les métriques pour mesurer l'impact de l'IA !**

🎯 **Commencez par 3 métriques simples : vélocité, bugs, satisfaction.**

📊 **Ajoutez progressivement d'autres métriques selon vos besoins.**

💰 **Calculez le ROI pour justifier l'investissement auprès de la direction.**
