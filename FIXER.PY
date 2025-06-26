import re

def fix_price_labels(conll_lines):
    fixed_lines = []
    buffer = []
    inside_price = False

    for line in conll_lines:
        line = line.strip()

        if line == "":
            # End of sentence or block
            fixed_lines.extend(buffer)
            fixed_lines.append("")
            buffer = []
            inside_price = False
            continue

        parts = line.split()
        if len(parts) != 2:
            continue  # skip malformed

        token, tag = parts

        # Detect start of price span
        if re.match(r"^ዋጋ[:፦\-]?$", token) or re.match(r"^\d+([,\.]?\d+)?$", token) or "ብር" in token:
            # Start new PRICE span if not already
            if not inside_price:
                buffer.append(f"{token} B-PRICE")
                inside_price = True
            else:
                buffer.append(f"{token} I-PRICE")
        else:
            buffer.append(f"{token} {tag}")
            inside_price = False

    # Handle trailing buffer
    if buffer:
        fixed_lines.extend(buffer)

    return fixed_lines

def fix_first_i_loc_to_b_loc(conll_lines):
    fixed_lines = []
    first_i_loc_found = False

    for line in conll_lines:
        line = line.strip()

        if line == "":
            # End of sentence → reset
            fixed_lines.append("")
            first_i_loc_found = False
            continue

        parts = line.split()
        if len(parts) != 2:
            fixed_lines.append(line)
            continue

        token, tag = parts

        if tag == "I-LOC" and not first_i_loc_found:
            tag = "B-LOC"
            first_i_loc_found = True

        fixed_lines.append(f"{token} {tag}")

    return fixed_lines


# RUN MAIN FUNCTION
if __name__ == "__main__":
    # Load your previously fixed .conll file
    with open("data/labeled/test_fixed.conll", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Apply LOC fix
    loc_fixed_lines = fix_first_i_loc_to_b_loc(lines)

    # Save to final cleaned file
    with open("data/labeled/test_final.conll", "w", encoding="utf-8") as f:
        f.write("\n".join(loc_fixed_lines))

    print("✅ LOC fix applied. Saved as 'test_final.conll'")

    # Example usage:
    # Load your existing .conll file
    # with open("data/labeled/test.conll", "r", encoding="utf-8") as f:
    #     lines = f.readlines()

    # # Fix PRICE labels
    # fixed_lines = fix_price_labels(lines)

    # # Save cleaned file
    # with open("data/labeled/test_fixed.conll", "w", encoding="utf-8") as f:
    #     f.write("\n".join(fixed_lines))

    # print("✅ PRICE labeling fixed and saved as 'ner_data_price_fixed.conll'")
