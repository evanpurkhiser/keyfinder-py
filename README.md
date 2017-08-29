## Keyfinder Python bindings

This package implements basic bindings for
[libKeyFinder](https://github.com/ibsh/libKeyFinder). It includes the
supporting libav code for reading audio data and passing it into libKeyFinder.

#### Usage

```python
import keyfinder

key = keyfinder.key('my-audio.mp3')

key            # A
key.camelot()  # 11B
key.open_key() # 4d
```

#### Build requirements

You must have the following dependencies installed to build this module

 - [libKeyFinder](https://github.com/ibsh/libKeyFinder#installation) which has
   it's own set of dependencies. On mac you can use homebrew to tap
   [`EvanPurkhiser/homebrew-personal`](https://github.com/EvanPurkhiser/homebrew-personal)
   and then `brew install libkeyfinder`.

 - ffmpeg. On mac use `brew install ffmpeg`
