from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from Difference import Difference

UPLOAD_FOLDER = 'uploads'
#許可する拡張子
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

#アプリケーションインスタンスの作成
app = Flask(__name__, static_url_path='/uploads', static_folder='uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#許可された拡張子を持っているか確認するメソッド
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #ファイルがアップロードされているか確認
        if 'file1' not in request.files or 'file2' not in request.files:
            return redirect(request.url)
        file1 = request.files['file1']
        file2 = request.files['file2']
        if file1.filename == '' or file2.filename == '':
            return redirect(request.url)
        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
            #画像比較の実行
            diff = Difference()
            diff.compareImages(os.path.join(app.config['UPLOAD_FOLDER'], filename1), os.path.join(app.config['UPLOAD_FOLDER'], filename2))

            return redirect(url_for('result'))
    return '''
    <!doctype html>
    <title>Upload Image</title>
    <h1>Upload two images to compare</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file1>
      <input type=file name=file2>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/result')
def result():
    return '''
    <!doctype html>
    <title>Result</title>
    <h1>Comparison Result</h1>
    <img src="/uploads/result.png" alt="Result">
    '''

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
