import server_python.config
import server_python.sv_questions
import server_python.sv_general
import server_python.sv_answers
from server_python.config import app

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5004
)