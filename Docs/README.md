# Xiaocai

Xiaocaitongxue is a voice interactive music assistant. It can open the corresponding function through voice interaction. And after waking up the device, you  can choose four modes to play:

1. Play piano
2. Music game
3. AI compose
4. Play previous music

And you can control the state of the equipment by gesture. We use lasers to make light projection on the fingers so that the camera can easily detect where is the fingers.

At first, we run the function wake\_up(). In this funciton, we set a detector about XiaoCaiTongXue and then open it. After the detector is opened, it will detect the hotword "xiaocaitongxue"

If the hotword is detected, the program will callback the function callback\_xctx().The function will terminate the detector about XiaoCaiTongXue.And then open the detector about the function.

If the hotword about different function is detected, the program will terminate the detector about the function. And then execute the specific function, callback\_game(), callback\_music(), callback\_AI() and callback\_piano().

If "alexa" is detected, it will run the function callback\_piano(). In this function, it will run the function playMusic() to play the piano.

If "Hey Friday" is detected, it will run the function callback\_game(). In this function, it will run the function music\_game.run() to play music game.

If "Jarvis" is detected, it will run the function callback\_music(). In this function, it will run the function play\_previous\_music() to play the previous music.

If "snowboy" is detected, it will run the function callback\_ai(). In this function, it will run the function playMusicWithAI() to play the piano with ai.

## How to run

1. Install packages required. (Listed in the report)
2. Run `xiaocaitongxue.py` on a Raspberry Pi

```
python xiaocaitongxue.py
```

3. If you want AI mode work, you should modify the IP address in `ai.py` and run `server.py` on the server because we may not run the program on our server all the time.