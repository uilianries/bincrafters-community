def update_travis_url(main, file):
    """ Update Travis CI URL
    """
    if main.replace_in_file(file, "https://travis-ci.org/bincrafters", "https://travis-ci.com/bincrafters"):
        main.output_result_update(title="README: Update Travis URL")
        return True
    return False
