from markdown_worker import MarkdownParser
import os


focus_docs_path = "finops_focus"
files = os.listdir(focus_docs_path)
files = [f for f in files if os.path.isfile(focus_docs_path+'/'+f)]
print(*files, sep="\n")
# markdown_parser = MarkdownParser(focus_docs_path)   
# print(markdown_parser.get_all_docs())