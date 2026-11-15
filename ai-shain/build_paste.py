# 社長代理に貼る文章を1つにまとめる：python3 ai-shain/build_paste.py
import re, pathlib
d = pathlib.Path(__file__).parent
def block(name, after=""):
    s = (d/name).read_text()
    s = s[s.index(after):] if after else s
    return re.search(r"```\n(.*?)```", s, re.S).group(1).strip()
common = block("README.md", "【共通：会社の基本情報】")
deputy = block("fukushacho.md")
note = re.sub(r"<!--.*?-->\n?", "", (d/"shacho-note.md").read_text(), flags=re.S)
note = note.split("---", 1)[1].strip()
out = f"{common}\n\n{deputy}\n\n# 社長ノート（社長の記憶。必ず前提にする）\n{note}\n"
(d/"harituke.txt").write_text(out)
print(len(out), "chars")
