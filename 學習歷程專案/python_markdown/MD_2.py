import markdown
import codecs

file_input = codecs.open("Python環境配置.md", mode="r", encoding="utf-8")
md_text = file_input.read()

html_text = markdown.markdown(md_text)

file_output = codecs.open("Python環境配置.html", mode="w", encoding="utf-8")
file_output.write(html_text)