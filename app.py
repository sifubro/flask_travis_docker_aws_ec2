from flask import Flask, render_template, request

#from tensorflow.keras.preprocessing.image import load_img, img_to_array
#from keras.applications.vgg16 import preprocess_input, decode_predictions #VGG16
#from keras.applications.xception import preprocess_input, decode_predictions, Xception
#from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions, MobileNetV2
#from keras.applications import Xception

#import os
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

#model = MobileNetV2()
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return 200

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imgfile = request.files['image_file']

    #imgpath = "./images/" + imgfile.filename
    #imgfile.save(imgpath)

    #224 for vgg16 and mobilenet
    #299 for xception
    # img = load_img(imgpath, target_size=(224,224))  #224  299
    # img = img_to_array(img)
    # img = img.reshape((1, img.shape[0],img.shape[1], img.shape[2] ))
    # img = preprocess_input(img)
    # yhat = model.predict(img)
    # label = decode_predictions(yhat)
    # label1 = label[0][0]
    # label2 = label[0][1]
    # label3 = label[0][2]

    # #classification = "%s (%.2f%%)" %(label1[1], label1[2]*100)
    # classification = "{}:{}%  ,  {}:{}%  ,  {}:{}%".format(label1[1], round(label1[2]*100,2),label2[1], round(label2[2]*100,2), label3[1], round(label3[2]*100,2) )

    return render_template('index.html', prediction=imgfile.filename)

if __name__ == '__main__':
    #https://stackoverflow.com/questions/28241989/flask-app-restarting-with-stat
    #Use run(use_reloader=False) to disable the reloader.
    #https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues/43015007#43015007
    app.run(host='0.0.0.0', debug=False) # port=3000,
