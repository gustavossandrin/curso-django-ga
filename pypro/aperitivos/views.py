from django.shortcuts import render

videos = [
        {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'youtube_id': '2aYplgJrPDU'},
        {'slug': 'instalacao-windows', 'titulo': 'instalação windows', 'youtube_id': 'ScmQ4I5Qr5s'},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
