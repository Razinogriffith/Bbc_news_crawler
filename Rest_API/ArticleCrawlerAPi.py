from   flask import Flask
from   flask_restful import Resource, Api
from   flask_pymongo import PyMongo
from   bson import json_util
import json

# Connecting to MongoDB containing the crawled BBC News Articles.
app    = Flask(__name__)
app.config['MONGO_DBNAME'] = 'Articles'
app.config['MONGO_URI']    = 'mongodb+srv://user1:kasdefghajklem@razinogriffith.r8vjd.mongodb.net/Articles?retryWrites=true&w=majority'
api                        = Api(app)
mongo                      = PyMongo(app)
def toJson(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps(data, default=json_util.default)

class NewsMeta(Resource):
    def get(self):
        '''
        DESCRIPTION:
        -----------
        Gets all the news articles in database.
        '''
        results = mongo.db.Articles_db.find()
        json_results = []
        for result in results:
            json_results.append(result)
        return toJson(json_results)

class SearchBodyKeyword(Resource):
    def get(self, keyword):
        '''
        DESCRIPTION:
        ------------
        GET news articles, where keyword appears in news article body.
        PARAMETERS:
        ----------
        1. keyword: string to be searched in news body.
        '''
        results = mongo.db.Articles_db.find({'body': {'$regex': '.*' + keyword + '.*'}})
        json_results = []
        for result in results:
            json_results.append(result)
        return toJson(json_results)

class SearchHeaderKeyword(Resource):
    def get(self, keyword):
        '''
        DESCRIPTION:
        ------------
        GET news articles, where keyword appears in news header.
        PARAMETERS:
        ----------
        1. keyword: string to be searched in header.
        '''
        results = mongo.db.Articles_db.find({'header': {'$regex': '.*' + keyword + '.*'}})
        json_results = []
        for result in results:
            json_results.append(result)
        return toJson(json_results)

class SearchTagsKeyword(Resource):
    def get(self, keyword):
        '''
        DESCRIPTION:
        ------------
        GET news articles, where keyword appears in news tags.
        PARAMETERS:
        ----------
        1. keyword: string to be searched in news tags.
        '''
        results = mongo.db.Articles_db.find({'tags': {'$regex': '.*' + keyword + '.*'}})
        json_results = []
        for result in results:
            json_results.append(result)
        return toJson(json_results)

api.add_resource(SearchHeaderKeyword, '/header/<string:keyword>')
api.add_resource(SearchBodyKeyword, '/body/<string:keyword>')
api.add_resource(SearchTagsKeyword, '/tags/<string:keyword>')
api.add_resource(NewsMeta, '/news')

if __name__ == '__main__':
    app.run()