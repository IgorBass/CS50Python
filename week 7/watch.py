import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    url = re.search (r"src=\"https?:\/{2}(www\.)?\w+\.\w+\/\w+\/\w+", s)
    if url:
        youtube = url.group()
        you_without_embed = re.sub("embed\/", "", youtube)
        you_tube = re.sub(r"(www\.)?youtube\.com", "youtu.be", you_without_embed)
        https = re.sub(r"https?", "https", you_tube)
        https_src = re.sub(r'src=\"', '', https)
        return https_src
    else: return None

if __name__ == "__main__":
    main()
