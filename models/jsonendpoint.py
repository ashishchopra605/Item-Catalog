from models.db import *


# JSON APIs to view News Information
@app.route('/category/<int:Category_id>/news/JSON')
def newsJSON(Category_id):
    category = session.query(Category).filter_by(id=Category_id).one()
    news = session.query(News).filter_by(
        category_id=Category_id).all()
    return jsonify(news=[i.serialize for i in news])


@app.route('/category/<int:Category_id>/news/<int:news_id>/JSON')
def NewsJSON(Category_id, news_id):
    news = session.query(News).filter_by(id=news_id).one()
    return jsonify(news=news.serialize)


@app.route('/category/JSON')
def newsCategoryJSON():
    category = session.query(Category).all()
    return jsonify(category=[r.serialize for r in category])
