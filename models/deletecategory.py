'''
  this file delete category.
'''

from models.login import *
from models.showcategory import *
from models.db import *
from models.userhelper import *


# Delete a Category
@app.route('/category/<int:Category_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteCategory(Category_id):
    CategoryToDelete = session.query(
        Category).filter_by(id=Category_id).one()
    if request.method == 'POST':
        if CategoryToDelete.user_id != login_session['user_id']:
            return redirect(url_for('shownewscategory',
                                    Category_id=Category_id))

        news_to_category = session.query(
            News).filter_by(id=Category_id).all()

        for news in news_to_category:
            session.delete(news)
            session.commit()

        session.delete(CategoryToDelete)
        flash('%s Successfully Deleted' % CategoryToDelete.name)
        session.commit()
        return redirect(url_for('shownewscategory', Category_id=Category_id))
    else:
        return render_template('deletecategory.html',
                               CategoryToDelete=CategoryToDelete)
