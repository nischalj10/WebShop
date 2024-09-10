import sys
import json
from tqdm import tqdm
sys.path.insert(0, '../')

from web_agent_site.utils import DEFAULT_FILE_PATH
from web_agent_site.engine.engine import load_products

def process_products(products):
    for p in tqdm(products, total=len(products)):
        option_texts = []
        options = p.get('options', {})
        for option_name, option_contents in options.items():
            option_contents_text = ', '.join(option_contents)
            option_texts.append(f'{option_name}: {option_contents_text}')
        option_text = ', and '.join(option_texts)

        yield {
            'id': p['asin'],
            'contents': ' '.join([
                p['Title'],
                p['Description'],
                p['BulletPoints'][0],
                option_text,
            ]).lower(),
            'product': p
        }

def write_jsonl(filename, data, limit=None):
    with open(filename, 'w') as f:
        for i, doc in enumerate(data):
            if limit and i >= limit:
                break
            f.write(json.dumps(doc) + '\n')

def main():
    all_products, *_ = load_products(filepath=DEFAULT_FILE_PATH)
    docs = process_products(all_products)

    write_jsonl('./resources_100/documents.jsonl', docs, limit=100)
    docs = process_products(all_products)  # Reset generator
    write_jsonl('./resources/documents.jsonl', docs)
    docs = process_products(all_products)  # Reset generator
    write_jsonl('./resources_1k/documents.jsonl', docs, limit=1000)
    docs = process_products(all_products)  # Reset generator
    write_jsonl('./resources_100k/documents.jsonl', docs, limit=100000)

if __name__ == "__main__":
    main()