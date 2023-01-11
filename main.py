import markdown2
from github import Github


git = Github(sys.argv[1])

def main():
    with open("README.md", "r") as md_file:
        md_text = md_file.read()
        
    html_text = markdown2.markdown(md_text)
    with open("new_index.html", "w") as html_file:
        html_file.write(html_text)


if __name__ == "__main__":
    main()
