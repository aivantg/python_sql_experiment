text = """<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='styles/common.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='styles/index.css') }}">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script src="{{url_for('static', filename='routing.js')}}" type="text/javascript"></script>
    <meta charset="utf-8">
    <title>FaceBook V2</title>
  </head>
  <body>
    <div class="post card">
      <h3 class="post-number">1</h3>
      <h5 class="post-title">Title of Post</h5>
      <p class="post-description">Post Description</p>
    </div>
    <div class="post card">
      <h3 class="post-number">1</h3>
      <h5 class="post-title">Title of Post</h5>
      <p class="post-description">Post Description</p>
    </div>
    <button onclick="new_post()"> New Post </button>
  </body>
</html>
"""


def generate_index():
    raw = open('templates/index.html', 'r+')
    raw.seek(0)                        # <- This is the missing piece
    raw.truncate()
    raw.write(text)
    raw.close()
