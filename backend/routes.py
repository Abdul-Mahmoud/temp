from turtle import done
from urllib import response
from flask import current_app,jsonify,request
from app import create_app,db
from models import Articles,articles_schema,article_schema

# Create an application instance
app = create_app()

# Define a route to fetch the avaialable articles

test = "";


@app.route("/articles", methods=["GET"], strict_slashes=False)
def articles():

	articles = Articles.query.all()
	results = articles_schema.dump(articles)

	return jsonify(results)


@app.route("/add", methods=["POST"], strict_slashes=False)
def add_articles():
	title = request.json['title']
	body = request.json['body']

	article = Articles(
		title=title,
		body=body
		)

	db.session.add(article)
	db.session.commit()

	return article_schema.jsonify(article)

@app.route("/get-parms", methods=["POST"], strict_slashes=False)
def get_parms():
	test = request.data
	response.headers.add('Access-Control-Allow-Origin', '*')
	return article_schema.jsonify(test)

@app.route("/results", methods=["GET"], strict_slashes=False)
def get_results():
	return jsonify(test)



if __name__ == "__main__":
	app.run(debug=True)