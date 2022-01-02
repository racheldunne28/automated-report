---
lang: "en"
fontsize: 10pt
header-includes:
- |
 ```{=latex}
  \usepackage{booktabs}
  \usepackage{float} 
  \usepackage[margin=0.5in]{geometry}
  \usepackage{graphicx}
  \usepackage{fontspec}
  \setmainfont{Helvetica}
 ```
pandoc-latex-environment:
  noteblock: [note]
  tipblock: [tip]
  warningblock: [warning]
  cautionblock: [caution]
  importantblock: [important]
...

# $date: Example automated report

\includegraphics[height=0.6\textheight]{$example_figure}

\newpage

# Table

$table

Here are some notes about this table

\newpage

# S3 table

$s3_table

Here are some notes about this table
