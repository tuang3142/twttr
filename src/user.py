# import flask
# import json
# import request
# from app import app
# from . import google_auth

# user_api = flask.Blueprint('users', __name__)
# user_schema = UserSchema()


# @user_api.route('/', methods=['POST'])
# def create():
#     req = request.get_json()
#     data, error = user_schema.load(req)

#     if error:
#         return custom_response(error, 400)

#     if User.find_by_email(data.get('email')):
#         message = {'error': 'email already exists'} #todo: change uppercase to regular
#         return custom_response(message, 400)

#     user = User(data)
#     user.save()
#     ser_data = user_schema.dump(user).data
#     token = Auth.generate_token(ser_data.get('id'))

#     return custom_response({'jwt_token': token}, 201)


# def custom_response(res, status_code):
#     return Response(
#         mimetype="application/json",
#         response=json.dumps(res),
#         status=status_code
#     )
