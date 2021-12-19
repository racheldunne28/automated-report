---
lang: "en"
fontsize: 10pt
header-includes:
- |
 ```{=latex}
  \usepackage{booktabs}
  \usepackage{float} 
  \usepackage{graphicx}
 ```
pandoc-latex-environment:
  noteblock: [note]
  tipblock: [tip]
  warningblock: [warning]
  cautionblock: [caution]
  importantblock: [important]
...

# $date: Test

\includegraphics[height=0.8\textheight]{$example_figure}


# Table

$table
