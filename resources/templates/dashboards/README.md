# 📊 Templates de Dashboards - Métriques IA

Ce dossier contient des templates de dashboards pour monitorer l'impact de l'IA sur votre équipe de développement.

---

## 🎯 Dashboards Disponibles

| Dashboard | Outil | Description | Fichier |
|-----------|-------|-------------|---------|
| **AI Metrics Overview** | Grafana | Vue d'ensemble des KPIs IA | [`grafana-ai-metrics.json`](./grafana-ai-metrics.json) |
| **Developer Productivity** | Grafana | Métriques de productivité | [`grafana-productivity.json`](./grafana-productivity.json) |
| **AI ROI Tracker** | Excel/Google Sheets | Calcul ROI automatique | [`roi-tracker.xlsx`](./roi-tracker.xlsx) |
| **Weekly Report** | Metabase/PowerBI | Rapport hebdomadaire auto | [`metabase-weekly.json`](./metabase-weekly.json) |

---

## 🚀 Quick Start

### Option 1 : Grafana (Recommandé)

1. **Prérequis**
   ```bash
   # Installer Grafana
   docker run -d -p 3000:3000 grafana/grafana
   ```

2. **Importer le dashboard**
   - Ouvrez Grafana : `http://localhost:3000`
   - Dashboard → Import → Upload JSON file
   - Sélectionnez `grafana-ai-metrics.json`

3. **Configurer la source de données**
   - Connectez votre source (Prometheus, InfluxDB, etc.)
   - Mappez les métriques (voir section Configuration)

---

### Option 2 : Google Sheets / Excel

1. **Téléchargez le template**
   - [`roi-tracker.xlsx`](./roi-tracker.xlsx)

2. **Remplissez vos données**
   - Onglet "Data" : Saisissez vos métriques hebdomadaires
   - Onglet "Dashboard" : Visualisations auto-générées
   - Onglet "ROI" : Calcul automatique du ROI

3. **Partagez avec votre équipe**
   - Exportez en PDF pour rapports
   - Partagez le lien Google Sheets

---

## 📊 Métriques à Tracker

### Productivité (Métriques primaires)

| Métrique | Source de données | Calcul | Fréquence |
|----------|-------------------|--------|-----------|
| **Pull Requests / dev / sprint** | GitHub/GitLab API | `COUNT(PRs) / COUNT(devs) / sprint` | Sprint |
| **Lead time** | JIRA/GitHub | `MERGE_TIME - CREATE_TIME` (moyenne) | Daily |
| **Cycle time** | JIRA | `DONE_TIME - IN_PROGRESS_TIME` | Daily |
| **Deployment frequency** | CI/CD | `COUNT(deployments) / semaine` | Weekly |

### Qualité (Métriques secondaires)

| Métrique | Source | Calcul | Fréquence |
|----------|--------|--------|-----------|
| **Bugs en production** | JIRA/Sentry | `COUNT(bugs WHERE env=prod)` | Weekly |
| **Couverture de tests** | SonarQube/Codecov | `covered_lines / total_lines` | Per PR |
| **Code smells** | SonarQube | `COUNT(code_smells)` | Daily |
| **Hotfixes** | GitHub | `COUNT(PRs WHERE label=hotfix)` | Weekly |

### Adoption IA

| Métrique | Source | Calcul | Fréquence |
|----------|--------|--------|-----------|
| **Taux d'utilisation Copilot** | GitHub Copilot API | `acceptation_rate` | Daily |
| **Prompts ChatGPT / dev** | Logs internes | `COUNT(prompts) / dev` | Weekly |
| **Satisfaction IA** | Survey | `AVG(note /10)` | Monthly |

---

## 🔧 Configuration

### Étape 1 : Configurer les sources de données

#### GitHub API

```bash
# Variables d'environnement
export GITHUB_TOKEN="your_github_token"
export GITHUB_ORG="your_org"
export GITHUB_REPO="your_repo"
```

**Endpoints utiles :**
- Pull Requests : `GET /repos/{owner}/{repo}/pulls`
- Commits : `GET /repos/{owner}/{repo}/commits`
- Issues : `GET /repos/{owner}/{repo}/issues`

#### JIRA API

```bash
export JIRA_URL="https://your-company.atlassian.net"
export JIRA_USER="your-email"
export JIRA_TOKEN="your_api_token"
```

**JQL queries utiles :**
```jql
# Bugs en production ce mois
project = MYPROJECT AND type = Bug AND environment = Production AND created >= startOfMonth()

# Lead time moyen
project = MYPROJECT AND status = Done AND resolved >= -7d
```

---

### Étape 2 : Créer un collecteur de métriques

**Script Python (exemple) :**

```python
#!/usr/bin/env python3
"""
Collecteur de métriques pour dashboard IA.
"""

import requests
import os
from datetime import datetime, timedelta

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_API = 'https://api.github.com'

def get_prs_last_week(org, repo):
    """Récupère les PRs de la semaine dernière."""
    since = (datetime.now() - timedelta(days=7)).isoformat()

    url = f'{GITHUB_API}/repos/{org}/{repo}/pulls'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    params = {'state': 'all', 'since': since}

    response = requests.get(url, headers=headers, params=params)
    prs = response.json()

    return {
        'count': len(prs),
        'avg_review_time': calculate_avg_review_time(prs),
        'merged_count': len([pr for pr in prs if pr.get('merged_at')])
    }

def calculate_avg_review_time(prs):
    """Calcule le temps moyen de review."""
    times = []
    for pr in prs:
        if pr.get('merged_at'):
            created = datetime.fromisoformat(pr['created_at'].replace('Z', '+00:00'))
            merged = datetime.fromisoformat(pr['merged_at'].replace('Z', '+00:00'))
            times.append((merged - created).total_seconds() / 3600)  # en heures

    return sum(times) / len(times) if times else 0

# Envoyer à Prometheus, InfluxDB, ou autre
def send_to_influxdb(metrics):
    """Envoie les métriques à InfluxDB."""
    # Implementation InfluxDB
    pass

if __name__ == '__main__':
    org = os.getenv('GITHUB_ORG')
    repo = os.getenv('GITHUB_REPO')

    metrics = get_prs_last_week(org, repo)
    print(f"PRs cette semaine : {metrics['count']}")
    print(f"Temps review moyen : {metrics['avg_review_time']:.2f}h")
    print(f"PRs mergées : {metrics['merged_count']}")

    # send_to_influxdb(metrics)
```

**Utilisation :**
```bash
chmod +x collect_metrics.py
./collect_metrics.py

# Ou via cron pour automatiser
# */5 * * * * /path/to/collect_metrics.py
```

---

### Étape 3 : Configurer les alertes

**Exemple Grafana (YAML) :**

```yaml
groups:
  - name: ai_metrics_alerts
    interval: 5m
    rules:
      - alert: ProductivityDrop
        expr: rate(pr_count[1w]) < 0.7 * rate(pr_count[1w] offset 1w)
        for: 1d
        labels:
          severity: warning
        annotations:
          summary: "Baisse de productivité détectée"
          description: "Le nombre de PRs a chuté de >30% cette semaine"

      - alert: BugSpike
        expr: bugs_production > 15
        for: 1d
        labels:
          severity: critical
        annotations:
          summary: "Pic de bugs en production"
          description: "Plus de 15 bugs détectés en production"
```

---

## 📈 Exemples de Visualisations

### 1. Évolution Productivité (Line Chart)

**Métriques :**
- PRs / semaine (ligne bleue)
- Lead time moyen (ligne orange)

**Query Prometheus :**
```promql
# PRs par semaine
rate(github_prs_total[1w])

# Lead time moyen
avg_over_time(github_pr_lead_time_seconds[1w]) / 3600
```

---

### 2. ROI Cumulé (Area Chart)

**Métriques :**
- Coûts cumulés (rouge)
- Gains cumulés (vert)
- ROI % (ligne)

**Calcul :**
```
ROI(t) = ((Gains(t) - Coûts(t)) / Coûts(t)) × 100
```

---

### 3. Heatmap Adoption IA

**Axes :**
- X : Jour de la semaine
- Y : Développeur
- Couleur : Taux d'utilisation Copilot (0-100%)

**Insight :** Identifier les champions IA et les besoins de formation.

---

## 🎨 Personnalisation

### Thèmes de couleurs

**Theme "Success" (défaut) :**
- Productivité : Vert (#28a745)
- Qualité : Bleu (#007bff)
- Adoption : Violet (#6f42c1)
- Alerts : Rouge (#dc3545)

**Theme "Dark mode" :**
- Background : #1a1a1a
- Text : #e0e0e0
- Accent : #00d9ff

---

## 📱 Dashboard Mobile

Les dashboards Grafana sont responsive. Optimisations recommandées :

- Limiter à 6 panneaux max par page
- Utiliser Single Stat pour KPIs clés
- Graphs simplifiés pour petits écrans

---

## 🔗 Intégrations

### Slack

Envoyez automatiquement le rapport hebdomadaire :

```bash
# Webhook Slack
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"📊 Rapport IA cette semaine:\n• PRs: +45%\n• Bugs: -12\n• ROI: 4512%"}' \
  YOUR_SLACK_WEBHOOK_URL
```

### Email

Exportez le dashboard en PDF et envoyez par email :

```python
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Exporter le dashboard Grafana en PDF
subprocess.run([
    'grafana-cli', 'dashboard', 'export',
    '--dashboard-id', '1',
    '--output', 'weekly-report.pdf'
])

# Envoyer par email
# ... (code SMTP)
```

---

## 💡 Best Practices

1. **Automatiser la collecte**
   - Cron job toutes les 5-15 minutes
   - Pas de collecte manuelle

2. **Versionner les dashboards**
   - Commit les JSON dans Git
   - Changelog des modifications

3. **Documenter les métriques**
   - Formules de calcul explicites
   - Sources de données claires

4. **Alertes intelligentes**
   - Pas de sur-alerting
   - Seuils basés sur historique

5. **Partager largement**
   - Dashboard public pour toute l'équipe
   - Exports hebdomadaires automatiques

---

## 📚 Ressources

- [Grafana Documentation](https://grafana.com/docs/)
- [Prometheus Query Language](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [InfluxDB Documentation](https://docs.influxdata.com/)
- [GitHub API Reference](https://docs.github.com/en/rest)
- [JIRA REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)

---

## ❓ Troubleshooting

**Dashboard vide ?**
- Vérifiez la connexion à la source de données
- Vérifiez les credentials API
- Consultez les logs Grafana

**Métriques incorrectes ?**
- Validez les queries avec l'outil de test
- Vérifiez le time range sélectionné
- Comparez avec les données sources

**Performance lente ?**
- Réduisez l'intervalle de refresh
- Optimisez les queries (indexation)
- Utilisez le caching

---

**Templates créés par AI Driven Dev**
**Version :** 1.0
**Dernière mise à jour :** 2025-11-08
