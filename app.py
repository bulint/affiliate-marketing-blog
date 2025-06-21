## 🔄❌🕒💤✔️📌 → todo: ask chatgpt or keep a note about cheatcodes: like key shortcuts to theme change and such so i always have a list on these, because my brain cannot remember! thank you, future me.

from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)

### todos ###
# Template Layouts with Tailwind ❌
    # base.html: header ❌, footer ❌, {% block content %} ❌
    # Style home.html ❌, blog.html ❌, post.html ❌ with Tailwind
# Navigation Bar
    # Add nav links in base.html ❌
    # Highlight current page using Tailwind classes ❌
# Add a favicon (static/images/favicon.ico) ❌
# Add SEO tags (title, meta description) ❌
# Add 404 route handler (@app.errorhandler(404)) ❌

@app.route('/') # @app.route('/',methods=['GET','POST'])
def home():
    # load home page ✅
    return render_template('blog.html')

@app.route('/blog')
@app.route('/blog/<slug>')
def blog():
     # /blog → list blog posts ❌
     # /blog/<slug> → list blog posts ❌
     # Render post previews dynamically in blog.html ❌
     # Slugify titles to generate routes (e.g. "best-lego-sets") ❌💤
    return render_template('home.html')

def contact():
    # /contact → contact form (basic) ❌
    return render_template('contact.html')



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)