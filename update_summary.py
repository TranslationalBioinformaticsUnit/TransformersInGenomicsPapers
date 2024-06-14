import re

# Read the README.md file
with open('README.md', 'r') as readme_file:
    readme_content = readme_file.read()

# Define patterns to match subsection headers and their tables
subsection_headers = ['Single-Cell Genomics (SCG)', 'DNA', 'Spatial Transcriptomics (ST)', 'Hybrids of SCG, DNA, and ST']
table_pattern = r'## {subsection}.*?\n(.*?\n)##'  # Assumes tables are under subsection headers

# Initialize counts
counts = {header: {'Original': 0, 'Benchmark': 0, 'Reviews': 0} for header in subsection_headers}

# Iterate over each subsection header
for header in subsection_headers:
    # Find the table for 'Original Papers'
    original_pattern = re.compile(table_pattern.format(subsection=re.escape(header) + r' Models\nOriginal Papers'), re.DOTALL)
    original_table_match = re.search(original_pattern, readme_content)
    if original_table_match:
        counts[header]['Original'] = original_table_match.group(1).strip().count('|') // 9  # Assuming 9 columns per row

    # Find the table for 'Benchmarking Papers'
    benchmark_pattern = re.compile(table_pattern.format(subsection=re.escape(header) + r' Models\nBenchmarking Papers'), re.DOTALL)
    benchmark_table_match = re.search(benchmark_pattern, readme_content)
    if benchmark_table_match:
        counts[header]['Benchmark'] = benchmark_table_match.group(1).strip().count('|') // 5  # Assuming 5 columns per row

    # Find the table for 'Review/Perspective Papers'
    reviews_pattern = re.compile(table_pattern.format(subsection=re.escape(header) + r' Models\nReview/Perspective Papers'), re.DOTALL)
    reviews_table_match = re.search(reviews_pattern, readme_content)
    if reviews_table_match:
        counts[header]['Reviews'] = reviews_table_match.group(1).strip().count('|') // 4  # Assuming 4 columns per row

# Update the summary statistics table at the top of the README.md file
summary_table = f"""
# Transformers In Genomics Papers
A curated repository of academic papers showcasing the use of Transformer models in genomics. This repository aims to guide researchers, data scientists, and enthusiasts in finding relevant literature and understanding the applications of Transformers in various genomic contexts.

## Summary Statistics

|                | Original | Benchmark | Reviews |
|----------------|---------:|----------:|--------:|
| SCG            | {counts['Single-Cell Genomics (SCG)']['Original']} | {counts['Single-Cell Genomics (SCG)']['Benchmark']} | {counts['Single-Cell Genomics (SCG)']['Reviews']} |
| DNA            | {counts['DNA']['Original']} | {counts['DNA']['Benchmark']} | {counts['DNA']['Reviews']} |
| ST             | {counts['Spatial Transcriptomics (ST)']['Original']} | {counts['Spatial Transcriptomics (ST)']['Benchmark']} | {counts['Spatial Transcriptomics (ST)']['Reviews']} |
| Hybrid         | {counts['Hybrids of SCG, DNA, and ST']['Original']} | {counts['Hybrids of SCG, DNA, and ST']['Benchmark']} | {counts['Hybrids of SCG, DNA, and ST']['Reviews']} |
"""

# Replace the existing summary table in the README.md file
updated_readme_content = re.sub(r'## Summary Statistics.*?```markdown\n.*?\n```', summary_table, readme_content, flags=re.DOTALL)

# Write the updated content back to README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(updated_readme_content)
