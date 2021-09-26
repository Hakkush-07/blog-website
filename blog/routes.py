from flask import render_template, url_for, flash, redirect, request
from blog import app, db
from blog.forms import PostForm
from blog.models import Post


@app.route("/")
@app.route("/home")
def index():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/post/new", methods=["GET", "POST"])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created", "success")
        return redirect(url_for("index"))
    return render_template("create.html", title="Create", form=form, legend="New Post", button_text="Post")


@app.route("/post/<int:post_id>")
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=["GET", "POST"])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated!", "success")
        return redirect(url_for("show_post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template("create.html", title="Edit", form=form, legend="Edit Post", button_text="Save")


@app.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("index"))
