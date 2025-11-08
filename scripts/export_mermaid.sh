#!/bin/bash
#
# Export Mermaid diagrams to SVG/PNG
#
# Usage:
#   bash scripts/export_mermaid.sh assets/diagrams assets/visuals
#   bash scripts/export_mermaid.sh --format png assets/diagrams output/
#
# Requirements:
#   npm install -g @mermaid-js/mermaid-cli

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
FORMAT="svg"
INPUT_DIR=""
OUTPUT_DIR=""

# Help message
show_help() {
    echo "Usage: $0 [OPTIONS] INPUT_DIR OUTPUT_DIR"
    echo ""
    echo "Export Mermaid diagrams to SVG or PNG format."
    echo ""
    echo "Options:"
    echo "  -f, --format FORMAT    Output format: svg or png (default: svg)"
    echo "  -h, --help             Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 assets/diagrams assets/visuals"
    echo "  $0 --format png assets/diagrams output/"
    echo ""
    echo "Requirements:"
    echo "  - @mermaid-js/mermaid-cli (npm install -g @mermaid-js/mermaid-cli)"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--format)
            FORMAT="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            if [ -z "$INPUT_DIR" ]; then
                INPUT_DIR="$1"
            elif [ -z "$OUTPUT_DIR" ]; then
                OUTPUT_DIR="$1"
            else
                echo -e "${RED}❌ Too many arguments${NC}"
                show_help
                exit 1
            fi
            shift
            ;;
    esac
done

# Validate arguments
if [ -z "$INPUT_DIR" ] || [ -z "$OUTPUT_DIR" ]; then
    echo -e "${RED}❌ Missing required arguments${NC}"
    show_help
    exit 1
fi

if [ ! -d "$INPUT_DIR" ]; then
    echo -e "${RED}❌ Input directory does not exist: $INPUT_DIR${NC}"
    exit 1
fi

# Validate format
if [ "$FORMAT" != "svg" ] && [ "$FORMAT" != "png" ]; then
    echo -e "${RED}❌ Invalid format: $FORMAT (must be svg or png)${NC}"
    exit 1
fi

# Check if mmdc is installed
if ! command -v mmdc &> /dev/null; then
    echo -e "${RED}❌ mermaid-cli (mmdc) is not installed${NC}"
    echo ""
    echo "Install with:"
    echo "  npm install -g @mermaid-js/mermaid-cli"
    echo ""
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo -e "${BLUE}📊 Exporting Mermaid diagrams...${NC}"
echo ""
echo "Input:  $INPUT_DIR"
echo "Output: $OUTPUT_DIR"
echo "Format: $FORMAT"
echo ""

# Find all .mmd files
mmd_files=$(find "$INPUT_DIR" -name "*.mmd" -type f)

if [ -z "$mmd_files" ]; then
    echo -e "${YELLOW}⚠️  No .mmd files found in $INPUT_DIR${NC}"
    exit 0
fi

# Count files
file_count=$(echo "$mmd_files" | wc -l | tr -d ' ')
echo -e "${GREEN}Found $file_count Mermaid file(s)${NC}"
echo ""

# Export each file
success_count=0
fail_count=0

while IFS= read -r mmd_file; do
    # Get filename without extension
    filename=$(basename "$mmd_file" .mmd)

    # Output path
    output_file="$OUTPUT_DIR/${filename}.${FORMAT}"

    echo -e "${BLUE}➜${NC} Exporting: $filename"

    # Export with mmdc
    if mmdc -i "$mmd_file" -o "$output_file" -b transparent 2>/dev/null; then
        echo -e "${GREEN}  ✅ Success: $output_file${NC}"
        ((success_count++))
    else
        echo -e "${RED}  ❌ Failed: $mmd_file${NC}"
        ((fail_count++))
    fi

    echo ""
done <<< "$mmd_files"

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ $fail_count -eq 0 ]; then
    echo -e "${GREEN}✅ Complete! All files exported successfully.${NC}"
else
    echo -e "${YELLOW}⚠️  Complete with errors.${NC}"
fi
echo ""
echo "Success: $success_count"
echo "Failed:  $fail_count"
echo "Total:   $file_count"
echo ""
echo -e "${GREEN}Output directory: $OUTPUT_DIR${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
