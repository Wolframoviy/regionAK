from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"nickname": "Wolframoviy"}
    posts = [{"author": {"name": "Aboba1", id: 34},
              "title": "Lorem ipsum dolor",
              "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem earum enim excepturi "
                         "expedita facere id inventore laborum maxime provident quisquam recusandae, repellendus "
                         "rerum saepe sed sunt tempora vero. Alias debitis est obcaecati perferendis rerum! Atque "
                         "blanditiis dicta eos esse facere quisquam. Ad animi aperiam consequuntur dignissimos "
                         "doloremque dolores, doloribus, earum eligendi facere fugiat id magnam minima nihil nisi, "
                         "odio optio perspiciatis placeat quisquam repellat sint tempora temporibus voluptatem! "
                         "Assumenda aut beatae commodi consectetur consequatur consequuntur corporis cupiditate "
                         "debitis dicta dignissimos doloribus ducimus eligendi enim et harum, impedit ipsum iure "
                         "iusto labore minus modi nobis non odio odit optio pariatur perspiciatis possimus qui quidem "
                         "quo recusandae reiciendis soluta temporibus, ullam vel voluptate voluptates. Adipisci "
                         "aliquam at, blanditiis doloribus est et explicabo facilis fugiat incidunt ipsam, "
                         "neque nostrum obcaecati quae repellendus tenetur. Cum doloribus, eum incidunt laboriosam "
                         "officia quisquam ratione sapiente temporibus? Deserunt facilis laboriosam velit? Doloremque "
                         "excepturi fugiat laudantium quod soluta?",
              "source": "Аноним",
              "image": "image.png",
              "date": "24.02.2022 04:55",
              "id": 69},
             {"author": {"name": "Aboba2", id: 69},
              "title": "Lorem ipsum dolor",
              "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem earum enim excepturi "
                         "expedita facere id inventore laborum maxime provident quisquam recusandae, repellendus "
                         "rerum saepe sed sunt tempora vero. Alias debitis est obcaecati perferendis rerum! Atque "
                         "blanditiis dicta eos esse facere quisquam.",
              "date": "24.02.2022 04:56",
              "id": 34}
             ]
    return render_template("index.html", posts=posts, title="Новости", user=user)


@app.route("/post<int:post_id>")
def post(post_id):
    return f"POST {post_id}\nTODO"


@app.route("/user<int:user_id>")
def user(user_id):
    return f"USER {user_id}\nTODO"
