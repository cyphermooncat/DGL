import random

def load_lines(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def save_lines(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

def randomize_sections(lines, section_size=10):
    sections = [lines[i:i+section_size] for i in range(0, len(lines), section_size)]
    for section in sections:
        random.shuffle(section)
    return [line for section in sections for line in section]

def find_and_tag(lines, keywords):
    selected_lines = []
    for keyword in keywords:
        for i, line in enumerate(lines):
            if keyword in line and 'UTILISE' not in line:
                selected_lines.append(line.strip())
                lines[i] = line.strip() + ' UTILISE\n'
                break
    return selected_lines, lines

def main():
    filename = 'data.txt'
    lines = load_lines(filename)

    for i in range(1, 11):
        lines = randomize_sections(lines)
        
        keywords = ['Arme', 'Vetement', 'Casque', 'Ceinture', 'Chaussures', 'Gants', 'Collier', 'Bague']
        selected_lines, lines = find_and_tag(lines, keywords)
        
        if len(selected_lines) == len(keywords):
            save_lines(f'selection_{i}.txt', [line + '\n' for line in selected_lines])
    
    save_lines(filename, lines)

if __name__ == "__main__":
    main()
