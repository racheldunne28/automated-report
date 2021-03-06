import os
import sys
from pathlib import Path
from string import Template

import pandas as pd
from pypandoc import convert_text

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from reports.assets import EXAMPLE_FIGURE  # noqa
from reports.s3_simple import get_s3_data  # noqa

CHARTS = {
    "example_figure": EXAMPLE_FIGURE,
}

EXTRA_ARGS = [
    "--pdf-engine",
    "lualatex",
    "--filter",
    "pandoc-latex-environment",
]


def get_data_dict(s3=True):
    date = pd.Timestamp.today().strftime("%d %B %Y")
    data_dict = {"date": date}
    example_df = pd.DataFrame(
        {
            "column1": ["A", "B", "C", "D", "E", "F", "G"],
            "column2": [1, 2, 3, 4, 5, 6, 7],
            "column3": [
                "red",
                "blue",
                "orange",
                "green",
                "yellow",
                "purple",
                "pink",
            ],
            "column4": [7, 6, 5, 4, 3, 2, 1],
        }
    )
    example_table = example_df.to_latex(
        header=["column1", "column2", "column3", "column4"],
        index=False,
        position="h",
    )
    data_dict["table"] = example_table
    if s3:
        s3_df = get_s3_data("overview_2021-11-08.csv").head(10)
        s3_table = s3_df.to_latex(
            header=list(s3_df.columns),
            index=False,
            position="h",
        )
        data_dict["s3_table"] = s3_table
    for chart in CHARTS.keys():
        data_dict[chart] = CHARTS[chart]
    return data_dict


def get_template(template_name, parent_dir, ext):
    if template_name.endswith(ext):
        filepath = f"{parent_dir}/{template_name}"
    else:
        filepath = f"{parent_dir}/{template_name}{ext}"

    template_file = Path(filepath)
    if template_file.is_file():
        with template_file.open() as open_file:
            template = Template(open_file.read())
    else:
        raise Exception(f"Warning template: {template_file} does not exist")
    return template


def template_to_pdf(template_name, data_dict):
    template = get_template(template_name, "templates", ext=".md")
    template_str = template.safe_substitute(**data_dict)
    output = f"output/{template_name}.pdf"
    convert_text(
        template_str,
        "pdf",
        "markdown",
        outputfile=output,
        extra_args=EXTRA_ARGS,
    )
    return output


if __name__ == "__main__":
    data_dict = get_data_dict(s3=True)
    template_to_pdf("example", data_dict)
