import mlflow

mlflow.set_experiment("Logging_interactions")

def log_interactions(model_name, user_id, mode, user_query, ai_response, response_time):
    with mlflow.start_run():  
        question_length = len(user_query)
        answer_length = len(ai_response)

        
        mlflow.log_param('user_session_id', user_id)
        mlflow.log_param('mode', mode)
        mlflow.log_param('user_question', user_query)
        mlflow.log_param('ai_answer', ai_response)
        mlflow.log_param('model_name', model_name)

        mlflow.log_metric('response_time', response_time)
        mlflow.log_metric('question_length', question_length)
        mlflow.log_metric('answer_length', answer_length)