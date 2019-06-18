from flask import Flask
import ai
import os

app = Flask(__name__, static_url_path='')

@app.route('/ai/<music_list>', methods=['GET'])
def main(music_list):
    music_list = music_list.split('_')
    beats_list = [eval(x) for x in music_list]
    ai.generateAIMusic(beats_list)
    file_list = os.listdir('/root/Desktop/Xiaocai/static')
    print(beats_list)
    return app.send_static_file(os.path.join('/root/Desktop/Xiaocai/static',file_list[0]))

if __name__ == '__main__':
    app.run()