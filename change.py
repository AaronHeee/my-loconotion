import os 

dir = "dist/aaronheee.github.io"

# 0. load index.html
with open(os.path.join(dir, "index.html"), "r") as f:
    html = "".join(f.readlines())

# 1. remove `min-width: 708px`
html = html.replace('min-width: 708px;', '')

# 2. remove `gallery view`
html = html.replace('data-block-id="fa7eaddf-5957-4433-9b0b-c0776122b310" style="position: relative;', 'data-block-id="fa7eaddf-5957-4433-9b0b-c0776122b310" style="position: relative; display: none')

# 3. store htmls
with open(os.path.join(dir, "zhankui-he.html"), "w") as f:
    f.write(html)

with open(os.path.join(dir, "index.html"), "w") as f:
    f.write(html)
