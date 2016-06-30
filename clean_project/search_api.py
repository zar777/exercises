"""
Search a word in a file and return all the occurrences specified the line numbers
"""
import argparse
from collections import defaultdict
import flask
import search_engine

BOLD = '\033[1m'
END = '\033[0m'


app = flask.Flask(__name__)


def config_app(search_object):
    app.config['search'] = search_object
    return app


@app.route('/search/<string:search_word>', methods=['GET'])
def search_operation(search_word):
    """
    Get request that returns the results of a search operation
    :param search_word: Word used for search
    :return: Response of the search request
    """
    save_result = defaultdict(lambda: defaultdict(list))
    result_search = app.config['search'].search(search_word)
    if result_search:
            for result_tuple in result_search:
                save_result[result_tuple[0]][result_tuple[1]] = result_tuple[2]
    return flask.jsonify({'search_response': save_result})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('connect_path')
    parser.add_argument('-debug', nargs='?', default=False)
    args = parser.parse_args()
    try:
        search_obj = search_engine.SearchEngine(args.connect_path)
        config_app(search_obj)
        app.run(debug=args.debug)
    except IOError as e:
        print 'File or path not found: %s' % e
