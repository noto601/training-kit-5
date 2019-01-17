from aiy.voice import audio


def main():
    print('Start playing...')
    audio.play_wav('sample.wav')
    print('Done.')


if __name__ == '__main__':
    main()
