import logging

from flask import request, jsonify
from demo import make_prediction
logging.basicConfig(level=logging.INFO,
                    format="{'time': '%(asctime)s', 'name': '%(funcName)s', \
 'level': '%(levelname)s', 'message': '%(message)s'}")
log = logging.getLogger("age gender estimator ")
log.setLevel(getattr(logging, "INFO"))


@myapp.route('/age_gender', methods=['POST'])
def summary():
    header = request.headers.get('age_gender')
    if header == 'contentstudio':
        content = request.json
        try:
            link=content['link']
            results=make_prediction(link)
            return jsonify({'data':results})

        except Exception as ex:
            log.error("Exception generic:{0} in age_gender model".format(ex))
            return jsonify({"Error": "Could Not serve request"}), 500
    else:
        jsonify({"Error": "Unvalidated request"}), 401
