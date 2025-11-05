#!/bin/bash
# ============================================================
# Script de réorganisation complète du projet IA-Dev
# Auteur : ChatGPT x ka8t
# Version : 2.0 — avec mode dry-run + mode interactif
# ============================================================

set -e

echo "🚀 Réorganisation du dossier IA-Dev..."

# === 1. Options ============================================================
DRY_RUN=false
INTERACTIVE=false

for arg in "$@"; do
    case $arg in
        --dry-run)
            DRY_RUN=true
            ;;
        --interactive)
            INTERACTIVE=true
            ;;
    esac
done

if $DRY_RUN; then
    echo "🧪 Mode simulation activé (aucune modification réelle ne sera effectuée)"
fi
if $INTERACTIVE; then
    echo "💬 Mode interactif activé (confirmation demandée pour chaque action)"
fi

# === 2. Variables ==========================================================
SRC_DIR="$(pwd)"
TARGET_DIR="$SRC_DIR/IA-Dev"
BACKUP_DIR="$SRC_DIR/archives/backup_$(date +%Y%m%d_%H%M%S)"

# === 3. Fonctions utilitaires ==============================================
ask_confirm() {
    if $INTERACTIVE; then
        read -p "👉 Confirmer cette action ? (o/N) " -n 1 -r
        echo
        [[ $REPLY =~ ^[Oo]$ ]] || return 1
    fi
    return 0
}

perform_action() {
    local action="$1"
    local src="$2"
    local dest="$3"

    if [ ! -e "$src" ]; then
        return
    fi

    if $DRY_RUN; then
        echo "   🔸 [SIMULATION] $action : $src → $dest"
    else
        if ask_confirm; then
            echo "   🔹 $action : $src → $dest"
            eval "$action \"$src\" \"$dest\" 2>/dev/null || true"
        else
            echo "   ⏭️  Action ignorée : $src"
        fi
    fi
}

# === 4. Sauvegarde =========================================================
echo "🗄️  Création d'une sauvegarde..."
if ! $DRY_RUN; then
    mkdir -p "$BACKUP_DIR"
    cp -r "$SRC_DIR"/* "$BACKUP_DIR" 2>/dev/null || true
    echo "✅ Sauvegarde effectuée dans : $BACKUP_DIR"
else
    echo "   🔸 [SIMULATION] Une sauvegarde serait créée dans : $BACKUP_DIR"
fi

# === 5. Structure de base ==================================================
echo "📁 Vérification / création de la structure..."
for d in guides resources examples scripts assets/visuals assets/pdf archives; do
    if ! $DRY_RUN; then
        mkdir -p "$TARGET_DIR/$d"
    else
        echo "   🔸 [SIMULATION] mkdir -p $TARGET_DIR/$d"
    fi
done

# === 6. Organisation des fichiers ==========================================
echo "📦 Organisation des fichiers principaux..."

# Guides
for f in "$SRC_DIR"/AI\ Driven\ Dev.* "$SRC_DIR"/AI\ Driven\ Dev_with_images.md "$SRC_DIR"/plan_guide_ia.md; do
    [ -e "$f" ] && perform_action mv "$f" "$TARGET_DIR/guides/"
done

# Scripts
for f in "$SRC_DIR"/setup_ia_dev_repo.sh "$SRC_DIR"/convert_mermaid.py "$SRC_DIR"/mermaid-filter.lua; do
    [ -e "$f" ] && perform_action mv "$f" "$TARGET_DIR/scripts/"
done

# Diagrammes
if [ -d "$SRC_DIR/mermaid_diagrams" ]; then
    echo "🖼️  Déplacement des diagrammes Mermaid..."
    for img in "$SRC_DIR/mermaid_diagrams/"*; do
        [ -e "$img" ] && perform_action mv "$img" "$TARGET_DIR/assets/visuals/"
    done
    if ! $DRY_RUN && ask_confirm; then
        rmdir "$SRC_DIR/mermaid_diagrams" 2>/dev/null || true
    fi
fi

# Fichiers de style et template
for f in "$SRC_DIR"/presentation_style.css "$SRC_DIR"/template.html; do
    [ -e "$f" ] && perform_action mv "$f" "$TARGET_DIR/assets/"
done

# README et archives
if [ -f "$SRC_DIR/README.md" ]; then
    perform_action mv "$SRC_DIR/README.md" "$TARGET_DIR/archives/README_old.md"
fi

if [ -d "$SRC_DIR/archives" ]; then
    for f in "$SRC_DIR/archives/"*; do
        [ -e "$f" ] && perform_action mv "$f" "$TARGET_DIR/archives/"
    done
fi

# === 7. Résumé =============================================================
echo ""
if $DRY_RUN; then
    echo "✅ Simulation terminée — aucune modification réelle effectuée."
else
    echo "✅ Réorganisation terminée avec succès."
fi

echo ""
echo "📂 Structure du dossier IA-Dev :"
if ! $DRY_RUN; then
    command -v tree >/dev/null && tree -L 3 "$TARGET_DIR" || ls -R "$TARGET_DIR"
else
    echo "   🔸 [SIMULATION] Affichage de la future structure : IA-Dev/(guides, resources, scripts, etc.)"
fi

echo ""
echo "💡 Étapes suivantes :"
echo "   cd IA-Dev"
echo "   git add . && git commit -m 'Réorganisation complète du dépôt'"
echo "   git push origin main"
echo ""
echo "🧠 Sauvegarde (réelle ou simulée) : $BACKUP_DIR"
