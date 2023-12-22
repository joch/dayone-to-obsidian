#!/usr/bin/env python

import json
import os

from jinja2 import Environment, FileSystemLoader

jinja = Environment(loader=FileSystemLoader("."), keep_trailing_newline=True)


def main(data, template_heading, template_item, out_folder):
    with open(data, "r") as file:
        entries = json.load(file)["entries"]

    for entry in entries:
        filename = entry["creationDate"].split("T")[0] + ".md"
        create_obsidian_file(
            template_heading, template_item, out_folder, filename, entry
        )


def create_obsidian_file(
    template_heading, template_item, output_folder, filename, json_data
):
    file_path = os.path.join(output_folder, filename)
    output = ""
    if not os.path.exists(file_path):
        heading_template = jinja.get_template(template_heading)
        output += heading_template.render(json_data)
    item_template = jinja.get_template(template_item)
    output += item_template.render(json_data)
    with open(file_path, "a") as file:
        file.write(output)


if __name__ == "__main__":
    main(
        data="data.json",
        template_heading="template-heading.jinja",
        template_item="template-item.jinja",
        out_folder="output/",
    )
