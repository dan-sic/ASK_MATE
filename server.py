from server_python import config
from server_python import sv_questions
from server_python import sv_general
from server_python import sv_answers
# from config import app


if __name__ == "__main__":
    config.app.run(
        debug=True,
        port=5004
)