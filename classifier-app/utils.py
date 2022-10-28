ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_closest_match(features):
    # ...encontrar la imagen más similar del conjunto objetivo...
    # ...retornar su nombre de archivo...
    return '1ec96051fd573348_lion.jpg'
