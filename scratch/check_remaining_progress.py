import os

inventory_file = "scratch/clean_inventory.txt"
skills_dir = ".agents/skills"
installed_skills = os.listdir(skills_dir)
print("Currently installed skills:", len(installed_skills))
for s in sorted(installed_skills):
    print("  -", s)

with open(inventory_file, encoding='utf-8') as f:
    files = [line.strip() for line in f if line.strip()]

print(f"\nTotal files in repository: {len(files)}")
