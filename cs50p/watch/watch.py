import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):

    if "iframe" not in s:
        return "None"
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    x = re.findall(regex,s)
    z =  str(x[0][0].replace("/embed", "").replace("youtube.com", "youtu.be").replace("http://", "https://").replace("www.youtube", "youtube").replace("www.youtu.be", "youtu.be"))
    if "youtu.be" not in z:
        return "None"
    else:
        return z


if __name__ == "__main__":
    main()
