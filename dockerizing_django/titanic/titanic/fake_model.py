def fake_predict(user_age):
    if user_age>10:
        prediction = 'survive'
    else:
        prediction = 'not survive'
    return prediction