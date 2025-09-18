import argparse
from jinja2 import Environment, FileSystemLoader
import time


time.sleep(0.5)  # Polling interval

def render_template(data, template_name, filename):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    output = template.render(data)
    filename = filename.lower().replace(' ', '-')

# os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(f'../docs/{filename}.md', 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"✅ File '{filename}.md' generated from 'templates/{template_name}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Markdown from a Jinja2 template")
    parser.add_argument('--title', default='')
    parser.add_argument('--author', default='Anonymous')
    parser.add_argument('--date', default='Not specified')
    parser.add_argument('--summary', default='No summary provided.')
    parser.add_argument('--notes', nargs='*', default=['No notes.'])
    parser.add_argument('--template', default='report.md.j2')
    # parser.add_argument('--output', default='output/report.md')
    parser.add_argument('--filename', default='untitled-report', help='Title of the report and file name')

    args = parser.parse_args()
    render_template(vars(args), args.template, args.filename)
