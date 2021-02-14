# Audio transcripter

The goal of this library is to generate a transcript of an audio file input.

## Installation

### Prerequisites:
- Python 3.9
- SWIG

### Basic install

```zsh
brew install python@3.9 swig
pip install pocketsphinx2 SpeechRecognition 
```

### Install French language for PocketSphinx.

Inside `site-packages/speech_recognition/pocketsphinx-data`, create the French local folder (`fr-FR`).

Get files from [Sphinx French language model](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/French/). Download:
- `fr-small.lm.bin` and rename it `language-model.lm.bin`
- `fr.dict` and rename it `pronounciation-dictionary.dict`
- `cmusphinx-fr-5.2.tar.gz` and unzip it as a folder named `acoustic-model`

More info in the [Documentation](https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst#notes-on-the-structure-of-the-language-data).
