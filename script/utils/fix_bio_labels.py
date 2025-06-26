def fix_bio_labels(conll_lines):
    """
    Fix BIO tagging by ensuring that each entity span starts with 'B-' and 
    'I-' tags only follow correct preceding labels.
    
    Parameters:
        conll_lines (list of str): Lines from a .conll file.
    
    Returns:
        list of str: Fixed lines with valid BIO tagging.
    """
    fixed_lines = []
    prev_tag = "O"

    for line in conll_lines:
        line = line.strip()

        # Sentence boundary
        if not line:
            fixed_lines.append("")
            prev_tag = "O"
            continue

        parts = line.split()
        if len(parts) != 2:
            continue  # skip malformed lines

        token, tag = parts

        if tag.startswith("I-"):
            if prev_tag == "O" or prev_tag[2:] != tag[2:]:
                # I-* not following same type → convert to B-*
                tag = "B-" + tag[2:]
        elif tag.startswith("B-") or tag == "O":
            prev_tag = tag
        else:
            # Fallback for any unknown tag
            tag = "O"
            prev_tag = tag

        fixed_lines.append(f"{token} {tag}")
        prev_tag = tag

    return fixed_lines

def improved_fix_bio_labels(conll_lines):
    fixed_lines = []
    prev_tag_type = "O"

    for line in conll_lines:
        line = line.strip()

        if not line:
            fixed_lines.append("")
            prev_tag_type = "O"
            continue

        parts = line.split()
        if len(parts) != 2:
            continue  # skip malformed lines

        token, tag = parts

        if tag == "O":
            fixed_lines.append(f"{token} O")
            prev_tag_type = "O"
            continue

        # Split BIO format
        if '-' not in tag:
            tag = "O"
            fixed_lines.append(f"{token} {tag}")
            prev_tag_type = "O"
            continue

        tag_prefix, tag_type = tag.split('-')

        if tag_prefix == "B":
            prev_tag_type = tag_type
            fixed_lines.append(f"{token} B-{tag_type}")
        elif tag_prefix == "I":
            if prev_tag_type == tag_type:
                fixed_lines.append(f"{token} I-{tag_type}")
            else:
                # invalid I-type: restart with B
                fixed_lines.append(f"{token} B-{tag_type}")
                prev_tag_type = tag_type
        else:
            fixed_lines.append(f"{token} O")
            prev_tag_type = "O"

    return fixed_lines
def strict_fix_bio(conll_lines):
    fixed_lines = []
    previous_label = "O"

    for line in conll_lines:
        line = line.strip()

        if not line:
            fixed_lines.append("")  # Sentence boundary
            previous_label = "O"
            continue

        parts = line.split()
        if len(parts) != 2:
            continue  # skip malformed lines

        token, tag = parts

        if tag == "O":
            fixed_lines.append(f"{token} O")
            previous_label = "O"
            continue

        # Check BIO format
        if "-" not in tag:
            tag = "O"
            fixed_lines.append(f"{token} O")
            previous_label = "O"
            continue

        prefix, entity_type = tag.split("-")

        # Fix invalid I-ENTITY cases
        if prefix == "I":
            if previous_label == f"B-{entity_type}" or previous_label == f"I-{entity_type}":
                fixed_lines.append(f"{token} I-{entity_type}")
            else:
                # No valid beginning → force B-
                fixed_lines.append(f"{token} B-{entity_type}")
                previous_label = f"B-{entity_type}"
        elif prefix == "B":
            fixed_lines.append(f"{token} B-{entity_type}")
            previous_label = f"B-{entity_type}"
        else:
            fixed_lines.append(f"{token} O")
            previous_label = "O"

    return fixed_lines
