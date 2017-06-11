'''
  this file includes edit category function.
'''

from models.login import *
from models.showcategory import *
from models.db import *
from models.userhelper import *


# Edit a Category
@app.route('/category/<int:Category_id>/edit/', methods=['GET', 'POST'])
@login_required
def editCategory(Category_id):
    editedCategory = session.query(
        Category).filter_by(id=Category_id).one()
    if request.method == 'POST':
        if editedCategory.user_id != login_session['user_id']:
            return redirect(url_for('shownewscategory'))

        if request.form['category-name']:
            editedCategory.name = request.form['category-name']
            editedCategory.description = request.form['category-description']
            editedCategory.imgurl = request.form['category-img']
            flash('Category Successfully Edited %s' % editedCategory.name)
            return redirect(url_for('shownewscategory'))
    else:
        return render_template('editcategory.html',
                               editedcategory=editedCategory)
