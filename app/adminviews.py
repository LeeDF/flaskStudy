from app import app, models
from flask import (render_template, request, jsonify)
from werkzeug.utils import secure_filename
import json
import os,uuid

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route('/')
@app.route('/admin/blogUpload')
def blogUploadView():
    categorys = models.Category.query.all()
    return render_template('blogUpload.html', categorys=categorys)


@app.route('/img/upload', methods=['GET', 'POST'])
def imgUpload():

    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'code': 0, 'msg': '失败'})
        file = request.files['file']

        if file.filename == '':
            return jsonify({'code': 0, 'msg': '失败'})
        if allowed_file(file.filename):
            filename = str(uuid.uuid1())+secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            link = app.config['IMGURL'] + filename
            rsp = {'errno': 0, 'data': [link]}
            return jsonify(rsp)
    return jsonify({'code': 0, 'msg': '失败'})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
